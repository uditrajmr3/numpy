# Uniform Distribution - used only for probability(p)
# ! note: dist. - distribution
# param - a(lower bound: 0.0), b(upper bound: 1.0), size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr = random.uniform(size=(2, 5))
print(arr)

# visualize the uniform distribution
sns.displot(random.uniform(size=1000), kind="kde")
plt.xlabel('Uniform Dist.')
plt.ylabel('Probability')
plt.show()
