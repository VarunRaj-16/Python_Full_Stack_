print("3. writelines()")
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("data.txt", "w") as f:
    f.writelines(lines)
print("writelines() done")
print("4. UNDERSTANDING r+, w+, a+")
with open("student.txt", "w") as f:   # Prepare a sample file
    f.write("Hello Varun")
with open("student.txt", "r+") as f:    # r+ → Read + Write
    f.write("Hi")
    f.seek(0)
    print("After r+:", f.read())  # Hello Varun
with open("student.txt", "w+") as f:   # w+ → Write + Read
    f.write("Python")
    f.seek(0)
    print("After w+:", f.read())
with open("student.txt", "a+") as f:    # a+ → Append + Read {adds at the end}
    f.write(" Learning")
    f.seek(0)
    print("After a+:", f.read())  # Python Learning
