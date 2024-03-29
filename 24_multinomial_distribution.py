# Multinomial distribution - (generalization of Binomial Distribution)
# ! note: dist. - distribution
# param - n(no. of outcomes), pvals(list of possibilities), size

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# draw out a sample for a dice roll
arr = random.multinomial(n=6, pvals=[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
print(arr)
