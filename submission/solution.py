"""Competition entry point: stateful features + GRU, one row at a time.

Per row: feature update (~10 us, numpy) + GRU step (~20 us with numba, ~28 us without, at
hidden 128). numba is optional: if it's missing the pure-numpy GRU is used automatically.
"""
import os

# one vCPU in the scorer: keep BLAS from spawning threads (must precede numpy import)
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMBA_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import lobfeat  # noqa: E402
import netstep  # noqa: E402


class PredictionModel:
    def __init__(self):
        # CNX_MODEL lets evaluate_local.py point at a run folder; the scorer uses model.npz here
        d = np.load(os.environ.get("CNX_MODEL", os.path.join(HERE, "model.npz")))
        if d["mu"].shape[0] != lobfeat.N_FEAT:
            raise RuntimeError(f"model.npz expects {d['mu'].shape[0]} features but lobfeat.py makes "
                               f"{lobfeat.N_FEAT}: the model was trained with a different kit version")
        self.features = lobfeat.Streamer(d["mu"], d["inv_sd"])
        self.net = netstep.make_net(d, prefer_numba=not os.environ.get("CNX_NO_NUMBA"))
        self.backend = (type(self.features).__name__, type(self.net).__name__)
        self.seq_ix = None

    def predict(self, data_point):
        if data_point.seq_ix != self.seq_ix:
            self.seq_ix = data_point.seq_ix
            self.features.reset()
            self.net.reset()
        z = self.features.update(data_point.state)
        y = self.net.step(z)            # state advances on every row, warm-up included
        if not data_point.need_prediction:
            return None
        return y
