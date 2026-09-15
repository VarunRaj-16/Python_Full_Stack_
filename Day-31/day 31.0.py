# DAY 32 - REGULAR EXPRESSIONS IN PYTHON
import re
print("1. match(), search(), fullmatch(), findall()")
text = "abaaababcc"
print("match():", re.match(r'ab', text))          # Start of string
print("search():", re.search(r'ab', text))        # Anywhere
print("fullmatch():", re.fullmatch(r'abaaababcc', text))
print("findall():", re.findall(r'ab', text))

print("2. split()")
text = "apple,banana;orange-grape"
result = re.split(r'\W+', text)
print(result)       # ['apple', 'banana', 'orange', 'grape']

print("3. sub() and subn()")
text = "Phone: 123-456-7890"
print("sub():", re.sub(r'\d', '#', text))
print("subn():", re.subn(r'\d', '#', text))

