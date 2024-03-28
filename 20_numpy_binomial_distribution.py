#  !! Discrete distribution (Binomial Distribution)
# ! note: dist. - distribution
# param - n(no. of trials), p(probability), size(shape of returned array)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

binomial = random.binomial(p=0.5, size=10, n=1000)
print(binomial)

sns.displot(binomial, kind="kde")
sns.displot(binomial, kind="hist")
plt.show()
