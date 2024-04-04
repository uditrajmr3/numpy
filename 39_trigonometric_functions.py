import numpy as np

# find value of sin(pi/2)
sin_half_pi = np.sin(np.pi / 2)
print(sin_half_pi)

# find value of array of sine angles
sin_arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5, np.pi / 6])
sin_arr_value = np.sin(sin_arr)
print(sin_arr_value)

# convert degree into radians
# !! radian = pi/180 degree
degree = np.array([90, 180, 270, 360])
radian = np.deg2rad(degree)
print(radian)

# convert radians into degree
radians = np.array([np.pi / 3, np.pi / 2, np.pi, np.pi * 1.5, np.pi * 2])
degrees = np.rad2deg(radians)
print(degrees)

# find sine angle of 1.0 radian
angle = np.arcsin(1.0)
print(angle)

# find sine angles of array of radian
arr = np.array([1.0, 0.1, -1.0])
angle_arr = np.arcsin(arr)
print(angle_arr)

# find hypotenuse using pythagoras theorem for b=4 & p=3
base = 4
perpendicular = 3
hypotenuse = np.hypot(base, perpendicular)
print(hypotenuse)
