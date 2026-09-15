#Type Casting
#1. Implicit Type Casting
a = 10        # int
b = 12.5      # float
print(a + b)  # 22.5   (10 is converted to 10.0)
a = True
b = 5
print(a + b)  # 6   (True is treated as 1)

#2. Explicit Type Casting
#Integer Conversion
Pythona = 10
print(a, type(a))          # 10 <class 'int'>
b = float(a)
print(b, type(b))          # 10.0 <class 'float'>
c = str(a)
print(c, type(c))          # 10 <class 'str'>
d = bool(a)
print(d, type(d))          # True <class 'bool'>

#Float Conversion
a = 10.5
print(int(a))     # 10   (truncates decimal, does not round)
print(str(a))     # '10.5'
print(bool(a))    # True

#String Conversion
x = "10"
print(int(x))     # 10
print(float(x))   # 10.0
print(bool(x))    # True  (non-empty string)

#Boolean Conversion
print(int(True))    # 1
print(int(False))   # 0
print(float(True))  # 1.0
print(str(False))   # False

