# WunderFundRNN

### Step 1
Do baseline analysis on some of the data to predict what features could have an impact on price formation and targets.




### Improvement 1
Use much more of the data. You’ve trained on 1,900 of the ~12,500 sequences that have targets. This is the most reliable lever by a wide margin. To fit more on disk, v3 stores only the 112 raw inputs (half the size) and computes the features during training.

### Improvement 2
Average 2 models. 

### Improvement 3

Regime and trend features, with your trend toggle built in. For each of the 13 column groups (bid prices, ask volumes, trades, and so on, per instrument), v3 adds:
Activity: how many columns changed on this row, plus EWMAs of that count.
Volatility: EWMAs of the squared changes.
Trend: an efficiency ratio, |EWMA(change)| ÷ EWMA(|change|), at two horizons. It’s near 1 when a column is trending and near 0 when it’s chopping back and forth.
An optional per-column block adds each column’s drift, plus its distance from a KAMA-style adaptive average. That average speeds up while a trend persists and slows down in chop: your “larger toggle”. These go in as switchable blocks, so you can A/B them on validation rather than taking them on faith.


### Improvement 4
For your GRU, these results favour three focused experiments:
1. Separate i0/i1 state descriptors: update activity, movement size conditional on updating, and short/long movement-scale ratios.
2. Persistence and displacement features: recent changes, direction consistency and distance from causal baselines.
3. Relationships between inputs: common movements and residual disagreements among the a features, followed by cross-instrument interactions.
