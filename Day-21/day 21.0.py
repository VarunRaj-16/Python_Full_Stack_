# DAY 20 - FILE HANDLING + DIRECTORY OPERATIONS + EMAIL PROJECT
print("1. FILE MODES & BASIC OPERATIONS")
with open("example.txt", "w") as file:   # Writing to a file
    file.write("Hello, World!\n")
    file.write("File handling is easy.")
print("File written successfully")
with open("example.txt", "r") as file:    # Reading entire content
    content = file.read()
    print("Content:\n", content)
with open("example.txt", "a") as file:   # Appending to a file
    file.write("\nThis line is appended.")
print("Content appended")
print("2. READING METHODS")
with open("example.txt", "r") as file:
    print("readline():", file.readline().strip())
with open("example.txt", "r") as file:
    print("readlines():", file.readlines())

