import numpy as np

'''
There are 5 types of rounding offs done in numpy:
1. truncation: trunc() - remove decimals and return the floating value closest to 0 
2. fix: fix() - remove decimals and return the floating value closest to 0 
3. rounding: round() - promotes the value to next floating value
4. floor: floor() - rounds off to nearest subsiding integer
5. ceil: ceil() - rounds off to nearest preceding integer
'''

arr = np.array([-3.666, 3.667])
arr_trunc = np.trunc([-3.666, 3.667])
arr_fix = np.fix([-3.666, 3.667])
arr_round = np.round([-3.666, 3.667])
arr_around = np.around([-3.666, 3.667])
arr_floor = np.floor([-3.666, 3.667])
arr_ceil = np.ceil([-3.666, 3.667])

print(arr)
print(arr_trunc)
print(arr_fix)
print(arr_round)
print(arr_around)
print(arr_floor)
print(arr_ceil)
