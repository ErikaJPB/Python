#  lISTS

# A list is a collection of different data types which is ordered and modifiable.

# Creating a list

# Sintax

lst = list()
lst = []


# Example

empty_list = list()
print(empty_list)
empty_list = []
print(empty_list)
print(len(empty_list))


# Lists with initial values

fruits = ['banana', 'orange', 'mango', 'lemon'] # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']  # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] # list of Nordic countries

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# List with multiple data types

lst = [1, 2, 3, 'banana', 'apple', 4, 5]
print(lst)



# Accessing list items using positive indexing

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] 
print(first_fruit) # banana
second_fruit = fruits[1] 
print(second_fruit) # orange
last_fruit = fruits[3] 
print(last_fruit) # lemon

last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit) # lemon


# Accessing list items using negative indexing

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
print(first_fruit)  # banana
last_fruit = fruits[-1] 
print(last_fruit) # lemon
second_last = fruits[-2] 
print(second_last) # lemon


# Unpacking list items

list_of_items = ['item 1 ', 'item 2', 'item 3', 'item 4', 'item 5']
first_item, second_item, third_item, *rest = list_of_items
print(first_item) # item 1
print(second_item) # item 2
print(third_item) # item 3
print(rest) # ['item 4', 'item 5']


# Slicing items from a list

# positive slicing

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
print(all_fruits) # ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:] # it will return all the fruits
print(all_fruits) # ['banana', 'orange', 'mango', 'lemon']
orange_and_mango = fruits[1:3]
print(orange_and_mango) # ['orange', 'mango']
orange_mango_lemon = fruits[1:]
print(orange_mango_lemon) # ['orange', 'mango', 'lemon']

# negative slicing

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]
print(all_fruits) # ['banana', 'orange', 'mango', 'lemon']
orange_and_mango = fruits[-3:-1]
print(orange_and_mango) # ['orange', 'mango']
orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon) # ['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1]
print(reverse_fruits) # ['lemon', 'mango', 'orange', 'banana']


# Modifying lists

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist) # True
does_exist = 'apple' in fruits
print(does_exist) # False


# Adding items to a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.insert(2, 'strawberry')
print(fruits) # ['banana', 'orange', 'strawberry', 'mango', 'lemon', 'apple']
fruits.insert(4, 'kiwi')
print(fruits) # ['banana', 'orange', 'strawberry', 'mango', 'kiwi', 'lemon', 'apple']

# Removing items from a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits) # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits) # ['orange', 'mango']
fruits.pop(0)
print(fruits) # ['mango']


# Removing items from a list using del

fruits = ['banana', 'orange', 'lemon', 'kiwi', 'mango', 'lemon']
del fruits[0]
print(fruits) # ['orange', 'lemon', 'kiwi', 'mango', 'lemon']
del fruits[1]
print(fruits) # ['orange', 'kiwi', 'mango', 'lemon']
del fruits[1:3] # it will delete items from index 1 to 2    
print(fruits) # ['orange', 'lemon']

# Clearing the list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits) # []


# Copying a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy) # ['banana', 'orange', 'mango', 'lemon']


# Joining lists

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']


# Joining lists using extend

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits.extend(vegetables)
print(fruits) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
num1 = [0, 1, 2, 3, 4]
num2 = [5, 6, 7, 8, 9]
num1.extend(num2)
print(num1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Counting items in a list

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
count = fruits.count('banana')
print(count) # 2


# Finding index of an item

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
index = fruits.index('orange')
print(index) # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
index = ages.index(24)
print(index) # 2, the first occurrence of 24 is at index 2


# Reversing a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']


# Sorting a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) # ['banana', 'lemon', 'mango', 'orange']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) # [19, 22, 24, 24, 24, 25, 25, 26]
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort(reverse=True)
print(ages) # [26, 25, 25, 24, 24, 24, 22, 19]


