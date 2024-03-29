"""
ufunc - stands for universal functions
- numpy functions that operates on the ndarray objects.
ufunc args. - where, dtype, out

vectorization - converting the iterative statements into a vector based statement
"""

import numpy as np

# add 2 arrays without ufunc
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = []
for i, j in zip(a, b):
    c.append(i + j)
print(c)

# add 2 arrays with ufunc (numpy add() func)
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = np.add(a, b)
print(c)
