import numpy as np

# arithmetic operators: +,-,*,/,%,^

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
arr3 = np.array([-1, 2, -3, -4, 5])

add = np.add(arr1, arr2)
diff = np.subtract(arr1, arr2)
product = np.multiply(arr1, arr2)
quotient = np.divide(arr1, arr2)
exponent = np.power(arr1, arr2)
remainder = np.remainder(arr1, arr2)
_divmod = np.divmod(arr1, arr2)
abst = np.absolute(arr3)

print(add)
print(diff)
print(product)
print(quotient)
print(exponent)
print(remainder)
print(_divmod)
print(abst)
