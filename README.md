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

## variables
we were given a large set of 115 variables/parameters, the first 22 or so were random orderings of the prices in the orderbook for one asset i0, the next were volumes or so, than some more variables I couldn't figure out what was.
the next group of variables were associated with the other asset i1.

We discovered that i0_p3 were most correlated with movements in t0. But that the weighted events were mostly on i1 price moves.

### Training variables 
To add to the standard variables(features), we added many more.
The initial find was that EWMA helped the initial improvement. 
Than another improvement happened based on event time features, checking whether any of the i0_ps had changed position.

1. it seems we should test EWMA on other prices than the 12 selected i0_ps, can we add more horizons for each ps? I am assuming we have 1 EWMA for 12 selected ps.
2. Can we add book crossing? Can we also add specific events on i0_p0, can we also add some features for delay between book change and expected t0, t1 change? can we also add more activity and efficiency horizons?
Can we also add orderbook direction changes due to the activities?
3. Do we have anything measuring the entire orderbook, we tested and could sort the book by lowest to highest, but they were somewhat based on order queue, rather than index and say sometimes i0_p3 would be the closest to the current mid on the bid side and i0_p17 would be. But than it would shift and i0_p4 would be closest and i0_p19 would be closest. We need something measuring that and sorting it so we can understand what the slope, regime, best bid, best ask were and how the gap and behaviors would be.
4. for the detection of regimes, do we have anything measuring linear trend slope of say i0p0, i0p20, so and so on, along with the entire orderbook. We would want to measure if the book is moving upwards, so buying is best, if the book is moving down the sell is best.
5. We want to also add something measuring chunkiness, say volatility of the book, say stds of all the prices, say something like various horizons, stds of all the prices on 12, 24, 36, 124, etc. rolling window. We also want to check those linear regression slopes for windows like that.
6. WE should also do something like rolling correlations, it might be that adjusting different importances, say how important are moving averages if the correllations increase.





## Hypothesis tested



## Information considered.
I knew right off the bat that a range of similar competitions had taken place. 
So I wanted to utilise the solutions from their winners.




