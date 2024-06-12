 # Higher order functions

# Functions as parameters

# Normal function
from functools import reduce
def sum_numbers(nums) : 
    return sum(nums)

# Higher order function

def higher_order_function(func, lst): # funciton as a parameter
    summation = func(lst)
    return summation

result = higher_order_function(sum_numbers, [1,2,3,4,5])

print(result) # 15


# Functions as a return value

def square (x):  # a square function
    return x ** 2

def cube(x): # a cube function
    return x ** 3

def absolute(x): # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)
    
def higher_order_function(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute
    

result = higher_order_function("square")
print(result(3)) # 9

result = higher_order_function("cube")
print(result(3)) # 27

result = higher_order_function("absolute")
print(result(-3)) # 3


# Python Closures
# allows a nested function to access the outer scope of the enclosing function. 

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()

print (closure_result(5)) # 15
print (closure_result(10)) # 20


# Python Decorators
# A decorator is a design pattern that allows the user to add a new functionality to an existing object without modifying its structure.

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return "Welcome to Python"
print(greeting()) # WELCOME TO PYTHON


# Multiple decorators to a single function


# First decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator
def greeting():
    return "Welcome to Python"

print(greeting()) # ['WELCOME', 'TO', 'PYTHON']



# Accepting parameters in decorator functions

def decorator_with_params (function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))

    return wrapper_accepting_parameters
    
@decorator_with_params
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love python.".format(first_name, last_name, country))


print_full_name("Erika", "Pineda", "Colombia") # I am Erika Pineda. I love python. I live in Colombia


# Built-in higher order functions


# Map

numbers = [1, 2, 3, 4, 5]

def square(num): 
    return num ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared)) # [1, 4, 9, 16, 25]

numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared)) # [1, 4, 9, 16, 25]

 #####

names = ["Erika", "Juan", "Pedro"]

def change_to_upper(name):
    return name.upper()

names_upper = map(change_to_upper, names)
print(list(names_upper)) # ['ERIKA', 'JUAN', 'PEDRO']


names_uper = map(lambda name: name.upper(), names)
print(list(names_uper)) # ['ERIKA', 'JUAN', 'PEDRO']



### Filter

numbers = [1, 2, 3, 4, 5]

def is_even (num) :
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers)) # [2, 4]


def is_odd (num): 
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers)) # [1, 3, 5]



names = ["Erika", "Bernardo", "Pedro", "Martin"]
def is_long_name (name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_long_name, names)
print(list(long_names)) 



# Reduce

numbers_string = ["1", "2", "3", "4", "5"]

def add_two_nums(x,y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_string)
print(total) # 15

