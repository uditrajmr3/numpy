# Poisson Distribution - estimation of how many times an event can happen
# ! note: dist. - distribution
# param - lam(no. of occurrences), size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# generate a random 1*10 dist. for occurrence of 2
dist_of_2 = random.poisson(lam=2, size=10)
print(dist_of_2)

sns.displot(random.poisson(lam=2, size=1000), kind="hist")
plt.xlabel('Poisson Distribution')
plt.ylabel('Occurrences')
plt.show()
