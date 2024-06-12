# CONDITIONALS

# if condition
    # this part of the code runs for truthy conditions

a = 3

if a > 0: 
    print("a is positive number") # a is positive number


# if else condition 

a = 3 

if a < 0:
    print ("a is negative number") # this will not run because is false
else:
    print ("a is positive number") # a is positive number


# if elif else condition

a = 0
if a > 0:
    print('a is a positive number') # this will not run because is false
elif a < 0:
    print('a is a negative number') # this will not run because is false
else:
    print('a is zero') # a is zero


# Nested if else condition
# we can avoid nested conditions by using logical operator and.
a = 0

if a > 0:
    if a % 2 == 0:
        print('a is a positive and even integer') # this will not run because is false
    else:
        print('a is a positive number') # this will not run because is false
elif a == 0:
    print('a is zero')  # a is zero
else:
    print('a is a negative number') # this will not run because is false


# if condition and logical operators.

# and operator

a = 0

if a > 0 and a % 2 == 0:
    print('a is an even and positive integer') # this will not run because is false
elif a > 0 and a % 2 != 0:
    print('a is a positive integer') # this will not run because is false
elif a == 0:
    print('a is zero') # a is zero
else:
    print('a is a negative number')


# or operator

user = 'James'
access_level = 3
if  user == 'admin' or access_level >= 4:
    print('Access granted!') # this will not run because is false
else : 
    print('Access denied!') # Access denied!


# Exercises

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

'''
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
'''

age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18 - age} more years to learn to drive.')

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

'''
Enter your age: 30
You are 5 years older than me.
'''


my_age = 30
your_age = int(input('Enter your age: '))

if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f'You are {age_difference} year older than me.')
    else:
        print(f'You are {age_difference} years older than me.')
elif my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f'I am {age_difference} year older than you.')
    else:
        print(f'I am {age_difference} years older than you.')
else:
    print("We are the same age!")


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

'''Enter number one: 4
Enter number two: 3
4 is greater than 3'''

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')


