print("14. KEYWORD-ONLY PARAMETERS (*)")
def User2(*, name, age):
    print(name, age)
User2(name="Jani", age=21)            # Correct
# User2("Jani", 21)                   # Error – must use keywords

print("\n15. / and * TOGETHER")
def Student(name, /, age, *, course):
    print(name, age, course)

Student("Ravi", 22, course="Python")

print("\n16. DOCSTRING")
def UserInfo3(**details):
    print(details)
print(UserInfo3.__doc__)


