import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

# iterate through the 1-D array
# for i in arr:
#     print(i)

# iterate through (each scalar element) in the 2-D array
_2d_arr = arr.reshape(2, 5)

# for i in _2d_arr:
#     for j in i:
#         print(j)

# iterate through (each scalar element) in the 2-D array
_3d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])

# for i in _3d_arr:
#     for j in i:
#         for k in j:
#             print(k)

# iterate through multidimensional array using nditer()
for i in np.nditer(_2d_arr):
    print(i)

for i in np.nditer(_3d_arr):
    print(i)
