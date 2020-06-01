import seaborn as sns
import numpy as np
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson


tips = sns.load_dataset('tips') 
print(tips.sample(20))

##
# Normality tests - check if your data has Gaussian distribution 
# Shapiro-Wilk test
# Observations in each sample are independent and identically distributed (iid)
# Interpretation: 
# H0: the sample has a Gaussian distribution.
# H1: the sample does not have a Gaussian distribution.
##

data = tips['total_bill']
stat, p = shapiro(data)
print('stat=%.3f, p=%.3f' % (stat, p))

if p > 0.05: 
  print('Probably Gaussian')
else:
  print('Probably not Gaussian')

# D'Agostino's K^2 test
# Observations in each sample are independent and identically distributed (iid)
# H0: the sample has a Gaussian distribution.
# H1: the sample does not have a Gaussian distribution.
stat, p = normaltest(data)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05: 
  print("D'Agostino: Probably Gaussian")
else:
  print("D'Agostino: Probably not Gaussian")


# Anderson-Darling Test
# Same conditions and hypotheses as before
result = anderson(data)
print("stat=%.3f" % (result.statistic))

for i in range(len(result.critical_values)):
  sl, cv = result.significance_level[i], result.critical_values[i]
  if result.statistic < cv:
    print("Anderson: Probably Gaussian at the %.1f%% level" %(sl)) 
  else:
    print("Anderson: Probably not Gaussian at the %.1f%% level" %(sl))


