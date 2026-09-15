##Sequence Type Conversions
# List → Tuple
numbers = [10, 20, 30]
print(tuple(numbers))     # (10, 20, 30)
# Tuple → List
numbers = (10, 20, 30)
print(list(numbers))      # [10, 20, 30]
# List → Set (removes duplicates)
numbers = [10, 20, 20, 30]
print(set(numbers))       # {10, 20, 30}
# String → List / Tuple / Set
name = "Python"
print(list(name))         # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(name))        # ('P', 'y', 't', 'h', 'o', 'n')
print(set(name))          # {'P', 'y', 't', 'h', 'o', 'n'}  (order may vary)

#Dictionary Conversion
# Correct – list of key-value pairs
data = [
    ("name", "Raju"),
    ("age", 23)
]
student = dict(data)
print(student)            # {'name': 'Raju', 'age': 23}
