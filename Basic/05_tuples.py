# TUPLES

# A tuple is a collection of different data types which is ordered and unmodifiable. Tuples are written with round brackets ().

# Creating a tuple

# Sintax

tpl = tuple()
tpl = ()

fruits = ('banana', 'orange', 'mango', 'lemon') # tuple of fruits

print(len(fruits)) # 4

# Accessing tuple items

# Positive indexing

first_fruit = fruits[0] 
print(first_fruit) # banana
second_fruit = fruits[1]
print(second_fruit) # orange
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit) # lemon

# Negative indexing

first_fruit = fruits[-4]
print(first_fruit) # banana
second_fruit = fruits[-3]
print(second_fruit) # orange
last_fruit = fruits[-1]
print(last_fruit) # lemon
second_last = fruits[-2]
print(second_last) # mango


# Slicing tuples

# Range of positive indexes

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]
print(all_fruits) # ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:] # it will return all the fruits
print(all_fruits) # ('banana', 'orange', 'mango', 'lemon')
orange_and_mango = fruits[1:3]
print(orange_and_mango) # ('orange', 'mango')

# Range of negative indexes

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]
print(all_fruits) # ('banana', 'orange', 'mango', 'lemon')
orange_and_mango = fruits[-3:-1]
print(orange_and_mango) # ('orange', 'mango')


# Changing tuples to lists

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits) # ['apple', 'orange', 'mango', 'lemon']

fruits = tuple(fruits)
print(fruits) # ('apple', 'orange', 'mango', 'lemon')


# Checking an item in a tuple

fruits = ('banana', 'orange', 'mango', 'lemon')

print('banana' in fruits) # True
print('apple' in fruits) # False

#fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment


# Joining Tuples

fruits1 = ('banana', 'orange', 'mango', 'lemon')
fruits2 = ('apple', 'grapes')
fruits3 = fruits1 + fruits2
print(fruits3) # ('banana', 'orange', 'mango', 'lemon', 'apple', 'grapes')


# Deleting Tuples

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
# print(fruits) # NameError: name 'fruits' is not defined