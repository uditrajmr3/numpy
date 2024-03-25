import numpy as np

"""
**** data types in numpy ****
01. i : integer
02. b : boolean
03. u : unsigned integer
04. f : float
05. c : complex float
06. m : timedelta
07. M : datetime
08. O : object
09. S : string
10. U : unicode string
11. V : memory
"""

# check data type of numpy array
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)  # output: int32

str_arr = np.array(['rose', 'lily', 'sunflower', 'daisy', 'lotus', 'dandelion'])
print(str_arr.dtype)  # output: <U9

# create an array with defined data type in numpy
new_arr = np.array([1, 2, 3, 4, 5], dtype='S')
print(new_arr)
print(new_arr.dtype)

# create an array with defined data type int with 4 byte size
size4_int_arr = np.array([1, 2, 3, 4, 5], dtype='i4')
print(size4_int_arr)
print(size4_int_arr.dtype)

# invalid casting example
# invalid_dtype_arr = np.array(['a', '2', '3'], dtype='i')
# print(invalid_dtype_arr.dtype)  # uncomment to see the error
# output: ValueError: invalid literal for int() with base 10: 'a'

# handle casting with astype()
example_arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
cast_to_int_arr = example_arr.astype('i')
cast_to_str_arr = example_arr.astype('S')
cast_to_bool_arr = example_arr.astype(bool)
print(cast_to_int_arr)  # output: [1 2 3 4 5]
print(cast_to_int_arr.dtype)  # output: int32
print(cast_to_str_arr)  # output: [b'1.1' b'2.2' b'3.3' b'4.4' b'5.5']
print(cast_to_str_arr.dtype)  # output: |S32
print(cast_to_bool_arr)  # output: [ True  True  True  True  True]
print(cast_to_bool_arr.dtype)  # output: bool
