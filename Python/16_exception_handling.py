# Exception Handling

try : 
    print(10 + '5') # This will give error because we can't add string to integer
except:
    print('Something went wrong')



try: 
    name = input('Enter your name:')
    year_born = input('Enter the year you were born:')
    age = 2024 - int(year_born)
    print(f'Your name is {name} and your age is {age}') #38
except:
    print('Something went wrong')


try: 
    name = input('Enter your name:')
    year_born = input('Enter the year you were born:')
    age = 2024 - (year_born)
    print(f'Your name is {name} and your age is {age}') 
except:
    print('Something went wrong') # This will print error because we can't subtract string from integer


    
try: 
    name = input('Enter your name:')
    year_born = input('Enter the year you were born:')
    age = 2024 - (year_born)
    print(f'Your name is {name} and your age is {age}') 
except TypeError:
    print("Type error occurred") # Type error occurred
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("Zero eivision Error occurred")


try: 
    name = input('Enter your name:')
    year_born = input('Enter the year you were born:')
    age = 2024 - int(year_born)
    print(f'Your name is {name} and your age is {age}')
except TypeError:
    print("Type error occurred") 
except ValueError:
    print("Value error occurred")
except ZeroDivisionError:
    print("Zero eivision Error occurred")
else: 
    print('I usually run with the try block')
finally:
    print('I always run')




# Packing and unpacking arguments in python

# we use two operators: * (for tuples) and **(for dictionaries)

def sum_of_five(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five(lst)) #Type Error, missing 4 required positional arguments: 'b', 'c', 'd' and 'e'

lst = [1, 2, 3, 4, 5]
print(sum_of_five(*lst)) # 15


# we can also unpacked in the range built-in function that expects a start and end value

numbers = range(2,7)
print(list(numbers)) # [2, 3, 4, 5, 6] 
args = [2,7]
numbers = range(*args)
print(list(numbers)) # [2, 3, 4, 5, 6]


# A list or a tuple can also be unpacked like this:

countries = ['Colombia', 'Mexico', 'Argentina', 'Brasil', 'Peru']
co, mx, ar, *rest = countries
print(co, mx, ar, rest) # Colombia Mexico Argentina ['Brasil', 'Peru']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
one, *middle, last = numbers
print(one, middle, last) # 1 [2, 3, 4, 5, 6, 7, 8, 9] 10


# Unpacking dictionaries

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. She is {age} years old.'

dct = {'name': 'Erika', 'country': 'Colombia', 'city': 'Bogota', 'age': 38}

print(unpacking_person_info(**dct)) # Erika lives in Colombia, Bogota. She is 38 years old.


# Packing

def sum_all(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(sum_all(1, 2, 3, 4, 5)) # 15


# Packing dictionaries

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name='Erika', country='Colombia', city='Bogota', age=38))


# Spreading

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst_one = ['Colombia', 'Mexico', 'Argentina']
country_lst_two = ['Brasil', 'Peru']
latam_countries = [*country_lst_one, *country_lst_two]
print(latam_countries) # ['Colombia', 'Mexico', 'Argentina', 'Brasil', 'Peru']


# Enumerate

for index, item in enumerate([20,30,40]):
    print(index, item) # 0 20 1 30 2 40

for index, i in enumerate(latam_countries):
    if i == 'Colombia': 
        print(f'The country {i} has been found at index {index}')


# Zip
# Combine list when looping through them

fruits = ['banana', 'orange', 'strawberry', 'mango', 'blueberry', 'lemon']
vegetables = ['tomato', 'cucumber', 'onion', 'potato', 'carrot']

fruits_and_vegetables = []
for fruit, vegetable in zip(fruits, vegetables):
    fruits_and_vegetables.append(({'fruit': fruit, "vegetable": vegetable}))

print(fruits_and_vegetables)

