# Data visualization using matplotlib(pyplot) >> seaborn

import matplotlib.pyplot as plt
import seaborn as sns

'''
* Distplot - Distribution Plot (curve plot - histogram)
'''

# visualize an array from 0 to 9
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sns.displot(arr)  # Output: distplot is deprecated
plt.show()
