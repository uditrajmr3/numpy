import numpy as np

'''
* Permutation: number of ways a particular set can be arranged
eg. [1,2,3], [2,1,3], [3,1,2] and so on

Numpy random module provides 2 methods: shuffle() and permutation()
'''

# change array elements order using shuffle() (changes original array)
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)

# change array elements order using permutation() (doesn't changes original array)
new_arr = np.array([1, 2, 3, 4, 5])
permutation_new_arr = np.random.permutation(new_arr)
print(new_arr)
print(permutation_new_arr)
