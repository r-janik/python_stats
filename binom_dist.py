import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

print(tips.sample(10))

n_samples = np.random.binomial(100, 0.05, size=10000)

