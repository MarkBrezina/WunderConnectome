# Connectome research log

Mark Brezina · Revised 21 October 2026

This is the working account of the project: what I observed, what I think might explain it, what I tested, and what should change next. Hypothesis IDs refer to the supplied `HYPOTHESIS_REGISTER.md`. The numbered experiments below are a shortlist within that larger register, not twenty independent discoveries.

## 1. Introduction

I came across the Connectome competition on LinkedIn and joined because the problem looked unusually interesting. My interest in pursuing the competition seriously later declined for personal and historical reasons. My family was displaced by the Soviet invasion of Czechoslovakia, and my concerns about the organiser's Russian connections changed how I felt about participating. I became more interested in documenting and sharing the research.

The practical constraints also shaped the project. I worked mainly on a laptop with roughly 2 GB of RAM available for training, alongside a customer-service job taking about nine hours of my day. Many experiments consisted of preparing a run in the evening and leaving the laptop working while I was at work. These constraints affected batch sizes, backpropagation lengths and the number of comparisons I could complete.

My starting point was quantitative research: before changing architectures, I wanted to understand what the inputs and targets represented. I explored price-like components, numerical weighted sums, event timing, target relationships and possible execution-edge interpretations. Some tests revealed useful statistical structure. Others mainly exposed assumptions that needed correcting.

The aim of this log is to preserve both outcomes. A plausible market explanation is a hypothesis; a repeatable association is evidence; a better held-out competition score is a separate result.

## 2. Current position

The strongest returned model on the common 300-sequence focus screen remains the **v8.1 base ensemble with scored-row head fine-tuning**, at **0.646531 masked WP**. The newer heads/flow and FiLM recipes have not replaced it.

My current description is a single GRU trained on all approximately 10,000 training sequences. The attached older commands use `hidden=128`; **112 is the raw input count**, not evidence of a hidden size. If the newest model really has 112 hidden units, that belongs in its own run manifest. Its exact checkpoint/configuration and a matched score are needed before treating it as identical to the frozen reference.

| Decision | Current position |
| --- | --- |
| Submission candidate | Preserve the strongest base-scored ensemble while testing challengers. |
| Separate nonlinear t0/t1 heads | No repeatable matched gain established; defer further complexity here. |
| Changing FiLM context | The tested signal hurt relative to constant context; defer this implementation. |
| More data | Reported as useful historically; the latest larger run changed other settings too. A clean learning curve remains useful. |
| Rolling and emergent behaviour | Still plausible. Test compact joint dynamics against the competitive GRU's remaining errors. |
| Next substantial training | Reproduce the stronger base recipe, then test one justified addition. |

The reported leaderboard benchmark of **0.672** is a historical comparison from the project notes, not a freshly verified leading score. The reference's **0.679120 local confirmation score** uses another sample and does not show that it beat that leaderboard. No fixed local-to-leaderboard offset has been established.

## 3. Data and objective

The official specification describes 112 inputs. Both targets concern the future movement of **i0**; their exact formulas are undisclosed. The second instrument, i1, is an input. Documented bid/ask membership is determined by the index group, while index is not depth order. [S1]

| Inputs | Count |
| --- | ---: |
| i0: 22 price-like, 22 volume-like, 4 trade-price, 4 trade-volume | 52 |
| i1: corresponding groups | 52 |
| a0–a7 | 8 |

The supplied parquet-derived notebook inventory reports 10,607 train and 1,873 validation sequences, each containing 20,000 rows. These counts describe those files, rather than how many sequences a particular fit actually used.

WP pools the selected rows globally, separately by target, then averages the two correlations. Selection is `need_prediction AND is_scored`; targets and predictions are clipped to [-2, 2], with weight equal to the absolute clipped target. The callback receives neither targets nor `is_scored`. [S1]

For a fixed target, let y and p denote the clipped labels and predictions, and w = |y|. The corresponding weighted correlation is

$$
r_w = \frac{\sum_i w_i(y_i-\bar y_w)(p_i-\bar p_w)}
{\sqrt{\sum_i w_i(y_i-\bar y_w)^2\sum_i w_i(p_i-\bar p_w)^2}}.
$$

Consequences for this project:

- Average predictions first, then recompute WP. Averaging the scores of individual runs does not score an ensemble.
- Keep masked and all-eligible-row results separate. Neither a mean of sequence correlations nor a mean of regime correlations is the official global score.
- A flat target can have substantial weight and still require an updated prediction as new information arrives.
- Positive affine rescaling leaves an unclipped Pearson correlation unchanged. Clipping can make output scaling matter; it should be tested separately.
- The two targets use different magnitude weights. Ordinary Pearson correlation is symmetric; differently weighted target comparisons can be asymmetric without implying directional influence.

State must advance on every row and reset between sequences. The stated execution budget is one CPU core, 16 GB RAM and 60 minutes for the complete test set. [S2]

## 4. Evidence language and updating rules

Each hypothesis needs **two statuses**: one for the proposed explanation and one for predictive usefulness. Descriptive evidence for a regime does not establish a benefit from regime conditioning.

| Status | Meaning |
| --- | --- |
| Observed | A numerical regularity in the stated sample; mechanism is unresolved. |
| Supported in this comparison | The specified candidate improved under the recorded protocol. Generalisation still depends on validation history. |
| Inconclusive | The test cannot distinguish a useful effect from noise or has insufficient coverage. |
| Against this implementation | The tested version underperformed or contradicted the stated claim. |
| Confounded | Multiple changes prevent attribution. |
| Implemented, result incomplete | Code or partial output exists; a completed comparison does not. |
| Open | A proposal without an adequate test. |
| Oracle only | Uses labels or future information unavailable to the live model. |

Keep failed versions in the record. Replace broad language such as “volatility is irrelevant” with “this volatility block did not improve this model under this protocol.” Do not count a synthetic software test as market evidence.

## 5. Scores that can be compared

### 5.1 Common focus screen: actual prediction ensembles

All rows in this table use the reported **300 sequences and 580,714 scored rows**. Equal seed weighting was used; these are prediction ensembles, not averages of individual scores.

| Recipe | t0 | t1 | Masked WP | All-eligible WP |
| --- | ---: | ---: | ---: | ---: |
| Original uploaded reference | 0.646955 | 0.644503 | 0.645729 | 0.512908 |
| v8.1 base + scored fine-tuning | 0.647388 | 0.645674 | **0.646531** | 0.512825 |
| v7 heads/flow parents | 0.625810 | 0.624191 | 0.625001 | 0.483148 |
| v8.1 heads/flow + scored fine-tuning | 0.626223 | 0.625183 | 0.625703 | 0.483249 |
| v8.2 larger heads/flow parents | 0.629338 | 0.625930 | 0.627634 | 0.484869 |
| v8.2 larger heads/flow + unweighted fine-tuning | 0.629012 | 0.625747 | 0.627380 | 0.484524 |
| v8.2 larger heads/flow + scored fine-tuning | 0.629278 | 0.626504 | 0.627891 | 0.484478 |
| Regimes: ordinary control | 0.627147 | 0.622719 | 0.624933 | 0.480951 |
| Regimes: constant FiLM context | 0.630533 | 0.623722 | 0.627127 | 0.482917 |
| Regimes: changing FiLM context | 0.626462 | 0.621507 | 0.623985 | 0.478720 |

| Paired contrast | ΔWP | Reported 95% sequence interval | Interpretation |
| --- | ---: | --- | --- |
| Base-scored − uploaded reference | +0.000802 | [+0.000455, +0.001130] | A small supported improvement on this screen. |
| Heads/flow-scored − its parents | +0.000702 | [+0.000541, +0.000855] | Fine-tuning helps this weaker family too. |
| Larger-scored − its unweighted fine-tune | +0.000511 | [+0.000368, +0.000646] | Supports the fine-tuning choice. |
| Larger-scored − earlier heads/flow-scored | +0.002188 | [-0.002206, +0.006750] | Inconclusive; not a clean data-size experiment. |
| Larger-scored − best base-scored | -0.018640 | [-0.026922, -0.009269] | This newer recipe is materially weaker here. |
| Constant FiLM − ordinary control | +0.002195 | [-0.000253, +0.004784] | Extra capacity alone has no confirmed win. |
| Changing FiLM − constant FiLM | -0.003143 | [-0.004986, -0.001297] | Against the tested changing-context mechanism. |

Intervals condition on the fitted models/seeds and their actual validation history. They do not account for every hypothesis tried, seed uncertainty or distribution shift. The broad reference-versus-heads/flow gap cannot be attributed to separate heads alone: features, training budgets and other settings differ.

### 5.2 Other samples: preserve their scope

| Evidence | Population | Result | What it establishes |
| --- | --- | --- | --- |
| v7 event/flow comparison | 420 screening sequences, 797,169 scored rows; two seeds | Event mean-run ΔWP -0.000593 [-0.004094, +0.003822]; flow +0.002739 [-0.000854, +0.006921] | Neither is a demonstrated ensemble win. Flow seeds disagree. |
| Book lab: Ridge family tests | 48 TRAIN, 100 validation sequences | Base 0.5389; ladder 0.5448; events 0.5555 | Some families help a simpler model. |
| Book lab: frozen-GRU stacking | Same 100 validation sequences, sequence cross-fitting | GRU-only about 0.6674; per-column family about +0.0005 and events about +0.0004, both intervals crossing zero | Linear family gains largely fail to add to this GRU. |
| v3 Ridge study | 64 TRAIN / 64 dev; another 64 reserved within this plan | i0 control 0.566015; full control 0.569622; events 0.570452 | Events/full inputs have higher point scores, with inconclusive contrasts versus i0 control. |
| v3 state interactions | Same 64 dev sequences | Interactions − additive state: -0.003150 [-0.007383, +0.000474] | No supported adaptive-weight benefit. |
| v3 frozen-GRU correction | Only **5 of 64** planned dev sequences had complete cached predictions | Raw 0.489361; all correction families lower | Coverage is too limited for a general conclusion or broad confirmation. |
| Expanded lab: Ridge | 32 TRAIN / 16 dev | Full 0.495236; i0-only 0.549176; full+volatility 0.513908 | Pilot evidence; the volatility addition is positive here but not a production GRU result. |
| Expanded lab: GRU | Small pilot, two intended seeds, eight intended epochs | Several fits are recorded; the saved cell ends during book seed 1, epoch 3 | Treat as partial. There is no completed suite/ensemble table in the saved output. |
| Old packaged-reference confirmation | Different local confirmation population; size not recorded here | WP 0.679120; t0 0.680711, t1 0.677530 | Challenger was the unchanged reference. Zero difference demonstrates no new gain. |

The expanded pilot's epoch-to-epoch scores also vary substantially. Audit its optimisation, state handling and fixed-epoch results before extending it. Do not select the best displayed epoch on the screening set after the fact.

The v3 plan is disjoint internally. Its own note says earlier use and base-GRU validation exposure are unknown. “Reserved by this notebook” therefore does not certify a historically untouched holdout.

## 6. What the targets and book appear to do

### Numerical structure

The price-like columns have a stable approximate numerical median order in the decoder samples. About 67% of held-out rows follow that full order; some pairs cross frequently. Many columns change together. These are useful observations about the encoded representation.

They do not recover physical touch, monetary spread, tick size, volume units, order clearance or queue inheritance. In particular, sorting across all 22 encoded values cannot override documented bid/ask membership. A rank change of an encoded component is not the position of an individual order in a price-time queue.

Suffix pairing tests were not decisive. Their failure does not disprove the documented price/volume grouping or identify a new pairing. A lag such as previous v17 predicting current v14 remains a numerical association until its physical interpretation is independently established.

### Target structure

t0 and t1 are strongly related, with opposing and shared components. The often-negative sum is compatible with a long/short edge interpretation, but does not identify it. The earlier “negative on about 87% of rows” statistic leaves zeros and positive sums unresolved in the remainder. Do not force a nonnegative cost or swap target identities by regime.

High autocorrelation does not identify an exact 100–200-row target construction. Likewise, flatness is population dependent: one earlier sequence had roughly 97% flat rows, while broader studies show roughly 10–11% update rates under their own definitions.

Some target-change diagnostics align closely with i0 price events. That does not imply the estimate should stay fixed between events. i1 inputs can revise beliefs about an unchanged hidden target.

### Lead–lag and reversal evidence already available

The v3 notebook directly tested the illustrative i1_p6 lead of three rows. Correlations with subsequent target changes were **-0.00045 for t0 and +0.00078 for t1**, with intervals spanning zero and circular-shift max-statistic p=1. This particular example is unsupported in that sample.

Several i0 four-row lag associations were larger. For example, i0_p7 change versus later t1 change was about 0.24972, but its relationship with the future target **level** was only about 0.02374. Co-changing columns, event flicker and own-history controls still matter. This is not yet evidence of a usable residual forecast.

The v3 exploratory reversal study found a matched low-encoded-volume difference of about **+9.84 percentage points** for one downward numerical-centre move rule over 50 rows, with a sequence interval [+2.32, +15.85] points. Many rules were searched. This is a candidate for frozen replication, not proof that low physical liquidity causes profitable reversion. Hitting the origin at any point within 50 rows also differs from ending beyond it at row 50.

## 7. Active hypothesis register

This is the decision-focused summary. Keep the existing 120-question register as supporting detail. Record a new run beneath the same ID rather than replacing its history.

| ID | Claim / interpretation | Current evidence | Status and next decision |
| --- | --- | --- | --- |
| H001–H015 | Numerical ordering decodes physical depth, queue identity or volume transfer | Stable approximate order; crossings; lag associations; no independently decoded units/queues | Mechanism unresolved. Use numerical descriptors with identities retained. |
| H016–H021 | t0/t1 are long/short edges with a simple cost formula | Anticorrelation and often-negative sums; gap-only sum R² around 0.03, broader state around 0.25 | Interpretation open. Keep unconstrained t0/t1 outputs. |
| H022–H023 | Target updates align with i0 price updates; a universal flatness rate exists | Strong alignment in examined samples; flatness rates differ by population | Alignment observed; universal rate unestablished. |
| H024–H026 | i1 price events identify scored rows well enough for proxy-weighted training | Mask enrichment observed; AUC 0.584, AP 0.138 versus prevalence 0.108 on 24 held-out calibration sequences | Weak proxy. Defer long proxy-weighted training. |
| H027 | Direct-mask head fine-tuning improves the strongest base | +0.000802 on common focus screen, interval above zero | Supported in that comparison. Preserve the candidate and replicate on declared data. |
| H028–H029 | Current target changes attract scoring; flat targets carry negligible weight | Returned 32-sequence summary contradicts both; flat rows carry about 92.9% of absolute-target weight | Against these claims in that sample. Do not discard stable periods. |
| H032–H033 | Particular i1/auxiliary groups help the competitive GRU | Small pilots sometimes favour i0-only; v3 Ridge full control has a positive but inconclusive delta; complete matched production ablations absent | Unresolved. Retrieve/repeat matched group removals. |
| H034–H041 | More smoothers, slopes or volatility features improve WP | Mixed small-model results; broad EWMA/volatility additions do not show a stable GRU gain | Inconclusive. Audit actual selected schema; test compact blocks. |
| H042–H045 | Correlation, rank and shape descriptors improve the model | Conditional associations vary; broad stacking results are mostly flat or negative | Descriptive support; predictive gain unestablished. |
| H047–H050 | Event/flow/delay features add beyond the GRU | v7 intervals span zero; event stacking has only a small uncertain gain | Inconclusive. Require competitive-base residual evidence. |
| H051, H057–H058 | i1 leads the relevant i0 state/target errors | Specific i1_p6 lag-3 test near zero; simple i1 Ridge corrections failed in returned summary | Against those probes; wider conditional nonlinear hypothesis remains open. |
| H053–H055 | Two clocks and observed flicker matter | Different event rates and reversals observed | Descriptive. Test row filters beside event filters, without freezing predictions. |
| H056 | An event can be called persistent using its next two events | Those events have not arrived at the original row | Not causal as a current input. Delayed confirmation or training-only label is possible. |
| H059–H063, H067 | State-dependent effects justify adaptive heads or HMMs | Conditional differences; interaction tests fail to improve; varying FiLM loses to constant context | Useful adaptation unproven. Test compact context and capacity controls first. |
| H064–H066 | Blips, low encoded volume and direction predict useful reversals | v3 exploratory matched reversal differences; reversion Ridge variant itself loses | Descriptive candidates exist; target/residual benefit open. |
| H069–H072 | More target heads or a constrained direction/cost decoder improve WP | No repeatable independent-head win; deriving t1 from t0 plus gap underperforms | Defer. The gap label adds no independent information if it is t0+t1. |
| H073–H079 | Future-state auxiliary supervision helps the shared representation | Future-state diagnostics exist; no completed matched auxiliary-head gain | Open. Test timing plus movement, with direct t0/t1 supervision dominant. |
| H080–H084 | A TCN/LSTM/other recurrence is better | Earlier small row-TCN pilot did not improve; event/post-GRU TCN and alternatives lack adequate results | Defer architecture search until a specific remaining error motivates it. |
| H085–H087 | Holding, smoothing or learned update gates improve estimates | Hard holding and two fixed smoothers hurt; learned gate not tested | Against fixed rules. Learned gate is distinct but lower priority. |
| H088–H090, H110 | Data size or memory settings explain newer-model weakness | 5k run changes heads, flow and checkpointing; original strong training settings incompletely recorded | Confounded. Recover the exact base recipe and a controlled learning curve. |
| H091–H095, H113 | Ensembles, metric-aware losses or selection improve WP | Historical two-seed gain; successful mask fine-tuning; several objective changes unproven | Preserve known gains; test one training/selection change at a time. |
| H096–H100 | Causal context recovers useful sequence effects | Target-based mean/scale oracles are strong; feasible volatility proxy much smaller | Oracle does not establish feasibility. Test prefix-only descriptors with shrinkage. |
| H101–H106, H118–H120 | Distillation, model diversity, faster inference or larger encoders help | Proposals/supporting implementations, without a returned final score improvement | Open. Evaluate quality together with complete callback cost. |

The returned 32/16-sequence holding/correction numbers are available here through `RESULTS_INTERPRETATION.md` and the register's account of `RESULTS.json`. The raw `RESULTS.json` is not among these fifteen attachments, so those figures have not been independently recomputed in this revision.

## 8. Feature map: idea, measurement, result

The supplied catalogue describes **available slots**, not which features every run used. Base mode has 225 features: 112 levels, 112 differences and time. Next mode has 361 slots; its 12 EWMA, 8 activity, 40 event, 36 flow, 14 context and 26 shape slots can be disabled. In the recorded v7 control only **225/361** were active. Do not describe all base models as already using EWMAs/activity.

| Research idea | Candidate measurement | What has actually happened | Design implication |
| --- | --- | --- | --- |
| Recent equilibrium / mean reversion | x minus past EWMA at several decays | Mixed research results; historical shortlists differ from kit schemas | Inspect names and whether settings are spans or half-lives. |
| Short pattern versus long state | Row- and event-clock filters; signed changes and ages | Timing/event blocks tested, without a repeatable production win | Keep small; match the same base. |
| Whole-vector movement | TRAIN-fitted common factor, orthogonal residuals, coherence | Numerical co-change observed | A few factors may be better than hundreds of correlated columns. |
| Shape and identity | Raw identities plus within-group ranks, quantiles and crossings | Shape/ladder probes exist; no verified physical ladder | Add a second view; do not replace documented sides. |
| Drift versus chop | Causal slope, efficiency, sign persistence | Regime differences observed; interactions inconclusive | Forecast target residuals, not a trading story. |
| Chunkiness | Level std, change RMS, jump concentration, sign-run lengths | Some Ridge gains; chunk stacking hurt | Separate these measurements rather than add a large undifferentiated block. |
| Coupling changes | Rolling input-factor correlations and short/long covariance changes | Broad rcorr did not establish a GRU benefit | Use selected input-to-input relationships only. |
| Breaks | Causal innovations and short/long state disagreement | Several generic detector versions hurt | New detectors need a specific remaining failure to address. |
| i1 lead–lag | Past i1 changes, ages and unmatched moves conditional on i0 | Simple probes have not helped | No assumed fixed economic basis between anonymised columns. |
| Learned future state | Training labels for timing, movement and uncertainty | Not established by auxiliary-input experiments | Auxiliary supervision is a separate experiment. |

## 9. Twenty ranked improvement ideas

The order prioritises decision value and compute discipline, not promised score increases. “Now” includes research and reproduction; it does not mean launch twenty training jobs.

### 1. Reproduce the strongest base exactly — now

**Question:** Can a fresh run recover the reference family under the same recipe?

Record checkpoint and schema hashes, raw/engineered input widths, hidden width, active features, float16 rounding, scaling, data IDs, loss, optimiser/schedule, state/burn-in policy, chunking and checkpoint rule. Replay the existing model first, then reproduce its training. The newer 5k heads/flow recipe is not this control. If the original settings cannot be recovered, declare a new baseline rather than claim reproduction. H089, H110.

### 2. Freeze one evaluation protocol and an exposure ledger — now

**Question:** Is an apparent improvement robust outside the data used to invent it?

Cache complete-sequence predictions with model/feature hashes and exact masks. Use declared research-fit, development and final confirmation roles. List historical exposure; do not claim old calibration rows are pristine. Resample complete sequences, recompute pooled clipped WP, report each target and compare actual seed ensembles. Sequence IDs are grouping identifiers, not a chronology. This protects every later decision. H109, H115.

### 3. Preserve and replicate scored-row head fine-tuning — now

**Question:** Does the small known gain survive another declared comparison?

Start from the strongest parent and retain its successful head-only recipe. Compare original, equal-budget unweighted fine-tuning and direct-mask fine-tuning. Use only a declared calibration slice for fitting/selection; hold screening and confirmation labels out of the fine-tune. The official FAQ permits supplied train/valid data, but permission to train on it does not make it held out. Do not replace the useful direct mask with the weak proxy. H027, H095.

### 4. Build a matched data learning curve — now, after the recipe audit

**Question:** Is the same model still improving with sample diversity?

Use nested 2,500 / 5,000 / full training-sequence sets with the same feature definition, architecture and selection rule. Report both epochs and optimiser steps/processed rows, since fixed epochs give larger datasets more work. A fixed-step comparison separately helps distinguish diversity from compute. If the newest model already uses all data, this is a diagnosis of scaling and schedule, not a recommendation simply to use all data again. H088–H090.

### 5. Test memory length and stabilise optimisation — now

**Question:** Are truncated history, batch changes or an aggressive schedule limiting the GRU?

Inspect learning curves and state handling before increasing capacity. Isolate chunk/backpropagation length, effective batch and learning-rate schedule; carry prefix state causally and compare against the existing burn-in. Gradient accumulation changes optimiser batch size but does not restore a truncated gradient path. Benchmark one context change at a time. Do not assume laptop settings explain the entire 0.0186 deficit. H090, H097, H110.

### 6. Complete input-group ablations on the competitive base — next

**Question:** Which i1 and auxiliary groups have nonlinear incremental value?

Compare full input, i0-only and i0+auxiliary, then selectively remove i1 prices, volume-like or trade-like groups. Resolve derived-feature dependencies so a supposedly removed group cannot remain through engineered inputs. Fix data, scaler policy, training schedule and seed set. Small Ridge/raw-input pilots cannot decide production GRU redundancy. H032–H033.

### 7. Add a compact multi-horizon equilibrium block — next

**Question:** Does explicit memory improve what the GRU already remembers?

For a few TRAIN-selected columns/factors, compare current-minus-EWMA and short/long filter disagreement at a small fixed set such as half-lives 8, 32, 128 and 512 rows. Use multiple decays per selected stream before expanding every component. Keep the raw values. Validate against the existing actual schema: earlier labs already covered more components/horizons than “twelve prices, one each.” H034–H035, H041.

### 8. Represent both elapsed rows and elapsed events — next

**Question:** Does the same pattern behave differently in quiet and burst periods?

Compute row-based and observed-event-based filters together, plus event age, recent signed event rate and event/row speed ratio. Only update an event filter on an event already seen. Compare a small descriptor block first; an event-only GRU is a later architecture option. The ordinary recurrent state and predictions must still be allowed to use intervening information. H053–H056.

### 9. Search for conditional lead–lag in GRU errors — next research priority

**Question:** Does recent i1 or i0 history add information after own-book history and the strong GRU prediction?

Preselect a small set of lags in rows and i0 events. Fit on TRAIN/out-of-sample predictions, include i0 co-change/common-factor controls, then check separate sequences. Test current target residuals as well as future encoded-factor movement. Include negative-lag and shifted-signal controls. The specific i1_p6/three-row example failed; broad repetitive scans need multiplicity control. H050–H051, H057–H058.

### 10. Freeze a small blip/reversion study — next research priority

**Question:** Do move size and recent activity change reversal probability, and does this help t0/t1?

Replicate at most two or three existing v3 rules, conditioning on starting level, move magnitude, own-history, encoded-volume state and overlap/event support. Distinguish “touched the origin within 50 rows” from endpoint displacement. Forecast reversal from present features and test whether that forecast corrects GRU errors. An event can be confirmed persistent only after the confirming observations arrive. H064–H066.

### 11. Measure joint dynamics rather than add every rolling column — next

**Question:** Is there an emergent collective state that single-column filters miss?

Fit a small input-only factor basis on TRAIN. Keep common motion, orthogonal shape residuals, co-change breadth, coherence and short/long factor-covariance differences. Cross these with activity or persistence only when a declared probe supports it. This gives “emergent behaviour” a measurable definition without asserting a physical book decode. Compare an equally sized ordinary feature block as a control. H014, H040, H042, H067.

### 12. Preserve identities while testing an additional shape view — next

**Question:** Can shape/rank features help without discarding fixed component information?

Combine raw columns with within-documented-side numerical quantiles, TRAIN-normalised residuals, crossings and change in rank. Fit every normalisation on TRAIN and retain raw values; normalising columns does not recover physical units. Compare raw versus raw+shape, not just raw versus globally sorted. Use a compact feature block before a set encoder or attention layer. H003–H005, H043–H045.

### 13. Retest regime/break context with strict controls — conditional

**Question:** Can a small causal context explain repeatable residual calibration differences?

Start with continuous activity, efficiency, short/long volatility, reversal frequency and input-factor coupling. Compare unchanged base, context-added model, same-capacity constant context, and time/sequence-shuffled-context diagnostic. Shrink conditioning towards identity and keep feature count low. An HMM would require TRAIN fitting and causal filtered state probabilities, not full-sequence smoothed states. FiLM and generic break detectors have already failed in tested forms. H059–H063, H119.

### 14. Learn prefix context with uncertainty and shrinkage — conditional

**Question:** Can past inputs identify useful sequence-specific behaviour?

Add expanding or slowly decaying input summaries with history length/counts. Optionally compare nearest TRAIN prefixes at the same available horizon; exclude the same sequence and never use a future/full-sequence summary. Shrink noisy mean/scale corrections toward the global model. Target-based sequence oracles justify investigation but do not forecast an attainable score. H096–H100.

### 15. Use training-only future-state auxiliary tasks — conditional, first new neural idea

**Question:** Can explicit supervision improve the shared GRU representation?

Keep the direct t0/t1 output path. Add a small loss for future TRAIN-fitted i0-factor displacement at 4/16/64 rows, with event-within-horizon labels as a separate timing task. Handle end-of-sequence censoring and normalise auxiliary loss scales on TRAIN. Test movement, timing and then their combination. Drop auxiliary readouts at inference if the main prediction does not use them. These heads differ from merely splitting the two main target heads. H073–H079.

### 16. Add a short causal residual TCN only if a pattern remains — later

**Question:** Are useful short patterns left after the GRU prediction?

Use a frozen competitive GRU and train a small residual branch with a zero-initialised final layer. Inputs can include past/current predictions, compressed hidden state, observed changes and event ages. Try a modest receptive field such as 15–31 rows, with an equal-capacity non-temporal control. Train corrections from valid out-of-sample base predictions, or assess a jointly trained system on separate sequences. A historical parallel row-TCN failure is not the same experiment, but lowers its priority. H080–H082.

### 17. Tune the objective, checkpoint rule and clipping separately — conditional

**Question:** Is the model optimised and selected for the rows and moments that matter?

Audit the existing absolute-clipped-target weighted loss; compare calibration-dev checkpointing on the official mask with the current rule while holding fitted trajectories fixed where possible. Test a small output clipping/scale setting on development data only. Add a correlation term only as a controlled follow-up: earlier hybrid-loss pilots did not improve, and minibatch correlation is not global WP. Avoid using true scoring weights or labels as live inputs. H093–H095, H112–H113.

### 18. Train one small complementary tabular model — later

**Question:** Does another model family make sufficiently different useful errors?

Fit a constrained GBDT or small MLP on causal compact features; optionally use out-of-sample GRU summaries. Assess a frozen blend, not model diversity by name. Optiver, G-Research and MITSUI support investigating feature quality and complementary learners; they do not establish the same winning recipe here. A weak standalone model may help a blend, but every feature and learner adds callback cost. H102.

### 19. Choose target-specific blends from actual predictions — later, cheap once cached

**Question:** Can one candidate help t0 while another helps t1?

Choose one restrained blend coefficient per target on development predictions, shrink toward the reference and freeze before confirmation. Compare seed averaging, a few complementary checkpoints and the candidate only if their residual diversity is useful. Recompute global WP after blending/clipping; do not combine bucket improvements arithmetically. Existing reports with candidate share zero do not establish a new blend gain. H091–H092.

### 20. Spend runtime deliberately; distil if needed — later

**Question:** Can a better model fit the complete submission budget?

Benchmark feature construction, state updates and all ensemble members on one core before scaling the architecture. Then test compilation or quantisation with numerical/callback parity, or distil a stronger frozen teacher ensemble into one student. Distillation should use TRAIN or declared fitting data, not confirmation labels. The reported 75.7 μs/row and projected 49.8 minutes are local estimates; adding a TCN/GBDT cannot be treated as free. H101, H105–H106.

## 10. What transfers from the nine distinct competitions

The repeated links in the request reduce to nine competitions. Leaderboards show outcomes, not why a technique worked. The table separates retrieved primary evidence from **our proposed adaptation**. Several direct Kaggle pages returned no extractable body; indexed author text and linked original code were used where available. The PKSHA write-up body could not be verified, so no detailed PKSHA architecture claim is made here.

| Competition | Primary evidence reviewed | Proposed Connectome adaptation | Boundary on transfer |
| --- | --- | --- | --- |
| Optiver Realized Volatility Prediction | Winner's nearest-neighbour write-up listing; seventh-place author's account of reconstructing time order [S3–S4] | TRAIN-only neighbours/collective context can be tested as input representations. | Do not assume sequence IDs are chronological or import a reconstruction trick that requires unavailable data. PKSHA method details remain unverified. |
| Optiver Trading at the Close | HYD reports CatBoost/GRU/Transformer weights 0.5/0.3/0.2; ADAM reports three seeded XGBoost models with 157 features and provides code [S5–S6] | Test one complementary learner and compact aggregations beside the GRU. | Cross-stock zero-sum constraints, exact weights and online retraining require their original semantics/label availability. |
| Jane Street Market Prediction | Yirun's first-place supervised-autoencoder/MLP discussion includes Gaussian-noise regularisation [S7] | Training-only auxiliary supervision or carefully tested denoising may help representation learning. | An autoencoder is not evidence that a semantic state bottleneck will improve this task. |
| MITSUI Commodity Prediction Challenge | ZLF's fifth-place account combines a conservative four-day-window RNN with a single-day MLP [S8] | Investigate slow recurrent context plus a complementary fast mapping. | No day/horizon equivalence between that problem and Connectome's anonymous rows. |
| Jane Street Real-Time Market Data Forecasting | Original API-use discussions describe explicitly supplied lagged responders [S9] | Audit exactly what labels and history the live callback receives. | Connectome does not provide true lagged targets. That online adaptation path cannot simply be copied. |
| G-Research Crypto Forecasting | Second-place author describes guided feature engineering, a single LightGBM learner and Numba feature generation [S10] | Compact residual-driven features and a fast tabular challenger are credible experiments. | It does not show that stacking more neural architectures is necessary. |
| Two Sigma Financial Modeling | Official fifth-place interview discusses lag/aggregate features, volatile versus calm periods and runtime-limited ensembles [S11] | Test input-derived collective context and stability across states. | Do not reproduce target-history rules without labels that genuinely arrive online. |
| Ubiquant Market Prediction | First-place authors describe LightGBM/TabNet, grouped features and limiting training to reduce overfitting [S12] | Compare compact aggregate representations and control training/selection exposure. | Full test-time cross-sectional aggregates are not available in a row-stream unless that information has arrived. |
| Two Sigma: Using News to Predict Stock Movements | Official task/data describe market plus news inputs and signed confidence over market-adjusted returns [S13] | Align every source to its availability time and test each family's incremental value. | No news/text stream is present here; NLP and that competition's confidence objective are not direct additions. |

The useful common thread is representation, validation, controlled complexity and measured complementarity. Our next-step choices come primarily from the Connectome results, with these competitions supplying candidate methods.

## 11. A bounded notebook pass before long training

Extend the existing v3 workflow rather than create another broad feature catalogue. Start with its existing 24 TRAIN / 32 diagnostic-sequence scale; increase only to resolve a declared uncertainty. Those historical calibration sequences are exploratory, not final confirmation.

| Panel | Question and output | Decision it supports |
| --- | --- | --- |
| 1. Run/coverage audit | Compare reference/current manifests; verify exact row keys, model hashes, feature order and masks. Resolve the v3 5/64 complete-GRU-cache coverage. | Decide whether the comparison is valid before reading feature rankings. |
| 2. Population profile | Recompute target-change rates with explicit clipping/tolerances, mask cross-tabs, target-weight shares and causal activity/efficiency profiles. | Resolve contradictory flatness claims; locate weak high-support populations. |
| 3. Residual lead–lag | Fit a predeclared small lag bank on out-of-sample predictions, conditioning on i0 history/common motion; compare both clocks and shifted controls. | Promote a causal lag block only if it adds stable held-sequence information. |
| 4. Frozen reversal rules | Replicate two or three v3 rules with support, overlap and own-history controls; report hit-within-window and endpoint labels separately. | Decide whether reversal supervision/features deserve a neural test. |
| 5. Joint state/calibration | Test compact factor/coherence and short/long-context descriptors against constant/capacity controls. Fit corrections only on research-fit rows. | Decide whether regime adaptation has a specific measurable residual to address. |
| 6. Frozen shortlist | Record at most two candidate families, schemas, lags, thresholds, fitting IDs and the exact next comparison. | Prevent the next desktop run from mixing unrelated changes. |

Strong univariate correlation is insufficient. A stable out-of-sample residual correction is a useful triage signal, but failure of a linear correction does not prove that a representation cannot help joint GRU training. Permit one bounded, predeclared neural representation test when there is a clear reason; do not require every nonlinear idea to pass a Ridge filter first.

Training order after the notebook pass:

1. Replay and recover the strongest shared-base recipe. Resolve the reproduction/configuration gap.
2. Establish the controlled full-data baseline and preserve the successful scored-head fine-tune.
3. Test one compact feature/context winner against that base with matched data and seeds.
4. If supported, test training-only movement auxiliaries separately. Timing is another arm, not bundled into the first comparison.
5. Only then consider the residual TCN or a complementary learner.
6. Freeze a selected candidate/blend, confirm once on a declared holdout, and benchmark the complete callback before packaging.

This is an experiment sequence, not a prediction that twenty changes will close a particular leaderboard gap.

## 12. Corrections that should remain visible

| Earlier statement | Corrected statement | Consequence |
| --- | --- | --- |
| “t0 and t1 are buy and sell execution edges.” | Compatible working interpretation; exact formulas remain unknown. | No hard cost sign or target-swap rule. |
| “The schema's bid/ask split is wrong because the encoded book crosses.” | Numerical comparability/depth is unresolved; documented side membership remains the specification. | Do not replace documented sides with a global numeric split. |
| “Rank crossings prove changing order-queue position.” | They show encoded numerical crossings. | Retain identity; use neutral feature names. |
| “Failed suffix matching disproves p/v pairing.” | The correlation-based test was not decisive under anonymisation. | Do not assert a recovered volume ladder. |
| “Targets are flat on 97% of all rows.” | That was population/definition dependent; broader samples differ. | Record sample, tolerance and clipping with every rate. |
| “Flat true targets justify fixed predictions.” | An unchanged hidden value may still have a changing conditional estimate. | Tested hard holding and smoothing hurt. |
| “Scoring follows target changes.” | Current-update enrichment was contradicted in the returned sample; i1 mask enrichment is a different observation. | Separate mask, target update and useful prediction revision. |
| “Weak volatility additions mean volatility has little effect.” | A tested addition may be redundant, noisy or poorly represented. | Assess conditional structure and incremental value separately. |
| “FiLM's extra layer proves useful regime adaptation.” | Changing context lost to constant context. | Attribute no gain to regime information. |
| “The 5k run disproves scaling.” | It used a different heads/flow recipe and selection settings. | Run a controlled learning curve if needed. |
| “TCNs and independent heads have never been tried.” | Small/main-head variants exist; event/post-GRU variants are distinct and largely unproven. | State the exact architecture variant before proposing a rerun. |
| “Twelve selected EWMAs means twelve prices at one horizon.” | Coverage differs by lab and resolved schema. | Record exact dependencies and decays. |
| “A future non-reverting event is a current persistent event.” | Persistence can only be confirmed after the required delay. | Use delayed features or training-only labels. |
| “Rolling target correlation can set live importance.” | True targets are unavailable at inference. | Use input-to-input features or offline diagnostics. |
| “An interval above zero proves a universal gain.” | It is conditional evidence under a particular selection history and fitted seed set. | Replication and declared confirmation still matter. |
| “An oracle WP of 0.671/0.695 is an achievable target.” | Target-based per-sequence calibration is unavailable online. | Treat it as a diagnostic, not a promised score. |
| “Local 0.679 beats leaderboard 0.672.” | Different populations and model-selection histories. | Compare submissions on the competition's own test. |

## 13. Templates for new work

### Hypothesis entry

```markdown
### H<next free ID>. <One falsifiable claim>

Date:
Mechanism status: open / observed / unresolved / contradicted
Predictive status: open / inconclusive / supported in comparison / against version
Motivation:
Observed evidence, with source file/cell:
Competing explanations:
Causal feature definition and source dependencies:
TRAIN-only fitted quantities:
Training/selection/confirmation sequence IDs and prior exposure:
Control and exactly one changed element:
Predicted result if the claim is useful:
Result that would count against this version:
Compute/runtime budget and stopping rule:
Run IDs and configuration hashes:
Actual t0, t1 and pooled masked WP:
All-eligible WP, support and paired interval:
Seed replication / actual ensemble definition:
Decision and next test:
```

### Result row

```markdown
| Run ID / date | H-ID | Candidate and control | Partition / mask / exposure | Seqs / scored rows | Seeds / epochs / optimiser steps | t0 / t1 / WP | ΔWP / interval | Runtime | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
```

### Correction row

```markdown
| Date | Previous wording | Evidence requiring correction | Narrower conclusion | Experiment/feature affected |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
```

Archive original numbers and verdicts. Add a dated revision explaining the changed conclusion so a future experiment does not unknowingly repeat an already failed version.

## 14. Evidence inventory and references

### Supplied project evidence

| Source | Use in this revision |
| --- | --- |
| `Connectome research log.md` | Earlier master summary; revised here where later evidence supersedes it. |
| `HYPOTHESIS_REGISTER.md` | Stable H001–H120 IDs, provenance and later scope corrections. |
| `RESULTS_INTERPRETATION.md` | Returned v8.3 mask/holding/smoothing/correction summary and model audit. |
| `HYPOTHESES_TESTED.md` | Earlier 17 October register; physical-semantic and universal-flatness conclusions require correction. |
| `Pasted text(7).txt` | Hypothesis audit distinguishing numerical structure from decoded semantics. |
| `Pasted text (2)(3).txt` | 225/245/361-slot feature catalogue and preprocessing descriptions. |
| `Pasted text (3).txt` | v7 commands, budgets, seeds and matched individual-run outputs. |
| `Pasted text (4).txt` | State/auxiliary/TCN proposals; proposals are not completed experiments. |
| `Pasted text (5).txt` | Actual common-screen regime ensembles and paired contrasts. |
| `Pasted text (6).txt` | Actual common-screen larger heads/flow ensembles and paired contrasts. |
| `Connectome_Book_Features_Lab(1).ipynb` | Saved outputs: cells 16/18 family Ridge and GRU stacking; 20 delay; 22 interactions. |
| `Connectome_Book_Features_Lab_v3(1).ipynb` | Saved outputs: cells 10/14/18/21 for Ridge, lead–lag, reversal and limited-coverage GRU corrections; 26 leaves confirmation unopened in this workflow. |
| `book_lab_v3_plan_pilot_64_64_64_20261017.json` | 64/64/64 internal split, data fingerprints and historical-exposure caveat. |
| `Connectome_Expanded_Feature_Hypothesis_Lab(1).ipynb` | Saved Ridge outputs and partial GRU log; confirmation disabled. |
| `Connectome_Horizons_Rolling_Plots(3).ipynb` | Saved horizon, gap/factor and decoder outputs; synthetic checks separated from real-data probes. |

This revision reviews saved outputs and supplied reports. Competition parquet files, the newest production checkpoint and its full training source/configuration were not attached; no new competition-data training or result replication was performed here.

### External primary sources

Access reviewed 21 October 2026. A retrievable title alone is not treated as a verified explanation of a winning method.

- **[S1]** [Connectome data and scoring specification](https://wundernn.io/connectome/docs/data_overview).
- **[S2]** [Connectome FAQ: data use, state reset and execution budget](https://wundernn.io/connectome/docs/faq).
- **[S3]** [Optiver RV first-place nearest-neighbours write-up](https://www.kaggle.com/competitions/optiver-realized-volatility-prediction/writeups/nyanp-1st-place-solution-nearest-neighbors). Indexed title/identity retrieved; detailed body access limited.
- **[S4]** [Optiver RV seventh-place author's repository and reconstruction account](https://github.com/michaelpoluektov/orvp).
- **[S5]** [HYD's Optiver Close first-place write-up](https://www.kaggle.com/competitions/optiver-trading-at-the-close/writeups/hyd-1st-place-solution); relevant author text was retrievable through [HYD's write-up index](https://www.kaggle.com/hydantess/writeups).
- **[S6]** [ADAM's ninth-place write-up](https://www.kaggle.com/competitions/optiver-trading-at-the-close/writeups/adam-9th-place-solution) and [original training repository](https://github.com/ChunhanLi/9th-kaggle-optiver-trading-close).
- **[S7]** [Yirun's first-place supervised-autoencoder/MLP discussion](https://www.kaggle.com/c/jane-street-market-prediction/discussion/224348).
- **[S8]** [ZLF's MITSUI fifth-place RNN/MLP account](https://www.kaggle.com/competitions/mitsui-commodity-prediction-challenge/writeups/zlf-solution-of-the-mitsui-commodity-predict).
- **[S9]** [Jane Street real-time API lag-use discussion](https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting/discussion/545073). This is an original implementation discussion, not a verified winning recipe.
- **[S10]** [Nathaniel Maddux's G-Research second-place solution](https://www.kaggle.com/competitions/g-research-crypto-forecasting/writeups/nathaniel-maddux-2nd-place-solution).
- **[S11]** [Official Kaggle fifth-place Two Sigma Financial Modeling interview](https://medium.com/kaggle-blog/two-sigma-financial-modeling-code-competition-5th-place-winners-interview-team-best-fitting-279a493c76bd).
- **[S12]** [Ubiquant first-place authors' account](https://www.kaggle.com/competitions/ubiquant-market-prediction/writeups/k-i-y-1st-place-solution-our-betting-strategy).
- **[S13]** [Two Sigma News overview](https://www.kaggle.com/c/two-sigma-financial-news/overview) and [official data description](https://www.kaggle.com/competitions/two-sigma-financial-news/data).

The supplied [PKSHA Optiver RV write-up](https://www.kaggle.com/competitions/optiver-realized-volatility-prediction/writeups/pksha-life-is-volatile-tentative-3rd-place-solutio) was located, but its method body was not extractable. It remains a reading item, not evidence for a specific imported architecture.
