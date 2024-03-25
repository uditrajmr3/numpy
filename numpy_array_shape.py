import numpy as np

# shape of an array : no of elements in each dimension of an array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr)
print("shape:", arr.shape)  # Output: shape: (2, 4)
# this output means array has dimensions 2*4

# Question: What is the shape of a 5 dimension array
new_arr = np.array([1, 2, 3, 4, 5], ndmin=5)

print(new_arr)  # Output: [[[[[1 2 3 4 5]]]]]
print("shape:", new_arr.shape)  # Output: shape: (1, 1, 1, 1, 5)

_3d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 7, 18]]])

print(_3d_array)
print("shape:", _3d_array.shape)  # Output: shape: (3, 2, 3)

_0d_arr = np.array(26)

print(_0d_arr)
print("shape:", _0d_arr.shape)  # Output: shape: ()

_1d_arr = np.array([22, 6, 2001])

print(_1d_arr)
print("shape:", _1d_arr.shape)  # Output: shape: (3,)
