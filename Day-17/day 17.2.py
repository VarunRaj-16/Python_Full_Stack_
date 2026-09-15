print("7. SORT DICTIONARIES IN DESCENDING ORDER")
students_dict = [
    {"name": "Rahul", "marks": 80},
    {"name": "Anil", "marks": 95},
    {"name": "Kiran", "marks": 70},
    {"name": "Suresh", "marks": 85}
]
result = sorted(students_dict, key=lambda x: x["marks"], reverse=True)
print("Descending by marks:", result)
print("8. SORT STRINGS BY LENGTH")
names = ["Ravi", "Alexander", "John", "Sai"]
result = sorted(names, key=lambda x: len(x))
print("Sorted by length (ascending):", result)
result = sorted(names, key=lambda x: len(x), reverse=True)
print("Sorted by length (descending):", result)
