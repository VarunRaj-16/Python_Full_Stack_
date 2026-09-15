print("6. NUMBER TRIANGLE (1 12 123 1234)")
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("7. SAME NUMBER IN EACH ROW (1 22 333 4444)")
for i in range(1, 5):
    for j in range(i):
        print(i, end="")           # Print row number, not column
    print()
