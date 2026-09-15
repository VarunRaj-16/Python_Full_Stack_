print("8. CONTINUOUS NUMBER PATTERN")
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num = num + 1
    print()

print("9. NUMBERS STARTING FROM 0")
for i in range(4):
    for j in range(i + 1):
        print(j, end="")
    print()


