print("13. reduce() FUNCTION")
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print("Sum:", total)
numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)
numbers = [10, 25, 8, 40, 15]
largest_num = reduce(lambda a, b: a if a > b else b, numbers)
print("Largest number:", largest_num)
words = ["python", "developer", "sql", "programming"]
longest = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print("Longest word:", longest)

