# Regular Expressions

# A RegEx is a special text string that helps find patterns in data. 


# The re module

import re

# Methods in Re Module

# 1. match()

txt = 'I love python and javascript'
match = re.match('I love', txt, re.I)
print(match) # <re.Match object; span=(0, 6), match='I love'>

match_one = re.match('I like', txt, re.I)
print(match_one) # None


# 2. search()

txt = 'I love python and javascript'
search = re.search('python', txt, re.I)

print(search) # <re.Match object; span=(7, 13), match='python'>

span = search.span()
print(span) # (7, 13)

start, end = span
print(start, end) # 7 13


# 3. findall()

txt = 'I love python and javascript languages. I recommend python for a first programming language. Python is awesome.'

matches = re.findall('python', txt, re.I)
print(matches)  # ['python', 'python', 'Python']

# without re.I we have to write the pattern differently.

matches_two = re.findall('python', txt)
print(matches_two) # ['python', 'python']

matches_three = re.findall('Python|python', txt)
print(matches_three) # ['python', 'python', 'Python']

matches_four = re.findall('[Pp]ython', txt)
print(matches_four) # ['python', 'python', 'Python']


# 4 Replacing a substring

txt = 'I love python and javascript languages. I recommend python for a first programming language. Python is awesome.'

match_replaced = re.sub(r'\bPython\b', 'JavaScript', txt, re.I)
print(match_replaced) #   I love javascript and javascript languages. I recommend javascript for a first programming language. JavaScript is awesome.

match_replaced_two = re.sub(r'\bpython\b', 'JavaScript', txt, flags=re.I)
print(match_replaced_two) # I love javascript and javascript languages. I recommend javascript for a first programming language. JavaScript is awesome.


# 5. split()

txt = 'I love python and javascript languages. I recommend python for a first programming language. Python is awesome.'

print(re.split('\n', txt)) # ['I love python and javascript languages. I recommend python for a first programming language. Python is awesome.']

print(re.split('\s', txt)) # ['I', 'love', 'python', 'and', 'javascript', 'languages.', 'I', 'recommend', 'python', 'for', 'a', 'first', 'programming', 'language.', 'Python', 'is', 'awesome.']


# Writing RegEx Patterns

regex_pattern = r'python'
txt = 'I love python and javascript languages. I recommend python for a first programming language. Python is awesome.'
matches = re.findall(regex_pattern, txt)
print(matches) # ['python', 'python']

matches_one = re.findall(r'Python|python', txt)
print(matches_one) # ['python', 'python', 'Python']

regex_pattern = r'[Pp]ython'
matches_two = re.findall(regex_pattern, txt)
print(matches_two) # ['python', 'python', 'Python']




 

