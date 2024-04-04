import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# addition of 2 arrays
addition = np.add(arr1, arr2)
print(addition)  # output: [ 7  9 11 13 15]

# summation of 2 arrays
summation = np.sum([arr1, arr2])
print(summation)  # output: 55

# summation of 2 arrays over an axis
summation = np.sum([arr1, arr2], axis=1)
print(summation)  # output: [15 40]

# cumulative sum of 2 arrays
cumulative_sum = np.cumsum([arr1, arr2])
print(cumulative_sum)  # output: [ 1  3  6 10 15 21 28 36 45 55]
