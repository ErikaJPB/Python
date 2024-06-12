# Built-in functions

# For example
print("Hello, World!") # returns Hello, World!
print(len('Hello World!'))# returns 11
print(type('Hello World!')) # returns <class 'str'>
print(str(10)) # '10'
print(int('10')) # 10
print(float('9')) # 9.0
# print(input('Enter your name: ')) # Allows user input


print(min(20,30,40,50)) # 20
print(max(20,30,40,50)) # 50
print(min([20,30,40,50])) # 20 it takes a list as an argument
print(max([20,30,40,50])) # 50 it takes a list as an argument
print(sum([20,30,40,50])) # 140 it takes a list as an argument


''' Variables in Python use lowercase and snake_case and cannot be built-in functions or reserved words. Variables store data in memory. if variable has more than one word we use the underscore. For example: my_name, my_age, my_country, my_address, my_date_of_birth, etc.
'''
my_string_variable = "hello I'm a string"
print(my_string_variable)

# first_name="Erika"
# last_name="Pineda"
# country="Colombia"
# city="Bogota"
# age=20
# is_married=False
# skills=['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#     'firstname':'Erika',
#     'lastname':'Pineda',
#     'country':'Colombia',
#     'city':'Bogota'
# }

# Printing the values stored in the variables

# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)

# Multiple variables in a line

# first_name, last_name, country, age, is_married = 'Erika', 'Pineda', 'Colombia', 20, False
# print(first_name, last_name, country, age, is_married)
# print ('Last name:', last_name)

# first_name = input('What is your name: ')
# age = input('How old are you? ')

# print(first_name)
# print(age)


# Check Data Types and Casting

# To check data types we use type function

print(type('Erika')) # str
print(type(20)) # int
print(type(20.0)) # float


   
''' Casting is the process of converting from one data type to another data type. For example converting a string to an integer or a string to a float, an integer to a string, etc. The functions to use for casting are int(), str(), float(). 
'''


# int to float

# num_int = 10
# print('num_int:', num_int) # 10
# num_float = float(num_int)
# print('num_float:', num_float) # 10.0

# float to int

pi = 3.14
print(int(pi)) # 3


# int to string

# num_int = 10
# print(num_int) # 10
# num_str = str(num_int)
# print(num_str) # '10'


# str to int or float

num_str = '10.4'
num_float = float(num_str)  # Convert to float first
num_int = int(num_float)    # Convert to int after removing decimal
print('num_int:', num_int)
print('num_float:', num_float)


# str to list
first_name = 'Erika'
print(first_name) # Erika
first_name_to_list = list(first_name)
print(first_name_to_list) # ['E', 'r', 'i', 'k', 'a']


# Numbers

#  1. Integers (negative, zero, positive). For example: -20, 0, 10
#  2. Floating point numbers (decimal numbers). For example: -20.2, 0.0, 10.1
#  3. Complex numbers. For example: 1 + j, 1 - j


num_one = 5 
num_two = 4

total = num_one + num_two
print(total) # 9

diff = num_one - num_two
print(diff) # 1

product = num_one * num_two
print(product) # 20

division = num_one / num_two
print(division) # 1.25

remainder = num_one % num_two
print(remainder) # 1

exp = num_one ** num_two
print(exp) # 625

floor_division = num_one // num_two
print(floor_division) # 1

radius = 30
area_of_circle = 3.14 * radius ** 2
print(area_of_circle) # 2826.0
circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle) # 188.4


first_name = input('What is your first name: ')
last_name = input('What is your last name: ')
country = input('What is your country: ')
age = input('How old are you: ')

