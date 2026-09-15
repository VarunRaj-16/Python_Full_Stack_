import re
print("4. Character Classes")
text = "My phone is 9876543210 and email is test@gmail.com"
print("Digits \\d:", re.findall(r'\d', text))
print("Non-digits \\D:", re.findall(r'\D', text)[:10], "...")
print("Word characters \\w:", re.findall(r'\w+', text))
print("Non-word \\W:", re.findall(r'\W', text))
print("Spaces \\s:", re.findall(r'\s', text))

print("5. Anchors (^ and $)")
print("Starts with Hello:", bool(re.match(r'^Hello', "Hello World")))
print("Ends with World:", bool(re.search(r'World$', "Hello World")))
