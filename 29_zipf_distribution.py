# ! note: dist. - distribution
# Zipf dist. - occurrence ratio/comparison
# param - a(dist param), size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sample for Pareto dist. with a 2 and size 2,3
arr = random.zipf(a=2, size=(2, 3))
print(arr)

# visualize
new_arr = random.zipf(a=2, size=1000)
sns.displot(new_arr, kind="hist")
sns.displot(new_arr[new_arr < 10], kind="hist")
plt.show()
