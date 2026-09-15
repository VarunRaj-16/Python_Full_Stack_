msg1 = "hello"
msg2 = "HELLO"
msg3 = "python programming"
msg4 = "PyThOn"
msg5 = "STRAẞE"
# swapcase() → Swaps uppercase to lowercase and vice-versa
print("swapcase():", msg4.swapcase())

# casefold() → Stronger version of lower() (handles special characters better)
print("casefold():", msg5.casefold())
print("\n" + "=" * 60)
print("4. ALIGNMENT & FORMATTING METHODS")
print("=" * 60)
word = "python"
short = "py"
number = "42"

# center() → Centers the string within the given width using a fill character
print("center():", word.center(12, "*"))

# ljust() → Left-aligns the string and fills the remaining space on the right
print("ljust():", short.ljust(8, "-"))

# rjust() → Right-aligns the string and fills the remaining space on the left
print("rjust():", short.rjust(8, "-"))

# zfill() → Pads the string with zeros on the left to reach the given width
print("zfill():", number.zfill(6))
print("\n" + "=" * 60)
print("5. SEARCH & FIND METHODS")
print("=" * 60)
sentence = "hello world"
fruit = "banana"

# find() → Returns the lowest index of the substring (returns -1 if not found)
print("find('l'):", sentence.find("l"))

# rfind() → Returns the highest index of the substring (searches from right)
print("rfind('l'):", sentence.rfind("l"))

# index() → Same as find(), but raises ValueError if substring is not found
print("index('e'):", sentence.index("e"))

# rindex() → Same as rfind(), but raises ValueError if substring is not found
print("rindex('l'):", sentence.rindex("l"))
