print("9. continue STATEMENT")
print("Printing numbers from 1 to 5, skipping 3:")
for i in range(1, 6):
    if i == 3:
        continue  # Skip current iteration
    print(i)
print("end")
