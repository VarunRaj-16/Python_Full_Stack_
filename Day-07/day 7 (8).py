csv_data = "a,b,c"
lines = "Hello\nWorld"
words = ["Hello", "World"]
dessert = "apple-pie"
# partition() → Splits into a 3-part tuple at the first occurrence of separator
print("partition('-'):", dessert.partition("-"))

# rpartition() → Splits into a 3-part tuple at the last occurrence of separator
print("rpartition('-'):", dessert.rpartition("-"))
print("\n" + "=" * 60)
print("9. WHITESPACE & TRIMMING METHODS")
print("=" * 60)
messy1 = "   hello   "
messy2 = "---hello"
messy3 = "hello---"

# strip() → Removes leading and trailing characters (default is whitespace)
print("strip():", messy1.strip())

# lstrip() → Removes leading (left side) characters
print("lstrip('-'):", messy2.lstrip("-"))

# rstrip() → Removes trailing (right side) characters
print("rstrip('-'):", messy3.rstrip("-"))
print("\n" + "=" * 60)
print("10. ENCODING & DECODING METHODS")
print("=" * 60)
unicode_text = "Hello नमस्ते 你好 café 🙂"

# encode() → Converts a string into bytes using the specified encoding
encoded_text = unicode_text.encode("utf-8")
print("Encoded (utf-8):", encoded_text)




