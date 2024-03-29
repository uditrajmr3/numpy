# Logistic Distribution - describes growth (used in regression problems and neural networks)
# ! note: dist. - distribution
# param -loc(mean: 0), scale(standard deviation: 1), size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# draw 2*2 samples of logistic with mean at 1 and sd 2
arr = random.logistic(loc=1, scale=2, size=(2, 3))
print(arr)

# visualize
sns.displot(random.logistic(size=1000), kind="kde")
plt.show()
