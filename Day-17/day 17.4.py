print("11. REASSIGNMENT vs MODIFICATION")
def reassign(x):
    x = [100, 200]          # Reassignment → original not affected
    print("Inside reassign:", x)
def modify(x):
    x.append(100)           # Modification → original is affected
    print("Inside modify:", x)
a = [10, 20]
print("Original before reassign:", a)
reassign(a)
print("Original after reassign:", a)
print()
b = [10, 20]
print("Original before modify:", b)
modify(b)
print("Original after modify:", b)

