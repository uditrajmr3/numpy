import numpy as np

# constants
pi = np.pi

# find value of sinh(pi/2)
sin_h = np.sinh(pi / 2)
print(sin_h)

# find value of array of sinh angles
sin_h_arr = np.array([pi / 2, pi / 3, pi / 4, pi / 5, pi / 6])
sin_h_arr_value = np.sinh(sin_h_arr)
print(sin_h_arr_value)

# find value of array of cosh angles
cos_h_arr = np.array([pi / 2, pi / 3, pi / 4, pi / 5, pi / 6])
cos_h_arr_value = np.cosh(cos_h_arr)
print(cos_h_arr_value)

# find sine angle of 1.0 radian
angle = np.arcsinh(1.0)
print(angle)

# find sine angles of array of radian
arr = np.array([0.1, 0.2, 0.5])
angle_arr = np.arctanh(arr)
print(angle_arr)
