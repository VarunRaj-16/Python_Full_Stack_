print("4. SORT IN DESCENDING ORDER")
students = [
    ("Rahul", 80),
    ("Anil", 95),
    ("Kiran", 70),
    ("Suresh", 85)
]
result = sorted(students, key=lambda x: x[1], reverse=True)
print("Sorted by marks (descending):", result)
print("5. SORT BY NAME")
result = sorted(students, key=lambda x: x[0])
print("Sorted by name:", result)
print("6. SORT LIST OF DICTIONARIES BY MARKS")
students_dict = [
    {"name": "Rahul", "marks": 80},
    {"name": "Anil", "marks": 95},
    {"name": "Kiran", "marks": 70},
    {"name": "Suresh", "marks": 85}
]
result = sorted(students_dict, key=lambda x: x["marks"])
print("Sorted by marks:", result)

