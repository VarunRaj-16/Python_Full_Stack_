# 14. Count Vowels
def count_vowels(s):
    if s == "":
        return 0
    return (1 if s[0].lower() in "aeiou" else 0) + count_vowels(s[1:])
print("Vowels in 'education':", count_vowels("education"))
# 15. Check Palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print("Is 'madam' palindrome ? :", "Palindrome" if is_palindrome("madam") else "Not Palindrome")
print("Is 'python' palindrome ? :", "Palindrome" if is_palindrome("python") else "Not Palindrome")
# 16. Decimal to Binary
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)
print("Binary of 10:", decimal_to_binary(10))