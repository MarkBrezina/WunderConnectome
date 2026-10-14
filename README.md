# WunderFundRNN

### Step 1
Do baseline analysis on some of the data to predict what features could have an impact on price formation and targets.

rejects the straightforward price×volume target formula.


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


The reversion table is promising, but its percentage needs careful interpretation. For i0_p0, you have approximately:
- Displacement/future-change correlation: −0.398.
- Opposing-direction share among active pairs: 77.9%.
This says that when the encoded component changes, its next change often points against its displacement from the past EWMA.
shows persistent levels with short-lived reversal in changes

reveals strong relationships between some additional features
a0, a4	Changes	0.907
a2, a3	Levels	0.864
a2, a3	Changes	0.842
a1, a4	Changes	0.821



### Improvement 4
For your GRU, these results favour three focused experiments:
1. Separate i0/i1 state descriptors: update activity, movement size conditional on updating, and short/long movement-scale ratios.
2. Persistence and displacement features: recent changes, direction consistency and distance from causal baselines.
3. Relationships between inputs: common movements and residual disagreements among the a features, followed by cross-instrument interactions.

The target table shows related but distinct outputs. In the displayed sequences, t0 and t1 have correlations roughly between −0.62 and −0.94.


For regime detection, I would give each instrument its own state vector first.
keep GRU128 and the training sample fixed: test raw inputs + changes, then add separate instrument state features, then add cross-instrument interactions.

State dimension	Features to test separately for i0 and i1
Activity	Recent update frequency; fraction of components changing; time since each group last changed
Movement size	RMS or absolute changes after accounting for component scales
Volatility expansion	Short-horizon movement scale divided by long-horizon scale
Persistence	Whether recent changes consistently continue in the same direction
Displacement	Distance from a past-only EWMA, scaled by recent movement
Response between instruments	Recent change correlation, update timing and whether one instrument’s changes precede the other’s
