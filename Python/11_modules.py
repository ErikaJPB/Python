# Modules

# A module is a file containing a set of codes or a set of functions which can be included to an application. It could contain a single variable, function, or a big code base. 


# Import Built-in modules

# OS module

# The OS module in Python provides functions for interacting with the operating system.

# import the module

'''import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()'''


# Sys Module

# The sys module provides functions and variables used to manipulate different parts of the python runtime environment. Function sys.argv returns a list of command line arguments passed to a Python script. 

'''import sys
print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))'''


# Statistics Module

# The statistics module provides functions for calculating mathematical statistics of numeric data.

from statistics import * # importing all the statistics modules

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print(mean(ages))       # ~21.09
print(median(ages))     # 22
print(mode(ages))       # 20
print(stdev(ages))      # ~6.10


# Math Module

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2.0, logarithm with 10 as base


from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2.0


# String module

import string
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print(string.digits)           # 0123456789
print(string.punctuation)      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# Random module

# The random module provides functions for generating random numbers.

from random import random, randint, choice, shuffle

print(random())                 # random float between 0 and 1
print(randint(5, 20))           # random integer between 5 and 20 # it returns a random integer number between [5, 20] inclusive
 