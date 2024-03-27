import numpy as np

# generate a random integer number between 0 to 100
random_int = np.random.randint(100)
print(random_int)

# generate a random floating number between 0 to 1
random_float = np.random.rand()
print(random_float)

# generate a 1-D array of random numbers of length 10
random_arr = np.random.randint(100, size=10)
print(random_arr)

# generate a 2-D array of random numbers of length 2,5
random_arr_2d = np.random.randint(100, size=(2, 5))
print(random_arr_2d)

# generate a 1-D array of random float numbers of length 3
random_arr_float = np.random.rand(3)
print(random_arr_float)

# generate a 2-D array of random float numbers of length 2,4
random_arr_2d_float = np.random.rand(2, 4)
print(random_arr_2d_float)

# get a random element(s) from an array
random_choice = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(random_choice)

# generate a 2-D array from random elements of an array
random_2d_choice = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], size=(2, 2))
print(random_2d_choice)
