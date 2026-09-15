print("10. RIGHT-ALIGNED TRIANGLE (Spaces + Stars)")
n = 4
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for j in range(i):
        print("*", end="")
    print()

