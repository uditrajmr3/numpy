import numpy as np

arr = np.array([7, 5, 2, 0, 4, 8, 4, 9, 7, 4])

# !! boolean list: list of boolean corresponding to indexes in the array (True/False)
bool_arr = [True, False, False, True, True, False, True, False, False, True]

# create an array based on bool_arr as condition
print(arr[bool_arr])  # Output: [7 0 4 4 4]

# get an array where element value is greater than 4
arr_gt3_bool = []
for i in arr:
    if i > 4:
        arr_gt3_bool.append(True)
    else:
        arr_gt3_bool.append(False)
arr_gt3 = arr[arr_gt3_bool]
print(arr_gt3)  # Output: [7 5 8 9 7]

# this can also be done simply like this:
print(arr[arr > 4])
