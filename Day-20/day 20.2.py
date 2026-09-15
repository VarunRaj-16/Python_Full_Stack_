print("5. json MODULE")
import json
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print("JSON String:", json_str)
parsed = json.loads(json_str)
print("Parsed name:", parsed["name"])
print("6. math MODULE")
import math
print("sqrt(25):", math.sqrt(25))
print("factorial(5):", math.factorial(5))
print("ceil(4.2):", math.ceil(4.2))
print("floor(4.8):", math.floor(4.8))
print("pow(2, 3):", math.pow(2, 3))
print("sin(pi/2):", math.sin(math.pi / 2))
