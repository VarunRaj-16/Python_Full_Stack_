##Output Formatting
#print()
#a) Printing Text
print("Hello, World!")
#b) Printing Multiple Items
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
#c) Using sep to Change the Separator
print("2026", "08", "11", sep="-")
#d) Using end to Control Line Endings
print("Hello,", end=" ")
print("World!")
##Printing Special Characters
#New Line (\n)
print("Line 1\nLine 2")
#Tab (\t)
print("Name:\tAlice")
#1. Using Commas (Simple Print Method)
name = "Alice"
age = 25
score = 95.5
print("Name:", name, "Age:", age, "Score:", score)
#2. Using Modulo Operator (% Formatting   )
name = "Bob"
age = 30
score = 88.75
print("Name: %s | Age: %d | Score: %.2f" % (name, age, score))
#3. Using f-strings (Formatted String Literals)
name = "Charlie"
age = 28
score = 92.389
print(f"Name: {name} | Age: {age} | Score: {score:.2f}")
#4. Using str.format() Method
name = "Diana"
age = 22
score = 89.456
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age, score))




