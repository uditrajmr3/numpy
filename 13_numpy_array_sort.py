import numpy as np

# unsorted array
arr = np.array([7, 7, 8, 2, 8, 4, 8, 9, 4, 6])
print(arr)

# show sorted array without changing original array
print(np.sort(arr))

# sort the string array alphabetically
str_arr = np.array(['numpy', 'tensorflow', 'ski-cit', 'python', 'computer vision'])
print(np.sort(str_arr))

# sort this boolean array
bool_arr = np.array([True, 65 > 50, False, True, 20 > 30, True, False])
print(np.sort(bool_arr))

# sort the 2-D array
_2d_array = np.array([[5, 2], [4, 7], [6, 1]])
print(np.sort(_2d_array))
