import re
print("7. Gmail Validation")
pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
emails = [
    "jani@gmail.com",
    "user.name@gmail.com",
    "basha@yahoo.com",
    "test@gmail.org"
]
for email in emails:
    if re.match(pattern, email):
        print(f"{email} → Valid Gmail")
    else:
        print(f"{email} → Invalid Gmail")



