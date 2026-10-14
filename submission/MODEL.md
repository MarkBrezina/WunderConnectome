# Model

Stateful GRU on the 112 inputs, their first differences and time (see lobfeat.py).

## config.json
```
{
 "prep": "prep",
 "out": "runs\\gru128",
 "hidden": 128,
 "layers": 1,
 "head": 64,
 "batch": 32,
 "chunk": 1000,
 "window": 5000,
 "burn_in": 1000,
 "threads": 0,
 "epochs": 12,
 "lr": 0.002,
 "wd": 0.0001,
 "warmup_steps": 300,
 "ema": 0.999,
 "dev_frac": 0.05,
 "max_train_seqs": 0,
 "max_dev_seqs": 400,
 "eval_valid_each_epoch": false,
 "amp": false,
 "device": "auto",
 "seed": 0
}
```

## summary.json
```
{
 "best_epoch": 10,
 "dev_wp": 0.45383084332033735,
 "valid_wp": 0.653240824858575,
 "valid_t0": 0.6536292463920135,
 "valid_t1": 0.6528524033251367,
 "out_scale": 0.8546100945766015
}
```
