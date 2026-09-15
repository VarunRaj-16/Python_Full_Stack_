print("11. **kwargs (Variable Length Keyword Arguments)")
def UserInfo(**details):
    print(details)
    print("Type:", type(details))     # dictionary
    print("Name:", details.get("name"))
UserInfo(name="Raju", age=23, height=5.7)

print("12. Normal Parameter + **kwargs")
def UserInfo2(color, **details):
    print("Color:", color)
    print("Details:", details)
UserInfo2(color="Black", name="Raju", age=23)

print("13. POSITIONAL-ONLY PARAMETERS (/)")
def User(name, age, /):
    print(name, age)
User("Varun", 21)                      # Correct
# User(name="Jani", age=21)           # Error – keyword not allowed


