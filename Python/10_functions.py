# Functions

# A function is a reusable block of code or programming statements designed to perform a certain task. 

def greet():
    print("Hello World")

greet()  # Hello World

def generate_full_name():
    first_name = "Erika"
    last_name = "Pineda"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)
   
generate_full_name()


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)

add_two_numbers()

# Returning a value


def add_two_numbers():
    num_one = 8
    num_two = 2
    total = num_one + num_two
    return total

print(add_two_numbers())  # 10


#Functions with parameters

def add_numbers(num_one, num_two):
    total = num_one + num_two
    return total

print(add_numbers(4, 5))  # 9 - we need to call the function with arguments

def greetings(name):
    message = name + ", welcome to Python for Everyone!"
    return message

print(greetings("Erika"))  # Erika, welcome to Python for Everyone!


def add_ten(num):
    ten = 10
    return num + ten

print(add_ten(70))  # 80


def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10)) # 314.0


def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

print(sum_of_numbers(10))  # 55


# Passing arguments with key and value

def generate_full_name(first_name , last_name):
    space = " "
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name(first_name="Erika", last_name="Pineda"))  # Erika Pineda

def add_two_numbers(num_one, num_two):
    total = num_one + num_two
    return total

print(add_two_numbers(num_one=4, num_two=9))  # 13


# Functions can return all kind of data types like strings, numbers, lists, dictionaries, sets, tuples, etc.

# Strings

def say_hello():
    return "Hello"

print(say_hello())  # Hello


# Numbers

def add_two_numbers():
    return 2 + 3

print(add_two_numbers())  # 5


# Boolean

def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(is_even(10))  # True
print(is_even(7))  # False


# Lists

def generate_list():
    return [1, 2, 3, 4, 5]

print(generate_list())  # [1, 2, 3, 4, 5]


# Dictionaries

def generate_dict():
    return {'name': 'Erika', 'age': 30}

print(generate_dict())  # {'name': 'Erika', 'age': 30}


# Tuples

def generate_tuple():
    return (1, 2, 3, 4, 5)

print(generate_tuple())  # (1, 2, 3, 4, 5)


# Sets

def generate_set():
    return {1, 2, 3, 4, 5}

print(generate_set())  # {1, 2, 3, 4, 5}


# Functions with default parameters


def greetings(name="James"):
    message = name + ", welcome to Python for Everyone!"
    return message

print(greetings("Oscar"))  # Oscar, welcome to Python for Everyone! - if we dont pass any argument, it will use the default value

print(greetings())  # James, welcome to Python for Everyone!


# Arbitrary number of arguments

def sum_all(*nums): 
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all(2, 3, 4, 5))  # 14


# Default and arbitrary number of parameters

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)

generate_groups("Team-1", "Erika", "Oscar", "Jack", "Jill")


# Function as a parameter of another function

def square_number(n):
    return n * n 

def do_something(f, x):
        return f(x)

print(do_something(square_number, 3))  # 9


