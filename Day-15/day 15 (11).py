print("11. filter() FUNCTION")
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)
odd = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odd)
prices = [500, 1200, 800, 2500, 600]
expensive = list(filter(lambda price: price > 1000, prices))
print("Prices > 1000:", expensive)
users = ["teja", "codegnan", "admin123", "raj"]
long_users = list(filter(lambda user: len(user) > 5, users))
print("Usernames longer than 5:", long_users)
