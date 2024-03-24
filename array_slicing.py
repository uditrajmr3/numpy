import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Slice format - array_name[start:end:step]

# slice this array from start index 0 to end index 3
print(arr[0:3])  # Output: [1 2 3]

# slice from start index 3 to last
print(arr[3:])

# slice up-to end index 3
print(arr[:3])

# slice arr from start index to end index 4 but only alternatives
print(arr[0:4:2])

new_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# slice new array to get only alternate numbers
print(new_arr[::2])

# slice new array to get only alternate numbers but the other half
print(new_arr[1::2])

_2d_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])

# slice 2d array to get 7,8,9
print(_2d_array[1, 1:4])

# slice to get only second element from each row
print(_2d_array[0:, 2])

_3d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 7, 18]]])

# slice 3d array to get 10,11,12
print(_3d_array[1, 1, 0:])  # also pass the end index if there are more elements in that row

# slice to get only second element from each row
print(_3d_array[0:, 0:, 2])
