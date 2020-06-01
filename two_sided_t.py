import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

tips = sns.load_dataset('tips')
print(tips.sample(20))
