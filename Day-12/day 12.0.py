print("1. REVERSE A NUMBER")
n = int(input("Enter a number to reverse: "))
original = n
rev = 0
while n > 0:
    r = n % 10                  # Get the last digit
    rev = rev * 10 + r          # Build the reverse number
    n = n // 10                 # Remove the last digit
print(f"The reverse of {original} is: {rev}")

print("2. CHECK WHETHER A NUMBER IS PALINDROME (Using while)")
n = int(input("Enter a number to check palindrome: "))
original = n
rev = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
if original == rev:
    print("Given number is a palindrome")
else:
    print("Given number is not a palindrome")

