# ! note: dist. - distribution
# Chi square dist. - used to verify a hypothesis
# param - df(degree of freedom), size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sample chi square dist. with df 2 and size 2,3
arr = random.chisquare(df=2, size=(2, 3))
print(arr)

# visualize
sns.displot(random.chisquare(size=1000, df=1), kind="kde")
plt.show()
