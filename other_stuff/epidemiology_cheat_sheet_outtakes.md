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
