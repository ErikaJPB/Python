# Classes and objects

num = 10
print(type(num))  # <class 'int'> 

string = "string"
print(type(string))  # <class 'str'>

boolean = True
print(type(boolean))  # <class 'bool'>

lst = []
print(type(lst))  # <class 'list'>

tpl = ()
print(type(tpl))  # <class 'tuple'>

set = set()
print(type(set))  # <class 'set'>

dct = {}
print(type(dct))  # <class 'dict'>


# Creating a class

class Person:
    pass
print(Person)  # <class '__main__.Person'>


# Creating an object

p = Person()
print(p)  # <__main__.Person object at 0x0000023EC3E66510>


# Class constructor

class Person:
    def __init__(self, name,age ):
        self.name = name
        self.age = age


p = Person("John", 30)
print(p.name)  # John
print(p.age)  # 30
print(p)  # <__main__.Person object at 0x000002153F3B6930>

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.name = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


p = Person ('John', 'Doe', 30, 'USA', 'New York')
print(p.name)  # John
print(p.lastname)  # Doe
print(p.age)  # 30
print(p.country)  # USA
print(p.city)  # New York


# Object methods


class Person: 
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'
    

p = Person('John', 'Doe', 30, 'USA', 'New York')
print(p.person_info())  # John Doe is 30 years old. He lives in New York, USA


# Object default methods

class Person:
    def __init__(self, firstname = 'Nicolas', lastname = 'Gomez', age=250, country = 'Colombia', city = 'Bogota' ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p1 = Person()
print(p1.person_info())  # Nicolas Gomez is 250 years old. He lives in Bogota, Colombia

p2 = Person('John','Doe', 30, 'USA', 'New York')
print(p2.person_info())  # John Doe is 30 years old. He lives in New York, USA


# Method to Modify Class Default Values

class Person:
    def __init__(self, firstname = 'Nicolas', lastname = 'Gomez', age=250, country = 'Colombia', city = 'Bogota'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'
    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
print(p1.person_info())  # Nicolas Gomez is 250 years old. He lives in Bogota, Colombia
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')

p2 = Person('John', 'Doe', 30, 'USA', 'New York')
print(p2.person_info())  # John Doe is 30 years old. He lives in New York, USA
print(p1.skills)  # ['HTML', 'CSS', 'JavaScript']
print(p2.skills)  # []


# Inheritance

class Student(Person):
    pass

s1 = Student('Jose', 'Perez', 30, 'Colombia', 'Bogota')
s2 = Student('Mario', 'Gomez', 25, 'USA', 'New York')
print(s1.person_info())  # Jose Perez is 30 years old. He lives in Bogota, Colombia
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)  # ['JavaScript', 'React', 'Python']

print(s2.person_info())  # Mario Gomez is 25 years old. He lives in New York, USA
s2.add_skill('HTML')
s2.add_skill('CSS')
s2.add_skill('JavaScript')
print(s2.skills)  # ['HTML', 'CSS', 'JavaScript']


# Overriding parent method

class Student(Person):
    def __init__(self, firstname='Nicolas', lastname='Gomez', age=250, country='Colombia', city='Bogota', gender = 'male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}'


s1 = Student('Jose', 'Perez', 30, 'Colombia', 'Bogota', 'male')
s2 = Student('Maria', 'Sanchez', 25, 'USA', 'New York', 'female')

print(s1.person_info())  # Jose Perez is 30 years old. He lives in Bogota, Colombia
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)  # ['JavaScript', 'React', 'Python']

print(s2.person_info())  # Maria Sanchez is 25 years old. She lives in New York, USA
s2.add_skill('HTML')
s2.add_skill('CSS')
s2.add_skill('JavaScript')
print(s2.skills)  # ['HTML', 'CSS', 'JavaScript']

