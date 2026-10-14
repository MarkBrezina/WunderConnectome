"""Single-step numpy version of model.Net, used at inference (no torch needed).

Loads the arrays written by model.export_npz and reproduces Net.forward one row at a time:
    a = silu(W_in z + b_in)
    GRU layers (PyTorch gate order r, z, n)
    y = W2 silu(W1 [h_last, a] + b1) + b2,   then * out_scale, clipped to [-2, 2]
"""
import json

import numpy as np


def _sigmoid(v):
    return 1.0 / (1.0 + np.exp(-v))


class NumpyNet:
    def __init__(self, d):
        meta = json.loads(str(d["meta"]))
        self.H = int(meta["hidden"])
        self.L = int(meta["layers"])
        f32 = lambda k: np.ascontiguousarray(d[k], dtype=np.float32)
        self.W_in, self.b_in = f32("W_in"), f32("b_in")
        self.W_ih = [f32(f"W_ih{l}") for l in range(self.L)]
        self.W_hh = [f32(f"W_hh{l}") for l in range(self.L)]
        self.b_ih = [f32(f"b_ih{l}") for l in range(self.L)]
        self.b_hh = [f32(f"b_hh{l}") for l in range(self.L)]
        self.W1, self.b1 = f32("W1"), f32("b1")
        self.W2, self.b2 = f32("W2"), f32("b2")
        self.scale = np.float32(d["out_scale"])
        self.cat = np.zeros(2 * self.H, dtype=np.float32)
        self.reset()

    def reset(self):
        self.h = [np.zeros(self.H, dtype=np.float32) for _ in range(self.L)]

    def step(self, z, need_output=True):
        H = self.H
        u = self.W_in @ z + self.b_in
        a = u * _sigmoid(u)
        inp = a
        for l in range(self.L):
            h = self.h[l]
            gi = self.W_ih[l] @ inp + self.b_ih[l]
            gh = self.W_hh[l] @ h + self.b_hh[l]
            rz = _sigmoid(gi[:2 * H] + gh[:2 * H])
            n = np.tanh(gi[2 * H:] + rz[:H] * gh[2 * H:])
            h = n + rz[H:] * (h - n)
            self.h[l] = h
            inp = h
        if not need_output:
            return None
        self.cat[:H] = inp
        self.cat[H:] = a
        v = self.W1 @ self.cat + self.b1
        v = v * _sigmoid(v)
        y = (self.W2 @ v + self.b2) * self.scale
        return np.clip(y, -2.0, 2.0).astype(np.float32)


# ----------------------------------------------------------------------------- compiled path
_NET_KERNEL = None


def _build_net_kernel():
    import math
    from numba import njit

    @njit(cache=True, fastmath=True)
    def matvec(W, x, b, out):
        n_out, n_in = W.shape
        for i in range(n_out):
            acc = b[i]
            for j in range(n_in):
                acc += W[i, j] * x[j]
            out[i] = acc

    @njit(cache=True, fastmath=True)
    def kernel(z, W_in, b_in, W_ih, W_hh, b_ih, b_hh, W1, b1, W2, b2, scale,
               h, a, gi, gh, cat, v, y):
        # h: (L, H); W_ih: (L, 3H, H); W_hh: (L, 3H, H)
        L = h.shape[0]
        H = h.shape[1]
        matvec(W_in, z, b_in, a)
        for i in range(H):
            a[i] = a[i] / (1.0 + math.exp(-a[i]))
        for l in range(L):
            if l == 0:
                matvec(W_ih[l], a, b_ih[l], gi)
            else:
                matvec(W_ih[l], h[l - 1], b_ih[l], gi)
            matvec(W_hh[l], h[l], b_hh[l], gh)
            for i in range(H):
                r = 1.0 / (1.0 + math.exp(-(gi[i] + gh[i])))
                u = 1.0 / (1.0 + math.exp(-(gi[H + i] + gh[H + i])))
                n = math.tanh(gi[2 * H + i] + r * gh[2 * H + i])
                h[l, i] = n + u * (h[l, i] - n)
        for i in range(H):
            cat[i] = h[L - 1, i]
            cat[H + i] = a[i]
        matvec(W1, cat, b1, v)
        for i in range(v.shape[0]):
            v[i] = v[i] / (1.0 + math.exp(-v[i]))
        matvec(W2, v, b2, y)
        for i in range(y.shape[0]):
            t = y[i] * scale
            y[i] = 2.0 if t > 2.0 else (-2.0 if t < -2.0 else t)

    return kernel


class NumbaNet(NumpyNet):
    """Same maths as NumpyNet, compiled; about 5-10x faster per row."""

    def __init__(self, d):
        global _NET_KERNEL
        super().__init__(d)
        if _NET_KERNEL is None:
            _NET_KERNEL = _build_net_kernel()
        self.kernel = _NET_KERNEL
        H = self.H
        self.Wih = np.ascontiguousarray(np.stack(self.W_ih))
        self.Whh = np.ascontiguousarray(np.stack(self.W_hh))
        self.bih = np.ascontiguousarray(np.stack(self.b_ih))
        self.bhh = np.ascontiguousarray(np.stack(self.b_hh))
        self.hs = np.zeros((self.L, H), dtype=np.float32)
        self.a = np.zeros(H, dtype=np.float32)
        self.gi = np.zeros(3 * H, dtype=np.float32)
        self.gh = np.zeros(3 * H, dtype=np.float32)
        self.v = np.zeros(self.W1.shape[0], dtype=np.float32)
        self.y = np.zeros(2, dtype=np.float32)
        self.step(np.zeros(self.W_in.shape[1], dtype=np.float32))   # compile
        self.reset()

    def reset(self):
        super().reset()
        if hasattr(self, "hs"):
            self.hs[:] = 0.0

    def step(self, z, need_output=True):
        self.kernel(z, self.W_in, self.b_in, self.Wih, self.Whh, self.bih, self.bhh,
                    self.W1, self.b1, self.W2, self.b2, self.scale,
                    self.hs, self.a, self.gi, self.gh, self.cat, self.v, self.y)
        return self.y.copy()


def make_net(d, prefer_numba=True):
    if prefer_numba:
        try:
            return NumbaNet(d)
        except Exception:
            pass
    return NumpyNet(d)
