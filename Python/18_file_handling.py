# File handling

# We store data in different file formats. File handling allows us to create, read, update and delete files. 

# open('filename', mode) # mode (r, a, w, x, t, b) could be to read, write, update

'''

"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

'''

# Opening files for reading

f = open('./Basic/files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./Basic/files/reading_file_example.txt' mode='r' encoding='cp1252'>

f = open('./Basic/files/reading_file_example.txt')
txt = f.read()
print(type(txt)) # <class 'str'>
print(txt) # This is an example to show how to open a file and read.This is the second line of the text.I love python
f.close()

f = open('./Basic/files/reading_file_example.txt')  
txt = f.read(10)
print(type(txt)) # <class 'str'>
print(txt) # This is an 
f.close()

# readline() 

f = open('./Basic/files/reading_file_example.txt')
line = f.readline()
print(type(line)) # <class 'str'>
print(line) # This is an example to show how to open a file and read.
f.close()


# readlines()

f = open('./Basic/files/reading_file_example.txt')
lines = f.readlines()
print(type(lines)) # <class 'list'>
print(lines) # ['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
f.close()


# splitlines()

f = open('./Basic/files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines)) # <class 'list'>
print(lines) # ['This is an example to show how to open a file and read.', 'This is the second line of the text.']
f.close()


# Opening files for writing and updating

'''
To write to an existing file we must add a mode as parameter to the open() function:

"a" - append - will append to the end of the file, if the file does not it creates a new file.
"w" - write - will overwrite any existing content, if the file does not exist it creates.

'''

with open('./Basic/files/reading_file_example.txt', 'a') as f:
    f.write('This text has to be appended at the end.')

with open('./Basic/files/writing_file_example.txt', 'w') as f:
    f.write('This text will be written in a newly created file')



# Deleting files

import os

# if os.path.exists('./Basic/files/example.txt'):
#     os.remove('./Basic/files/example.txt')
# else: 
#     print('The file does not exist')


# File Types

# Json Files

# dictionary
person_dct = {
    "name": "Erika", 
    "country": "Colombia",
    "city" : "Bogota",
    "skills": ["JavaScript", "React", "Python"]
}

# json
person_json = "{'name':'Erika', 'country':'Colombia', 'city':'Bogota', 'skills': ['JavaScript', 'React', 'Python']}"

person_json = '''{
    "name": "Erika",
    "country": "Colombia",
    "city" : "Bogota",
    "skills": ["JavaScript", "React", "Python"]
}'''

# changing json to dictionary

import json

person_json = '''{
    "name": "Erika",
    "country": "Colombia",
    "city" : "Bogota",
    "skills": ["JavaScript", "React", "Python"]
}'''

person_dct = json.loads(person_json)
print(type(person_dct)) # <class 'dict'>
print(person_dct) # {'name': 'Erika', 'country': 'Colombia', 'city': 'Bogota', 'skills': ['JavaScript', 'React', 'Python']}
print(person_dct["name"]) # Erika


# changing dictionary to json

import json

person = {
    "name": "Erika",
    "country": "Colombia",
    "city" : "Bogota",
    "skills": ["JavaScript", "React", "Python"]
}

person_json = json.dumps(person, indent=4)
print(type(person_json)) # <class 'str'>
print(person_json) # {'name': 'Erika', 'country': 'Colombia', 'city': 'Bogota', 'skills': ['JavaScript', 'React', 'Python']}


# saving as json file

import json

person = {
    "name": "Erika",
    "country": "Colombia",
    "city" : "Bogota",
    "skills": ["JavaScript", "React", "Python"]
}

with open('./Basic/files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)



# csv files

import csv

with open('./Basic/files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are : {",".join(row)}')
            line_count += 1
        else:
            print(
                 f'\t{row[0]} is a student. She lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
            
  

# xlsx files

# Using pip install xlrd package. xlrd is a library for reading Excel files.


# xml files

import xml.etree.ElementTree as ET

tree = ET.parse('./Basic/files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)

for child in root:
    print('field: ', child.tag, child.text)
