from numpy import random

"""
Data distribution: list of all the possible values and how often each of the value occurs
* They are important when working with statistics and data science

Random distribution: probability function
"""

# generate 1-D array of 100 elements where each value has to be either of 2,6,5,3
# P(2) = 0.25
# P(6) = 0.25
# P(5) = 0.10
# P(3) = 0.40

arr = random.choice([2, 6, 5, 3], p=[0.25, 0.25, 0.10, 0.40], size=100)
print(arr)

# generate a 2-D array of dimension 4,4 with same probability distribution
# P(2) = 0.25
# P(6) = 0.25
# P(5) = 0.25
# P(3) = 0.25
_2d_arr = random.choice([2, 6, 5, 3], p=[0.25, 0.25, 0.25, 0.25], size=(4, 4))
print(_2d_arr)
