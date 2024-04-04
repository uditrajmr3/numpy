import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# product of 1 1-D array
product_arr1 = np.prod(arr1)
print(product_arr1)  # output: 120

# product of 2 1-D array
product = np.prod([arr1, arr2])
print(product)  # output: 3628800

# product of 2 1-D array over an axis
product_axis = np.prod([arr1, arr2], axis=1)
print(product_axis)  # output: [  120 30240]

# cumulative product of 2 1-D arrays
cumulative_prod = np.cumprod([arr1, arr2])
print(cumulative_prod)  # output: [      1       2       6      24     120     720    5040   40320  362880 3628800]
