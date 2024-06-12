# List comprehension

# List comprehension is a compact way of creating a list from a sequence, is a short way to create a new list. Is considerably faster than processing a list using the for loop. 


word = "Python"


# One way

lst = list(word)
print(type(lst)) # <class 'list'>
print(lst) # ['P', 'y', 't', 'h', 'o', 'n']


# Second way: List comprehension

lst =[i for i in word]
print(type(lst)) # <class 'list'>
print(lst) # ['P', 'y', 't', 'h', 'o', 'n']

# generating numbers
numbers = [i for i in range(11)]
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# doing math operations during iteration
squares = [i * i for i in range(11)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# making a list of tuples
numbers = [(i, i * i ) for i in range(11)]
print(numbers) # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]


# List comprehension can be combined with if expression

# generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# flattening a three dimentional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row] 
print(flattened_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]



# LAMBDA FUNCTION

# The lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression. We need it when we want to write an anonymous function inside another function. 


add_two_numbers = lambda a, b: a + b
print(add_two_numbers(2, 3)) # 5

square = lambda a: a ** 2
print(square(3)) # 9

cube = lambda a: a ** 3
print(cube(3)) # 27

multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5 ,5 , 3)) # 22


# Lambda function inside another function

def power(x):
    return lambda n: x ** n

cube = power(2)(3)
print(cube) # 8

two_power_of_five = power(2)(5)
print(two_power_of_five) # 32