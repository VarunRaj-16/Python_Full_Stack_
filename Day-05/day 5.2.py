#3. Comparison (Relational) Operators
a = 100
b = 50
print(a > b)                # True
print(a == b)               # False
print(a != b)               # True
# Real-time: Voting Eligibility
age = 20
print(age >= 18)            # True

#4. Logical Operators
a = 300
b = 200
c = 100
print(a > b and a > c)      # True
# Real-time: College Admission
marks = 85
age = 19
print(marks >= 60 and age >= 18)   # True
print(a < b or a > c)       # True
# Real-time: Login
username = "admin"
email = "admin@gmail.com"
print(username == "admin" or email == "admin@gmail.com")  # True
print(not (10 > 5))         # False
# Real-time
is_logged_in = False
print(not is_logged_in)     # True

#5. Bitwise Operators
a = 10
b = 15
# Bitwise AND (&)
print(a & b)                # 10 # 1010 # 1111 # ---- # 1010
# Bitwise OR (|)
print(10 | 15)              # 15
# Bitwise XOR (^)
print(10 ^ 15)              # 5
# Bitwise NOT (~)
print(~10)                  # -11
# Left Shift (<<)
print(10 << 2)              # 40   (10 × 2²)
# Right Shift (>>)
print(10 >> 2)              # 2    (10 ÷ 2²)
