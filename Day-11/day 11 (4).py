print("7. for LOOP Basics")
numbers = [10, 20, 30, 40]
for i in numbers:
    print(i)
# How for Loop Works Internally (iter & next)
l = [1, 2, 3, 4]
iterator = iter(l)               # Create iterator from iterable
print(next(iterator))            # 1
print(next(iterator))            # 2
print(next(iterator))            # 3
print(next(iterator))            # 4
# print(next(iterator))          # Would raise StopIteration

