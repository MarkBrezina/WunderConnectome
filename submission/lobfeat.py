"""Feature layer shared by training and inference (v2).

What the forensics on the real data showed:
  * every input is already quantile-normalised (columns sit in about +-2.5, the extra columns
    bottom out at -5.19934 = sklearn QuantileTransformer's floor, and "no trade" is a single atom
    near 0.025);
  * the price-like columns are not monotone prices: max(bid columns) >= min(ask columns) on 100%
    of rows, and each column sits in a narrow band around its own fixed value.
So nothing here assumes book structure (best quotes, mid, spread, order flow); v1 did, and on
this data those features were meaningless. Per row:
  * x     the 112 inputs as given (NaN -> 0)
  * dx    x_t - x_{t-1}, 0 on a sequence's first row: what just changed (the event type)
  * time  log1p(step) / log1p(20000)
Every column is then centred, scaled and passed through asinh, which compresses rare large
excursions instead of clipping them away. The GRU does the temporal modelling.

`batch_features` (training) and `Streamer.update` (inference, one row at a time) must agree;
tests/test_parity.py checks them against each other.
"""
import math

import numpy as np

KIT_VERSION = "2"
N_RAW = 112
WARMUP = 99
SEQ_LEN = 20_000
N_FEAT = 2 * N_RAW + 1
TIME_NORM = math.log1p(SEQ_LEN)
Z_CLIP = 8.0

RAW_NAMES = ([f"i0_p{k}" for k in range(22)] + [f"i0_v{k}" for k in range(22)]
             + [f"i0_dp{k}" for k in range(4)] + [f"i0_dv{k}" for k in range(4)]
             + [f"i1_p{k}" for k in range(22)] + [f"i1_v{k}" for k in range(22)]
             + [f"i1_dp{k}" for k in range(4)] + [f"i1_dv{k}" for k in range(4)]
             + [f"a{k}" for k in range(8)])


def feature_names():
    names = list(RAW_NAMES) + [f"d_{n}" for n in RAW_NAMES] + ["time"]
    assert len(names) == N_FEAT
    return names


def _fin(a):
    return np.nan_to_num(a, nan=0.0, posinf=0.0, neginf=0.0)


def batch_features(X):
    """X: (T, 112) rows of one sequence from step 0. Returns (T, N_FEAT) float64."""
    X = _fin(np.asarray(X, dtype=np.float64))
    dX = np.zeros_like(X)
    dX[1:] = X[1:] - X[:-1]
    t = np.log1p(np.arange(len(X), dtype=np.float64)) / TIME_NORM
    return np.concatenate([X, dX, t[:, None]], axis=1)


def fit_scaler(S):
    """S: (n, N_FEAT) sample of batch features. Returns (mu, inv_sd, dead).

    Centre = median. Scale = std after winsorising at 0.05% / 99.95%, falling back to the plain
    std for columns that are almost always one value (e.g. diffs of rarely-changing columns).
    """
    S = np.asarray(S, dtype=np.float64)
    mu = np.median(S, axis=0)
    lo, hi = np.percentile(S, [0.05, 99.95], axis=0)
    sd = np.clip(S, lo, hi).std(axis=0)
    weak = sd <= 1e-12
    if weak.any():
        sd[weak] = S[:, weak].std(axis=0)
    dead = sd <= 1e-12
    inv_sd = np.where(dead, 0.0, 1.0 / np.where(dead, 1.0, sd))
    return mu, inv_sd, dead


def normalize(F, mu, inv_sd):
    return np.clip(np.arcsinh(_fin((F - mu) * inv_sd)), -Z_CLIP, Z_CLIP).astype(np.float32)


class Streamer:
    """Row-at-a-time version of batch_features + normalize."""

    def __init__(self, mu, inv_sd):
        self.mu = np.asarray(mu, dtype=np.float64)
        self.inv_sd = np.asarray(inv_sd, dtype=np.float64)
        self.prev = np.zeros(N_RAW)
        self.buf = np.zeros(N_FEAT)
        self.z = np.zeros(N_FEAT)
        self.x = self.buf[:N_RAW]
        self.d = self.buf[N_RAW:2 * N_RAW]
        self.reset()

    def reset(self):
        self.step = 0

    def raw_update(self, x):
        xb, d = self.x, self.d
        np.copyto(xb, x)                              # float32 -> float64
        if not math.isfinite(float(xb.sum())):        # rare: only pay for nan_to_num when needed
            np.nan_to_num(xb, copy=False, nan=0.0, posinf=0.0, neginf=0.0)
        if self.step == 0:
            d[:] = 0.0
        else:
            np.subtract(xb, self.prev, out=d)
        self.prev[:] = xb
        self.buf[2 * N_RAW] = math.log1p(self.step) / TIME_NORM
        self.step += 1
        return self.buf

    def update(self, x):
        z = self.z
        np.subtract(self.raw_update(x), self.mu, out=z)
        np.multiply(z, self.inv_sd, out=z)
        np.arcsinh(z, out=z)
        np.minimum(z, Z_CLIP, out=z)
        np.maximum(z, -Z_CLIP, out=z)
        return z.astype(np.float32)
