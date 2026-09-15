print("13. Understanding Indentation (if inside for)")
for i in range(1, 6):     #print("--- Case 1: print outside if ---")
    if i % 2 == 0:
        print(i)
    print("end of if")          # Executes every iteration
print("end of loop")

for i in range(1, 6): #print("\n--- Case 2: print inside if ---")
    if i % 2 == 0:
        print(i)
        print("end of if")      # Executes only when even
print("end of loop")
