# LOOPS

# While loop

# We use the reserved word while to make a while loop. It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.

count = 0

while count < 5:
    print(count)
    count += 1  # prints 0 1 2 3 4

# The condition becomes false when count is 5, so the loop stops executing.


count = 0

while count < 5:
    print(count)
    count += 1
else:
    print(count)

# the loop condition will be false when count is 5 and the loop stops, and execution starts the else statement and prints 5.


# Break and continue

# The break statement is used to exit the loop. It is used to exit the loop when a condition becomes true.

count = 0
while count < 5: 
    print(count)
    count += 1
    if count == 3:
        break
# only prints 0 1 2 when it reaches 3 it stops.

# The continue statement is used to skip the current block and move to the next iteration of the loop.

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

# prints 0 1 2 4, when count is 3 it skips the print statement and continues to the next iteration.


# For loop

# The for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects. It is used to execute a block of statements repeatedly until the given condition is satisfied.

# For loop with list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number) # 0 1 2 3 4 5


# For loop with string
language = 'Python'
for letter in language:
    print(letter)   # P y t h o n

for i in range(len(language)):
    print(language[i])  # P y t h o n

# For loop with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number) # 0 1 2 3 4 5

# For loop with dictionary
person = {
    'first_name': 'James',
    'last_name': 'Bond',
    'age': 30,
    'country': 'UK',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': '20-45 32nd St',
        'zipcode': '11105'
    }
    
}

for key in person:
    print(key) # first_name last_name age country is_married skills address

for key, value in person.items():
    print(key, value) # first_name James last_name Bond age 30 country UK is_married False skills ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'] address {'street': '20-45 32nd St', 'zipcode': '11105'}


# loops in set

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for company in it_companies:
    print(company) # Facebook Google Microsoft Apple IBM Oracle Amazon


# Break and continue

# Break when we want to stop the loop before is completed.

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break # 0 1 2 3


# Continue when we want to skip the current iteration and move to the next iteration.

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    if number == 3:
        continue
    print(number) # 0 1 2 4 5


# Range function

# The range() function is used to generate a sequence of numbers. It is commonly used in for loops.

lst = list(range(11))
print (lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

st = set(range(1, 11))
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

list = list(range(0, 11, 2))
print(list) # [0, 2, 4, 6, 8, 10]

set = set(range(0, 11, 2))
print(set) # {0, 2, 4, 6, 8, 10}


# Nested for loop

for i in range(3):
    for j in range(3):
        print('i:', i, 'j:', j) # prints i: 0 j: 0 i: 0 j: 1 i: 0 j: 2 i: 1 j: 0 i: 1 j: 1 i: 1 j: 2 i: 2 j: 0 i: 2 j: 1 i: 2 j: 2


person = {
    'first_name': 'James',
    'last_name': 'Bond',
    'age': 30,
    'country': 'UK',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': '20-45 32nd St',
        'zipcode': '11105'
    }
    
}

for key in person: 
    if key == 'skills':
        for skill in person['skills']:
            print(skill) # JavaScript React Node MongoDB Python


# For else
for number in range(11):
    print(number)
else: 
    print('The loop stops at', number) # prints 0 1 2 3 4 5 6 7 8 9 10 The loop stops at 10


# Pass

# When a statement is required but we dont want to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder for future statements. 
for number in range(6):
    pass


# Exercises

# Iterate 0 to 10 using for loop, do the same using while loop.

for number in range(11):
    print(number) # 0 1 2 3 4 5 6 7 8 9 10

count = 0
while count < 11:
    print(count)
    count += 1 # 0 1 2 3 4 5 6 7 8 9 10


# Iterate 10 to 0 using for loop, do the same using while loop.

for number in range(10, -1, -1):
    print(number) # 10 9 8 7 6 5 4 3 2 1 0

count = 10
while count >= 0:
    print(count)
    count -= 1 # 10 9 8 7 6 5 4 3 2 1 0


for i in range(11): 
    result = i * i
    print(f"{i} x {i} = {result}")


# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

frameworks = ['Python', 'Numpy','Pandas','Django', 'Flask']
for framework in frameworks:
    print(framework) # Python Numpy Pandas Django Flask


# Use for loop to iterate from 0 to 100 and print only even numbers

for number in range(101):
    if number % 2 == 0:
        print(number) # 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100

# Use for loop to iterate from 0 to 100 and print only odd numbers

for number in range(101): 
    if number % 2 != 0:
        print(number) # 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99       