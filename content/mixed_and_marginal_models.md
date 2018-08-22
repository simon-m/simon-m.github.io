Title: Taking random effects into account: mixed-(effect) models and marginal models.
Date: 2017-10-31 21:30
Modified: 2017-11-25 18:59
Category: Statistics
Tags: Statistics, Mixed models,Generalized estimating equations, Marginal models, Conditional models, Random effects
Authors: Simon-M
Summary: A review of fixed and random effects, linear mixed models and GEE

# Context
I am going to get my hands on some data with correlated measurements and thus have been reading
about to handle these. Among existing methods are various kinds of [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance)
(two-way ANOVA, repeated-measures ANOVA, clustered ANOVA, nested / hierarchical ANOVA,
split-plot ANOVA), [mixed-(effects) models](https://en.wikipedia.org/wiki/Mixed_model)
and [generalized estimating equations](https://en.wikipedia.org/wiki/Generalized_estimating_equation)
also called marginal models.

As of now, mixed models and marginal models are pretty much the standard tools for such analyses,
mainly because ANOVA-based methods require stronger assumptions and do not handle missing data well.
I will almost exclusively focus on *linear* models but be aware that there exist generalized linear mixed
models (GLMM) which are the "mixed-model version" of generalized linear models (GLM). Similarly, generalized
estimating equations are an extension of GLM for correlated responses, and as such they can handle the same
kind of dependencies between covariates and responses through the link function.

# Linear fixed-effects models
The response variable \\(Y_i\\) of observation \\(i\\) is a random variable which linearly depends
on the covariates \\(x_{ij}\\) through coefficients \\(\\beta_j\\) up to an random error term \\(\\epsilon_i\\):
\\[ Y_i = \\beta_1 x_{i1} + \\dots + \\beta_p x_{ip} + \\epsilon_i = \\sum_{j=1}^{p} \\beta_j x_{ij} + \\epsilon_i\\]
Equivalently letting \\(\\mathbf{\\beta} = (\\beta_1, \\dots \\beta_p)\\) and  
\\(\\mathbf{x_i} = (x_{i1}, \\dots x_{ip})^T\\) we have:
\\[ Y_i = \\mathbf{\\beta} \\mathbf{x_i} + \\epsilon_i \\]

The assumptions of the model are that

- \\(E[\\epsilon_i] = 0\\)
- \\(Var[\\epsilon_i] = \\sigma_i^2\\),
- \\(cov[\\epsilon] = \\Sigma\\).

Most often, \\(\\epsilon\\) is assumed to follow a multivariate Gaussian centered at 0:
 \\(\\epsilon \\sim \\mathcal{N}(0, \\Sigma)\\).

Let \\(\\mathbf{Y}\\) be the \\(n \\times 1\\) vector of responses,
\\(\\mathbf{X}\\) be the \\(n \\times p\\) *design matrix*, and \\(\\mathbf{\\epsilon}\\)
be the \\(n \\times 1\\) vector of random errors. In the more compact matrix notation, we have:
\\[ \\mathbf{Y} = \\mathbf{\\beta} \\mathbf{X} + \\mathbf{\\epsilon} \\]

In the fixed-effects model, \\(\\mathbf{X}\\) is assumed to be fixed, and does not contribute to
the variance of \\(\\mathbf{Y}\\):
\\[Y \\sim \\mathcal{N}(\\mathbf{\\beta} \\mathbf{X}, \\Sigma)\\]

# Fixed versus random effects: an example
In the course of an analysis, one may want to include a specific categorical covariate
in the model as a *dummy variable*; for instance whether a given patient has diabetes.
In that case, this covariate is relevant to the analysis and not expected to change
should the experiment be carried-out again.

One may also want to control for the center (A or B) in which the measurements were made (as in a
multi-center study) since it could have an impact on the measurements. However, the effect of the center on the
response is not of primary interest, but should merely be taken into account as a source of heterogeneity
(it is a *nuisance* variable). Moreover, the distribution of patients among centers could well change in
another study as a result of *e.g.* sampling.

In the first case there are two groups (diabetes / no diabetes) whose effect on the response is
expected to be accurately quantified by the corresponding dummy variable. In the second case,
there are two groups whose effect on the response can only be estimated given the current data
because another study using other groups will result in different effects.

The first case is typical of a *fixed effect* whereas the second is typical of a *random effect*.
Most models including random effects also include fixed effects and can be called *random effect models*,
*mixed models*, *conditional models* \\(\dots\\)

Note that in a more general setting, random effects can be either categorical or continuous.


# Linear mixed effects models (LMM):
Linar mixed models include both fixed and random effects which are described separately.
For observation \\(j\\) belonging to group \\(i\\), we have:
\\[ Y_{ij} = \\beta_1 x_{ij1} + \\dots + \\beta_p x_{ijp} + U_{i1} Z_{ij1}  + \\dots + U_{iq} Z_{ijq} + \\epsilon_{ij}
= \\sum_{k=1}^{p} \\beta_j x_{ijk} + \\sum_{l=1}^{q} U_{il} Z_{ijl} + \\epsilon_{ij}\\]

As for the fixed effects model above, given and \\(\\mathbf{U_i} = (U_{i1}, \\dots, U_{iq})\\) and
\\(\\mathbf{Z_{ij]} = (Z_{ij1}, \\dots, Z_{1jq})^T\\), we can write this as:
\\[ Y_{ij} = \\mathbf{\\beta} \\mathbf{x_{ij}} + \\mathbf{U_i} \\mathbf{Z_{ij}} + \\epsilon_{ij}\\]

Note that this is essentially the fixed-effects models to which were added with the random effects
\\(\\mathbf{Z_{ij}}\\) and the corresponding group-specific coefficients \\(\mathbf{U_i}\\).

The equations above assume that all groups have random effects of the
same dimension \\(q\\). This is not mandatory and it is possible to have
and \\(\\mathbf{U_i} = (U_{i1}, \\dots, U_{iq_i})\\) and
\\(\\mathbf{Z_{ij}} = (Z_{ij1}, \\dots, Z_{ijq_i})^T\\)

Let \\(n_i\\) be the number of observations in group \\(i\\) and \\(\\mathbf{Z_i}\\) be the
\\(n_i \\times q_i\\) design matrix for random effects.
The other terms are similar to those in the fixed-effects model but restricted to group \\(i\\).
Namely \\(\\mathbf{x_i}\\) is of dimension \\(n_i \\times p\\), and \\(\\mathbf{\\epsilon_i}\\)
is of dimension \\(n_i \\times 1\\).
Then a mixed model takes the following form for group \\(i\\):
\\[ \\mathbf{Y_i} = \\mathbf{\\beta} \\mathbf{x_i} + \\mathbf{U_i} \\mathbf{Z_i} + \\mathbf{\\epsilon_i}\\]

Finally, letting \\(n = \\sum_{i} n_i\\) and \\(q = \\sum_{i} q_i\\) we have the full matrix form:
\\[ \\mathbf{Y} = \\mathbf{\\beta} \\mathbf{x} + \\mathbf{U} \\mathbf{Z} + \\mathbf{\\epsilon}\\]
with \\(\\mathbf{Z}\\) of dimension \\(n \\times q\\) and  \\(\\mathbf{U}\\) of dimension \\(q \\times 1\\).

## Variance components
As opposed to the fixed effects model, in this setting \\(mathbf{\\epsilon}\\) is no longer the only contributor to
the variance of \\(\\mathbf{Y}\\).
Specifically, we have \\(U \\sim \\mathcal{N}(0, R)\\), \\(R\\) being the random effects covariance matrix, and
\\(\\epsilon\\) and \\(U\\) are assumed to be independent, i.e. \\(cov[U, \\epsilon] = 0_{q \\times n}\\).

Therefore, we have
\\(\\mathbf{Y|U} \\sim \\mathcal{N}(\\mathbf{X}\\mathbf{\\beta} + \\mathbf{Z}\\mathbf{U}, \\Sigma\\))
and
\\(\\mathbf{Y} \\sim \\mathcal{N}(\\mathbf{X}\\mathbf{\\beta}, ZRZ^T + \\Sigma) =
\\mathcal{N}(\\mathbf{X}\\mathbf{\\beta}, V)\\).
The matrix \\(V\\) is called the *variance-covariance matrix*.


# Model fitting / parameter estimation
For a mixed model, the unknown quantities \\(\\mathbf{\\beta}\\), \\(\\mathbf{U}\\), \\(\\Sigma\\) and \\(R\\)
must be estimated.
More specifically, \\(\\mathbf{\\beta}\\), \\(\\Sigma\\) and \\(R\\) are fixed and can be directly
estimated from the data. The situation is rather different for \\(\\mathbf{U}\\) which is a matrix of
random variables and must be *predicted*.

In the following, we will first assume that the covariance matrices are known in order to estimate
\\(\\mathbf{\\beta}\\) and \\(\\mathbf{U}\\)
This is almost never the case but makes the explanation simpler. In practice the covariance matrices
and the remaining parameters are estimated jointly.
Parameter estimation is usually performed using either
[maximum likelihood](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation) (ML)
or [residual/restricted maximum likelihood](https://en.wikipedia.org/wiki/Restricted_maximum_likelihood)
(RML / REML).

## Random and fixed effects estimation
Let us start by assuming that the variance-covariance matrix \\(V = ZRZ^T + \\Sigma\\) is known,
implying that  \\(R\\) and
\\(\\Sigma\\) are known too, and try to estimate \\(\\mathbf{\\beta}\\) and \\(\\mathbf{U}\\).
One to do this way is to solve Henderson's equations also called *mixed model equations* which have
the following solutions:
\\[ \\mathbf{\\hat{\\beta}} = (\\mathbf{X}^T V^{-1} \\mathbf{X})^{-1} X^T V^{-1} \\mathbf{Y}\\]
\\[ \\mathbf{\\tilde{U}} = R Z^T V^{-1}(\\mathbf{Y} - \\mathbf{X}\\mathbf{\\hat{\\beta}})\\]

Note that \\(\\mathbf{\\hat{\\beta}}\\) is a essentially a least squares estimate
(recall the usual estimate \\((X^T X)^{-1}X^T Y\\)) weighted by the inverse of the variance-covariance
matrix. It is also called *generalized least squares estimate* and is unbiased:
\\(E[\\mathbf{\\hat{\\beta}}] = \\mathbf{\\beta}\\).

The estimate \\(\\mathbf{\\tilde{U}}\\) is the best linear unbiased predictor (BLUP) of
\\(\\mathbf{U}\\) and as such, we have \\(E[\\mathbf{\\tilde{U}}] = \\mathbf{U}\\).
Here *best* refers to the fact that it is the most *efficient*, i.e. has the lowest variance among
unbiased predictors. Note how it depends on the residuals \\(\\mathbf{Y} - \\mathbf{X}\\mathbf{\\hat{\\beta}}\\)
of the "fixed effect model".

## Variance parameter estimation
For the previous estimations to be computed, one needs to first estimate \\(V\\) and
thus \\(R\\) and \\(\\Sigma\\). "First" here is misleading however as the estimation of
effects and variance parameters are usually done jointly.

The experimental design can sometimes give some information about the structure of these matrices which
can be specified prior to estimation.
For instance knowing that the random effects are independent from each other, one may enforce a
diagonal structure for \\(R\\).
Similarly for the random errors \\(\\Sigma\\), one may, for instance, assume that all observations are
equally correlated (compound symmetry) or that their correlations get weaker with their distance
in the dataset (e.g. autoregressive structure for longitudinal data where obervations are sorted
by time). Virtually any correlation structure can be specified but only the most commonly used are
supported by statistical softwares, which is usually enough for most type of analysis.


## Variance parameter estimation with maximum likelihood
Let \\(\\theta\\) be the vector containing unknown parameters in \\(R\\) and \\(\\Sigma\\). Their number
depends on the correlation structure specified: more constraints lead to less parameters to estimate.
To derivate the likelihood of the model, recall that
\\(\\mathbf{Y} \\sim \\mathcal{N}(\\mathbf{X}\\mathbf{\\beta}, V(\\theta))\\). Thus the log-likelihood
\\(l(\\mathbf{Y}; \\mathbf{\\beta}, V(\\theta))\\) of \\(\\mathbf{Y}\\) satisfies:
\\[-2 l(\\mathbf{Y}; \\mathbf{\\beta}, V(\\theta)) = \\log |V(\\theta)| +
    (\\mathbf{Y} - \\mathbf{X}\\mathbf{\\beta})^T V(\\theta)^{-1}(\\mathbf{Y} - \\mathbf{X}\\mathbf{\\beta}) + n \\log 2 \\pi\\]

Minimizing this log-likelihood can be done by replacing \\(\\mathbf{\\beta}\\) by its maximum
likelihood estimator given the current parameter vector \\(\\theta\\):  
\\(\\mathbf{\\hat{\\beta}}(\\theta) = (\\mathbf{X}^T V(\\theta)^{-1} \\mathbf{X})^{-1} X^T V(\\theta)^{-1} \\mathbf{Y}\\).

One can start with random intial parameters \\(\\theta\\) and minimize
\\(l(\\mathbf{Y}; \\mathbf{\\hat{\\beta}}(\\theta), V(\\theta))\\).
Alternating the estimation of \\(\\theta\\) and \\(\\mathbf{\\beta}(\\theta)\\) until convergence yield the
final parameter values.

The main caveat of the ML estimation is that the variance estimates are negatively biased
as they do not take into account the degrees of freedom lost while estimating the fixed effects.
Indeed, as it depends on \\(\\theta\\), mathbf{\\beta}\\) is estimated alongside
\\(V(\\theta)\\), and this is not taken into account in the number of degrees of freedom: \\(n\\) should be
replaced by a smaller value.

## Variance parameter estimation with restricted maximum likelihood
Restricted maximum likelihood estimation addresses the biasedness of MLE estimators.
The core idea is to perform MLE on a modified version of the data, namely using a
linear combinations of \\(\\mathbf{Y}\\).

First, notice that the design matrix \\(\\mathbf{X}\\) has rank at most \\(p\\) since it is a \\( n \\times p\\)
matrix.
Let \\(r = rank(\\mathbf{X})\\) and \\(K\\) be the full rank \\((n - r) \\times n\\) matrix satisfying
\\(E[K\\mathbf{Y}] = 0 \\iff E(K\\mathbf{X}\\mathbf{\\beta}) = 0\\).
Thus, \\(K\\mathbf{Y} \\sim \\mathcal{N}(0, K V(\\theta) K^T)\\) and maximum likelihood
estimation can be carried out on \\(K\\mathbf{Y}\\) with \\((n - r)\\) degrees of freedom.
Moreover, notice that as opposed to \\(\\mathbf{Y} (distributed according to \\mathcal{N}(\\mathbf{X}\\mathbf{\\beta}, V)\\),
\\(\\mathbf{\\beta}\\) no longer appear in the distribution of \\(K\\mathbf{Y}\\), meaning that the
dependence on fixed effects has been removed.

More concretely, the transformed response \\(K\\mathbf{Y}\\) consists of the residuals obtained after
fitting the fixed effects while ignoring the variance parameters.
This is related to the formulation in terms of marginal likelihood: the marginal likelihood
\\(L_R(\\mathbf{Y}; V(\\theta))\\) with respect to \\(\\mathbf{Y}\\) is found by integrating out the fixed
effects:
\\(L_R(\\mathbf{Y}; V(\\theta)) = \\int L(\\mathbf{Y}; \\mathbf{\\beta}, V(\\theta)) d \\mathbf{\\beta}\\).
The log of the marginal likelihood is then maximized.

In contrast with ML, the REML estimates for fixed effect are *biased* and those for random effect
are *unbiased*.

Remark:

In practice, ML and REML are typically computed using iterative schemes such as the [Newton-Raphson](https://en.wikipedia.org/wiki/Newton%27s_method)
optimization algorithm and variants thereof, or the [expectation-maximization](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm)
algorithm.


# Marginal models and Generalized estimating equations
As an alternative to LMM, generalized estimating equations (GEE) are often used for modeling correlated
data. In that context they commonly appear under the name *marginal models*. Marginal models are actually
a subset of the more general GEE, population-average GEE (PA-GEE), as opposed to subject-specific
GEE (SS-GEE).

## GEE are an extension of generalized linear models (GLM).
Let us forget about random effects for a moment.
The difference between fixed-effects linear models and generalized linear models (GLM) is that for the latter,
the response variable is no longer restricted to be normally distributed. Instead, it can follow any distribution from the
[exponential family](https://en.wikipedia.org/wiki/Exponential_family).
Moreover, a *link* function \\(g\\) describes how the expectation \\(\\mu_i\\) of \\(Y_i\\) depends
on a linear combination of covariates.
This results in a model of the following form:
\\[ g(E[Y_i]) = \\beta_1 x_{i1} + \\dots + \\beta_p x_{ip}= \\mathbf{x_i} \\mathbf{\\beta}\\]
or in compact form:
\\[ g(E[Y]) = \\mathbf{X}\\mathbf{\\beta} \\]

Linear regression consists of a normally distributed \\(Y\\) with a identity
link function, and logistic regression consists of a binomially distributed \\(Y\\) with a logit
\\((x \\mapsto \\ log \\frac{x}{1-x}) \\) link function.

GEE extend GLM by allowing correlated \\(Y_i\\). The covariance structure can be specified as for
mixed models. However, note that the covariance is no longer between random effects or random errors
but between responses.
As such, the formulation of GEE does not explicitely include random effects.
In the linear case (\\(g\\) is the identify function), the model is therefore:
\\[ Y_i = \\beta_1 x_{i1} + \\dots + \\beta_p x_{ip} + \\epsilon_i = \\mathbf{x_i} \\mathbf{\\beta} + \\epsilon_i \\]
or in compact form
\\[ Y = \\mathbf{\\beta} \\mathbf{X} + \\epsilon \\]
where \\(\\epsilon \\sim \\mathcal{N}(0, \\Sigma)\\).
In that case, there is no \\(R\\) matrix and  \\(V = \\Sigma\\) is the variance-covariance matrix of
the model.


## Parameter estimation
The parameter estimation of marginal models relies on *quasi-likelihood* instead of the
(restricted)-likelihood for LMM. It does not require the full distribution of \\(Y\\) to be known
but only its mean and covariance matrix.
In practice, this amounts to solving the following *quasi-likelihood estimating equation*
(see [here](https://onlinecourses.science.psu.edu/stat504/node/182) and
[here](https://en.wikipedia.org/wiki/Generalized_estimating_equation)):
\\[X^T V^{-1}(Y - \\mathbf{X} \\mathbf{\\beta)} = 0\\]

However, note that the covariance matrix \\(V\\) is unknown at this point, thus it is replaced by
an estimate \\(\\tilde{V}\\) which depends on \\(\\beta\\) and initially assumes independence
(\\(\\tilde{V}\\) is diagonal).
The quasi-likelihood estimating equation is then solved iteratively, alternating between the
estimation of \\(\\mathbf{\\beta}\\) with fixed \\(\\tilde{V}\\) and of \\(\\tilde{V}\\) with fixed
\\(\\mathbf{\\beta}\\).

A very rough description of the algorithm is therefore:

1. Fit an intial fixed effect model without taking into account any covariance
  (assume independence, diagonal \\(V^0\\)), yielding \\(\\beta^0\\)

2. At step \\(i\\), update the covariance matrix \\(V^i\\) using the current
   estimates \\(\\beta^{i-1}\\).

3. Update \\(\\beta^i\\) from the covariance matrix \\(V^i\\).

4. Iterate 2. and 3. until convergence.

I will not go into more details, but good explanations can be found
[here](http://support.sas.com/documentation/cdl/en/statug/67523/HTML/default/viewer.htm#statug_gee_details01.htm),
[here](http://support.sas.com/documentation/cdl/en/statug/67523/HTML/default/viewer.htm#statug_gee_details06.htm) and
[here](https://www.ibm.com/support/knowledgecenter/de/SSLVMB_20.0.0/com.ibm.spss.statistics.help/alg_genlin_gee_estimation_param.htm).

Since
The estimation of the variance of \\(\\beta\\) uses the so-called *robust sandwich estimator*
(some nice and short explanations in the context of OLS regression
[here](http://thestatsgeek.com/2013/10/12/the-robust-sandwich-variance-estimator-for-linear-regression/)
and [here](https://stats.stackexchange.com/questions/50778/sandwich-estimator-intuition)).


# Mixed-effect models versus marginal models
For linear models, mixed and marginal models yield the same estimates.
This is however not true in the general case.

## Interpretation
Mixed-models aim at estimating group-specific coefficients i.e. they condition on both the design matrix and
random effects:
\\[E[Y | \\mathbf{U}] = \\mathbf{X} \\mathbf{\\beta} + \\mathbf{Z} \\mathbf{U}\\]
In other words, they describe how the response of individual groups changes with
the covariates. The random effects allow the covariate coefficients to vary randomly from one group
to another, thereby providing a group-specific response. For this reason they are sometimes called
*conditional models* as opposed to marginal models.

On the other hand, marginal models aim at estimating population average coefficients.
Indeed, as their name suggests, they focuses on marginals, i.e. take averages over random effects,
only conditioning on the design matrix:
\\[E[Y] = \\mathbf{X} \\mathbf{\\beta} \\]
In other words, marginal models focus on the impact of covariates on the response over the whole population.

In terms of interpretation of the coefficients, a very clear example is provided
[here](https://stats.stackexchange.com/questions/86309/marginal-model-versus-random-effects-model-how-to-choose-between-them-an-advi):

"*If you are a doctor and you want an estimate of how much a statin drug will lower your
patient’s odds of getting a heart attack, the subject-specific coefficient
is the clear choice. On the other hand, if you are a state health official and you want to
know how the number of people who die of heart attacks would change if everyone in the at-risk population
took the stain drug, you would probably want to use the population–averaged coefficients. (Allison, 2009)*"

Where "subject-specific" refers to the mixed effect / conditional model whereas "population-averaged" refers
to the GEE / marginal model.


## Assumptions and robustness

As opposed to LMM, marginal models do not rely on the assumption that random effects are
normally distributed.

Marginal models are more robust than LMM when the covariance structure is misspecified, a nice
feature of the sandwich estimator.

Marginal models can only handle data missing completely at random (MCAR, "really random") wheread LMM
can also handle data missing at random (MAR, randomness which depends on covariates).

Choosing between mixed models and marginal models is therefore primarily a question of scope (group-specific
versus population-wise) and also depend on what is known about the data (how certain are we about the correlation
structure? about the complete randomness of missing data?).


# References:

- Campbell, Michael J. Statistics at square two: understanding modern statistical applications in medicine. BMJ, 2001
- Duchateau, Luc, Paul Janssen, and John Rowlands. Linear mixed models. An introduction with applications in veterinary research. ILRI (aka ILCA and ILRAD), 1998
- Burton, Paul, Lyle Gurrin, and Peter Sly. "Extending the simple linear regression model to account for correlated responses: an introduction to generalized estimating equations and multilevel mixed modelling." (2004): 1-33
- Hardin, James W. Generalized estimating equations (GEE). John Wiley & Sons, Ltd, 2005
- Naseri, Parisa, et al. "Comparison of generalized estimating equations (GEE), mixed effects models (MEM) and repeated measures ANOVA in analysis of menorrhagia data." Journal of Paramedical Sciences 7.1 (2016): 32-40
#
- [http://statistics.ma.tum.de/fileadmin/w00bdb/www/czado/lec10.pdf](http://statistics.ma.tum.de/fileadmin/w00bdb/www/czado/lec10.pdf)
- [http://people.musc.edu/simhille/Presentations/GEE_tutorial_Betsy/GEE_Tutorial.pdf](http://people.musc.edu/simhille/Presentations/GEE_tutorial_Betsy/GEE_Tutorial.pdf)
- [http://www.misug.org/uploads/8/1/9/1/8191072/kwelch_repeated_measures.pdf](http://www.misug.org/uploads/8/1/9/1/8191072/kwelch_repeated_measures.pdf)
- [http://statmath.wu.ac.at/courses/heather_turner/glmCourse_001.pdf](http://statmath.wu.ac.at/courses/heather_turner/glmCourse_001.pdf)
- [http://www.stat.cmu.edu/~hseltman/309/Book/chapter15.pdf](http://www.stat.cmu.edu/~hseltman/309/Book/chapter15.pdf)
- [http://www.stat.ncsu.edu/people/bloomfield/courses/ST732/02-21.pdf](http://www.stat.ncsu.edu/people/bloomfield/courses/ST732/02-21.pdf)
- [http://www.stat.ncsu.edu/people/bloomfield/courses/ST732/03-23.pdf](http://www.stat.ncsu.edu/people/bloomfield/courses/ST732/03-23.pdf)
- [http://www.stat.ncsu.edu/people/bloomfield/courses/ST732/04-06.pdf](http://www.stat.ncsu.edu/people/bloomfield/courses/ST732/04-06.pdf)
- [http://www.stat.ncsu.edu/people/bloomfield/courses/ST732/04-18.pdf}](http://www.stat.ncsu.edu/people/bloomfield/courses/ST732/04-18.pdf)
#
- [https://onlinecourses.science.psu.edu/stat504/node/180](https://onlinecourses.science.psu.edu/stat504/node/180)
- [https://support.sas.com/documentation/cdl/en/statug/67523/HTML/default/viewer.htm#statug_genmod_details29.htm](https://support.sas.com/documentation/cdl/en/statug/67523/HTML/default/viewer.htm#statug_genmod_details29.htm)
- [http://support.sas.com/documentation/cdl/en/statug/67523/HTML/default/viewer.htm#statug_gee_details01.htm](http://support.sas.com/documentation/cdl/en/statug/67523/HTML/default/viewer.htm#statug_gee_details01.htm)
- [http://support.sas.com/documentation/cdl/en/statug/67523/HTML/default/viewer.htm#statug_gee_details06.htm](http://support.sas.com/documentation/cdl/en/statug/67523/HTML/default/viewer.htm#statug_gee_details06.htm)
- [https://www.ibm.com/support/knowledgecenter/de/SSLVMB_20.0.0/com.ibm.spss.statistics.help/alg_genlin_gee_estimation_param.htm](https://www.ibm.com/support/knowledgecenter/de/SSLVMB_20.0.0/com.ibm.spss.statistics.help/alg_genlin_gee_estimation_param.htm)
- [https://en.wikipedia.org/wiki/Generalized_estimating_equation](https://en.wikipedia.org/wiki/Generalized_estimating_equation)
- [https://en.wikipedia.org/wiki/Generalized_linear_model](https://en.wikipedia.org/wiki/Generalized_linear_model)
#
- [http://thestatsgeek.com/2013/10/12/the-robust-sandwich-variance-estimator-for-linear-regression/](http://thestatsgeek.com/2013/10/12/the-robust-sandwich-variance-estimator-for-linear-regression/)
#
- [https://stats.stackexchange.com/questions/17331/what-is-the-difference-between-generalized-estimating-equations-and-glmm](https://stats.stackexchange.com/questions/17331/what-is-the-difference-between-generalized-estimating-equations-and-glmm)
- [https://stats.stackexchange.com/questions/48671/what-is-restricted-maximum-likelihood-and-when-should-it-be-used](https://stats.stackexchange.com/questions/48671/what-is-restricted-maximum-likelihood-and-when-should-it-be-used)
- [https://stats.stackexchange.com/questions/21760/what-is-a-difference-between-random-effects-fixed-effects-and-marginal-model/68753#68753](https://stats.stackexchange.com/questions/21760/what-is-a-difference-between-random-effects-fixed-effects-and-marginal-model/68753#68753)
- [https://stats.stackexchange.com/questions/86309/marginal-model-versus-random-effects-model-how-to-choose-between-them-an-advi](https://stats.stackexchange.com/questions/86309/marginal-model-versus-random-effects-model-how-to-choose-between-them-an-advi)
- [https://stats.stackexchange.com/questions/62923/models-for-generalized-estimating-equation](https://stats.stackexchange.com/questions/62923/models-for-generalized-estimating-equation)
- [https://stats.stackexchange.com/questions/62939/gee-quasi-likelihood-and-what-it-generalizes](https://stats.stackexchange.com/questions/62939/gee-quasi-likelihood-and-what-it-generalizes)
- [https://stats.stackexchange.com/questions/50778/sandwich-estimator-intuition](https://stats.stackexchange.com/questions/50778/sandwich-estimator-intuition)
- [https://www.reddit.com/r/statistics/comments/16k9z6/can_anyone_help_me_understand_when_to_use/](https://www.reddit.com/r/statistics/comments/16k9z6/can_anyone_help_me_understand_when_to_use/)
