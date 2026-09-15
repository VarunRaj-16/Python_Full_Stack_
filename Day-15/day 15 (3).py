print("6. LEGB RULE")
x = 100                           # Global
def outer_legb():
    x = 50                        # Enclosing
    def inner_legb():
        x = 20                    # Local
        print("LEGB finds:", x)   # Prints Local (20)
    inner_legb()
outer_legb()

print("7. PASS BY VALUE (Immutable Objects)")
def update_number(number):
    number = 100
    print("Inside Function:", number)
value = 50
update_number(value)
print("Outside Function:", value)   # Original remains unchanged

