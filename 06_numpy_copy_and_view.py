import numpy as np

arr = np.array([1, 2, 3, 4, 5])
copy_arr = arr.copy()
view_arr = arr.view()

print(arr)  # Output: [1 2 3 4 5]
print(copy_arr)  # Output: [1 2 3 4 5]
print(view_arr)  # Output: [1 2 3 4 5]

arr[0] = 14

print(arr)  # Output: [14  2  3  4  5]
print(copy_arr)  # Output: [1 2 3 4 5]
print(view_arr)  # Output: [14  2  3  4  5]

copy_arr[0] = 26

print(arr)  # Output: [14  2  3  4  5]
print(copy_arr)  # Output: [26  2  3  4  5]
print(view_arr)  # Output: [14  2  3  4  5]

view_arr[0] = 53

print(arr)  # Output: [53  2  3  4  5]
print(copy_arr)  # Output: [26  2  3  4  5]
print(view_arr)  # Output: [53  2  3  4  5]
