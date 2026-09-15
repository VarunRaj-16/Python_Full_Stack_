print("10. break vs continue")
print("--- Using continue (skips only 3) ---")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print("--- Using break (stops at 3) ---")
for i in range(1, 6):
    if i == 3:
        break                   # Exit the entire loop
    print(i)