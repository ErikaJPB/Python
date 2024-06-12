# SETS

# A set is a collection of items which is unordered and unindexed. Sets are written with curly brackets {}. A set doesn't allow duplicate items.

# Creating a set

# Sintax

st = set()

st = {'item 1', 'item 2', 'item 3', 'item 4', 'item 5'}

fruits = {'banana', 'orange', 'mango', 'lemon'} # set of fruits

print(len(fruits)) # 4


# Checking items in a set

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('banana' in fruits) # True
print('apple' in fruits) # False


# Adding items to a set

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('apple')
print(fruits) # {'orange', 'mango', 'lemon', 'banana', 'apple'}


# Adding multiple items to a set

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.update(['apple', 'grapes'])
print(fruits) # {'orange', 'mango', 'lemon', 'banana', 'apple', 'grapes'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
more_fruits = ['apple', 'grapes', 'lime', 'kiwi']
fruits.update(more_fruits)
print(fruits) # {'orange', 'mango', 'lemon', 'banana', 'apple', 'grapes', 'kiwi', 'lime'}


# Removing items from a set

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.remove('banana')
print(fruits) # {'orange', 'mango', 'lemon'}

fruits.pop() # removes a random item
print(fruits) # {'orange', 'lemon'}


# Clearing items in a set

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()


# Deleting a set

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
#print(fruits) # NameError: name 'fruits' is not defined


# Convertin a list to a set

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = set(fruits)
print(fruits) # {'orange', 'mango', 'lemon', 'banana'}


# Joining sets

fruits = {'banana', 'orange', 'mango', 'lemon'}
more_fruits = {'apple', 'grapes', 'kiwi', 'orange'}
all_fruits = fruits.union(more_fruits)
print(all_fruits) # {'orange', 'mango', 'lemon', 'banana', 'apple', 'grapes', 'kiwi'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
more_fruits = {'apple', 'grapes', 'kiwi', 'orange'}
fruits.update(more_fruits)
print(fruits) # {'orange', 'mango', 'lemon', 'banana', 'apple', 'grapes', 'kiwi'}


# Finding intersection items in sets

fruits = {'banana', 'orange', 'mango', 'lemon'}
more_fruits = {'apple', 'grapes', 'kiwi', 'orange'}
common_fruits = fruits.intersection(more_fruits)
print(common_fruits) # {'orange'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
numbers = whole_numbers.intersection(even_numbers)
print(numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon)) # {'o', 'n'}


# Checking a subset and a superset

fruits = {'banana', 'orange', 'mango', 'lemon'}
more_fruits = {'banana', 'orange'}
print(more_fruits.issubset(fruits)) # True
print(fruits.issuperset(more_fruits)) # True

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(even_numbers.issubset(whole_numbers)) # True
print(whole_numbers.issuperset(even_numbers)) # True


# Finding the difference between two sets

fruits = {'banana', 'orange', 'mango', 'lemon'}
more_fruits = {'banana', 'orange'}
print(fruits.difference(more_fruits)) # {'mango', 'lemon'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers)) # {1, 3, 5, 7, 9}


# Finding the symmetric difference between two sets

fruits = {'banana', 'orange', 'mango', 'lemon'}
more_fruits = {'banana', 'orange'}
print(more_fruits.symmetric_difference(fruits)) # {'mango', 'lemon'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.symmetric_difference(even_numbers)) # {1, 3, 5, 7, 9}


# Joining sets 

# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.

fruits = {'banana', 'orange', 'mango', 'lemon'}
more_fruits = {'banana', 'orange'}
print(more_fruits.isdisjoint(fruits)) # False

numbers = {1, 2, 3, 4, 5}
more_numbers = {6, 7, 8, 9, 10}
print(numbers.isdisjoint(more_numbers)) # True, because no item is common in both sets

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}
