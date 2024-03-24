import numpy as np

# 0 dimensional array
_0d = np.array(26)
print(_0d)
print(_0d.ndim)

# 1 dimensional array
_1d = np.array([1, 2])
print(_1d)
print(_1d.ndim)

# 2 dimensional array
_2d = np.array([[1, 2], [3, 4]])
print(_2d)
print(_2d.ndim)

# 3 dimensional array
_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(_3d)
print(_3d.ndim)
