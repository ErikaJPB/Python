# STRINGS

letter = 'p'
print(letter)  # p
print(len(letter))  # 1

greeting = 'Hello, World!'
print(greeting)  # Hello, World!
print(len(greeting))  # 13

multiline_string = """Lorep ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt"""
print(multiline_string)


# STRING CONCATENATION

first_name = 'Erika'
last_name = 'Pineda'
space = ' '
full_name = first_name + space + last_name
print(full_name) # Erika Pineda
print(len(full_name)) # 12


# ESCAPE SEQUENCES IN A STRING

# line break
print('Hello, World!\nWelcome to Python Programming') # Hello, World!


# adding tab space 

print('Hello, World!\tWelcome to Python Programming') # Hello, World!    Welcome to Python Programming


print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')


# backslash
print('This is a backslash (\\)') # This is a backslash \

# write a double quote inside a single quote
print('In every programming language it starts with \"Hello, World!\"') # This is a double quote (")


# String formatting

# Old style - % operator
# In python, we can use the % operator to format a string. It allows us to insert a value into a string.

# %s - String
# %d - Integers
# %f - Float
# %.number of digits f - Float with number of digits

first_name = 'Erika'
last_name = 'Pineda'
language = 'Python'
formated_string = 'I am %s %s. I am learning %s' % (first_name, last_name, language)
print(formated_string) # I am Erika Pineda. I am learning Python

# Strings and numbers

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with radius %d is %.2f' % (radius, area)
print(formated_string) # The area of a circle with radius 10 is 314.00

python_libraries = ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries: %s' % python_libraries
print(formated_string) # The following are python libraries: ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']



# New style - .format() method

first_name = 'Erika'
last_name = 'Pineda'
language = 'Python'
formated_string = 'I am {} {}. I am learning {}'.format(first_name, last_name, language)
print(formated_string) # I am Erika Pineda. I am learning Python

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b)) # 4 + 3 = 7
print('{} - {} = {}'.format(a, b, a - b)) # 4 - 3 = 1
print('{} * {} = {}'.format(a, b, a * b)) # 4 * 3 = 12
print('{} / {} = {:.2f}'.format(a, b, a / b)) # 4 / 3 = 1.33
print('{} // {} = {}'.format(a, b, a // b)) # 4 // 3 = 1
print('{} % {} = {}'.format(a, b, a % b)) # 4 % 3 = 1
print('{} ** {} = {}'.format(a, b, a ** b)) # 4 ** 3 = 64


radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with radius {} is {:.2f}'.format(radius, area) 
print(formated_string) # The area of a circle with radius 10 is 314.00


# String Interpolation / f-strings

a = 4
b = 3

print(f'{a} + {b} = {a + b}') # 4 + 3 = 7
print(f'{a} - {b} = {a - b}') # 4 - 3 = 1
print(f'{a} * {b} = {a * b}') # 4 * 3 = 12
print(f'{a} / {b} = {a / b:.2f}') # 4 / 3 = 1.33
print(f'{a} // {b} = {a // b}') # 4 // 3 = 1
print(f'{a} % {b} = {a % b}') # 4 % 3 = 1
print(f'{a} ** {b} = {a ** b}') # 4 ** 3 = 64


# Strings as sequences of characters

language = 'Python'
a,b,c,d,e,f = language
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n


# Accesing characters in strings by index

language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# Slicing strings

language = 'Python'
first_three = language[0:3]
print(first_three) # Pyt
last_three = language[3:6]
print(last_three) # hon
last_three = language[3:]
print(last_three) # hon
last_three = language[-3:]
print(last_three) # hon

# Reversing a string

greeting = 'Hello, World!'
reversed_greeting = greeting[::-1]
print(reversed_greeting) # !dlroW ,olleH

# Skipping characters while slicing\

language = 'Python'
pto = language[0:6:2]
print(pto) # Pto

# STRING METHODS

# capitalize

language = 'python'
capitalized_language = language.capitalize() 
print(capitalized_language) # Python

# count 

language = 'python programming language'
print(language.count('p')) # 2
print(language.count('pro')) # 1
print(language.count('p', 7, 18)) # 1

# endswith

language = 'Python'
print(language.endswith('on')) # True
print(language.endswith('tion')) # False\

# expandtabs

language = 'Python\tIs\tAwesome'
expanded_language = language.expandtabs(20)
print(expanded_language) # Python  Is      Awesome

# find

language = 'Python Programming'
print(language.find('thon')) # 2 (index of the first occurrence of 'thon')
print(language.find('ing')) # 15 (index of the first occurrence of 'ing')

# rfind

language = 'Python Programming'
print(language.rfind('i')) # 15 (index of the last occurrence of 'i')
print(language.rfind('g')) # 17 (index of the last occurrence of 'g')

# index

language = 'Python Programming'
sub_string = 'thon'
print(language.index(sub_string)) # 2

#  rindex

language = 'Python programming'
sub_string = 'pro'
print(language.rindex(sub_string)) # 7 (highest index of the last occurrence of 'pro')

# isalnum

language = 'PythonProgramming'
print(language.isalnum()) # True

language = 'PythonProgramming123'
print(language.isalnum()) # True

language = "Python Programming"
print(language.isalnum()) # False (space is not an alphanumeric character)

# isalpha

language = 'PythonProgramming'
print(language.isalpha()) # True

language = 'PythonProgramming123'
print(language.isalpha()) # False (numbers are present)


# isdecimal

language = '12345'
print(language.isdecimal()) # True

language = 'PythonProgramming123'
print(language.isdecimal()) # False (letters are present)


# isdigit

language = '12345'
print(language.isdigit()) # True

language = 'PythonProgramming123'
print(language.isdigit()) # False (letters are present)


# isnumeric

language = '12345'
print(language.isnumeric()) # True

num = "10.5"
print(num.isnumeric()) # False (decimal point is present)

language = 'PythonProgramming123'
print(language.isnumeric()) # False (letters are present)

# isidentifier

language = 'Python'
print(language.isidentifier()) # True

language = "123Python"
print(language.isidentifier()) # False (starts with a number)

# islower / isupper

language = 'python'
print(language.islower()) # True

language = 'Python'
print(language.isupper()) # False

language = 'PYTHON'
print(language.isupper()) # True


# join 

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # HTML CSS JavaScript React

result = ' and '.join(web_tech)
print(result) # HTML and CSS and JavaScript and React



# strip

language = 'Python Programming'
language = language.strip('Py')
print(language) # thon Programming


# replace

language = 'Python Programming'
print(language.replace('Python', 'Java')) # Java Programming


# split

language = 'Python, Java, JavaScript'
result = language.split(', ')
print(result) # ['Python', 'Java', 'JavaScript']


# title

language = 'python programming'
print(language.title()) # Python Programming


# swapcase

language = 'python programming'
print(language.swapcase()) # PYTHON PROGRAMMING

language = "PYTHON PROGRAMMING"
print(language.swapcase()) # python programming


# Starts with

language = 'Python Programming'
print(language.startswith('Python')) # True

language = 'Python Programming'
print(language.startswith('programming')) # False