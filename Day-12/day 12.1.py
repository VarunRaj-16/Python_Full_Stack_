print("3. PALINDROME USING STRING SLICING")
n = int(input("Enter a number (string method): "))
s = str(n)
if s == s[::-1]:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")
print("4. COUNT EVEN DIGITS IN A NUMBER")
print("=" * 65)
n = int(input("Enter a number to count even digits: "))
s = str(n)
count = 0
for i in s:
    if int(i) % 2 == 0:         # Convert character to int and check even
        count = count + 1
print("Count of even digits:", count)

