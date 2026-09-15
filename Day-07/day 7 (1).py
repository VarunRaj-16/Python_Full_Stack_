#1. Introduction to Strings
# Defining strings
str1 = 'Hello'
str2 = "World"
str3 = '''This is a multi-line
string example.'''

print(str1)   # Hello
print(str2)   # World
print(str3)   # This is a multi-line
# string examples

#2. Operations on Strings
# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)                    # Hello World

# Repetition
print("Python! " * 3)            # Python! Python! Python!

# Indexing
text = "Python"
print(text[0])                   # P
print(text[-1])                  # n

# Slicing
print(text[0:3])                 # Pyt
print(text[:4])                  # Pyth
print(text[2:])                  # thon

# Membership
print('Pyt' in text)             # True
print('Java' not in text)        # True
