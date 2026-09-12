# A Simple Method for Automated Equilibration Detection in Molecular Simulations

**Authors:** John D. Chodera
**Year:** 2016
**Venue:** Journal of Chemical Theory and Computation
**DOI:** 10.1021/acs.jctc.5b00784
**Source PDF URL:** https://www.biorxiv.org/content/10.1101/021659v2.full.pdf
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

Note: this Markdown is derived from the bioRxiv preprint (doi:10.1101/021659v2), the legal open-access version of this paper; the ACS-hosted published PDF was not accessible (Cloudflare bot-detection). Body text matches the published article; the bioRxiv preprint predates final JCTC copyediting.

---



A simple method for automated equilibration detection in molecular simulations

John D. Chodera1, ∗

Computational Biology Program, Sloan Kettering Institute,
Memorial Sloan Kettering Cancer Center, New York, NY 10065
(Dated: July 4, 2015)

Molecular simulations intended to compute equilibrium properties are often initiated from configurations
that are highly atypical of equilibrium samples, a practice which can generate a distinct initial transient
in mechanical observables computed from the simulation trajectory. Traditional practice in simulation
data analysis recommends this initial portion be discarded to equilibration, but no simple, general, and
automated procedure for this process exists. Here, we suggest a conceptually simple automated procedure
that does not make strict assumptions about the distribution of the observable of interest, in which the
equilibration time is chosen to maximize the number of effectively uncorrelated samples in the production
timespan used to compute equilibrium averages. We present a simple Python reference implementation of
this procedure, and demonstrate its utility on typical molecular simulation data.
Keywords: molecular dynamics (MD); Metropolis-Hastings; Monte Carlo (MC); Markov chain Monte Carlo
(MCMC); equilibration; burn-in; timeseries analysis; statistical inefficiency; integrated autocorrelation time

INTRODUCTION

induced by atypical initial starting conditions. It is worth
noting that a similar procedure is not a practice universally
40 recommended by statisticians when sampling from poste41 rior distributions in statistical inference [4]; the differences
42 in complexity of probability densities typically encountered
43 in statistics and molecular simulation may explain the dif44 ference in historical practice.
As a motivating example, consider the computation of
46 the average density of liquid argon under a given set of re47 duced temperature and pressure conditions shown in Fig48 ure 1. To initiate the simulation, an initial dense liquid ge∗
49 ometry at reduced density ρ
≡ ρσ 3 = 0.960 was pre50 pared and subjected to local energy minimization. The up51 per panel of Figure 1 depicts the average relaxation behav52 ior of simulations initiated from the same configuration with
53 different random initial velocities and integrator random
54 number seeds (see Simulation Details). The average (black
55 line) and 95% confidence interval (shaded grey) of 500 re56 alizations of this process show a characteristic relaxation
57 behavior away from the initial density toward the equilib58 rium density. The expectation of the running average of the
59 density over many realizations of this procedure (Figure 1,
60 lower panel) significantly deviates from the true expecta61 tion (dashed line), leading to significantly biased estimates
62 of the expectation unless simulations are sufficiently long to
63 eliminate this starting point dependent bias—a surprisingly
64 long 30 ns in this case. Note that this bias is present even in
65 the average of many realizations because the same atypical
66 starting condition is used for every realization of this simu67 lation process.
To develop an automatic approach to eliminating this
69 bias, we take motivation from the concept of reverse cumu70 lative averaging from Yang et al. [6], in which the trajectory
71 statistics over the production region of the trajectory are
72 examined for different choices of the end of the discarded
73 equilibration region to determine the optimal production
74 region to use for computing expectations and other statis75 tical properties. We begin by first formalizing our objectives
76 mathematically.

Molecular simulations use Markov chain Monte Carlo
(MCMC) techniques [1] to sample configurations x from an
9 equilibrium distribution π(x), either exactly (using Monte
10 Carlo methods such as Metropolis-Hastings) or approx11 imately (using molecular dynamics integrators without
12 Metropolization) [2].
Due to the sensitivity of the equilibrium probability den14 sity π(x) to small perturbations in configuration x and the
15 difficulty of producing sufficiently good guesses of typical
16 equilibrium configurations x ∼ π(x), these molecular sim17 ulations are often started from highly atypical initial con18 ditions. For example, simulations of biopolymers might be
19 initiated from a fully extended conformation unrepresenta20 tive of behavior in solution, or a geometry derived from a fit
21 to diffraction data collected from a cryocooled crystal; sol22 vated systems may be prepared by periodically replicating
23 a small solvent box equilibrated under different conditions,
24 yielding atypical densities and solvent structure; liquid mix25 tures or lipid bilayers may be constructed by using methods
26 that fulfill spatial constraints (e.g. PackMol [3]) but create lo27 cally aytpical geometries, requiring long simulation times to
28 relax to typical configurations.
As a result, traditional practice in molecular simulation
30 has recommended some initial portion of the trajectory be
31 discarded to equilibration (also called burn-in in the MCMC
32 literature [4]). While the process of discarding initial sam33 ples is strictly unnecessary for the time-average of quanti34 ties of interest to eventually converge to the desired expec35 tations [5], this nevertheless often allows the practitioner to
36 avoid what may be impractically long run times to eliminate
37 the bias in computed properties in finite-length simulations

∗ Corresponding author; john.chodera@choderalab.org
1 The term burn-in comes from the field of electronics,

in which a
short “burn-in” period is used to ensure that a device is free of faulty
components—which often fail quickly—and is operating normally [4].

reduced density ρ ∗ reduced density ρ ∗

1.00
0.95
0.90
0.85
0.80
0.75
1.00
0.95
0.90
0.85
0.80
0.75

true expectation
cumulative average
discarding first 100 τ to equilibration

simulation length / τ

FIG. 1. Illustration of the motivation for discarding data to equilibration. To illustrate the bias in expectations induced by relaxation
away from initial conditions, 500 replicates of a simulation of liquid argon were initiated from the same energy-minimized initial configuration constructed with initial reduced density ρ∗ ≡ ρσ 3 = 0.960 but different random number seeds for stochastic integration. Top: The
average of the reduced density (black line) over the replicates relaxes to the region of typical equilibrium densities over the first ∼ 90 τ
of simulation time, where τ is a natural time unit (see Simulation Details). Bottom: If the average density is estimated by a cumulative
average from the beginning of the simulation (red dotted line), the estimate will be heavily biased by the atypical starting density even
beyond 1000 τ . Discarding even a small amount of initial data—in this case 500 initial samples—results in a cumulative average estimate
that converges to the true average (black dashed line) much more rapidly. Shaded regions denote 95% confidence intervals.

true expectation
discarding initial [0,t0 ]

ρ

­ ∗®

[t0 ,T]

Neff

g / iterations

0.794
0.790
0.786
0.782
0.778

equilibration end time t0 / τ

FIG. 2. Statistical inefficiency, number of uncorrelated samples, and bias for different equilibration times. Trajectories of length
T = 2000 τ for the argon system described in Figure 1 were analyzed as a function of equilibration time choice t0 . Averages over all 500
replicate simulations (all starting from the same initial conditions) are shown as dark lines, with shaded lines showing standard deviation
of estimates among replicates. Top: The statistical inefficiency g as a function of equilibration time choice t0 is initially very large, but
diminishes rapidly after the system has relaxed to equilibrium. Middle: The number of effectively uncorrelated samples Neff = (T − t0 +
1)/g shows a maximum at t0 ∼ 90 τ (red vertical lines), suggesting the system has equilibrated by this time. Bottom: The cumulative
average density hρ∗ i computed over the span [t0 , T ] shows that the bias (deviation from the true estimate, shown as red dashed lines)
is minimized for choices of t0 ≥ 90 τ . The standard deviation among replicates (shaded region) grows with t0 because fewer data are
included in the estimate. The choice of optimal t0 that maximizes Neff (red vertical line) strikes a good balance between bias and variance.
The true estimate (red dashed lines) is computed from averaging over the range [5 000, 10 000] τ over all 500 replicates.

STATEMENT OF THE PROBLEM

BIAS-VARIANCE TRADEOFF

Consider T successively sampled configurations xt from 104 With increasing equilibration time t0 , bias is reduced, but
a molecular simulation, with t = 1, . . . , T , initiated from x0 . 105 the variance—the contribution to error due to random varia80 We presume we are interested in computing the expectation 106 tion from having a finite number of uncorrelated samples—
Z
107 will increase because less data is included in the estimate.
hAi ≡ dx A(x) π(x)
(1) 108 This can be seen in the bottom panel of Figure 2, where
109 the shaded region (95% confidence interval of the mean) in81 of a mechanical property A(x). For convenience, we will re110 creases in width with increasing equilibration time t0 .
82 fer to the timeseries at ≡ A(xt ), with t ∈ [1, T ]. The esti111
To examine the tradeoff between bias and variance ex83 mator Â ≈ hAi constructed from the entire dataset is given
112 plicitly, Figure 3 plots the bias and variance (here, shown as
84 by
113 standard error) contributions against each other as a funcT
114 tion of t0 (denoted by color) as computed from statistics
X
Â[1,T ] ≡
at .
(2) 115 over all 500 replicates. At t0 = 0, the bias is large but
T t=1
116 variance is minimized. With increasing t0 , bias is eventu117 ally eliminated but then variance rapidly grows as fewer un85 While limT →∞ Â[1,T ] = hAi for an infinitely long simula118 correlated samples are included in the estimate. There is a
86 tion , the bias in Â[1,T ] may be significant in a simulation of
119 clear optimal choice at t0 ∼ 90 τ that minimizes variance
87 finite length T .
120 while also effectively eliminating bias (where τ is a natural
By discarding samples t < t0 to equilibration, we hope to 121 time unit—see Simulation Details).
89 exclude the initial transient from our sample average, and
90 provide a less biased estimate of hAi,

Â[t0 ,T ] ≡

T
X
at .
T − t0 + 1 t=t

(3)

SELECTING THE EQUILIBRATION TIME

Is there a simple approach to choosing an optimal equilibration time t0 that provides a significantly improved esti125 mate Â[t ,T ] , even when we do not have access to multiple
126 realizations? At worst, we hope that such a procedure would
127 at least give some improvement over the naive estimate,
128 such that δ Â[t ,T ] < δ Â[0,T ] ; at best, we hope that we can
129 achieve a reasonable bias-variance tradeoff close to the op94 where Ex [·] denotes the expectation over independent re0
130 timal point identified in Figure 3 that minimizes bias with95 alizations of the specific simulation process initiated from
131 out greatly increasing variance. We remark that, for cases
96 configuration x0 , but with different velocities and random
132 in which the simulation is not long enough to reach equilib97 number seeds.
133 rium, no choice of t0 will eliminate bias completely; the best
We can rewrite the expected error δ 2 Â by separating it
134 we can hope for is to minimize this bias.
99 into two components:
While automated methods for selecting the equilibration

2 
136 time t0 have been proposed, these approaches have shortδ 2 Â[t0 ,T ] = Ex0 Â[t0 ,T ] − Ex0 [Â[t0 ,T ] ]
137 comings that have greatly limited their use. The reverse

2
138 cumulative averaging (RCA) method proposed by Yang et
+ Ex0 [Â[t0 ,T ] ] − hAi
(5) 139 al. [6], for example, uses a statistical test for normality to de140 termine the point before which which the observable time100 The first term denotes the variance in the estimator Â,
141 series deviates from normality when examining the timeh
i2
142 series in reverse. While this concept may be reasonable for
varx0 (Â[t0 ,T ] ) ≡ Ex0 Â[t0 ,T ] − Ex0 [Â[t0 ,T ] ]
(6)
143 experimental data, where measurements often represent
101 while the second term denotes the contribution from the 144 the sum of many random variables such that the central
145 limit theorem’s guarantee of asymptotic normality ensures
102 squared bias,

2
146 the distribution of the observable will be approximately norbias2x0 (Â[t0 ,T ] ) ≡ Ex0 [Â[t0 ,T ] ] − hAi
(7) 147 mal, there is no such guarantee that instantaneous mea148 surements of a simulation property of interest will be nor149 mally distributed. In fact, many properties will be decidedly
150 non-normal. For a biomolecule such as a protein, for exam2 We note that this equality only holds for simulation schemes that sam151 ple, the radius of gyration, end-to-end distance, and torsion
ple from the true equilibrium density π(x), such as Metropolis-Hastings
152 angles sampled during a simulation will all be highly nonMonte Carlo or Metropolized dynamical integration schemes such as hybrid Monte Carlo (HMC). Molecular dynamics simulations utilizing finite 153 normal. Instead, we require a method that makes no astimestep integration without Metropolization will produce averages that 154 sumptions about the nature of the distribution of the propmay deviate from the true expectation hAi [2].
155 erty under study.
We can quantify the overall error in an estimator Â[t0 ,T ]
92 in a sample average that starts at x0 and excludes samples
93 where t < t0 by the expected error δ Â[t ,T ] ,

2 
δ Â[t0 ,T ] ≡ Ex0 Â[t0 ,T ] − hAi
(4)

AUTOCORRELATION ANALYSIS

with the discrete-time normalized fluctuation autocorrelation function Ct defined as

The set of successively sampled configurations {xt } and
han an+t i − han i2
.
(13)
Ct ≡
their corresponding observables {at } compose a correlated
ha2n i − han i2
159 timeseries of observations. To estimate the statistical er160 ror or uncertainty in a stationary timeseries free of bias, 185 In practice, it is difficult to estimate Ct for t ∼ T , due to
161 we must be able to quantify the effective number of un- 186 growth in the statistical error, so common estimators of g
162 correlated samples present in the dataset. This is usually 187 make use of several additional properties of Ct to provide
163 accomplished through computation of the statistical ineffi- 188 useful estimates (see Practical Computation of Statistical In164 ciency g, which quantifies the number of correlated time- 189 efficiencies).
The t0 subscript for the variance σ 2 , the integrated auto165 series samples needed to produce a single effectively un- 190
191 correlation time τ , and the statistical inefficiency t0 mean
166 correlated sample of the observable of interest. While these
167 concepts are well-established for the analysis of both Monte 192 that these quantities are only estimated over the production
T
168 Carlo and molecular dynamics simulations [7–10], we re- 193 portion of the timeseries, {at }t=t0 . Since we assumed that
the
bias
was
eliminated
by
judicious
choice of the equilibra169 view them here for the sake of clarity.
tion
time
t
,
this
estimate
of
the
statistical
error will be poor
For a given equilibration time choice t0 , the statistical un196 for choices of t0 that are too small.
171 certainty in our estimator Â[t ,T ] can be written as,

2 
δ Â[t0 ,T ] ≡ Ex0 Â[t0 ,T ] − hÂi
THE ESSENTIAL IDEA

h
i
i2
h
= Ex0 Â2[t0 ,T ] − Ex0 Â[t0 ,T ]

Suppose we choose some arbitrary time t0 and discard
all samples t ∈ [0, t0 ) to equilibration, keeping [t0 , T ] as the
200 dataset to analyze. How much data remains? We can de{Ex0 [at at0 ] − Ex0 [at ] Ex0 [at0 ]}
= 2
201 termine this by computing the statistical inefficiency gt0 for
Tt0 0
t,t =t0
202 the interval [t0 , T ], and computing the effective number of
T
o
 
203 uncorrelated samples Neff (t0 ) ≡ (T − t0 + 1)/gt . If we
1 Xn
Ex0 x2t − Ex0 [xt ]
(8) 204 start at t ≡ T and move t to earlier and earlier points
= 2
in
Tt0 t=t
205 time, we expect that the effective number of uncorrelated
T
206 samples Neff (t0 ) will continue to grow until we start to in1 X
+ 2
{Ex0 [at at0 ] − Ex0 [at ] Ex0 [at0 ]} , 207 clude the highly atypical initial data. At that point, the inteTt0
t6=t0 =t0
208 grated autocorrelation time τ (and hence the statistical in209 efficiency g) will greatly increase (a phenomenon observed
172 where Tt0 ≡ T − t0 + 1, the number of correlated samples
210 earlier, e.g. Figure 2 of [6]). As a result, the effective number
T
173 in the timeseries {at }t . In the last step, we have split the
211 of samples Neff will start to plummet.
174 double-sum into two separate sums—a term capturing the
Figure 2 demonstrates this behavior for the liquid argon
175 variance in the observations at , and a remaining term cap213 system described above, using averages of the statistical
176 turing the correlation between observations.
If t0 is sufficiently large for the initial bias to be eliminated, 214 inefficiency gt0 and Neff (t0 ) computed over 500 indepen215 dent replicate trajectories. At short t0 , the average statisT
178 the remaining timeseries {at }t will obey the properties of
216 tical inefficiency g (Figure 2, top panel) is large due to the
179 both stationarity and time-reversibility, allowing us to write,
217 contribution from slow relaxation from atypical initial con
1  2
218 ditions, while at long t0 the statistical inefficiency estimate
2 equil
δ Â[t0 ,T ] =
hat i − hat i
219 is much shorter and nearly constant of a large span of time
Tt0
220 origins. As a result, the average effective number of uncor
TX
−t0 
Tt0 − n
221 related samples Neff (Figure 2, middle panel) has a peak at
+
[hat at+n i − hat ihat+n i]
Tt0 n=1
Tt0
222 t0 ∼ 90 τ (Figure 2, vertical red lines). The effect on bias in
∗
223 the estimated average reduced density hρ i (Figure 2, botσt20
σt20
≡
(1 + 2τt0 ) =
,
(9) 224 tom panel) is striking—the bias is essentially eliminated for
Tt0
Tt0 /gt0
225 the choice of equilibration time t0 that maximizes the num226 ber of uncorrelated samples Neff .
180 where the variance σ , statistical inefficiency g, and inte227
This suggests an alluringly simple algorithm for identify181 grated autocorrelation time τ (in units of the sampling in228 ing the optimal equilibration time—pick the t0 which maxi182 terval) are given by
229 mizes the number of uncorrelated samples Neff . In mathe2
matical terms,
σ ≡ hat i − hat i ,
(10)


T
−1
topt
= argmax Neff (t0 )
(14)
X
t
t0
Ct ,
(11)
τ≡
1−
T
T − t0 + 1
t=1
= argmax
g ≡ 1 + 2τ ,
(12)
gt0
t0
T
X

Overall RMS error. How well does this strategy perform
in terms of decreasing the overall error δ Â[t0 ,T ] compared
249 to δ Â[0,T ] ? Figure 4 compares the expected standard er250 ror (denoted δ Â) as a function of a fixed initial equilibration
251 time t0 (black line with shaded region denoting 95% confi252 dence interval) with the strategy of selecting t0 to maximize
253 Neff for each realization (red line with shaded region de254 noting 95% confidence interval). While the minimum error
255 for the fixed-t0 strategy (0.00154±0.00005) is achieved at
256 90 τ —a fact that could only be determined from knowledge
257 of multiple realizations—the simple strategy of selecting t0
258 using Eq. 14 achieves a minimum error of 0.00171±0.00006,
259 only 11% worse (compared to errors of 0.00456±0.00007, or
260 296% worse, should no data have been discarded).

standard error

0.006
0.004
0.002
0.000
0.000 0.002 0.004 0.006
bias

DISCUSSION

The scheme described here—in which the equilibration
time t0 is computed using Eq. 14 as the choice that maxi264 mizes the number of uncorrelated samples in the producFIG. 3. Bias-variance tradeoff for fixed equilibration time 265 tion region [t0 , T ]—is both conceptually and computationversus automatic equilibration time selection. Trajectories of 266 ally straightforward. It provides an approach to determining
length T = 2000τ for the argon system described in Figure 1 were 267 the optimal amount of initial data to discard to equilibration
analyzed as a function of equilibration time choice t0 , with col- 268 in order to minimize variance while also minimizing initial
ors denoting the value of t0 (in units of τ ) corresponding to each 269 bias, and does this without employing statistical tests that
plotted point. Using 500 replicate simulations, the average bias 270 require generally unsatisfiable assumptions of normality of
(average deviation from true expectation) and standard deviation 271 the observable of interest. As we have seen, this scheme em(random variation from replicate to replicate) were computed as 272 pirically appears to select a practical compromise between
a function of a prespecified fixed equilibration time t0 , with colors 273 bias and variance even when the statistical inefficiency g is
running from violet (0 τ ) to red (1800 τ ). As is readily discerned,
274 estimated directly from the trajectory using Eq. 12.
the bias for small t0 is initially large, but minimized for larger t0 . By
A word of caution is necessary. One can certainly envision
contrast, the standard error (a measure of variance, estimated here
276 pathological scenarios where this algorithm for selecting an
by standard deviation among replicates) grows as t0 grows above
a certain critical time (here, ∼ 90 τ ). If the t0 that maximizes Neff 277 optimal equilibration time will break down. In cases where
is instead chosen individually for each trajectory based on that tra- 278 the simulation is not long enough to reach equilibrium—let
jectory’s estimates of statistical inefficiency g[t0 ,T ] , the resulting 279 alone collect many uncorrelated samples from it—no choice
bias-variance tradeoff (black triangle) does an excellent job min- 280 of equilibration time will bestow upon the experimenter the
imizing bias and variance simultaneously, comparable to what is 281 ability to produce an unbiased estimate of the true expectapossible for a choice of equilibration time t0 based on knowledge 282 tion. Similarly, in cases where insufficient data is available
of the true bias and variance among many replicate estimates.
283 for the statistical inefficiency to be estimated well, this al284 gorithm is expected to perform poorly. However, in these
285 cases, the data itself should be suspect if the trajectory is
Bias-variance tradeoff. How will the simple strategy of 286 not at least an order of magnitude longer than the minimum
232 selecting the equilibration time t0 using Eq 14 work for cases 287 estimated autocorrelation time.
233 where we do not know the statistical inefficiency g as a func234 tion of the equilibration time t0 precisely? When all that is
SIMULATION DETAILS
235 available is a single simulation, our best estimate of gt is 288
236 derived from that simulation alone over the span [t0 , T ]—
237 will this affect the quality of our estimate of equilibration 289
All molecular dynamics simulations described here were
238 time? Empirically, this does not appear to be the case— 290 performed with OpenMM 6.2 [11] (available at openmm.org)
239 the black triangle in Figure 3 shows the bias and variance 291 using the Python API. All scripts used to retrieve the software
240 contributions to the error for estimates computed over the 292 versions used here, run the simulations, analyze data, and
241 500 replicates where t0 is individually determined from each 293 generate plots—along with the simulation data itself and
242 simulation using this simple scheme based on selecting t0 294 scripts for generating figures—are available on GitHub .
243 to maximize Neff for each individual realization. Despite not
244 having knowledge about multiple realizations, this strategy
3 All Python scripts necessary to reproduce this work—along with data
245 effectively achieves a near-optimal balance between miniplotted in the published version—are available at:
246 mizing bias without increasing variance.

δÂ

0.006
0.005
0.004
0.003
0.002
0.001
0.000

equilibration end time t0 / τ

FIG. 4. RMS error for fixed equilibration time versus automatic equilibration time selection. Trajectories of length T = 2000τ for
the argon system described in Figure 1 were analyzed as a function of fixed equilibration time choice t0 . Using 500 replicate simulations,
the root-mean-squared (RMS) error (Eq. 4) was computed (black line) along with 95% confidence interval (gray shading). The RMS error is
minimized for fixed equilibration time choices in the range 90–200 τ . If the t0 that maximizes Neff is instead chosen individually for each
trajectory based on that trajectory’s estimated statistical inefficiency g[t0 ,T ] using Eq. 14, the resulting RMS error (red line, 95% confidence
interval shown as red shading) is quite close to the minimum RMS error achieved from any particular fixed choice of equilibration time t0 ,
suggesting that this simple automated approach to selecting t0 achieves close to optimal performance.

To model liquid argon, the LennardJonesFluid model 321 PRACTICAL COMPUTATION OF STATISTICAL INEFFICIENCIES
system in the openmmtools package4 was used with param297 eters appropriate for liquid argon (σ = 3.4 Å,  = 0.238
The robust computation of the statistical inefficiency g
298 kcal/mol). All results are reported in reduced (dimension323 (defined by Eq. 12) for a finite timeseries at , t = 0, . . . , T
299 less) units. A cubic switching function was employed, with
324 deserves some comment. There are, in fact, a variety of
300 the potential gently switched to zero over r ∈ [σ, 3σ], and
325 schemes for estimating g described in the literature, and
301 a long-range isotropic dispersion correction accounting for
326 their behaviors for finite datasets may differ, leading to dif302 this switching behavior used to include neglected contribu327 ferent estimates of the equilibration time t0 using the algo303 tions. Simulations were performed using a periodic box of
328 rithm of Eq. 14.
∗
304 N = 500 atoms at reduced temperature T
≡ kB T / = 329 The main issue is that a straightforward approach to es∗
305 0.850 and reduced pressure p
≡ pσ / = 1.266 using a 330 timating the statistical inefficiency using Eqs. 11–13 in which
306 Langevin integrator [12] with timestep ∆t = 0.01τ and col331 the expectations are simply replaced with sample estimates
−1
307 lision rate ν = τ
, with characteristic oscillation timescale 332 causes the statistical error in the estimated correlation funcp
mr02 /72 and r0 = 21/6 σ [13]. All times are reported 333 tion Ct to grow with t in a manner that allows this error to
308 τ =
309 in multiples of the characteristic timescale τ . A molecu334 quickly overwhelm the sum of Eq. 11. As a result, a number of
310 lar scaling Metropolis Monte Carlo barostat with Gaussian
335 alternative schemes—generally based on controlling the er311 simulation volume change proposal moves attempted ev336 ror in the estimated Ct or truncating the sum of Eq. 11 when
312 ery τ (100 timesteps), using an adaptive algorithm that ad337 the error grows too large—have been proposed.
313 justs the proposal width during the initial part of the simu338
For stationary, irreducible, reversible Markov chains,
314 lation [11]. Densities were recorded every τ (100 timesteps).
339 Geyer observed that a function Γk ≡ γ2k + γ2k+1 of the
∗
315 The true expectation hρ i was estimated from the sample
340 unnormalized fluctuation autocorrelation function γt
≡
316 average over all 500 realizations over [5000,10000] τ .
341 hai ai+t i − hai i has a number of pleasant properties (The317
The automated equilibration detection scheme is also 342 orem 3.1 of [14]): It is strictly positive, strictly decreasing,
318 available in the timeseries module of the pymbar pack343 and strictly convex. Some or all of these properties can be
319 age as detectEquilibration(), and can be accessed us344 exploited to define a family of estimators called initial se320 ing the following code:
345 quence methods (see Section 3.3 of [14] and Section 1.10.2
346 of [4]), of which the initial convex sequence (ICS) estimator is
347 generally agreed to be optimal, if somewhat more complex
from pymbar.timeseries import detectEquilibration
348 to implement.
# determine equilibrated region
All computations in this manuscript used the fast mul[t0, g, Neff_max] = detectEquilibration(A_t)
350 tiscale method described in Section 5.2 of [10], which we
# discard initial samples to equilibration
351 found performed equivalently well to the Geyer estimators
A_t = A_t[t0:]
352 (data not shown). This method is related to a multiscale

5 Implementations of these methods are provided with the code dishttp://github.com/choderalab/automatic-equilibration-detection
tributed with this manuscript.

4 available at http://github.com/choderalab/openmmtools

ACKNOWLEDGMENTS
variant of the initial positive sequence (IPS) method of Geyer 359
[15], where contributions are accumulated at increasingly
355 longer lag times and the sum of Eq. 11 is truncated when the
We are grateful to William C. Swope (IBM Almaden Re356 terms become negative. We have found this method to be
361 search Center) for his illuminating introduction to the use
357 both fast and to provide useful estimates of the statistical
362 of autocorrelation analysis for the characterization of sta358 inefficiency, but it may not perform well for all problems.
363 tistical error, as well as Michael R. Shirts (University of Vir364 ginia), David L. Mobley (University of California, Irvine),
365 Michael K. Gilson (University of California, San Diego), Kyle
366 A. Beauchamp (MSKCC), and Robert C. McGibbon (Stan367 ford University) for valuable discussions on this topic, and
368 Joshua L. Adelman (University of Pittsburgh) for helpful
369 feedback and encouragement. We are grateful to Michael
370 K. Gilson (University of California, San Diego) and Wei
371 Yang (Florida State University) for critical feedback on the
372 manuscript itself.

[1] J. S. Liu, Monte Carlo strategies in scientific computing, 2nd ed. 392
Marx, and A. Murmatsu (John von Neumann Institute for Comed. (Springer-Verlag, New York, 2002).
puting, ADDRESS, 2002), Vol. 10, pp. 423–445.
[2] D. Sivak, J. Chodera, and G. Crooks, Physical Review X 3, 394 [10] J. D. Chodera, W. C. Swope, J. W. Pitera, C. Seok, and K. A. Dill,
011007 (2013), bibtex: Sivak:2013:Phys.Rev.X.
J. Chem. Theor. Comput. 3, 26 (2007).
[3] L. Martínez, R. Andrade, E. G. Birgin, and J. M. Martínez, J. 396 [11] P. Eastman, M. Friedrichs, J. D. Chodera, R. Radmer, C. Bruns,
Chem. Theor. Comput. 30, 2157 (2009).
J. Ku, K. Beauchamp, T. J. Lane, L.-P. Wang, D. Shukla, T. Tye,
[4] S. Brooks, A. Gelman, G. L. Jones, and X.-L. Meng, in Hand- 398
M. Houston, T. Stitch, and C. Klein, J. Chem. Theor. Comput. 9,
book of Markov chain Monte Carlo, Chapman & Hall/CRC Hand- 399
461 (2012).
books of Modern Statistical Methods (CRC Press, ADDRESS, 400 [12] D. A. Sivak, J. D. Chodera, and G. E. Crooks, J. Phys. Chem. B
2011), Chap. Introduction to Markov chain Monte Carlo.
118, 6466 (2014).
[5] C. Geyer, Burn-in is unnecessary., http://users.stat.umn. 402 [13] B. Veytsman and M. Kotelyanskii, Lennard-Jones potenedu/~geyer/mcmc/burn.html.
tial revisited., http://borisv.lk.net/matsc597c-1997/
[6] W. Yang, R. Bittetti-Putzer, and M. Karplus, J. Chem. Phys. 120, 404
simulations/Lecture5/node3.html.
2618 (2004).
405 [14] C. J. Geyer, Stat. Sci. 76, 473 (1992).
[7] H. Müller-Krumbhaar and K. Binder, J. Stat. Phys. 8, 1 (1973). 406 [15] C. J. Geyer and E. A. Thompson, J. Royal Stat. Soc. B 54, 657
[8] W. C. Swope, H. C. Andersen, P. H. Berens, and K. R. Wilson, J. 407
(1992).
Chem. Phys. 76, 637 (1982).
[9] W. Janke, in Quantum Simulations of Complex Many-Body Systems: From Theory to Algorithms, edited by J. Grotendorst, D.

