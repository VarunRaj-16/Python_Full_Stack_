print("18. MUTABLE VALUES INSIDE DICTIONARIES")
student = {"marks": [90, 85, 88]}
student["marks"].append(95)
print(student)
print("19. VALID DICTIONARY KEYS")
data = {
    101: "Ravi",
    3.14: "Pi",
    True: "Yes",
    "name": "Python",
    (1, 2): "Tuple Key"
}
print(data)