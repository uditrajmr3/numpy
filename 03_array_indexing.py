import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr[0])  # first element of array

_2d_array = np.array([[1, 2], [3, 4]])
print(_2d_array[0][1])  # second element for first row or row1 column2
print(_2d_array[0, 1])

_3d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 7, 18]]])
print(_3d_array[1][1][0])  # first element of the second column of second row or row2 column2 element1
print(_3d_array[1, 1, 0])

# practice question : print 15 from 3d array - Solution: print(_3d_array[2][0][2])
