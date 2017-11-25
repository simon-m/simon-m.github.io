# Cohort trials
Ref: [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture13.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture13.pdf)
- group patients by exposure (non-random)
- follow how the disease develops

Remarks: 
- propective cohort trials define groups now and follow them in the future
- retrospective cohort trials define groups from past data and observe the disease now
- cohort trials allow the computation of both relative risk and odd ratios


# Case-control trials
Ref: [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture14.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture14.pdf)
- group patients by disease (non-random)
- check past exposures


# Cohort versus case-control
Ref: [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture16.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture16.pdf)
Remark: Case-control trials only allow the computation of odd ratios (no relative risk),
because groups are defined by finding people with the disease (acse) and getting a similar 
number of people without disease (control). Therefore, the numbers in an adjacency table 
do not give any information about the number of patients sampled to build the case and control 
groups. Thus we do not know the total number of exposed and non-exposed patients needed to 
compute the relative risk. 
In other words, we need to know the prevalence (or incidence) which is only known for cohort trials since 
it is not used for making the groups a sopposed to case-control trials.

**Calculations below are wrong**
More precisely, let D be the event "get the disease" and E be the event "exposed" and
consider the follwing adjacency table:

|     |  D  |  ~D  |
|-----|-----|------|
|  E  |  a  |   b  |
| ~E  |  c  |   d  |

In the case of a perfect knowledge, we have
- \\(a = P(D \\cap E)\\)
- \\(b = P(~D \\cap E)\\)
- \\(c = P(D \\cap ~E)\\)
- \\(d = P(~D \\cap ~E)\\)
and the relative risk is 
\\[\\frac{P(D | E)}{P(D | ~E} = \\frac{P(D \\cap E) / P(E)}{P(D \\cap ~E) / P(~E)}\\]
\\[= \\frac{a / (a + b)}{c / (c + d)} = \\frac{a (c + d)}{c (a + b)}\\]

For a cohort trial, we have
- \\(a = P(D | E)\\)
- \\(b = P(~D | E)\\)
- \\(c = P(D | ~E)\\)
- \\(d = P(~D | ~E)\\)

so the relative risk is simply 
\\[\\frac{P(D | E)}{P(D | ~E} = \\frac{a}{c}\\]

and 
\\[\\frac{a}{a + b} = \\frac{P(D | E)}{P(D | E) + P(~D | E)}\\]
\\[ = \\frac{P(D \\cap E)P(E)}{P(D \\cap E)P(E) + P(~D \\cap E)P(E)}\\]
\\[ = \\frac{P(D \\cap E)}{P(D \\cap E) + P(~D \\cap E)}\\]
\\[ = \\frac{P(D \\cap E)}{P(E)}\\]
which is the relative risk.

For a case-control trials however, we have 
- \\(a = P(E | D)\\)
- \\(b = P(E | ~D)\\)
- \\(c = P(~E | D)\\)
- \\(d = P(~E | ~D)\\)

and 
\\[\\frac{a}{a + b} = \\frac{P(E | D)}{P(E | D) + P(E | ~D)}\\]
\\[ = \\frac{P(E \\cap D)P(D)}{P(E \\cap D)P(D) + P(E \\cap ~D)P(~D)}\\]
which is not a relative risk.


# Cross-sectional trials:
Ref: [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture15.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture15.pdf)
- record exposure and disease at the same time

Remark: no causality can be infered.


# Randomized clinical trial:
Ref: [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture12.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture12.pdf)
- assign patients to groups randomly (possibly stratify with respect to some variables). Give treatment (exposure)
- follow disease

Remark: necessarily prospective.

# Randomzed versus non-randomized trials
Remark: non-randomized trials have a higher risk to include biases. 
For instance, coffee drinkers (exposure) may be more likely to develop lung cancer (disease)
if coffee drinkers are often heavy smokers.


# References
- [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture13.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture13.pdf)
- [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture14.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture14.pdf)
- [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture16.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture16.pdf)
- [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture15.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture15.pdf)
- [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture12.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture12.pdf)



