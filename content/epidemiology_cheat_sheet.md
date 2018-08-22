Title: Epidemiology cheat sheet
Date: 2017-11-25 18:47
Modified: 2017-11-25 18:47
Category: Epidemiology
Tags: Epidemiology, Incidence, Prevalence, Random trial, Risk, Cohort, Cross-sectional, Case-control
Authors: Simon-M
Summary: The very basics of epidemiology: populations, various measures, types of studies

I am currently learning about epidemiology so here is a short summary of the essential concepts of the field.
Most of what you will find below is a summary of the excellent lecture slides of the
[Fundamentals of Epidemiology](http://ocw.jhsph.edu/index.cfm/go/viewCourse/course/fundepiii/coursePage/lectureNotes/)
and
[Fundamentals of Epidemiology II](http://ocw.jhsph.edu/index.cfm/go/viewCourse/course/FundEpi/coursePage/lectureNotes/)
courses from the [Johns Hopkins Bloomberg School of Public Health](https://www.jhsph.edu/) so most credits go to them.


# Summary measures
Sources:

- [This lecture](http://ocw.jhsph.edu/courses/FundEpi/PDFs/Lecture5.pdf)
- Rothman, Kenneth J., Sander Greenland, and Timothy L. Lash, eds. Modern epidemiology Chapter 3. Lippincott Williams & Wilkins, 2008.

## Ratio vs proportion vs rates vs odds vs odds ratio:
Variables \\(a\\) and \\(b\\) are absolute frequencies (counts).
Variable \\(p\\) and \\(q\\) are proportions.

- **Ratio**: \\(r = (a / b)\\)
- **Proportion**: ratio when \\(a\\) is counted whithin \\(b\\) (e.g. \\(b = a + c \\)), relative frequency
- **Rate**: ratio or proportion within a specified time period (must be the same period for the numerator and denominator)
- **Odds**: \\(o = p / (1 - p)\\)
- **Odds ratio**: \\(o_1 / o_2 = \\frac{p / (1 - p)}{q / (1 - q)} = \\frac{p (1 - q)}{q (1 - p)}\\)

## Person-time
The time period of a study is not always the measure of time of interest.
In general the *exposure time* (or exposed time, also person-time) is the amount of time
during which an event of interest could occur (e.g. the duration of a treatment which can be shorter than the
length of the study if a patient drops out.)
Over a population, the total person-time is the sum of individual person-times.

Its unit are *person-time*, for instance "patient-month", "child-year". Years being the most common.
As an exemple, following 5 people during 3 year leads to a 15 person-year of total exposure time.
If two patients dropped-out after 1 year, the resulting exposure time is \\(3 \\times 3 + 2 \\times 1 = 11\\)
person-year.
It is also called the total *time at risk* for the population of interest.

## Open and closed populations
**Closed population or cohort**: fixed number of individuals, except for loss to
follow-up or death (which must be corrected in subsequent analyses, see
[censoring](https://en.wikipedia.org/wiki/Censoring_(statistics))).

**Open population**: inflow and outflow are possible, the size of the population can vary.

**Stationary population**: open population with constant size (inflow compensates outflow).

## Incidence rate
Consider an *event* to be a new diagnosis for a pathology of interest. Then, the incidence rate
IR can then be computed as:
\\[ \text{IR} = \frac{ \\#\text{events}}{\sum_{s \in \text{subjects}} \text{person_time}(s)} \\]
\\[ = \frac{ \\#\text{events}}{\text{total_person_time}} \\]
For instance, following 100 people for one year and getting one case, one has
\\( \text{IR} = 1 / 100 = 0.01 \text{ year}^{-1} \\).
Following 40 people for 5 years and getting four cases, one has
\\( \text{IR} = 4 / 200 = 0.02 \text{ year}^{-1} \\)

Often, neither the patient exposure times (\\(\text{person_time}(s)\\)) or total exposure time
\\(\text{total_person_time}\\) are known. The denominator is therefore approximated by the mid-period population size \\(N_{1/2}\\) times the length of the time period \\(T\\):
\\[ = \frac{ \\#\text{events}}{N_{1/2} T} \\]

Defining the individual rate \\( \text{individual_rate}(s) \\) of a subject \\( s \\) as \\( 0 \\)
if no event occured and \\( 1 / \text{person_time}(s)\\) if it did, the IR can be defined as:
\\[ IR = \frac{\sum_{s \in \text{subjects}} \text{person_time}(s) \cdot \text{individual_rate}(s) }
{\sum_{s \in \text{subjects}} \text{person_time}(s)} \\]

This is the average of individual rate, weighted by person-time.
For the examples above, we get
\\( \text{IR} = 1 * (1 * 1 / 1) / 100 = 0.01 \text{ year}^{-1} \\) and
\\( IR = 4 * (5 * 1 / 5) / 200 = 0.02 \text{ year}^{-1} \\).

**Remark**: the IR depends on the time unit, which should be reported. It is not a proportion.

**Remark 2**: the IR can be computed for both open and closed (cohort) populations.
For open populations, the total person-time can be approximated by the average population size
multiplied by the study duration. This assumes that the in and out-flows are of similar
magnitude and independent of the "event" / "no event" state.


## Incidence proportion
Also called attack-rate (although it is not a rate).
In contrast to the incidence rate, the incidence proportion does not divide the number of new
cases by the total person-time but by the number of prople at risk at the beginning of the trial period:
\\[ \text{IP} = \frac{ \\#\text{events}}{\\#\text{people initially at risk}} \\]

**Remark**: incidence proportion can easily be confused with *period prevalence* (see below).
The numerator for the former is the number of *new cases* whereas for the latter, it is the number
of *diseased* people even if the onset took place before the period of study.

**Remark 2**: incidence proportion can only be computed for closed populations (cohorts).
Indeed, in an open population we do not know the number of people initially at risk.
Therefore a new case could either be a person a risk having experienced the event or a
person who already had experienced the event but flowed to the population under study later
on; and we cannot find out which is true.


## Prevalence proportion
Prevalence proportion is also called prevalence rate (although not a rate) or absolute risk.
As opposed to an *event* defined above, consider a *case* to be a patient with the pathology of interest
(i.e. whose event occured immediately or in the past).

As opposed to incidence, the prevalence is concerned with all cases, not only new ones.
Let \\(N_t\\) be the population size at time \\(t\\). The *point prevalence* at time \\(t\\) is then:
\\[ \\text{PR}\cdot = \\frac{ \\text{#cases}}{N_t} \\]
Here the number of cases refers to both cases with diagnosis in the past and during
period \\(T\\).

Let \\(N_T\\) be the average population size during for period \\(T\\), assuming it remains fixed.
The *period prevalence* period \\(T\\) is:
\\[ \\text{PR}_{[-]} = \\frac{ \\text{#cases with disease during T}}{N_T} \\]



## Incidence versus prevalence
Sources:

- [Lecture](http://ocw.jhsph.edu/courses/FundEpi/PDFs/Lecture6.pdf)
- [https://en.wikipedia.org/wiki/Incidence_(epidemiology)](https://en.wikipedia.org/wiki/Incidence_(epidemiology))
- [https://en.wikipedia.org/wiki/Prevalence#Period_prevalence](https://en.wikipedia.org/wiki/Prevalence#Period_prevalence)

Incidence is a *rate*, i.e. it gives information on the rate (~ speed) of occurrence of the event.
This can be seen as the denominator has a time dimension.

Prevalence, on the other hand is a proportion of people who experienced the event, whether it is
at a given time and including all past occurrences (point prevalence), or during a specified
time period where both new and past cases are recorded (period prevalence). The denominator does not
quantify time, only the population size.

For rare diseases (small incident rate) and a closed, or open *stationary* population, we have:
\\[ \text{PR}_{[-]} \\approx IR \\cdot \\text{average disease duration} \\]


# Measures of association
Used to quantify the association between a factor (e.g. higher education) and the occurence of a
condition (e.g. disease).

Let D be the event "get the disease" and E be the event "exposed". The negative operator is denoted by "~"". Consider the following adjacency table:

|                 |  \\(D\\)  |  \\( \\tilde D\\)  |
|-----------------|-----------|--------------------|
| \\(E\\)         |  \\(a\\)  |      \\(b\\)       |
| \\(\\tilde E\\) |  \\(c\\)  |      \\(d\\)       |

## Relative risk (RR)
Also called risk ratio.
If \\(P_1\\) is the prevalence of a pathology in a population *exposed* to some factor, and
\\(P_0\\) is the prevalence of the same pathology in a population not exposed to this factor, the relative risk is:
\\[ \\text{RR} = P_1 / P_0\\ = \\frac{a / (a + b)}{c / (c + d)} = \\frac{a (c + d)}{c (a + b)} \\]

In terms of probabilities we have:
\\[ \\text{RR} = \\frac{P(D | E)}{P(D | \\tilde E)}\\]


## Odds ratio (OR)
Odds of having the disease in the exposed group:
\\[O_1 = \\frac{a /(a + b)}{b / (a + b)} = \\frac{a}{b}\\]
In terms of probabilities:
\\[O_1 = \\frac{P(D | E)}{P(\\tilde D | E)}\\]

Odds of having the disease in the non-exposed group:
\\[O_0 = \\frac{c / (c + d)}{d / (c + d)} = \\frac{c}{d}\\]
In terms of probabilities:
\\[O_0 = \\frac{P(D| \\tilde E)}{P( \\tilde D|  \\tilde E)}\\]

Odds ratio:
\\[\\text{OR} = O_1 / O_0 = \\frac{ad}{bc}\\]
In terms of probabilities:
\\[\\text{OR} = \\frac{P(D | E)}{P( \\tilde D | E)} \\frac{P( \\tilde D | \\tilde E)}{P(D | \\tilde E)} \\]

## Odds ratio versus relative risk
Relative risk can only be calculated for cohort studies whereas odds ratio can be calculated for
both case-control and cohort studies (see section "Cohort versus case-control" below).

If the incidence of the disease is low, OR is a good approximation of RR since
\\(a + b \\approx b\\) and \\(c + d \\approx d\\). Thus,
\\[\\text{RR} = \\frac{a (c + d)}{c (a + b)} \\approx \\frac{ad}{bc} = \\text{OR}\\]


# Stratification and adjustment strategies
[Source](http://ocw.jhsph.edu/courses/FundEpi/PDFs/Lecture7.pdf)

Stata are basically groups among the data defined by a variable. It could be age groups, sex
or combinations thereof for instance.

When comparing rate or proportions between two populations, the overall measure may be confounded
by their difference in composition. For instance, a young population may be less likely to die of
an heart attack than an older one. This calls for *adjustments strategies*.

## Direct method
1. Compute the proportion or rate of interest for each stratum in both populations.
   For instance prevalence of heart pathology by age group.
2. Build a *reference population* by summing the sizes of both populations for each stratum.
3. For each group, use the proportion or rate of interest to compute the *expected* number of cases in
   the reference population for each stratum.
4. Compute the overall proportion or rate for each group from the corresponding expected number of cases
   instead of the original ones.

This methods requires to have access to the proportions or rates of interest for each stratum
of the populations. Sometime, we only have access to the number of cases. Then the indirect method
is of use.

## Indirect method
1. Build a *reference population* for the population under study. Both populations should be similar enough.
   The rate or proportion of interest (or estimates thereof) must be available for the reference population.
2. Using the stratum-specific rates or proportions from the reference population and the stratum sizes in the population
  under study, compute the *expected* number of cases in the the population under study.
3. Compute the ratio between the total expected and observed number of cases.


# Types of study
## Cohort trials
[Source](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture13.pdf)

- Group patients by exposure (non-random).
- Follow how the disease develops.

Remarks:

- Propective cohort trials define groups now and follow them in the future.
- Retrospective cohort trials define groups from past data and observe the disease now.
- Cohort trials allow the computation of both relative risk and odd ratios.


## Case-control trials
[Source](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture14.pdf)

- Group patients by disease (non-random).
- Check past exposures.


## Cohort versus case-control
[Source](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture16.pdf)

Case-control trials allow the computation of odd ratios but not of not of the relative risk.
The reason is that groups are defined by finding people with the disease (cases) and getting a
number of people without disease (controls). Therefore, the numbers in an adjacency table
do not give any information about the number of patients sampled to build the case and control
groups.

In particular, case-control trials are often conducted for rare diseases so that cases are
oversampled compared to controls: the prevalence is what the study design wants it to be.
Thus we do not know the total number of exposed and non-exposed patients needed to compute the relative risk.

In other words, we need to know the prevalence  which is only known for cohort trials since disease status is not used
for defining the groups as opposed to case-control trials.

## Cross-sectional trials:
[Source](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture15.pdf)

Record both exposure and disease at the same time.

**Remark**: no causality can be infered.


## Randomized clinical trial:
[Source](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture12.pdf)

- Assign patients to groups randomly (possibly stratify with respect to some variables).
- Administer the treatments to non-control groups (exposure).
- Follow how the disease develops.

**Remark**: necessarily prospective.

## Randomzed versus non-randomized trials
Non-randomized trials have a higher risk to include biases.
For instance, coffee drinkers (exposure) may be more likely to develop lung cancer (disease)
if coffee drinkers are often heavy smokers.


# References

- Rothman, Kenneth J., Sander Greenland, and Timothy L. Lash, eds. Modern epidemiology Chapter 3. Lippincott Williams & Wilkins, 2008.
- [http://ocw.jhsph.edu/courses/FundEpi/PDFs/Lecture5.pdf](http://ocw.jhsph.edu/courses/FundEpi/PDFs/Lecture5.pdf)
- [http://ocw.jhsph.edu/courses/FundEpi/PDFs/Lecture6.pdf](http://ocw.jhsph.edu/courses/FundEpi/PDFs/Lecture6.pdf)
- [http://ocw.jhsph.edu/courses/FundEpi/PDFs/Lecture7.pdf](http://ocw.jhsph.edu/courses/FundEpi/PDFs/Lecture7.pdf)
- [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture13.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture13.pdf)
- [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture14.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture14.pdf)
- [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture16.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture16.pdf)
- [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture15.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture15.pdf)
- [http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture12.pdf](http://ocw.jhsph.edu/courses/FundEpiII/PDFs/Lecture12.pdf)

- [https://en.wikipedia.org/wiki/Incidence_(epidemiology)](https://en.wikipedia.org/wiki/Incidence_(epidemiology))
- [https://en.wikipedia.org/wiki/Prevalence#Period_prevalence](https://en.wikipedia.org/wiki/Prevalence#Period_prevalence)

- [https://www.cdc.gov/ophss/csels/dsepd/ss1978/lesson3/section2.html](https://www.cdc.gov/ophss/csels/dsepd/ss1978/lesson3/section2.html)
- [http://health.knowledgeblog.org/2011/07/22/basic-statistics-for-epidemiology/](http://health.knowledgeblog.org/2011/07/22/basic-statistics-for-epidemiology/)
- [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3465772/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3465772/)
