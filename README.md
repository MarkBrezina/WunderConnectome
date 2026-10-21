## Introduction

I went at this competition because it popped up on Linkedin randomly. It seemed very oddly interesting and along the way I have dropped much of my desire to finish properly.
Mostly due to the fact I found out Wunderfund is a russian HFT firm, actively advertising to russians.
My family was driven out of Czechia due to russian invasion, and I am therefore strongly inclined to drop genuine participation.

However, as a person to another person, I am therefore significantly more incline to give away findings.
The actual struggle, working out of 1 laptop with at max 2gb to spare for training loops and having to spend about 9 hours per day at work as customer service.
Meant I had very limited time to run code, do experiments and let models train. I would regularly setup a training session and leave my laptop to run for the day

## Targets
Being a quant for the sake of quant, rather than for the sake of AI, ML or otherwise.
My initial goal was to figure out, what the fuck are we actually targetting?

My initial idea was to stupidly believe what Wunderfund wrote on the hero in the index screen.
We are predicting future prices, I therefore ran a range of tests to show that t0 and t1 had to do with microprice, volume weighted moving price and more.
These all fell flat and never picked up in any way. Some things did become conclusive from it in a better manner, but we'll take that later.

I than believed targets might be something more trading oriented, say optimal inventory for asset i0 and asset i1.
Which made a lot of sense, but also showed to be inconclusive.

At the end I understood, that t0 and t1 was correlated but inversely, the targets were also correlated with price.

It seemed that The targets were buying edge and sell edge, so these are "of course" related to each other.
Buy now sell later, short now buy back later are inversely correlated and as correctly can be pointed out.
Those two are inversely correlated, with a certain gap, relating to execution, slippage, fee and more.
But they are also somewhat positively related, if one says buy now sell later, t0 will be buy now, t1 will be sell later.
But in reverse, t1 will be sell now, t0 will be buyback later.

# Connectome research log

Oct 21, 2026 · @Mark

## How to read and update this log

Each hypothesis carries one verdict, the evidence behind it and the next test. When a result lands, add it to the run log, then update the register row. When a claim is walked back, add a row to the corrections log.

| Verdict | Meaning |
| --- | --- |
| Supported | Held on held-out sequences: the interval excludes zero or the pattern replicated |
| Partly supported | Part of the claim holds; the rest is untested or contradicted |
| Inconclusive | Tested, but the interval spans zero, the sample was small, or the test cannot decide |
| No gain | A model change that did not beat its matched control |
| Rejected | Tested and contradicted |
| Open | Not yet tested |

Scores from different partitions are not comparable. The uploaded reference scores 0.6457 on the focus screen and 0.6791 on the confirmation set.

| Partition | Size | Used for |
| --- | --- | --- |
| focus\_screen | 300 sequences, 580,714 scored rows | Ensemble assessments (evaluate\_next) |
| screen | 420 sequences, 797,169 scored rows | v7 matched single runs |
| calibration | 120 sequences, 24 held out | Scoring-mask model |
| confirmation | Size not recorded here | One frozen check per candidate |
| internal dev | 300 training sequences, all rows from step 99 | Checkpoint selection only |

Dev WP (about 0.40, all rows) and masked WP (about 0.63) measure different rows. Regime buckets are refitted per run: "quiet" held 85,696 rows in the regimes report and 102,785 in the v8.2 report. Compare buckets within one report only.

## Where things stand

The submission candidate is the v8.1 base with scored fine-tuning: 0.6465 masked WP on the focus screen, +0.0008 over the uploaded reference. Nothing trained since v7 comes within 0.018 of it.

&#91;embedded content: evaluate\_next.py assessments, focus\_screen partition: 300 sequences, 580,714 scored rows\]

| Item | Value |
| --- | --- |
| Packaged ZIP | submission\_v7\_best.zip (uploaded reference); not yet rebuilt for the v8.1 candidate |
| ZIP confirmation WP | 0.6791 (t0 0.6807, t1 0.6775). The challenger equalled the reference, so no improvement was shown |
| Callback speed | 75.7 µs per row; 49.8 of 60 minutes projected including start-up, if the test set matches valid in size |
| Checks passed | Model hash, model order and weights, callback/cache parity, reset, output contract, staged smoke test |
| Best single v7 run | Flow block, seed 1: 0.6346 on the 420-sequence screen |
| Leaderboard | Top score 0.672 (mid-October). v2 dropped 0.015 from valid (0.6532) to public (0.638) |

## Run log

Scored fine-tuning is the only change whose interval sits above zero every time it was compared with an unweighted fine-tune. Each row is a paired contrast on the same sequences, newest run first. Intervals are 95% whole-sequence bootstraps, conditional on the fitted seeds.

| Run | Comparison | Partition | Δt0 | Δt1 | ΔWP \[95% interval\] | Register |
| --- | --- | --- | --- | --- | --- | --- |
| v8.2 regimes | FiLM, constant context − control | focus, 300 seqs | +0.0034 | +0.0010 | +0.0022 \[−0.0003, +0.0048\] | E3 |
| v8.2 regimes | FiLM, changing context − constant context | focus, 300 seqs | −0.0041 | −0.0022 | −0.0031 \[−0.0050, −0.0013\] | E3 |
| v8.2 regimes | Uploaded reference − regimes control | focus, 300 seqs | +0.0198 | +0.0218 | +0.0208 \[+0.0149, +0.0266\] | E7 |
| v8.2 | Scored fine-tune − unweighted fine-tune | focus, 300 seqs | +0.0003 | +0.0008 | +0.0005 \[+0.0004, +0.0006\] | C4 |
| v8.2 | Scored fine-tune − parent | focus, 300 seqs | −0.0001 | +0.0006 | +0.0003 \[−0.0003, +0.0007\] | C4 |
| v8.2 | v8.1 heads + scored − v8.2 unweighted fine-tune | focus, 300 seqs | −0.0028 | −0.0006 | −0.0017 \[−0.0063, +0.0027\] | E2 |
| v8.1 | Base scored fine-tune − uploaded reference | focus, 300 seqs | +0.0004 | +0.0012 | +0.0008 \[+0.0005, +0.0011\] | C4 |
| v8.1 heads | Scored fine-tune − unweighted fine-tune | focus, 300 seqs | +0.0004 | +0.0010 | +0.0007 \[+0.0005, +0.0010\] | C4 |
| v8.1 heads | Scored fine-tune − parent (v7 heads) | focus, 300 seqs | +0.0004 | +0.0010 | +0.0007 \[+0.0005, +0.0009\] | C4 |
| v7 features | Event block − control, mean of two single runs | screen, 420 seqs | +0.0002 | −0.0013 | −0.0006 \[−0.0041, +0.0038\] | D5 |
| v7 features | Flow block − control, mean of two single runs | screen, 420 seqs | +0.0030 | +0.0024 | +0.0027 \[−0.0009, +0.0069\] | D6 |

- **Seed noise is 6–12 times what the ratchet assumes.** Seeds of one configuration differ by 0.0034 (control), 0.0040 (event) and 0.0071 (flow) on the screen. R0's 0.0006 came from the kit defaults. Flow's +0.0027 is −0.0025 for seed 0 and +0.0080 for seed 1.
- **The scoring mask is only weakly predictable.** On 24 held-out calibration sequences: AUC 0.584, average precision 0.138 against a 0.108 base rate, Brier loss 0.8% below a constant. Enough to keep the direct-mask fine-tune; not enough for a proxy-weighted long run.
- **The reference's lead is largest in chop.** Over the regimes control it leads by +0.034 \[+0.016, +0.050\] in choppy rows and +0.049 \[+0.002, +0.091\] in quiet-choppy rows, against +0.014 \[+0.010, +0.017\] in strongly active, directional rows.

## Hypothesis register

The target structure is well established (B1–B3), but almost every attempt to exploit more of it than the base GRU already does has shown no gain at matched settings (D, E). The verdict column is a dropdown: change it when the evidence changes, and say why in the evidence cell.

### A. Encoding and book structure

| ID | Hypothesis | Evidence | Verdict | Next |
| --- | --- | --- | --- | --- |
| A1 | The 22 price columns are a sorted ladder whose columns were shuffled | Sorted medians track normal quantiles (r 0.999). The home order replicates across sequences and is the same for i0 and i1. Only \~67% of held-out rows are fully in order; crossings sit in a few pairs (p4/p7 \~28%, p10/p20 \~13%). | Partly supported | Run the shape block in a GRU beside the raw columns (D7) |
| A2 | The schema split (p0–10 bid, p11–21 ask) gives a valid book | Crossed on 100% of rows when values are compared across columns. Corrected 17 Oct: the schema's sides stand; the crossing shows encoded values cannot be compared across columns. | Inconclusive | None planned |
| A3 | Prices are discrete ticks | \~500 distinct values per column and no exact repeats. A continuous transform could hide discrete ticks. | Inconclusive | Tolerance-based shift test, only if decoding becomes a priority |
| A4 | v\_k is the queue size at p\_k (pairing by suffix) | Suffix pairing matches 3 of 22 levels (i0) and 4 of 22 (i1). Lagged links exist: v17 to v14 adds \~0.19 held-out R² (i0). | Rejected | Test the lag links as features |
| A5 | p0 is the touch level | p0 sits deep (−1 to −2.2) and never crossed p1 in 2,000 rows. Corrected 17 Oct: per-column transforms mean raw position cannot settle it. | Inconclusive | None planned |
| A6 | An i0 price event re-encodes the whole book | All 22 columns change on 96–97% of i0 price-event rows; the first principal component holds 56% of change variance (i1: 91–92%, 45%). | Supported | — |
| A7 | Consecutive events flicker back and forth | Event-lag correlation alternates sign out to ±150 events. Large single-column jumps retrace 53–66% within 8–32 rows. | Supported | Count only events that do not revert within 1–2 events |
| A8 | t0 and t1 are sums of p×v | 0% tolerance matches, \|r\| ≤ 0.13; −0.0037 WP as features. | Rejected | — |
| A9 | i0 and i1 share each column's home value | Identical medians and snapshot values. | Supported | Basis i0\_pk − i1\_pk against its own EWMA (N3) |

### B. Targets

| ID | Hypothesis | Evidence | Verdict | Next |
| --- | --- | --- | --- | --- |
| B1 | The targets are a smoothed future move over \~100–200 rows | ACF 0.97 at lag 1, 0.45–0.6 at lag 100, \~0 by 500–1,000. Flat on 97% of rows; 21% of values exactly zero. | Supported | — |
| B2 | The targets change only on i0 price-event rows | P(change \| no i0 price event) = 0.000; lift 9.2. The reverse does not hold: one inner-rank trigger changed t0 on \~35% and t1 on \~34% of its rows. | Supported | Between i0 events the target is constant; test an output-update gate (N5) |
| B3 | The targets react to the current and the next i0 event | Signature peaks at k = 0 and k + 1, \|r\| 0.34–0.54 (50 sequences); i1 events show \~0. The k + 1 peak uses a future event, so it is a diagnostic only. | Supported | — |
| B4 | t0 is the long round-trip edge and t1 the short one, sharing a cost | t1 = −0.976·t0 + s; s is negative on 90% of rows and t0 + t1 < 0 on 87%. The other 13% is not yet split into zero and positive. The trading meaning remains a working interpretation. | Partly supported | Report negative, zero and positive shares of t0 + t1 before any sign constraint |
| B5 | The shared cost tracks the inner gap | Correlation −0.19 in levels, −0.35 within sequences, −0.76 in first differences. R² of the target sum: gap alone 0.03, all prices 0.22, richer state 0.25. | Partly supported | — |
| B6 | Deriving t1 from a t0 prediction plus a gap model beats predicting t1 directly | Derived 0.541 against 0.663 direct (100 valid sequences); best stacked blend +0.0007. The GRU's implied gap already beats the gap model (corr 0.463 against 0.417). | Rejected | — |
| B7 | The opposing factor (z0 − z1) is the predictable part | It holds 82–88% of the variance, but the common factor is more predictable: linear R² 0.23–0.24 against 0.05–0.07. | Rejected | — |
| B8 | The targets relate to future displacement of the i0 columns | \|r\| 0.10–0.17 at 200–1,000 rows, same sign from train to dev (diagnostic). | Partly supported | Use as an auxiliary training target (N4) |
| B9 | The alternating auxiliary sum −a0 + a1 − … + a7 tracks the targets | Held-out R² ≤ 0. | Rejected | — |
| B10 | t0 and t1 swap roles (buy and sell) in some states | No evidence. Their relative strength reverses and feature associations can flip; the identities have not been shown to swap. | Open | Keep fixed t0 and t1 outputs, with no swap rule |

### C. Scoring mask

| ID | Hypothesis | Evidence | Verdict | Next |
| --- | --- | --- | --- | --- |
| C1 | Scored rows are easier to predict than the rest | Same 300 sequences: masked WP 0.627 against 0.485 on all eligible rows (v8.2 control). Earlier: dev on all rows \~0.43 against valid on scored rows \~0.655. | Supported | — |
| C2 | Scored rows are enriched on i1 price changes | Share of rows scored (120 calibration sequences): neither instrument changed 9.01%, only i0 6.49%, only i1 14.86%, both 14.88%. | Supported | — |
| C3 | The mask can be predicted from causal inputs | AUC 0.584; average precision 0.138 against a 0.108 base rate; Brier loss 0.8% lower (24 held-out sequences). Weak. | Partly supported | Defer proxy-weighted training |
| C4 | Fine-tuning toward scored rows raises masked WP | Beats an unweighted fine-tune in both runs (+0.0007, +0.0005) and the base gains +0.0008 over its parent, all intervals above zero. v8.2 against its own parent is inconclusive. See run log. | Supported | Keep in every final model |
| C5 | The mask favours rows where t0 or t1 change | Not tested directly. Leans against: targets change only on i0 price rows, yet rows where only i0 changed are scored less often (6.5%) than rows with no price change (9.0%). | Open | Notebook: P(scored \| target changed) against unchanged, and the share of scored weight on unchanged rows (N2) |

### D. Features

| ID | Hypothesis | Evidence | Verdict | Next |
| --- | --- | --- | --- | --- |
| D1 | Smoother residuals (x − EWMA, SMA, WMA) add information | Horizons lab +0.0055 \[+0.0014, +0.0085\] (20 train, 8 dev sequences). Later probes +0.0008 and +0.0088, both intervals spanning zero. GRU pilot: t0 +0.032, t1 −0.032. In the kit as 12 residuals, one horizon each (mostly 512 rows); never ablated alone at scale. | Inconclusive | Multi-horizon residuals per price (N7); ablate against none at matched settings |
| D2 | Momentum x\[t\] − x\[t−w\] | +0.0005 and −0.006. | Rejected | — |
| D3 | Volatility of changes (std, RMS, mean absolute) | +0.0031 \[−0.0065, +0.0110\] and −0.0097. Model WP still differs by volatility bucket (0.457 against 0.683 in one research model). | Inconclusive | Level std, change std and jump concentration as separate measures |
| D4 | Timing features (ages, shocks, update-clock EWMA) | Ridge −0.016 \[−0.031, −0.001\]. | Rejected | Superseded by the event block |
| D5 | Event block (40: ages, intervals, persistence, event-clock EWMAs) | GRU, two seeds: −0.0006 \[−0.0041, +0.0038\]. | No gain | Recheck only on a matched-settings base |
| D6 | Flow block (36: volume, dp and dv update statistics) | GRU, two seeds: +0.0027 \[−0.0009, +0.0069\]; the seeds disagree (−0.0025 and +0.0080). | Inconclusive | Retest on a matched-settings base (N1) |
| D7 | Shape block (26: sorted ladder, central gap, centre, range) | Built in v7; never run. | Open | One matched two-seed run (N8) |
| D8 | Context block (14: expanding-prefix statistics) | Built in v7; never run. The per-sequence mean oracle (0.695) says sequence-level information is worth having. | Open | One matched two-seed run (N8) |
| D9 | Group state descriptors (activity, RMS scale, efficiency) | COMP\_TEST: t0 +0.087, t1 −0.018 on 6 sequences; interval spans zero. The legacy regime block (91) has never run. | Inconclusive | — |
| D10 | Break detectors (AR innovations, CUSUM, Shiryaev–Roberts) | AR(level) −0.013; Shiryaev–Roberts −0.020 with interval below zero. | Rejected | — |
| D11 | Auxiliary inputs a0–a7 as compressed or dynamic features | −0.001 and +0.0005; −0.030 when added to the masked-auxiliary variant. | Rejected | — |
| D12 | Raw i1 inputs help the GRU | Pilot: masking i1 gave +0.045 \[+0.003, +0.076\] (32 train, 12 valid sequences, 2 epochs, 1 seed). Ridge with i0 + i1 0.403 against i0 alone 0.433. Signed lead-lag \|r\| < 0.01. Never tested at scale; every current model includes i1. | Inconclusive | i1-masked ablation at matched settings plus a lead-lag test on GRU residuals (N3) |
| D13 | Volume imbalance by index half | Below noise on one sequence; index halves mix the two ladder sides. | Inconclusive | Retest on sorted sides |
| D14 | Own-column reversion predicts the targets | r −0.30 to −0.62 against the column's own next change; mechanical (flicker plus shared current value). | Rejected | — |
| D15 | Volatility changes how book moves map to the targets | corr(Δp0, target) 0.02 at low volatility, 0.07–0.12 at high. | Partly supported | — |
| D16 | Book-features lab (1,261 features in 12 families) | Built 17 Oct; results not yet logged here. | Open | Promote a family only if ridge and GRU stacking both clear zero |

### E. Architecture and training

| ID | Hypothesis | Evidence | Verdict | Next |
| --- | --- | --- | --- | --- |
| E1 | More data and seed averaging help | R0 0.6551, two-seed pair 0.6570 (+0.0019, 600 valid sequences). The full-data model is the reference family. | Supported | — |
| E2 | Separate t0 and t1 heads beat a shared head | Against the v8.2 unweighted fine-tune −0.0017 \[−0.0063, +0.0027\]; against the regimes control +0.0008 \[−0.0028, +0.0039\]. Earlier pilot −0.003. | No gain | Defer |
| E3 | FiLM regime conditioning helps | Constant context +0.0022 \[−0.0003, +0.0048\] over control; changing context −0.0031 \[−0.0050, −0.0013\] against constant, worst in active (−0.0036) and directional (−0.0045) rows. Any gain comes from the extra layer, not the regime signal. | Rejected | Defer until the base is competitive |
| E4 | Soft GMM regime experts | t0 0.503 and t1 0.386, both below the single model; difference interval below zero (6 sequences). | Rejected | — |
| E5 | Correlation-hybrid loss | 0.4394 against 0.4535 for two-head MSE (pilot). | No gain | — |
| E6 | Row TCN beside the GRU, skip MLP, weighted Huber | TCN 0.4510 against 0.4563 baseline; skip MLP −0.042; weighted Huber −0.019 (pilot). | No gain | — |
| E7 | The \~0.02 gap to the reference comes from the training setup, not the architecture | Post-v7 ensembles score 0.624–0.628; the reference family 0.6457–0.6465 on the same sequences. The lead is largest in chop. The v7 runs used 2,500 sequences, 4 sequences per step and 256-row backprop chunks; the kit defaults are 32 and 1,000, and the reference used all \~10,000 sequences (to confirm). v8.2, described as larger, still scored 0.6279. | Open | Retrain the control with one setting matched at a time (N1) |
| E8 | Auxiliary state targets (event timing, future i0 moves) improve the shared representation | Never trained. Auxiliary-input tests (D11) are a different thing. | Open | N4 |
| E9 | An output-update gate (hold or revise the last prediction) helps | Proposed 21 Oct, motivated by B2. Untested. | Open | N5 |

### F. Regimes and where the score is

| ID | Hypothesis | Evidence | Verdict | Next |
| --- | --- | --- | --- | --- |
| F1 | Model accuracy differs by regime | R0 pair: trending 0.81 against chop 0.39–0.43; quiet 0.41 against busy 0.76; volatility fifths 0.52, 0.71, 0.61. Descriptive, not causal. | Supported | — |
| F2 | Feature–target associations vary across sequences and states | One p0 EWMA residual: r from 0.012 to 0.302 across 16 sequences; some conditional correlations change sign. Predicting when they change has not been shown. | Supported | — |
| F3 | Explicit regime adaptation improves WP | Interaction test 0.545348 to 0.544998 (t0 up, t1 down); state interactions no gain; FiLM's regime signal hurt (E3); experts worse (E4). | No gain | Revisit only if per-bucket calibration slopes differ on a competitive base |
| F4 | Rescaling by volatility recovers the per-sequence scale | Feasible proxy +0.0007; true volatility buckets +0.003; per-sequence scale oracle 0.671. Scale tracks how predictable a sequence is more than how volatile. | Rejected | Online self-calibration is the remaining route (N11) |
| F5 | The heaviest sequences carry the score | Top fifth by scored-row count: 44% of metric weight at WP 0.576, against 0.70–0.75 for the other fifths. | Supported | Profile them (N10) |

## Corrections log

Nineteen claims have been walked back so far; most overstated what the encoded book can tell us. Newest first.

| Date | Original claim | Correction | Consequence |
| --- | --- | --- | --- |
| 21 Oct | Seed noise is 0.0006, so a 0.001 change is real | That was R0 at the kit defaults. The v7 laptop runs differ by 0.003–0.007 between seeds | Two-seed ensembles and paired intervals at minimum; re-measure the ratchet threshold at the settings in use |
| 21 Oct | FiLM gives the model regime adaptation | Its constant-context control matched it; the changing regime signal cost −0.0031 | E3 Rejected as built; defer FiLM |
| 21 Oct | Scoring follows i1 because the targets move with i1 | i1's link to the mask is established. The targets change only on i0 price rows. i1 leading i0 is untested | Test lead-lag on GRU residuals before building on it (N3) |
| 21 Oct | Volatility has little effect | Volatility features gave no reliable gain, but WP differs a lot by volatility bucket (0.457 against 0.683) | Treat volatility as untested in better forms, not as irrelevant |
| 21 Oct | t0 and t1 swap identities in some states | Their relative strength reverses; the identities have not been shown to swap | Keep fixed outputs, no swap rule (B10) |
| 21 Oct | A column such as p3 changing means a level cleared or a queue moved | Rank swaps fit several mechanisms; no trade, cancel or queue meaning is established | Name features by what they measure (rank flip), not by mechanism |
| 17 Oct | The 12 selected EWMAs are 12 prices with one EWMA each | Earlier lab: span-100 and span-256 residuals of 6 prices plus v15; 12 of 22 prices never had one. v7: all 22 screened at half-lives 8, 32, 128 and 512 rows, 12 kept with one horizon each | Multi-horizon residuals per price remain untested in the kit (N7) |
| 17 Oct | Normal-quantile medians (r 0.999) prove one shared transform | They do not. Sorting is a useful representation, not a decode | Add sorted features beside the raw columns, never instead without an ablation |
| 17 Oct | The schema's bid/ask split is rejected | The schema's sides stand; the crossing shows values cannot be compared across columns | A2 to Inconclusive |
| 17 Oct | p0 is not the touch level | Per-column transforms mean raw position cannot settle it | A5 to Inconclusive |
| 17 Oct | Prices are not discrete | A continuous transform can remove exact repeats | A3 to Inconclusive |
| 17 Oct | The k + 1 event signature is predictive | It uses an event not yet seen at prediction time | Diagnostic only; live features use past events |
| 17 Oct | An upward encoded slope means buy | Encoded coordinates can move without an executable price rise | Test slope against both targets on held-out sequences |
| 17 Oct | Rolling correlations with the targets can be features | Targets are unavailable at inference | Use input–input correlations only |
| 17 Oct | +0.04 on the heaviest fifth adds +0.018 overall | Pooled WP is not additive by bucket | Recompute global weighted moments from the candidate's predictions |
| 17 Oct | t0 + t1 < 0 on 87% of rows means the cost is always paid | The other 13% may be zeros rather than positives | Report negative, zero and positive shares before any sign constraint (B4) |
| 17 Oct | The auxiliary-input tests covered auxiliary targets | Different things; no auxiliary-target head has been trained | E8 stays Open |
| 17 Oct | The oracle scores (0.671, 0.695) are attainable gains | They use labels unavailable at inference | Ceilings only, not expected gains |
| 17 Oct | Overlapping rows give independent tests | Rows are autocorrelated and features were screened many times | Resample whole sequences, fix shortlists, keep confirmation untouched |

## Feature map

Three feature ideas have GRU results at scale (event, flow, FiLM regime context) and none cleared zero; scored fine-tuning is the only addition that did. Kit = the v7/v8 training kit (361 slots in next mode); lab = the 17 Oct book-features lab. The ask column refers to the six numbered feature requests in the write-up.

| Idea | Ask | Kit features (slots) | Lab features | GRU result | Register |
| --- | --- | --- | --- | --- | --- |
| Distance from a recent level (reversion) | 1 | ewma: 12 residuals, one horizon each (225–236) | ewm (401): 22 raw prices, 22 sorted levels and 5 summaries × spans 8–1,024; crossovers | In every v7/v8 model; never ablated alone | D1 |
| Busy against quiet, trend against chop | 2 | activity (8: 237–244); legacy regime (91) | activity (96: 4–1,024 rows) | Activity in every model; regime block never run | D9 |
| Event clock, persistence, flicker | 2 | event (40: 245–284) | events (66), cross (25), focus (78: p0, p3, p7, p17, p10, p20) | −0.0006 \[−0.0041, +0.0038\] | D5 |
| Volume and trade-column flow | — | flow (36: 285–320) | — | +0.0027 \[−0.0009, +0.0069\]; seeds disagree | D6 |
| Whole-book shape, best levels, gap | 3 | shape (26: 335–360) | ladder (83: three best-level rules, gaps, ranks, carried volumes) | Not run | D7 |
| Sequence-level context | — | context (14: 321–334) | — | Not run | D8 |
| Book trend and slope (buy or sell pressure) | 4 | legacy trend (224: drift, KAMA distance) | trend (80: OLS slope 12–1,024 rows), percol (198) | Not run | Open |
| Chunkiness (spread of levels and changes) | 5 | — | chunk (88: level and change std, cross-sectional std, 12–1,024 rows) | Not run | Open |
| Rolling correlations, regime-dependent importance | 6 | FiLM regime context | rcorr (21: side against side, i0 against i1, price against volume) | FiLM regime signal −0.0031 | E3 |
| Cross-instrument lead-lag and relative value | — | Raw i1 inputs and changes (52–103, 164–215) | — | Never ablated at scale; the pilot favoured masking i1 | D12 |
| Scoring-mask awareness | — | Scored fine-tune (direct mask) | Mask proxy model | Fine-tune +0.0005 to +0.0008; proxy AUC 0.584 | C3, C4 |

The event and flow descriptors are i0-only. No i1 event features exist yet, so the lead-lag idea has no dedicated features to test.

## Open ideas and backlog

The four Now items are notebooks or single matched runs; none needs new architecture. Sorted by priority.

| ID | Idea | Why | Cost | Priority |
| --- | --- | --- | --- | --- |
| N1 | Match the reference's training settings (data size, sequences per step, chunk length), one setting at a time | E7: the 0.02 gap dwarfs every architecture effect measured so far | Desktop runs, no new code | Now |
| N2 | Test whether the mask favours rows where t0 or t1 change | C5; decides whether to weight training toward update rows | Notebook, no training | Now |
| N3 | i1's role: an i1-masked ablation at matched settings, plus a test of whether recent i1 history predicts GRU errors after conditioning on i0 history | D12's pilot and C2's mask enrichment pull opposite ways | Notebook plus two runs | Now |
| N10 | Profile the heaviest sequences: i1-only row share, i0 event rate, volatility, efficiency ratio | F5: 44% of the weight at WP 0.576 | Notebook | Now |
| N4 | Auxiliary training heads: P(next i0 price event within 1, 4, 16, 64 rows); future moves of a few train-fitted i0 price factors at 4, 16, 64 rows; optionally t0 + t1. Keep the direct path to t0 and t1 | B2, B8; the target is flat 97% of the time, so its gradient is sparse | Training only; dropped at inference | Next |
| N5 | Output-update gate: ŷt = (1 − g)·ŷt−1 + g·bt, one gate each for t0 and t1, recurrent state still updated every row | B2: between i0 events the target is constant | Small; tiny inference cost | Next |
| N7 | Multi-horizon EWMA residuals per price in the kit | D1; write-up ask 1 | Small | Next |
| N8 | Shape and context blocks in matched two-seed runs | D7, D8 | Two runs each | Next |
| N12 | Full-history training: carry recurrent state from step 0 instead of a zero-state warm-up | Slow units never learn sequence context; may feed E7 | Code change | Next |
| N6 | Zero-initialised causal TCN correction after the GRU (16 channels, 31 rows) | Short lead-lag patterns a GRU blurs | Live compute | Later |
| N9 | Per-target blend weights, fitted on dev, frozen, then confirmed | Additions often help one target and hurt the other | Small | Later |
| N11 | Hindsight reconstruction feeding online self-calibration | F4: scale oracle 0.671, volatility explains little | Go/no-go first: build if reconstruction corr ≥ 0.9, drop if < 0.7 | Later |
| N13 | Distil a larger ensemble into one model | Seed averaging gave +0.0019 | Teachers trained offline | Later |
| N14 | GRU plus compiled GBDT blend | Different model families blend better than seeds | Medium | Later |
| N15 | Inference speed: fp16 weights, skip the head when no prediction is needed | 75.7 µs per row leaves about 10 minutes of the 60 | Medium | Later |
| N16 | FiLM, row TCN, more seeds of heads or flow | E2, E3: no gain so far | — | Deferred |

## Evidence standard

A change is promoted only when a two-seed ensemble beats its matched control on the same sequences with an interval above zero.

1. Same partition, paired by sequence, with a whole-sequence bootstrap of pooled WP.
2. Two seeds per arm, compared as ensembles. At the laptop settings a single seed swings by up to 0.007.
3. Both targets reported. A change that helps one and hurts the other is not a win until a per-target blend says otherwise.
4. An interval spanning zero is inconclusive, not a small win.
5. Regime buckets compared within one report only; bucket gains do not add up to the pooled score.
6. A feature family earns a kit run when base + family clears zero in the ridge test and GRU + family clears zero in the stacking test.
7. One frozen confirmation per candidate, on sequences never used for selection.
8. Before upload: a full callback benchmark with the projected time comfortably under 60 minutes.

## Next steps

Explain the 0.02 gap before any new architecture: until the base matches the reference, every comparison is made on a handicapped model.

- [ ] Write the reference's exact training settings next to v7, v8.1 and v8.2: sequences, epochs, sequences per step, chunk length, window, burn-in, feature blocks.
- [ ] On the desktop, retrain the v8.2 control with one setting moved toward the reference: first sequences per step and chunk length (the laptop's memory limit), then data size. Two seeds, focus screen (N1).
- [ ] Notebook: does the mask favour rows where t0 or t1 change (N2)?
- [ ] Notebook: profile the heaviest sequences (N10) and test i1 lead-lag on GRU residuals (N3).
- [ ] Read the book-features lab results; promote at most one or two families (D16).
- [ ] On a competitive base only: auxiliary heads (N4), then the output gate (N5), each against a matched control.
- [ ] Package the v8.1 base + scored fine-tune and benchmark the full callback before uploading.

## Adding an entry

One result usually touches three places: a run-log row, a register verdict, and sometimes a correction. Copy the matching row shape below into its table.

```markdown
Run log:     | <run> | <candidate> − <control> | <partition, seqs> | Δt0 | Δt1 | ΔWP [low, high] | <register ID> |
Register:    | <next free ID in its group> | <claim, stated so it can fail> | <test, partition, seeds, numbers> | <verdict> | <next test> |
Correction:  | <date> | <claim as first stated> | <what the evidence supports> | <what changes: verdict, feature, plan> |
Backlog:     | N<next> | <idea> | <register ID it answers> | <runs or notebook> | <priority> |
```

State every hypothesis so that a result could prove it wrong. Record the seeds, partition and interval with every number.




