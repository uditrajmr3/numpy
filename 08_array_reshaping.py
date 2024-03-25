import numpy as np

# Reshaping an array: adding/removing elements from array to change its shape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshaping from 1-D to 2-D
_2d_arr = arr.reshape(4, 3)

print(_2d_arr)
print("shape:", _2d_arr.shape)
print("dimensions:", _2d_arr.ndim)

# Reshaping from 1-D to 3-D
_3d_array = arr.reshape(2, 2, 3)

print(_3d_array)
print("shape:", _3d_array.shape)
print("dimensions:", _3d_array.ndim)

# Unknown dimension reshaping: when length of array is unknown
reshape_arr = arr.reshape(2, 2, -1)

print(reshape_arr)
print(reshape_arr.shape)  # output: (2, 2, 3)

# Flatten the array from 3-D to 1-D
new_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 7, 18]]])

flatten_arr = new_array.flatten()  # or new_array.reshape(-1)

print(flatten_arr)
print(flatten_arr.shape)  # Output: (18,)
print(flatten_arr.ndim)  # Output: 1
