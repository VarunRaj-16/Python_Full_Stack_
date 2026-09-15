#3. Built-in String Functions

text = "Hello World"

# 1. len() → length of the string

print(len(text))                 # 11

# 2. max() / min() → based on ASCII values

print(max("abcXYZ"))             # 'c'

print(min("abcXYZ"))             # 'X'

# 3. sorted() → returns a sorted list of characters

print(sorted("python"))          # ['h', 'n', 'o', 'p', 't', 'y']

# 4. ord() / chr() → character ↔ ASCII

print(ord('A'))                  # 65

print(chr(97))                   # 'a'
