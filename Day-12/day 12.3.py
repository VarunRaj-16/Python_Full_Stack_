print("7. FACTORIAL OF A NUMBER")
n = int(input("Enter a number to find factorial: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial:", fact)
print("8. ARMSTRONG NUMBER (3-digit)")
n = int(input("Enter a 3-digit number to check Armstrong: "))
original = n
total = 0
while n > 0:
    r = n % 10
    total = total + r ** 3      # Cube of the digit
    n = n // 10
if original == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
