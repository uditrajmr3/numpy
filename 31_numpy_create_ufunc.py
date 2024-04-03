import numpy as np


def addition(a, b):
    return a + b


addition = np.frompyfunc(addition, 2, 1)
arr_1 = [7, 7, 8, 2, 8, 4, 8, 9, 4, 6]
arr_2 = [7, 5, 2, 0, 4, 8, 4, 9, 7, 4]
print(addition(arr_1, arr_2))
print(type(addition))
