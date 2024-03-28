# !!! Gaussian Distribution (Normal Distribution)
# also known as continuous distribution
# ! note: dist. - distribution
# loc: mean, scale: standard deviation, size: size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# normal dist. of size 2,3
arr = random.normal(size=[2, 3])
print(arr)

# normal dist. of size 2,3 with mean 1 and sd 2
new_arr = random.normal(loc=1, scale=2, size=(2, 3))
print(new_arr)

# visualization of normal dist. (bell curve)
sns.displot(random.normal(size=1000))
plt.show()
