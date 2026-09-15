sentence = "hello world"
fruit = "banana"
# count() → Counts how many times a substring appears
print("count('a'):", fruit.count("a"))
print("\n" + "=" * 60)
print("6. STRING TESTING METHODS (Boolean Results)")
print("=" * 60)
alpha_str = "Hello"
alnum_str = "abc123"
lower_str = "hello"
upper_str = "HELLO"
space_str = "   "
title_str = "Hello World"
id_str = "variable1"
num_str = "123"

# startswith() → Checks whether the string starts with the given substring
print("startswith('He'):", alpha_str.startswith("He"))

# endswith() → Checks whether the string ends with the given substring
print("endswith('lo'):", alpha_str.endswith("lo"))

# isalpha() → Returns True if all characters are alphabets
print("isalpha():", alpha_str.isalpha())

# isalnum() → Returns True if all characters are alphanumeric (letters + digits)
print("isalnum():", alnum_str.isalnum())

# islower() → Returns True if all characters are lowercase
print("islower():", lower_str.islower())

# isupper() → Returns True if all characters are uppercase
print("isupper():", upper_str.isupper())

# isspace() → Returns True if the string contains only whitespace
print("isspace():", space_str.isspace())

# istitle() → Returns True if the string follows title case
print("istitle():", title_str.istitle())

# isidentifier() → Checks if the string is a valid Python identifier
print("isidentifier():", id_str.isidentifier())
