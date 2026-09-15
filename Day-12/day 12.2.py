print("5. FACTORS OF A NUMBER")
n = int(input("Enter a number to find factors: "))
print(f"Factors of {n} are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
print("6. COUNT NUMBER OF FACTORS")
n = int(input("Enter a number to count factors: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
print("Number of factors:", count)
