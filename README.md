## Introduction

I went at this competition because it popped up on Linkedin randomly. It seemed very oddly interesting and along the way I have dropped much of my desire to finish properly.
Mostly due to the fact I found out Wunderfund is a russian HFT firm, actively advertising to russians.
My family was driven out of Czechia due to russian invasion, and I am therefore strongly inclined to drop genuine participation.

However, as a person to another person, I am therefore significantly more incline to give away findings.

## Targets
Being a quant for the sake of quant, rather than for the sake of AI, ML or otherwise.
My initial goal was to figure out, what the fuck are we actually targetting?

My initial idea was to stupidly believe what Wunderfund wrote on the hero in the index screen.
We are predicting future prices, I therefore ran a range of tests to show that t0 and t1 had to do with microprice, volume weighted moving price and more.
These all fell flat and never picked up in any way. Some things did become conclusive from it in a better manner, but we'll take that later.

I than believed targets might be something more trading oriented, say optimal inventory for asset i0 and asset i1.
Which made a lot of sense, but also showed to be inconclusive.

At the end I understood, that t0 and t1 was correlated but inversely, the targets were also correlated with price.

The targets are buying edge and sell edge, so these are "of course" related to each other.
Buy now sell later, short now buy back later are inversely correlated and as correctly can be pointed out.
Those two are inversely correlated, with a certain gap, relating to execution, slippage, fee and more.

## variables


### Training variables 
| Feature family | Slots |
|---|---:|
| Original i0/i1 inputs and auxiliary columns | 112 |
| One-row differences | 112 |
| Sequence time | 1 |
| TRAIN-selected EWMA residuals | 12 | 
| Activity/persistence descriptors | 8 |
| Event-clock histories and reversal descriptors | 40 |
| Volume/trade-column innovations | 36 |
| Causal expanding-context statistics | 14 |
| Sorted encoded-price descriptors | 26 |
| **Total available** | **361** |


| slot | feature | block | source | formula |
|---|---|---|---|---|
| 0 | i0_p0 | base | i0_p0 | current rounded input x[t] |
| 1 | i0_p1 | base | i0_p1 | current rounded input x[t] |
| 2 | i0_p2 | base | i0_p2 | current rounded input x[t] |
| 3 | i0_p3 | base | i0_p3 | current rounded input x[t] |
| 4 | i0_p4 | base | i0_p4 | current rounded input x[t] |
| 5 | i0_p5 | base | i0_p5 | current rounded input x[t] |
| 6 | i0_p6 | base | i0_p6 | current rounded input x[t] |
| 7 | i0_p7 | base | i0_p7 | current rounded input x[t] |
| 8 | i0_p8 | base | i0_p8 | current rounded input x[t] |
| 9 | i0_p9 | base | i0_p9 | current rounded input x[t] |
| 10 | i0_p10 | base | i0_p10 | current rounded input x[t] |
| 11 | i0_p11 | base | i0_p11 | current rounded input x[t] |
| 12 | i0_p12 | base | i0_p12 | current rounded input x[t] |
| 13 | i0_p13 | base | i0_p13 | current rounded input x[t] |
| 14 | i0_p14 | base | i0_p14 | current rounded input x[t] |
| 15 | i0_p15 | base | i0_p15 | current rounded input x[t] |
| 16 | i0_p16 | base | i0_p16 | current rounded input x[t] |
| 17 | i0_p17 | base | i0_p17 | current rounded input x[t] |
| 18 | i0_p18 | base | i0_p18 | current rounded input x[t] |
| 19 | i0_p19 | base | i0_p19 | current rounded input x[t] |
| 20 | i0_p20 | base | i0_p20 | current rounded input x[t] |
| 21 | i0_p21 | base | i0_p21 | current rounded input x[t] |
| 22 | i0_v0 | base | i0_v0 | current rounded input x[t] |
| 23 | i0_v1 | base | i0_v1 | current rounded input x[t] |
| 24 | i0_v2 | base | i0_v2 | current rounded input x[t] |
| 25 | i0_v3 | base | i0_v3 | current rounded input x[t] |
| 26 | i0_v4 | base | i0_v4 | current rounded input x[t] |
| 27 | i0_v5 | base | i0_v5 | current rounded input x[t] |
| 28 | i0_v6 | base | i0_v6 | current rounded input x[t] |
| 29 | i0_v7 | base | i0_v7 | current rounded input x[t] |
| 30 | i0_v8 | base | i0_v8 | current rounded input x[t] |
| 31 | i0_v9 | base | i0_v9 | current rounded input x[t] |
| 32 | i0_v10 | base | i0_v10 | current rounded input x[t] |
| 33 | i0_v11 | base | i0_v11 | current rounded input x[t] |
| 34 | i0_v12 | base | i0_v12 | current rounded input x[t] |
| 35 | i0_v13 | base | i0_v13 | current rounded input x[t] |
| 36 | i0_v14 | base | i0_v14 | current rounded input x[t] |
| 37 | i0_v15 | base | i0_v15 | current rounded input x[t] |
| 38 | i0_v16 | base | i0_v16 | current rounded input x[t] |
| 39 | i0_v17 | base | i0_v17 | current rounded input x[t] |
| 40 | i0_v18 | base | i0_v18 | current rounded input x[t] |
| 41 | i0_v19 | base | i0_v19 | current rounded input x[t] |
| 42 | i0_v20 | base | i0_v20 | current rounded input x[t] |
| 43 | i0_v21 | base | i0_v21 | current rounded input x[t] |
| 44 | i0_dp0 | base | i0_dp0 | current rounded input x[t] |
| 45 | i0_dp1 | base | i0_dp1 | current rounded input x[t] |
| 46 | i0_dp2 | base | i0_dp2 | current rounded input x[t] |
| 47 | i0_dp3 | base | i0_dp3 | current rounded input x[t] |
| 48 | i0_dv0 | base | i0_dv0 | current rounded input x[t] |
| 49 | i0_dv1 | base | i0_dv1 | current rounded input x[t] |
| 50 | i0_dv2 | base | i0_dv2 | current rounded input x[t] |
| 51 | i0_dv3 | base | i0_dv3 | current rounded input x[t] |
| 52 | i1_p0 | base | i1_p0 | current rounded input x[t] |
| 53 | i1_p1 | base | i1_p1 | current rounded input x[t] |
| 54 | i1_p2 | base | i1_p2 | current rounded input x[t] |
| 55 | i1_p3 | base | i1_p3 | current rounded input x[t] |
| 56 | i1_p4 | base | i1_p4 | current rounded input x[t] |
| 57 | i1_p5 | base | i1_p5 | current rounded input x[t] |
| 58 | i1_p6 | base | i1_p6 | current rounded input x[t] |
| 59 | i1_p7 | base | i1_p7 | current rounded input x[t] |
| 60 | i1_p8 | base | i1_p8 | current rounded input x[t] |
| 61 | i1_p9 | base | i1_p9 | current rounded input x[t] |
| 62 | i1_p10 | base | i1_p10 | current rounded input x[t] |
| 63 | i1_p11 | base | i1_p11 | current rounded input x[t] |
| 64 | i1_p12 | base | i1_p12 | current rounded input x[t] |
| 65 | i1_p13 | base | i1_p13 | current rounded input x[t] |
| 66 | i1_p14 | base | i1_p14 | current rounded input x[t] |
| 67 | i1_p15 | base | i1_p15 | current rounded input x[t] |
| 68 | i1_p16 | base | i1_p16 | current rounded input x[t] |
| 69 | i1_p17 | base | i1_p17 | current rounded input x[t] |
| 70 | i1_p18 | base | i1_p18 | current rounded input x[t] |
| 71 | i1_p19 | base | i1_p19 | current rounded input x[t] |
| 72 | i1_p20 | base | i1_p20 | current rounded input x[t] |
| 73 | i1_p21 | base | i1_p21 | current rounded input x[t] |
| 74 | i1_v0 | base | i1_v0 | current rounded input x[t] |
| 75 | i1_v1 | base | i1_v1 | current rounded input x[t] |
| 76 | i1_v2 | base | i1_v2 | current rounded input x[t] |
| 77 | i1_v3 | base | i1_v3 | current rounded input x[t] |
| 78 | i1_v4 | base | i1_v4 | current rounded input x[t] |
| 79 | i1_v5 | base | i1_v5 | current rounded input x[t] |
| 80 | i1_v6 | base | i1_v6 | current rounded input x[t] |
| 81 | i1_v7 | base | i1_v7 | current rounded input x[t] |
| 82 | i1_v8 | base | i1_v8 | current rounded input x[t] |
| 83 | i1_v9 | base | i1_v9 | current rounded input x[t] |
| 84 | i1_v10 | base | i1_v10 | current rounded input x[t] |
| 85 | i1_v11 | base | i1_v11 | current rounded input x[t] |
| 86 | i1_v12 | base | i1_v12 | current rounded input x[t] |
| 87 | i1_v13 | base | i1_v13 | current rounded input x[t] |
| 88 | i1_v14 | base | i1_v14 | current rounded input x[t] |
| 89 | i1_v15 | base | i1_v15 | current rounded input x[t] |
| 90 | i1_v16 | base | i1_v16 | current rounded input x[t] |
| 91 | i1_v17 | base | i1_v17 | current rounded input x[t] |
| 92 | i1_v18 | base | i1_v18 | current rounded input x[t] |
| 93 | i1_v19 | base | i1_v19 | current rounded input x[t] |
| 94 | i1_v20 | base | i1_v20 | current rounded input x[t] |
| 95 | i1_v21 | base | i1_v21 | current rounded input x[t] |
| 96 | i1_dp0 | base | i1_dp0 | current rounded input x[t] |
| 97 | i1_dp1 | base | i1_dp1 | current rounded input x[t] |
| 98 | i1_dp2 | base | i1_dp2 | current rounded input x[t] |
| 99 | i1_dp3 | base | i1_dp3 | current rounded input x[t] |
| 100 | i1_dv0 | base | i1_dv0 | current rounded input x[t] |
| 101 | i1_dv1 | base | i1_dv1 | current rounded input x[t] |
| 102 | i1_dv2 | base | i1_dv2 | current rounded input x[t] |
| 103 | i1_dv3 | base | i1_dv3 | current rounded input x[t] |
| 104 | a0 | base | a0 | current rounded input x[t] |
| 105 | a1 | base | a1 | current rounded input x[t] |
| 106 | a2 | base | a2 | current rounded input x[t] |
| 107 | a3 | base | a3 | current rounded input x[t] |
| 108 | a4 | base | a4 | current rounded input x[t] |
| 109 | a5 | base | a5 | current rounded input x[t] |
| 110 | a6 | base | a6 | current rounded input x[t] |
| 111 | a7 | base | a7 | current rounded input x[t] |
| 112 | d_i0_p0 | base | i0_p0 | x[t]-x[t-1]; zero at row 0 |
| 113 | d_i0_p1 | base | i0_p1 | x[t]-x[t-1]; zero at row 0 |
| 114 | d_i0_p2 | base | i0_p2 | x[t]-x[t-1]; zero at row 0 |
| 115 | d_i0_p3 | base | i0_p3 | x[t]-x[t-1]; zero at row 0 |
| 116 | d_i0_p4 | base | i0_p4 | x[t]-x[t-1]; zero at row 0 |
| 117 | d_i0_p5 | base | i0_p5 | x[t]-x[t-1]; zero at row 0 |
| 118 | d_i0_p6 | base | i0_p6 | x[t]-x[t-1]; zero at row 0 |
| 119 | d_i0_p7 | base | i0_p7 | x[t]-x[t-1]; zero at row 0 |
| 120 | d_i0_p8 | base | i0_p8 | x[t]-x[t-1]; zero at row 0 |
| 121 | d_i0_p9 | base | i0_p9 | x[t]-x[t-1]; zero at row 0 |
| 122 | d_i0_p10 | base | i0_p10 | x[t]-x[t-1]; zero at row 0 |
| 123 | d_i0_p11 | base | i0_p11 | x[t]-x[t-1]; zero at row 0 |
| 124 | d_i0_p12 | base | i0_p12 | x[t]-x[t-1]; zero at row 0 |
| 125 | d_i0_p13 | base | i0_p13 | x[t]-x[t-1]; zero at row 0 |
| 126 | d_i0_p14 | base | i0_p14 | x[t]-x[t-1]; zero at row 0 |
| 127 | d_i0_p15 | base | i0_p15 | x[t]-x[t-1]; zero at row 0 |
| 128 | d_i0_p16 | base | i0_p16 | x[t]-x[t-1]; zero at row 0 |
| 129 | d_i0_p17 | base | i0_p17 | x[t]-x[t-1]; zero at row 0 |
| 130 | d_i0_p18 | base | i0_p18 | x[t]-x[t-1]; zero at row 0 |
| 131 | d_i0_p19 | base | i0_p19 | x[t]-x[t-1]; zero at row 0 |
| 132 | d_i0_p20 | base | i0_p20 | x[t]-x[t-1]; zero at row 0 |
| 133 | d_i0_p21 | base | i0_p21 | x[t]-x[t-1]; zero at row 0 |
| 134 | d_i0_v0 | base | i0_v0 | x[t]-x[t-1]; zero at row 0 |
| 135 | d_i0_v1 | base | i0_v1 | x[t]-x[t-1]; zero at row 0 |
| 136 | d_i0_v2 | base | i0_v2 | x[t]-x[t-1]; zero at row 0 |
| 137 | d_i0_v3 | base | i0_v3 | x[t]-x[t-1]; zero at row 0 |
| 138 | d_i0_v4 | base | i0_v4 | x[t]-x[t-1]; zero at row 0 |
| 139 | d_i0_v5 | base | i0_v5 | x[t]-x[t-1]; zero at row 0 |
| 140 | d_i0_v6 | base | i0_v6 | x[t]-x[t-1]; zero at row 0 |
| 141 | d_i0_v7 | base | i0_v7 | x[t]-x[t-1]; zero at row 0 |
| 142 | d_i0_v8 | base | i0_v8 | x[t]-x[t-1]; zero at row 0 |
| 143 | d_i0_v9 | base | i0_v9 | x[t]-x[t-1]; zero at row 0 |
| 144 | d_i0_v10 | base | i0_v10 | x[t]-x[t-1]; zero at row 0 |
| 145 | d_i0_v11 | base | i0_v11 | x[t]-x[t-1]; zero at row 0 |
| 146 | d_i0_v12 | base | i0_v12 | x[t]-x[t-1]; zero at row 0 |
| 147 | d_i0_v13 | base | i0_v13 | x[t]-x[t-1]; zero at row 0 |
| 148 | d_i0_v14 | base | i0_v14 | x[t]-x[t-1]; zero at row 0 |
| 149 | d_i0_v15 | base | i0_v15 | x[t]-x[t-1]; zero at row 0 |
| 150 | d_i0_v16 | base | i0_v16 | x[t]-x[t-1]; zero at row 0 |
| 151 | d_i0_v17 | base | i0_v17 | x[t]-x[t-1]; zero at row 0 |
| 152 | d_i0_v18 | base | i0_v18 | x[t]-x[t-1]; zero at row 0 |
| 153 | d_i0_v19 | base | i0_v19 | x[t]-x[t-1]; zero at row 0 |
| 154 | d_i0_v20 | base | i0_v20 | x[t]-x[t-1]; zero at row 0 |
| 155 | d_i0_v21 | base | i0_v21 | x[t]-x[t-1]; zero at row 0 |
| 156 | d_i0_dp0 | base | i0_dp0 | x[t]-x[t-1]; zero at row 0 |
| 157 | d_i0_dp1 | base | i0_dp1 | x[t]-x[t-1]; zero at row 0 |
| 158 | d_i0_dp2 | base | i0_dp2 | x[t]-x[t-1]; zero at row 0 |
| 159 | d_i0_dp3 | base | i0_dp3 | x[t]-x[t-1]; zero at row 0 |
| 160 | d_i0_dv0 | base | i0_dv0 | x[t]-x[t-1]; zero at row 0 |
| 161 | d_i0_dv1 | base | i0_dv1 | x[t]-x[t-1]; zero at row 0 |
| 162 | d_i0_dv2 | base | i0_dv2 | x[t]-x[t-1]; zero at row 0 |
| 163 | d_i0_dv3 | base | i0_dv3 | x[t]-x[t-1]; zero at row 0 |
| 164 | d_i1_p0 | base | i1_p0 | x[t]-x[t-1]; zero at row 0 |
| 165 | d_i1_p1 | base | i1_p1 | x[t]-x[t-1]; zero at row 0 |
| 166 | d_i1_p2 | base | i1_p2 | x[t]-x[t-1]; zero at row 0 |
| 167 | d_i1_p3 | base | i1_p3 | x[t]-x[t-1]; zero at row 0 |
| 168 | d_i1_p4 | base | i1_p4 | x[t]-x[t-1]; zero at row 0 |
| 169 | d_i1_p5 | base | i1_p5 | x[t]-x[t-1]; zero at row 0 |
| 170 | d_i1_p6 | base | i1_p6 | x[t]-x[t-1]; zero at row 0 |
| 171 | d_i1_p7 | base | i1_p7 | x[t]-x[t-1]; zero at row 0 |
| 172 | d_i1_p8 | base | i1_p8 | x[t]-x[t-1]; zero at row 0 |
| 173 | d_i1_p9 | base | i1_p9 | x[t]-x[t-1]; zero at row 0 |
| 174 | d_i1_p10 | base | i1_p10 | x[t]-x[t-1]; zero at row 0 |
| 175 | d_i1_p11 | base | i1_p11 | x[t]-x[t-1]; zero at row 0 |
| 176 | d_i1_p12 | base | i1_p12 | x[t]-x[t-1]; zero at row 0 |
| 177 | d_i1_p13 | base | i1_p13 | x[t]-x[t-1]; zero at row 0 |
| 178 | d_i1_p14 | base | i1_p14 | x[t]-x[t-1]; zero at row 0 |
| 179 | d_i1_p15 | base | i1_p15 | x[t]-x[t-1]; zero at row 0 |
| 180 | d_i1_p16 | base | i1_p16 | x[t]-x[t-1]; zero at row 0 |
| 181 | d_i1_p17 | base | i1_p17 | x[t]-x[t-1]; zero at row 0 |
| 182 | d_i1_p18 | base | i1_p18 | x[t]-x[t-1]; zero at row 0 |
| 183 | d_i1_p19 | base | i1_p19 | x[t]-x[t-1]; zero at row 0 |
| 184 | d_i1_p20 | base | i1_p20 | x[t]-x[t-1]; zero at row 0 |
| 185 | d_i1_p21 | base | i1_p21 | x[t]-x[t-1]; zero at row 0 |
| 186 | d_i1_v0 | base | i1_v0 | x[t]-x[t-1]; zero at row 0 |
| 187 | d_i1_v1 | base | i1_v1 | x[t]-x[t-1]; zero at row 0 |
| 188 | d_i1_v2 | base | i1_v2 | x[t]-x[t-1]; zero at row 0 |
| 189 | d_i1_v3 | base | i1_v3 | x[t]-x[t-1]; zero at row 0 |
| 190 | d_i1_v4 | base | i1_v4 | x[t]-x[t-1]; zero at row 0 |
| 191 | d_i1_v5 | base | i1_v5 | x[t]-x[t-1]; zero at row 0 |
| 192 | d_i1_v6 | base | i1_v6 | x[t]-x[t-1]; zero at row 0 |
| 193 | d_i1_v7 | base | i1_v7 | x[t]-x[t-1]; zero at row 0 |
| 194 | d_i1_v8 | base | i1_v8 | x[t]-x[t-1]; zero at row 0 |
| 195 | d_i1_v9 | base | i1_v9 | x[t]-x[t-1]; zero at row 0 |
| 196 | d_i1_v10 | base | i1_v10 | x[t]-x[t-1]; zero at row 0 |
| 197 | d_i1_v11 | base | i1_v11 | x[t]-x[t-1]; zero at row 0 |
| 198 | d_i1_v12 | base | i1_v12 | x[t]-x[t-1]; zero at row 0 |
| 199 | d_i1_v13 | base | i1_v13 | x[t]-x[t-1]; zero at row 0 |
| 200 | d_i1_v14 | base | i1_v14 | x[t]-x[t-1]; zero at row 0 |
| 201 | d_i1_v15 | base | i1_v15 | x[t]-x[t-1]; zero at row 0 |
| 202 | d_i1_v16 | base | i1_v16 | x[t]-x[t-1]; zero at row 0 |
| 203 | d_i1_v17 | base | i1_v17 | x[t]-x[t-1]; zero at row 0 |
| 204 | d_i1_v18 | base | i1_v18 | x[t]-x[t-1]; zero at row 0 |
| 205 | d_i1_v19 | base | i1_v19 | x[t]-x[t-1]; zero at row 0 |
| 206 | d_i1_v20 | base | i1_v20 | x[t]-x[t-1]; zero at row 0 |
| 207 | d_i1_v21 | base | i1_v21 | x[t]-x[t-1]; zero at row 0 |
| 208 | d_i1_dp0 | base | i1_dp0 | x[t]-x[t-1]; zero at row 0 |
| 209 | d_i1_dp1 | base | i1_dp1 | x[t]-x[t-1]; zero at row 0 |
| 210 | d_i1_dp2 | base | i1_dp2 | x[t]-x[t-1]; zero at row 0 |
| 211 | d_i1_dp3 | base | i1_dp3 | x[t]-x[t-1]; zero at row 0 |
| 212 | d_i1_dv0 | base | i1_dv0 | x[t]-x[t-1]; zero at row 0 |
| 213 | d_i1_dv1 | base | i1_dv1 | x[t]-x[t-1]; zero at row 0 |
| 214 | d_i1_dv2 | base | i1_dv2 | x[t]-x[t-1]; zero at row 0 |
| 215 | d_i1_dv3 | base | i1_dv3 | x[t]-x[t-1]; zero at row 0 |
| 216 | d_a0 | base | a0 | x[t]-x[t-1]; zero at row 0 |
| 217 | d_a1 | base | a1 | x[t]-x[t-1]; zero at row 0 |
| 218 | d_a2 | base | a2 | x[t]-x[t-1]; zero at row 0 |
| 219 | d_a3 | base | a3 | x[t]-x[t-1]; zero at row 0 |
| 220 | d_a4 | base | a4 | x[t]-x[t-1]; zero at row 0 |
| 221 | d_a5 | base | a5 | x[t]-x[t-1]; zero at row 0 |
| 222 | d_a6 | base | a6 | x[t]-x[t-1]; zero at row 0 |
| 223 | d_a7 | base | a7 | x[t]-x[t-1]; zero at row 0 |
| 224 | time | base | row index | log1p(row)/log1p(20000) |
| 225 | ewma_slot_00 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 226 | ewma_slot_01 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 227 | ewma_slot_02 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 228 | ewma_slot_03 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 229 | ewma_slot_04 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 230 | ewma_slot_05 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 231 | ewma_slot_06 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 232 | ewma_slot_07 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 233 | ewma_slot_08 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 234 | ewma_slot_09 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 235 | ewma_slot_10 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 236 | ewma_slot_11 | ewma | TRAIN-selected i0_p column | x[t]-m[t]; m[0]=x[0]; m[t]=beta*m[t-1]+(1-beta)*x[t]; beta=0.5**(1/half_life_rows) |
| 237 | any_book_update | activity | i0_p0..21 and i0_v0..21 | 1 if any i0 p/v column changed on this row; 0 at row 0 |
| 238 | book_changed_fraction | activity | i0_p0..21 and i0_v0..21 | number changed among 44 i0 p/v columns / 44; 0 at row 0 |
| 239 | activity_h32 | activity | i0_p0..21 and i0_v0..21 | startup-corrected row EWMA of changed fraction, half-life 32 rows |
| 240 | activity_h512 | activity | i0_p0..21 and i0_v0..21 | startup-corrected row EWMA of changed fraction, half-life 512 rows |
| 241 | log_book_age | activity | i0_p0..21 and i0_v0..21 | log1p(rows since any i0 p/v update)/log1p(20000) |
| 242 | log_price_age | activity | i0_p0..21 and i0_v0..21 | log1p(rows since any i0 p update)/log1p(20000) |
| 243 | efficiency_h64 | activity | i0_p0..21 and i0_v0..21 | sum_c abs(EWMA_h64(dx_c)) / (sum_c EWMA_h64(abs(dx_c)) + 1e-12), i0 prices |
| 244 | efficiency_h512 | activity | i0_p0..21 and i0_v0..21 | sum_c abs(EWMA_h512(dx_c)) / (sum_c EWMA_h512(abs(dx_c)) + 1e-12), i0 prices |
| 245 | price_event | event | i0_p0..21; event = any current rounded price-column change | 1 on a current price event; 0 at row 0 |
| 246 | price_changed_fraction | event | i0_p0..21; event = any current rounded price-column change | number of i0 price columns changed / 22 |
| 247 | log_price_event_age | event | i0_p0..21; event = any current rounded price-column change | log1p(rows since price event)/log1p(20000) |
| 248 | log_price_event_count | event | i0_p0..21; event = any current rounded price-column change | log1p(events observed so far)/log1p(20000) |
| 249 | log_last_event_interval | event | i0_p0..21; event = any current rounded price-column change | log1p(rows between last two events)/log1p(20000); first measured from row 0 |
| 250 | last_event_mean_delta | event | i0_p0..21; event = any current rounded price-column change | mean_c dx_c at most recent event |
| 251 | last_event_mean_abs_delta | event | i0_p0..21; event = any current rounded price-column change | mean_c abs(dx_c) at most recent event |
| 252 | last_event_rms_delta | event | i0_p0..21; event = any current rounded price-column change | sqrt(mean_c dx_c**2) at most recent event |
| 253 | last_event_cosine | event | i0_p0..21; event = any current rounded price-column change | cosine(last_event_delta, previous_event_delta); zero without both nonzero norms |
| 254 | last_two_event_return_fraction | event | i0_p0..21; event = any current rounded price-column change | fraction with d_last+d_previous==0 among columns changed in either event; zero before first event |
| 255 | last_event_sign_agreement | event | i0_p0..21; event = any current rounded price-column change | mean sign(d_last)*sign(d_previous) among columns changed in both events; zero if none |
| 256 | price_delta_sign_mean | event | i0_p0..21; event = any current rounded price-column change | current row mean_c sign(dx_c); zero on a non-event |
| 257 | event_h2_signed_delta | event | i0_p0..21; event = any current rounded price-column change | mean signed delta; half-life 2 observed price events; held between events; startup-corrected EWMA starting from zero |
| 258 | event_h2_abs_delta | event | i0_p0..21; event = any current rounded price-column change | mean absolute delta; half-life 2 observed price events; held between events; startup-corrected EWMA starting from zero |
| 259 | event_h2_rms_delta | event | i0_p0..21; event = any current rounded price-column change | RMS delta; half-life 2 observed price events; held between events; startup-corrected EWMA starting from zero |
| 260 | event_h2_cosine | event | i0_p0..21; event = any current rounded price-column change | consecutive-event cosine; half-life 2 observed price events; held between events; startup-corrected EWMA starting from zero |
| 261 | event_h2_log_interval | event | i0_p0..21; event = any current rounded price-column change | log event interval / log1p(20000); half-life 2 observed price events; held between events; startup-corrected EWMA starting from zero |
| 262 | event_h2_level_residual_mean | event | i0_p0..21; event = any current rounded price-column change | mean_c(x_c - event_EWMA_h(x_c)); half-life 2 observed price events; held between events; price EWMA initialised from row 0 |
| 263 | event_h2_level_residual_abs | event | i0_p0..21; event = any current rounded price-column change | mean_c abs(x_c - event_EWMA_h(x_c)); half-life 2 observed price events; held between events; price EWMA initialised from row 0 |
| 264 | event_h8_signed_delta | event | i0_p0..21; event = any current rounded price-column change | mean signed delta; half-life 8 observed price events; held between events; startup-corrected EWMA starting from zero |
| 265 | event_h8_abs_delta | event | i0_p0..21; event = any current rounded price-column change | mean absolute delta; half-life 8 observed price events; held between events; startup-corrected EWMA starting from zero |
| 266 | event_h8_rms_delta | event | i0_p0..21; event = any current rounded price-column change | RMS delta; half-life 8 observed price events; held between events; startup-corrected EWMA starting from zero |
| 267 | event_h8_cosine | event | i0_p0..21; event = any current rounded price-column change | consecutive-event cosine; half-life 8 observed price events; held between events; startup-corrected EWMA starting from zero |
| 268 | event_h8_log_interval | event | i0_p0..21; event = any current rounded price-column change | log event interval / log1p(20000); half-life 8 observed price events; held between events; startup-corrected EWMA starting from zero |
| 269 | event_h8_level_residual_mean | event | i0_p0..21; event = any current rounded price-column change | mean_c(x_c - event_EWMA_h(x_c)); half-life 8 observed price events; held between events; price EWMA initialised from row 0 |
| 270 | event_h8_level_residual_abs | event | i0_p0..21; event = any current rounded price-column change | mean_c abs(x_c - event_EWMA_h(x_c)); half-life 8 observed price events; held between events; price EWMA initialised from row 0 |
| 271 | event_h32_signed_delta | event | i0_p0..21; event = any current rounded price-column change | mean signed delta; half-life 32 observed price events; held between events; startup-corrected EWMA starting from zero |
| 272 | event_h32_abs_delta | event | i0_p0..21; event = any current rounded price-column change | mean absolute delta; half-life 32 observed price events; held between events; startup-corrected EWMA starting from zero |
| 273 | event_h32_rms_delta | event | i0_p0..21; event = any current rounded price-column change | RMS delta; half-life 32 observed price events; held between events; startup-corrected EWMA starting from zero |
| 274 | event_h32_cosine | event | i0_p0..21; event = any current rounded price-column change | consecutive-event cosine; half-life 32 observed price events; held between events; startup-corrected EWMA starting from zero |
| 275 | event_h32_log_interval | event | i0_p0..21; event = any current rounded price-column change | log event interval / log1p(20000); half-life 32 observed price events; held between events; startup-corrected EWMA starting from zero |
| 276 | event_h32_level_residual_mean | event | i0_p0..21; event = any current rounded price-column change | mean_c(x_c - event_EWMA_h(x_c)); half-life 32 observed price events; held between events; price EWMA initialised from row 0 |
| 277 | event_h32_level_residual_abs | event | i0_p0..21; event = any current rounded price-column change | mean_c abs(x_c - event_EWMA_h(x_c)); half-life 32 observed price events; held between events; price EWMA initialised from row 0 |
| 278 | event_h128_signed_delta | event | i0_p0..21; event = any current rounded price-column change | mean signed delta; half-life 128 observed price events; held between events; startup-corrected EWMA starting from zero |
| 279 | event_h128_abs_delta | event | i0_p0..21; event = any current rounded price-column change | mean absolute delta; half-life 128 observed price events; held between events; startup-corrected EWMA starting from zero |
| 280 | event_h128_rms_delta | event | i0_p0..21; event = any current rounded price-column change | RMS delta; half-life 128 observed price events; held between events; startup-corrected EWMA starting from zero |
| 281 | event_h128_cosine | event | i0_p0..21; event = any current rounded price-column change | consecutive-event cosine; half-life 128 observed price events; held between events; startup-corrected EWMA starting from zero |
| 282 | event_h128_log_interval | event | i0_p0..21; event = any current rounded price-column change | log event interval / log1p(20000); half-life 128 observed price events; held between events; startup-corrected EWMA starting from zero |
| 283 | event_h128_level_residual_mean | event | i0_p0..21; event = any current rounded price-column change | mean_c(x_c - event_EWMA_h(x_c)); half-life 128 observed price events; held between events; price EWMA initialised from row 0 |
| 284 | event_h128_level_residual_abs | event | i0_p0..21; event = any current rounded price-column change | mean_c abs(x_c - event_EWMA_h(x_c)); half-life 128 observed price events; held between events; price EWMA initialised from row 0 |
| 285 | i0_v_changed_fraction | flow | i0_v0..21 | fraction of source columns changed on current row |
| 286 | i0_v_log_update_age | flow | i0_v0..21 | log1p(rows since any source-column update)/log1p(20000) |
| 287 | i0_v_delta_mean | flow | i0_v0..21 | mean source delta |
| 288 | i0_v_delta_abs_mean | flow | i0_v0..21 | mean absolute source delta |
| 289 | i0_v_delta_rms | flow | i0_v0..21 | RMS source delta |
| 290 | i0_v_update_rate_h32 | flow | i0_v0..21 | startup-corrected row EWMA of changed fraction, half-life 32 |
| 291 | i0_v_update_rate_h512 | flow | i0_v0..21 | startup-corrected row EWMA of changed fraction, half-life 512 |
| 292 | i0_v_abs_delta_h32 | flow | i0_v0..21 | startup-corrected row EWMA of mean absolute delta, half-life 32 |
| 293 | i0_v_abs_delta_h512 | flow | i0_v0..21 | startup-corrected row EWMA of mean absolute delta, half-life 512 |
| 294 | i0_v_level_residual_mean_h32 | flow | i0_v0..21 | mean source value minus its row EWMA_h32; level EWMA initialised from row 0 |
| 295 | i0_v_delta_rms_ratio_h512 | flow | i0_v0..21 | sqrt(mean(dx**2)/(startup-corrected EWMA_h512(mean(dx**2))+1e-12)) |
| 296 | i0_dp_changed_fraction | flow | i0_dp0..3 | fraction of source columns changed on current row |
| 297 | i0_dp_log_update_age | flow | i0_dp0..3 | log1p(rows since any source-column update)/log1p(20000) |
| 298 | i0_dp_delta_mean | flow | i0_dp0..3 | mean source delta |
| 299 | i0_dp_delta_abs_mean | flow | i0_dp0..3 | mean absolute source delta |
| 300 | i0_dp_delta_rms | flow | i0_dp0..3 | RMS source delta |
| 301 | i0_dp_update_rate_h32 | flow | i0_dp0..3 | startup-corrected row EWMA of changed fraction, half-life 32 |
| 302 | i0_dp_update_rate_h512 | flow | i0_dp0..3 | startup-corrected row EWMA of changed fraction, half-life 512 |
| 303 | i0_dp_abs_delta_h32 | flow | i0_dp0..3 | startup-corrected row EWMA of mean absolute delta, half-life 32 |
| 304 | i0_dp_abs_delta_h512 | flow | i0_dp0..3 | startup-corrected row EWMA of mean absolute delta, half-life 512 |
| 305 | i0_dp_level_residual_mean_h32 | flow | i0_dp0..3 | mean source value minus its row EWMA_h32; level EWMA initialised from row 0 |
| 306 | i0_dp_delta_rms_ratio_h512 | flow | i0_dp0..3 | sqrt(mean(dx**2)/(startup-corrected EWMA_h512(mean(dx**2))+1e-12)) |
| 307 | i0_dv_changed_fraction | flow | i0_dv0..3 | fraction of source columns changed on current row |
| 308 | i0_dv_log_update_age | flow | i0_dv0..3 | log1p(rows since any source-column update)/log1p(20000) |
| 309 | i0_dv_delta_mean | flow | i0_dv0..3 | mean source delta |
| 310 | i0_dv_delta_abs_mean | flow | i0_dv0..3 | mean absolute source delta |
| 311 | i0_dv_delta_rms | flow | i0_dv0..3 | RMS source delta |
| 312 | i0_dv_update_rate_h32 | flow | i0_dv0..3 | startup-corrected row EWMA of changed fraction, half-life 32 |
| 313 | i0_dv_update_rate_h512 | flow | i0_dv0..3 | startup-corrected row EWMA of changed fraction, half-life 512 |
| 314 | i0_dv_abs_delta_h32 | flow | i0_dv0..3 | startup-corrected row EWMA of mean absolute delta, half-life 32 |
| 315 | i0_dv_abs_delta_h512 | flow | i0_dv0..3 | startup-corrected row EWMA of mean absolute delta, half-life 512 |
| 316 | i0_dv_level_residual_mean_h32 | flow | i0_dv0..3 | mean source value minus its row EWMA_h32; level EWMA initialised from row 0 |
| 317 | i0_dv_delta_rms_ratio_h512 | flow | i0_dv0..3 | sqrt(mean(dx**2)/(startup-corrected EWMA_h512(mean(dx**2))+1e-12)) |
| 318 | volume_abs_delta_on_price_event | flow | i0 only | mean absolute volume delta times current price-event flag |
| 319 | dp_update_on_price_event | flow | i0 only | current dp-column update AND current price event |
| 320 | dv_update_on_price_event | flow | i0 only | current dv-column update AND current price event |
| 321 | i0_p_prefix_residual_mean | context | i0_p0..21 | mean_c(x_c - causal expanding mean_c); prefix includes current row only |
| 322 | i0_p_prefix_residual_abs_mean | context | i0_p0..21 | mean_c abs(x_c - causal expanding mean_c); prefix includes current row only |
| 323 | i0_p_prefix_z_mean | context | i0_p0..21 | mean_c ((x_c-prefix_mean_c)/(prefix_std_c+1e-6)); prefix includes current row only |
| 324 | i0_p_prefix_z_abs_mean | context | i0_p0..21 | mean_c abs((x_c-prefix_mean_c)/(prefix_std_c+1e-6)); prefix includes current row only |
| 325 | i0_p_prefix_std_mean | context | i0_p0..21 | mean_c prefix_std_c, population denominator t+1 (Welford update); prefix includes current row only |
| 326 | i0_p_prefix_opening_displacement_mean | context | i0_p0..21 | mean_c(x_c-x_c[0]); prefix includes current row only |
| 327 | i0_p_prefix_opening_displacement_abs_mean | context | i0_p0..21 | mean_c abs(x_c-x_c[0]); prefix includes current row only |
| 328 | i0_v_prefix_residual_mean | context | i0_v0..21 | mean_c(x_c - causal expanding mean_c); prefix includes current row only |
| 329 | i0_v_prefix_residual_abs_mean | context | i0_v0..21 | mean_c abs(x_c - causal expanding mean_c); prefix includes current row only |
| 330 | i0_v_prefix_z_mean | context | i0_v0..21 | mean_c ((x_c-prefix_mean_c)/(prefix_std_c+1e-6)); prefix includes current row only |
| 331 | i0_v_prefix_z_abs_mean | context | i0_v0..21 | mean_c abs((x_c-prefix_mean_c)/(prefix_std_c+1e-6)); prefix includes current row only |
| 332 | i0_v_prefix_std_mean | context | i0_v0..21 | mean_c prefix_std_c, population denominator t+1 (Welford update); prefix includes current row only |
| 333 | i0_v_prefix_opening_displacement_mean | context | i0_v0..21 | mean_c(x_c-x_c[0]); prefix includes current row only |
| 334 | i0_v_prefix_opening_displacement_abs_mean | context | i0_v0..21 | mean_c abs(x_c-x_c[0]); prefix includes current row only |
| 335 | i0_encoded_order_00 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[0] |
| 336 | i0_encoded_order_01 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[1] |
| 337 | i0_encoded_order_02 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[2] |
| 338 | i0_encoded_order_03 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[3] |
| 339 | i0_encoded_order_04 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[4] |
| 340 | i0_encoded_order_05 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[5] |
| 341 | i0_encoded_order_06 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[6] |
| 342 | i0_encoded_order_07 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[7] |
| 343 | i0_encoded_order_08 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[8] |
| 344 | i0_encoded_order_09 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[9] |
| 345 | i0_encoded_order_10 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[10] |
| 346 | i0_encoded_order_11 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[11] |
| 347 | i0_encoded_order_12 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[12] |
| 348 | i0_encoded_order_13 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[13] |
| 349 | i0_encoded_order_14 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[14] |
| 350 | i0_encoded_order_15 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[15] |
| 351 | i0_encoded_order_16 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[16] |
| 352 | i0_encoded_order_17 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[17] |
| 353 | i0_encoded_order_18 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[18] |
| 354 | i0_encoded_order_19 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[19] |
| 355 | i0_encoded_order_20 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[20] |
| 356 | i0_encoded_order_21 | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sort(x_i0p)[21] |
| 357 | i0_encoded_central_order_gap | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sorted[11]-sorted[10] |
| 358 | i0_encoded_order_centre | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | (sorted[10]+sorted[11])/2 |
| 359 | i0_encoded_order_range | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | sorted[21]-sorted[0] |
| 360 | i0_encoded_order_abs_delta_mean | shape | all 22 encoded i0 price-column values; no bid/ask interpretation | mean absolute change in sorted values since previous row; zero at row 0 |

1. it seems we should test EWMA on other prices than the 12 selected i0_ps, can we add more horizons for each ps? I am assuming we have 1 EWMA for 12 selected ps.
2. Can we add book crossing? Can we also add specific events on i0_p0, can we also add some features for delay between book change and expected t0, t1 change? can we also add more activity and efficiency horizons?
Can we also add orderbook direction changes due to the activities?
3. Do we have anything measuring the entire orderbook, we tested and could sort the book by lowest to highest, but they were somewhat based on order queue, rather than index and say sometimes i0_p3 would be the closest to the current mid on the bid side and i0_p17 would be. But than it would shift and i0_p4 would be closest and i0_p19 would be closest. We need something measuring that and sorting it so we can understand what the slope, regime, best bid, best ask were and how the gap and behaviors would be.


## Hypothesis tested


4. for the detection of regimes, do we have anything measuring linear trend slope of say i0p0, i0p20, so and so on, along with the entire orderbook. We would want to measure if the book is moving upwards, so buying is best, if the book is moving down the sell is best.
5. We want to also add something measuring chunkiness, say volatility of the book, say stds of all the prices, say something like various horizons, stds of all the prices on 12, 24, 36, 124, etc. rolling window. We also want to check those linear regression slopes for windows like that.
6. WE should also do something like rolling correlations, it might be that adjusting different importances, say how important are moving averages if the correllations increase.
