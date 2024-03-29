# ! note: dist. - distribution
# Exponential dist: used for describing the time till next event (success/failure)
# param = scale(inverse of lam), size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# draw a sample for exponential dist with scale 2 and size 2,3
arr = random.exponential(scale=2, size=(2, 3))
print(arr)

# visualization
sns.displot(random.exponential(size=1000), kind="kde")
plt.show()
