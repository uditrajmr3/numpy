# ! note: dist. - distribution
# !! Rayleigh dist. - used in signal processing
# param - scale(how flat the distribution is: 1.0), size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Sample for Raleigh with scale 2 and size 2,3
arr = random.rayleigh(scale=2, size=(2, 3))
print(arr)

# visualization
sns.displot(random.rayleigh(size=1000), kind="kde")
plt.show()
