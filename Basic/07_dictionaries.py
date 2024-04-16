# DICTIONARIES

# Dictionaries are a collection of key-value pairs that are unordered, mutables and indexed. Dictionaries are written with curly brackets {} and they have keys and values. A key-value pair is separated by a colon. A dictionary doesn't allow duplicate keys.



# Creating a dictionary

empty_dict = {}
print(empty_dict) # {}


# Creating a dictionary with key-value pairs

dct = {
    'key 1 ': 'value 1',
    'key 2 ': 'value 2',
    'key 3 ': 'value 3',
    'key 4 ': 'value 4',
}

print(dct) # {'key 1 ': 'value 1', 'key 2 ': 'value 2', 'key 3 ': 'value 3', '

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(person) # {'first_name': 'Erika', 'last_name': 'Pineda', 'age': 280, 'country': 'Colombia', 'is_married': False, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'address': {'street': 'Space street', 'zipcode': '02210'}}



# Dictionary length

dct = {
    'key 1 ': 'value 1',
    'key 2 ': 'value 2',
    'key 3 ': 'value 3',
    'key 4 ': 'value 4',
}

print(len(dct)) # 4

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(len(person)) # 7


# Accessing items in a dictionary

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(person['last_name']) # Pineda
print(person['country']) # Colombia
print(person['skills']) # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0]) # JavaScript
#print(person['city']) # KeyError: 'city'


# get() method

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(person.get('first_name')) # Erika
print(person.get('country')) # Colombia
print(person.get('city')) # None


# Adding items to a dictionary

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

person['job_title'] = 'Python Developer'
person['skills'].append('HTML')
print(person) # {'first_name': 'Erika', 'last_name': 'Pineda', 'age': 280, 'country': 'Colombia', 'is_married': False, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML'], 'address': {'street': 'Space street', 'zipcode': '02210'}, 'job_title': 'Python Developer'}


# Modifying items in a dictionary

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

person['first_name'] = 'Lizzy'
person['age'] = 38

print(person) # {'first_name': 'Lizzy', 'last_name': 'Pineda', 'age': 38, 'country': 'Colombia', 'is_married': False, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'address': {'street': 'Space street', 'zipcode': '02210'}}


# Removing items from a dictionary

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

person.pop('first_name')
person.popitem() # removes the last item
del person['is_married']

print(person) # {'last_name': 'Pineda', 'age': 280, 'country': 'Colombia', 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']}


# Changing dictionary to a list of items

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(person.items()) # dict_items([('first_name', 'Erika'), ('last_name', 'Pineda'), ('age', 280), ('country', 'Colombia'), ('is_married', False), ('skills', ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']), ('address', {'street': 'Space street', 'zipcode': '02210'})])


# Clearing a dictionary

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

person.clear()
print(person) # {}


# Deleting a dictionary

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

del person
# print(person) # NameError: name 'person' is not defined


# Copying a dictionary

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

copy_person = person.copy() 
print(copy_person) # {'first_name': 'Erika', 'last_name': 'Pineda', 'age': 280, 'country': 'Colombia', 'is_married': False, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'address': {'street': 'Space street', 'zipcode': '02210'}}


# Getting dictionary keys as a list

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(person.keys()) # dict_keys(['first_name', 'last_name', 'age', 'country', 'is_married', 'skills', 'address'])


# Getting dictionary values as a list

person = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'age': 280,
    'country': 'Colombia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(person.values()) # dict_values(['Erika', 'Pineda', 280, 'Colombia', False, ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], {'street': 'Space street', 'zipcode': '02210'}])


# Exercises

# Create an empty dictionary called dog

dog = {}


# Add name, color, breed, legs, age to the dog dictionary

dog['name'] = 'Doggy'
dog['color'] = 'Black'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 10

print(dog) # {'name': 'Doggy', 'color': 'Black', 'breed': 'Labrador', 'legs': 4, 'age': 10}


# Create a student dictionary and add first_name, last_name, age, skills, country, city and address as keys for the dictionary

student = {
    'first_name': 'Erika',
    'last_name': 'Pineda',
    'gender' : 'female',
    'age': 280,
    'marital status': 'single',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country': 'Colombia',
    'city': 'Bogota',
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print(student) # {'first_name': 'Erika', 'last_name': 'Pineda', 'age': 280, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'country': 'Colombia', 'city': 'Bogota', 'address': {'street': 'Space street', 'zipcode': '02210'}}

print(len(student)) # 9


# Get the value of skills and check the data type, it should be a list

print(student['skills']) # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(type(student['skills'])) # <class 'list'>


# Modify the skills values by adding one or two skills

student['skills'].append('HTML')
student['skills'].append('CSS')

print(student) # {'first_name': 'Erika', 'last_name': 'Pineda', 'age': 280, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML', 'CSS'], 'country': 'Colombia', 'city': 'Bogota', 'address': {'street': 'Space street', 'zipcode': '02210'}}


# Get the dictionary keys as a list

print(student.keys()) # dict_keys(['first_name', 'last_name', 'age', 'skills', 'country', 'city', 'address'])


# Get the dictionary values as a list

print(student.values()) # dict_values(['Erika', 'Pineda', 280, ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML', 'CSS'], 'Colombia', 'Bogota', {'street': 'Space street', 'zipcode': '02210'}])


# Change the dictionary to a list of tuples using items() method

print(student.items()) # dict_items([('first_name', 'Erika'), ('last_name', 'Pineda'), ('age', 280), ('skills', ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML', 'CSS']), ('country', 'Colombia'), ('city', 'Bogota'), ('address', {'street': 'Space street', 'zipcode': '02210'})])


# Delete one of the items in the dictionary

student.pop('city')
print(student) # {'first_name': 'Erika', 'last_name': 'Pineda', 'age': 280, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML', 'CSS'], 'country': 'Colombia', 'address': {'street': 'Space street', 'zipcode': '02210'}}


# Delete one of the dictionaries

del student
# print(student) # NameError: name 'student' is not defined