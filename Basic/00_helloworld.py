# hello world program

print("Hello World!")


# Math Operations

print(3+2) # 5 (Addition)
print(3-2) # 1 (Subtraction)
print(3*2) # 6 (Multiplication)
print(3/2) # 1.5 (Division)
print(3//2) # 1 (Floor Division)
print(3%2) # 1 (Modulus)
print(3**2) # 9 (Exponentiation)


# Data Types

print(type("Hello World!")) # <class 'str'>
print(type(17)) # <class 'int'>
print(type(3.2)) # <class 'float'>
print(type(False)) # <class 'bool'>
print(type(1+3j)) # <class 'complex'>
print(type([1,2,3])) # <class 'list'>
print(type((1,2,3))) # <class 'tuple'> Like a list that can't be modified
print(type({1,2,3})) # <class 'set'>
print(type({1: 'one', 2: 'two', 3: 'three'})) # <class 'dict'>


'''Exercise 1
Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)
'''

print(3+4) # 7 (Addition)
print(3-4) # -1 (Subtraction)
print(3*4) # 12 (Multiplication)
print(3%4) # 3 (Modulus)
print(3/4) # 0.75 (Division)
print(3**4) # 81 (Exponentiation)
print(3//4) # 0 (Floor Division)


'''Exercise 2
Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python
'''

print("Erika")
print("Pineda")
print("Colombia")
print("I am enjoying 30 days of python")

'''Exercise 3
Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country
'''

print(type(10)) # <class 'int'>
print(type(9.8)) # <class 'float'>
print(type(3.14)) # <class 'float'>
print(type(4-4j)) # <class 'complex'>
print(type(['Asabeneh', 'Python', 'Finland'])) # <class 'list'>
print(type("Erika")) # <class 'str'>
print(type("Pineda")) # <class 'str'>
print(type("Colombia")) # <class 'str'>