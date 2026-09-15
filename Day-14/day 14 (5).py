print("7. KEYWORD ARGUMENTS")
def Greet_KW(name, age):
    print(f"My name is {name} and age is {age}")
Greet_KW(name="Raju", age=23)
Greet_KW(age=25, name="Harish")       # Order can be changed

print("\n8. DEFAULT PARAMETERS")
def CountryDetails(country="India"):
    print("My country is:", country)
CountryDetails("USA")
CountryDetails()                      # Uses default value

