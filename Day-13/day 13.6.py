print("11. PYRAMID PATTERN")
n = 4
for i in range(1, n + 1):# Spaces
    for j in range(n - i):
        print(" ", end="")# Stars (odd numbers: 1, 3, 5, 7...)
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print("12. HOLLOW SQUARE")
n = 4
for i in range(n):
    for j in range(n):# Print * on borders only
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


