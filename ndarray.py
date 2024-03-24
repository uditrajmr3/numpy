import numpy as np

# check numpy version
print(np.__version__)

# create arrays
# -- create ndarray object -- : array object in numpy is called ndarray
num_arr = np.array([1, 2, 3, 4, 5])
print(num_arr)
print(type(num_arr))

num_tuple = np.array((1, 2, 3, 4, 5))
print(num_tuple)
print(type(num_tuple))
