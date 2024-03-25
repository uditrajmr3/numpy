import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr_2 = np.array([6, 7, 8, 9, 10])

joined_arr = np.concatenate((arr, arr_2))

print(joined_arr)

# join 2-D arrays along with rows (axis = 1)
_2d_arr = np.array([[1, 2, 3], [4, 5, 6]])
_2d_arr_2 = np.array([[7, 8, 9], [10, 11, 12]])

joined_2d_arr = np.concatenate((_2d_arr, _2d_arr_2), axis=1)

print(joined_2d_arr)

# join array using stack function
arr_new = np.array([1, 2, 3, 4, 5])
arr_new_2 = np.array([6, 7, 8, 9, 10])

joined_arr_new = np.stack((arr_new, arr_new_2), axis=1)

print(joined_arr_new)

# stack arrays along rows : hstack()
arr_other = np.array([1, 2, 3, 4, 5])
arr_other_2 = np.array([6, 7, 8, 9, 10])

joined_arr_other = np.hstack((arr_other, arr_other_2))

print(joined_arr_other)

# stack along column
arr_column = np.array([1, 2, 3, 4, 5])
arr_column_2 = np.array([6, 7, 8, 9, 10])

joined_arr_column = np.vstack((arr_column, arr_column_2))

print(joined_arr_column)

# stack along height(depth)
arr_height = np.array([1, 2, 3, 4, 5])
arr_height_2 = np.array([6, 7, 8, 9, 10])

joined_arr_height = np.dstack((arr_height, arr_height_2))

print(joined_arr_height)
