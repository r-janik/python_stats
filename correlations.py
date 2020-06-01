import seaborn as sns
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau
from scipy.stats import chi2_contingency

tips = sns.load_dataset('tips')

data1 = tips['total_bill'] 
data2 = tips['tip']

stat, p = pearsonr(data1, data2)

##  Tests whether two samples have a linear relationship.
#Assumptions
  #Observations in each sample are independent and identically distributed (iid).
  #Observations in each sample are normally distributed.
  #Observations in each sample have the same variance.

print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
  print("Pearson: Probably independent")
else:
  print("Pearson: Probably dependent")

##  Spearman Rank Correlation
# Observations in each sample are independent and identically distributed (iid).
# Observations in each sample can be ranked
## Interpretation
# H0: The two samples are independent 
# H1: There is a dependency between tthte samples

stat, p = spearmanr(data1, data2)

print('stat=%.3f, p=%.3f' % (stat, p))

if p > 0.05:
  print("Spearman: Probably independent")
else:
  print("Spearman: Probably dependent")

## Kendall's Rank Correlation

# Tests whether two samples have a monotonic relationship
# Assumptions:
  # Observations in each sample are independent and identically distributed (iid).
  # Observations in each sample can be ranked
  # H0: The two samples are independent 
  # H1: There is a dependency between tthte samples

stat, p = kendalltau(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))

if p > 0.05:
  print("Kendall: Probably independent")
else:
  print("Kendall: Probably dependent")

## Chi-Squared Test
# Tests whether two categorical variables are related or independent
# Assumptions
  # Observations used in ttthe calculation of the contigency table are independent
  # 25 or more exmaples in each cell of the contingency table

  # Interpretation:
    # H0: the two samples are independent
    # H1: there is a dependency between the samples



  





