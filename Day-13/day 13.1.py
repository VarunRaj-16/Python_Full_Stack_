print("2. SQUARE PATTERN (using end='')")
for i in range(1, 5):              # 4 rows
    for j in range(1, 5):          # 4 columns
        print("*", end="")
    print() # Move to next line after each row

print("3. RECTANGLE PATTERN (3 rows × 5 columns)")
for i in range(1, 4):              # 3 rows
    for j in range(1, 6):          # 5 columns
        print("*", end="")
    print()
