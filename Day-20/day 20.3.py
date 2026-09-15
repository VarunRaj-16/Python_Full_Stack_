print("7. random MODULE")
import random
print("random.random():", random.random())
print("random.randint(1, 100):", random.randint(1, 100))
print("random.choice(['apple','banana','cherry']):",
      random.choice(['apple', 'banana', 'cherry']))
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("After shuffle:", nums)
print("8. collections MODULE")
from collections import Counter, defaultdict
data = ['a', 'b', 'a', 'c', 'b', 'a']
counter = Counter(data)
print("Counter:", counter)
dd = defaultdict(int)
dd['missing'] += 1
print("defaultdict missing key:", dd['missing'])

