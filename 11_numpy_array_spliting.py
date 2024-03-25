import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# split into 3
arr_split_3 = np.array_split(arr, 3)
print(arr_split_3)

# split into 4
arr_split_4 = np.array_split(arr, 4)
print(arr_split_4)

# split into array with index
print(arr_split_4[0])

# split 2-D array into 3 2-D arrays
_2d_array = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

arr_2d_split_3 = np.array_split(_2d_array, 3)

print(arr_2d_split_3)

# split 2-D array into 3 2-D arrays along rows
arr_2d_split_3_with_axis = np.array_split(_2d_array, 3, axis=1)

print(arr_2d_split_3_with_axis)

# split alternatively using hsplit()
arr_2d_split_3_row = np.hsplit(_2d_array, 2)

print(arr_2d_split_3_row)
