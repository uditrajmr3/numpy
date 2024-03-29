# ! note: dist. - distribution
# Pareto dist. - 80:20 ratio. (20% event >> 80% outcome)
# param - a(shape), size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sample for Pareto dist. with shape 2 and size 2,3
arr = random.pareto(a=2, size=(2, 3))
print(arr)

# visualize
sns.displot(random.pareto(a=2, size=1000), kind="hist")
plt.show()
