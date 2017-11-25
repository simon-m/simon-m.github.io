Title: Maximum likelihood estimation
Date: 2017-11-25 18:50
Modified: 2017-11-25 18:50
Category: Statistics
Tags: Statistics, Maximum likelihood
Authors: Simon-M
Summary: Some notes about maximum likelihood estimation


Beside [epidemiology](epidemiology-cheat-sheet.html), I am also studying some statistics.
Below you can find my notes on far on maximum likelihood estimation (MLE).

Let \\(X = (X_1, \\dots, X_n)\\) be a vector of iid random variables following a
distribution \\(D_{\\theta_0}\\) parametrized by the vector \\(\\theta_0\\).
In the continuous case, let \\(f_{\\theta_0}\\) be the probability density function (PDF) of \\(D_{\\theta_0}\\).
In the discrete case, let \\(P_{\\theta_0}\\) be the probability mass function (PMF) of \\(D_{\\theta_0}\\)
Let \\(x = (x_1, \\dots, x_n)\\) be a realization of \\(X\\), i.e. the *observed data*.

Then, the maximum likelihood estimator (MLE) \\(\\hat{\\theta}\\) of \\(\\theta_0\\) is computed as follows.

First compute the likelihood \\(\mathcal{L}(\\theta) = P(X; \\theta)\\).
If \\(F_{\\theta}\\) is continuous, then
\\[\mathcal{L}(\\theta) = \\prod\{i=1}^{n} f_{\\theta}(x_i)\\]
If \\(F_{\\theta}\\) is discrete, then
\\[\mathcal{L}(\\theta) = \\prod\{i=1}^{n} P_{\\theta}(x_i)\\]

**NB**: the iid assumtion is crucial as it allows the total probability to be equal to the product
of individual probabilities.

The log-likelihood \\(\mathcal{l}(\\theta)\\) is simply the logarithm of \\(\mathcal{L}(\\theta)\\).
Since \\(\\log\\) is a strictly increasing function, the value maximizing \\(\mathcal{l}(\\theta)\\) is the
same as that maximizing \\(\mathcal{L}(\\theta)\\). The log-likelihood has the added benefit that it
allows to get rid of the product which will prove useful for the next calculations.

In order to maximize the likelihood, we first need to compute its derivative which respect to the
parameter of interest (namely \\(\\theta\\)), set the derivative to 0 and solve for \\(\\theta\\):
\\[u(\\theta) = \\frac{\\partial \mathcal{l}(\\theta)}{\\partial \\theta} = 0\\]
This derivative is sometimes called *score function* or "Fisher's score function".

The score is a random vector whose expectation at the true parameter value \\(E_{\\theta}[u(\\theta)_0]\\)
is equal to 0.

The score variance also called *information matrix* of "Fisher information matrix" is the positive
semidefinite symmetric matrix:
\\[\\mathcal{I}(\\theta) = var(u(\\theta)) =
   E_{\\theta} \\left[ \\left( \\frac{\\partial \mathcal{l}(\\theta)}{\\partial \\theta} \\right)^2 \\right] \\]
which under mild regularity conditions can be written
\\[\\mathcal{I}(\\theta) =
   -E_{\\theta} \\left[ \\frac{\\partial^2 \mathcal{l}(\\theta)}{\\partial \\theta\\theta^T} \\right] \\]


Asymptotically we have: \\( E[\\hat{\\theta}] = \\theta_0\\) and
\\( \\sigma^2(\\hat{\\theta}) = \\mathcal{I}(\\theta_0)^{-1})\\)
Therefore, \\(\\hat{\\theta}\\) is an unbiased estimator for \\(\\theta_0)\\).

<!--
The Cramér-Rao bound gives us a lower bound on the variance of \\(\\hat{\\theta}\\):
\\[var(\\hat{\\theta}) \\ge 1 / \\mathcal{I}(\\theta)\\]
-->

**Remark**: The second order derivative of the log-likelihood is a measure of its curvature, i.e. how "sharply peaked" it is.

# References

- [https://en.wikipedia.org/wiki/Maximum_likelihood_estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)
- [https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93Rao_bound](https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93Rao_bound)
- [https://en.wikipedia.org/wiki/Fisher_information](https://en.wikipedia.org/wiki/Fisher_information)
- [https://en.wikipedia.org/wiki/Likelihood_function](https://en.wikipedia.org/wiki/Likelihood_function)
- [https://stats.stackexchange.com/questions/68080/basic-question-about-fisher-information-matrix-and-relationship-to-hessian-and-s](https://stats.stackexchange.com/questions/68080/basic-question-about-fisher-information-matrix-and-relationship-to-hessian-and-s)
