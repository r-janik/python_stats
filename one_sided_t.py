import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
import math

tips = sns.load_dataset('tips')
#print(tips.sample(20))


# Graphical Exploratory data analysis
def ecdf(data):
  '''
  Compute the ECDF of a one-dimensional array of measurements.
  '''
  n = len(data)
  # x-data of the ECDF: x
  x = np.sort(data) 

  # Y-data for the ECDF: y 
  y = np.arange(1, n+1) / n

  return x, y
#
#x_tips, y_tips = ecdf(tips)
#plt.plot(x_tips, y_tips, marker='.', linestyle='none')
#plt.xlabel('dunno')
#plt.ylabel('ECDF')
#plt.show()

# Summary statistics
mean_total_bill = np.mean(tips['total_bill']) 

x_bill, y_bill = ecdf(tips['total_bill'])
percentiles = np.array([2.5, 25, 50, 75, 97.5])
ptiles_bill = np.percentile(tips['total_bill'], percentiles)


#_ = plt.plot(x_bill, y_bill, '.')
#_ = plt.xlabel('Total bills') 
#_ = plt.ylabel('ECDF')
#_ = plt.plot(ptiles_bill, percentiles/100, marker='D', color='red', linestyle='none')

differences = tips['total_bill'] - np.mean(tips['total_bill'])
diff_sq = differences**2 

explicit_variance = np.mean(diff_sq)

variance_np = np.var(tips['total_bill'])

# Standard Deviation

# Covariance and Pearson correlation
plt.plot(tips['total_bill'], tips['tip'], marker='.', linestyle='none')
plt.xlabel('total_bill')
plt.ylabel('tips')
#plt.show()

cov_matrix = np.cov(tips['total_bill'], tips['tip'])

def pearson_r(x, y):
  '''
  Compute Pearson correlation coefficient between two arrays
  '''

  # Compute the correlation matrix: corr_mat
  corr_mat = np.corrcoef(x, y)
  return corr_mat[0, 1]

r = pearson_r(tips['total_bill'], tips['tip'])
print(r)



