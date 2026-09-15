# DAY 17 - LAMBDA + sorted() + CALL BY OBJECT REFERENCE
print("1. BASIC LAMBDA FUNCTION")
# Normal function
def square(x):
    return x * x
print("Normal function:", square(5))
# Same using lambda
square_lambda = lambda x: x * x
print("Lambda function:", square_lambda(5))
print("2. sorted() WITH LAMBDA")
numbers = [50, 10, 40, 20, 30]
print("Normal sorted:", sorted(numbers))
print("3. SORT LIST OF TUPLES BY SECOND VALUE (MARKS)")
students = [
    ("Rahul", 80),
    ("Anil", 95),
    ("Kiran", 70),
    ("Suresh", 85)
]
result = sorted(students, key=lambda x: x[1])
print("Sorted by marks (ascending):", result)
