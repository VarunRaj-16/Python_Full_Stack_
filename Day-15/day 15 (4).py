print("8. PASS BY REFERENCE (Mutable Objects)")
def update_list(items):
    items.append("Laptop")
cart = ["Mobile", "Watch"]
update_list(cart)
print("Updated cart:", cart)        # Original list is modified
def update_dict(profile):
    profile["city"] = "Hyderabad"
customer = {"name": "Teja"}
update_dict(customer)
print("Updated customer:", customer)

print("9. RECURSIVE FUNCTIONS")
def print_1_to_n(n):# (1. Print numbers from 1 to N)
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")
print("1 to 5:", end=" ")
print_1_to_n(5)
print()
