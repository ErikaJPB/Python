# OPERATORS


# BOOLEAN
# In python we have two boolean values: True and False. They need to be written in uppercase.

print(True)
print(False)


# ASSIGNMENT OPERATORS


# = assignment operator
x = 5
print(x) # 5


# += addition assignment operator
x += 3
print(x) # 8

# -= subtraction assignment operator
x -= 3
print(x) # 5

# *= multiplication assignment operator
x *= 3
print(x) # 15

# /= division assignment operator
x /= 3 
print(x) # 5.0

# %= modulus assignment operator
x %= 3
print(x) # 2.0
 
# //= floor division assignment operator
x //= 3
print(x) # 0.0

# **= exponent assignment operator
x **= 3
print(x)    # 0.0

# &= bitwise AND assignment operator
x = 10
x &= 3
print(x)   # 2

# |= bitwise OR assignment operator
x = 10
x |= 3
print(x)  # 11

# ^= bitwise XOR assignment operator
x = 10
x ^= 3
print(x) # 9

# >>= bitwise right shift assignment operator
x = 10
x >>= 3
print(x)    # 1

# <<= bitwise left shift assignment operator
x = 10
x <<= 3
print(x)   # 80

# ARITHMETIC OPERATORS

x = 5
y = 3

# + addition

print(x + y)  # 8

# - subtraction

print(x - y) # 2

# * multiplication

print(x * y) # 15

# / division

print(x / y) # 1.6666666666666667

# % modulus

print(x % y) # 2

# ** exponent

print(x ** y) # 125

# // floor division

print(x // y)


# COMPARISON OPERATORS

x = 5
y = 3

# == equal

print(x == y) # False

# != not equal

print(x != y) # True

# > greater than

print(x > y) # True

# < less than

print(x < y) # False

# >= greater than or equal to

print(x >= y)  # True

# <= less than or equal to

print(x <= y) # False   

# More examples

print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon')) 

print('True == True: ', True == True)  # True
print('True == False: ', True == False) # False
print('False == False:', False == False) # True

# MORE COMPARISON OPERATORS

# is: Returns true if both variables are the same object

x = 5
y = 5

print(x is y) # True

# is not: Returns true if both variables are not the same object

x = 5
y = 3

print(x is not y) # True

#  in : Returns True if a sequence with the specified value is present in the object

x = ['apple', 'banana']
print('banana' in x) # True
print('pineapple' in x) # False


# not in : Returns True if a sequence with the specified value is not present in the object

x = ['apple', 'banana']
print('banana' not in x) # False
print('pineapple' not in x) # True


# LOGICAL OPERATORS

# and: Returns True if both statements are true

x = 5
print(x > 3 and x < 10) # True

# or: Returns True if one of the statements is true

x = 5
print(x > 3 or x < 4) # True

# not: Reverse the result, returns False if the result is true

x = 5
print(not(x > 3 and x < 10)) # False


# Exercises

age = 35

height = 5.7

complex = 1 + 2j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

# base = float(input('Enter the base of the triangle: '))
# height = float(input('Enter the height of the triangle: '))
# area = 0.5 * base * height
# print(f'The area of the triangle is {area}')

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

# side_a = float(input('Enter side a of the triangle: '))
# side_b = float(input('Enter side b of the triangle: '))
# side_c = float(input('Enter side c of the triangle: '))
# perimeter = side_a + side_b + side_c
# print(f'The perimeter of the triangle is {perimeter}')


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

# length = float(input('Enter the length of the rectangle: '))
# width = float(input('Enter the width of the rectangle: '))
# area = length * width
# perimeter = 2 * (length + width)
# print(f'The area of the rectangle is {area} and the perimeter is {perimeter}')

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len('python') == len('dragon')) # False

# Use and operator to check if 'on' is found in both 'python' and 'dragon'

print('on' in 'python' and 'on' in 'dragon') # True

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentence = 'I hope this course is not full of jargon'

print('jargon' in sentence) # True

# There is no 'on' in both dragon and python

print('on' not in 'python' and 'on' not in 'dragon') # False

# Find the length of the text python and convert the value to float and convert it to string

print(str(float(len('python')))) # 6.0

# Check if type of '10' is equal to type of 10
print(type('10' == 10)) # False

# Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10) # True

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

# years = int(input('Enter the number of years: '))
# seconds = years * 365 * 24 * 60 * 60
# print('you have lived for', seconds, 'seconds')


# Write a python script that displays the following table

# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)




