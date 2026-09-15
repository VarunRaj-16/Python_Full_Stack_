print("4. INCREASING TRIANGLE (Right-Angled)")
for i in range(1, 5):              # Rows
    for j in range(i):             # Stars = current row number
        print("*", end="")
    print()

print("5. DECREASING / INVERTED TRIANGLE")
for i in range(4, 0, -1):          # Start from 4 down to 1
    for j in range(i):
        print("*", end="")
    print()
