import numpy as np
from matplotlib import pyplot as plt


def ecdf(data):
  '''
  Compute the ECDF of a one-dimensional array of measurements
  '''
  n = len(data)
  # x-data of the ECDF: x
  x = np.sort(data)

  # y-data for the ECDF: y
  y = np.arange(1, n+1) / n

  return x, y
  



def bernoulli_trials(n, p):
  '''
  perform Bernoulli trials with success probability p and return number of successes
  '''
  # Initialise the of successes: n_success
  n_success = 0

  # Perform trials
  for i in range(n):
    random_number = np.random.random()

    # If less than p, it's a success, so add one to n_success
    if random_number < p:
      n_success += 1
  return n_success

np.random.seed(42)

# Initialise the number of defaults:
n_defaults = np.empty(1000)

for i in range(1000):
  n_defaults[i] = bernoulli_trials(100, 0.05)

_ = plt.hist(n_defaults, density=True)
_ = plt.xlabel('number of defaults out of 100 loansi') 

plt.show()
