import numpy as np

a = 4
b = 6

lcm_ab = np.lcm(a, b)
print(lcm_ab)

# find lcm of an array
arr = np.array([3, 5, 16, 27])
lcm = np.lcm.reduce(arr)
print(lcm)

# find lcm of numbers from 1 to 10
arr_1_to_10 = np.arange(1, 11)
lcm_1_to_10 = np.lcm.reduce(arr_1_to_10)
print(lcm_1_to_10)
