import numpy as np

a = 4
b = 6

hcf_ab = np.gcd(a, b)
print(hcf_ab)

# find hcf of an array
arr = np.array([3, 9, 42, 21])
hcf = np.gcd.reduce(arr)
print(hcf)
