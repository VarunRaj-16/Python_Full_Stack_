print("3. if-elif-else STATEMENT")
n = int(input("Enter a number: "))
if n > 0:
    print(f"{n} is positive")
elif n < 0:
    print(f"{n} is negative")
else:
    print(f"{n} is neutral")

print("\n4. Finding Largest Among Three Numbers")
a = 3000
b = 200
c = 1000
if a > b and a > c:
    print(f"a = {a} is the largest number")
elif b > a and b > c:
    print(f"b = {b} is the largest number")
else:
    print(f"c = {c} is the largest number")


