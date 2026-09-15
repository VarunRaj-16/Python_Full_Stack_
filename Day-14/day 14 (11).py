print("20. REAL-TIME EXAMPLES")# Even or Odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("10 is", check_even_odd(10))# Discount Calculation
def calculate_discount(amount):
    if amount >= 5000:
        discount = amount * 0.20
    elif amount >= 2000:
        discount = amount * 0.10
    else:
        discount = 0
    return discount
print("Discount on 6000:", calculate_discount(6000))# Login Function
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid username or password"
print(login("admin", "1234"))# Student Result System
def calculate_total(m1, m2, m3):
    return m1 + m2 + m3
def calculate_average(total):
    return total / 3
def check_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"
marks1, marks2, marks3 = 80, 70, 90
total = calculate_total(marks1, marks2, marks3)
average = calculate_average(total)
result = check_result(average)
print("Total:", total)
print("Average:", average)
print("Result:", result)

