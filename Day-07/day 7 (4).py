# len() → Returns the total number of characters in the string
sample_text="Varun"
print("Length:", len(sample_text))

# max() → Returns the character with the highest ASCII value
print("Max character:", max("abcXYZ"))

# min() → Returns the character with the lowest ASCII value
print("Min character:", min("abcXYZ"))

# sorted() → Returns a sorted list of all characters
print("Sorted characters:", sorted("python"))

# ord() → Converts a character to its ASCII / Unicode code point
print("ASCII of 'A':", ord('A'))

# chr() → Converts an ASCII / Unicode code point back to a character
print("Character of 97:", chr(97))
print("\n" + "=" * 60)
print("3. CASE CONVERSION METHODS")
print("=" * 60)
msg1 = "hello"
msg2 = "HELLO"
msg3 = "python programming"
msg4 = "PyThOn"
msg5 = "STRAẞE"

# upper() → Converts all characters to uppercase
print("upper():", msg1.upper())

# lower() → Converts all characters to lowercase
print("lower():", msg2.lower())

# capitalize() → Converts only the first character to uppercase
print("capitalize():", msg3.capitalize())

# title() → Capitalizes the first letter of every word
print("title():", msg3.title())

