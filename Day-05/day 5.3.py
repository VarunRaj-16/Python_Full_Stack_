#6. Membership Operators
ids = [101, 102, 103]
print(101 in ids)           # True
print(105 in ids)           # False
print(105 not in ids)       # True

#7. Identity Operators
a = 10
b = 10
print(a is b)               # True  (small integers are cached)
a = [10]
b = [10]
print(a == b)               # True   (values are equal)
print(a is b)               # False  (different objects in memory)

#8. Conditional (Ternary) Operator     #(value_if_true if condition else value_if_false)
age = 20
result = "Eligible" if age >= 18 else "Not Eligible"
print(result)               # Eligible
#ex1: Weekend or Weekday
day = 6
result = "Weekend" if day >= 6 else "Weekday"
print(result)               # Weekend


