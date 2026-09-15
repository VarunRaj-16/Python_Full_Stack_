print("4. global KEYWORD")
count = 10
def update():
    global count                  # Allows modification of global variable
    count = 20
update()
print("Updated global count:", count)

print("5. nonlocal KEYWORD (Nested Functions)")
def outer():
    count = 10
    def inner():
        nonlocal count            # Modifies variable from enclosing scope
        count += 5
    inner()
    print("After inner():", count)
outer()

