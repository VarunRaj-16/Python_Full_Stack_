# DAY 15 - SCOPE, RECURSION, LAMBDA, FILTER, MAP, REDUCE
print("1. LOCAL SCOPE")
def student():
    name = "Varun"                 # Local variable
    print("Inside function:", name)
student() # print(name)                     # Error: name is not accessible outside

print("2. GLOBAL SCOPE")
company = "Codegnan"              # Global variable
def display():
    print("Inside function:", company)
display()
print("Outside function:", company)

print("3. LOCAL vs GLOBAL VARIABLE")
name = "Global Name"
def display_name():
    name = "Local Name"           # Local variable has higher priority
    print("Inside:", name)
display_name()
print("Outside:", name)

