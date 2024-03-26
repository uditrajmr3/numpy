import numpy as np

sorted_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 18])

# search array using where() for 3
index_of_3 = np.where(sorted_arr == 3)
print(index_of_3)

# search array for even numbers
multiples_2_indexes = np.where(sorted_arr % 2 == 0)
print(multiples_2_indexes)

# perform binary search in array using searchSorted() to find 8
index_of_8 = np.searchsorted(sorted_arr, 8)
print(index_of_8)

# find the index for 3 from right/opposite side
opposite_index_of_3 = np.searchsorted(sorted_arr, 3, side='right')
print(opposite_index_of_3)

# find the indexes for [0, 11, 13, 15, 16, 17]
indexes_array = np.searchsorted(sorted_arr, [0, 11, 13, 15, 16, 17])
print(indexes_array)
