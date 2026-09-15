alpha_str = "Hello"
alnum_str = "abc123"
lower_str = "hello"
upper_str = "HELLO"
space_str = "   "
title_str = "Hello World"
id_str = "variable1"
num_str = "123"
# isdecimal() → Most strict: only base-10 digits
print("isdecimal():", num_str.isdecimal())

# isdigit() → Allows digits including superscripts
print("isdigit():", num_str.isdigit())

# isnumeric() → Most flexible: digits, fractions, Roman numerals, etc.
print("isnumeric():", num_str.isnumeric())
print("\n" + "=" * 60)
print("7. REPLACE & MODIFY METHODS")
print("=" * 60)
fruit2 = "apple"
code = "python"

# replace() → Replaces all occurrences of a substring with another
print("replace('p', 'b'):", fruit2.replace("p", "b"))

# maketrans() → Creates a translation table
# translate() → Applies the translation table to replace characters
trans_table = str.maketrans("aon", "%#5")
print("maketrans + translate:", code.translate(trans_table))
print("\n" + "=" * 60)
print("8. SPLITTING & JOINING METHODS")
print("=" * 60)
csv_data = "a,b,c"
lines = "Hello\nWorld"
words = ["Hello", "World"]
dessert = "apple-pie"

# split() → Splits the string into a list using the given separator
print("split(','):", csv_data.split(","))

# rsplit() → Splits from the right side
print("rsplit(',', 1):", csv_data.rsplit(",", 1))

# splitlines() → Splits the string at line boundaries (\n)
print("splitlines():", lines.splitlines())

# join() → Joins elements of an iterable using the string as separator
print("join():", " ".join(words))
