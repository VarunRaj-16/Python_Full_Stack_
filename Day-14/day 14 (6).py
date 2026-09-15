print("9. *args (Variable Length Positional Arguments)")
def ItemBillCal(*items):
    print("All items:", items)
    print("Type:", type(items))       # tuple
    print("Total:", sum(items))
ItemBillCal(100, 200, 300, 400)

print("10. Normal Parameters + *args")
def ItemBillCal2(a, b, *items):
    print("First item:", a)
    print("Second item:", b)
    print("Remaining items:", items)
ItemBillCal2(10, 20, 30, 40, 50)
