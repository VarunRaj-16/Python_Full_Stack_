print("15. ALPHABET PATTERN (A AB ABC ABCD)")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")   # 65 = 'A', 66 = 'B', ...
    print()
