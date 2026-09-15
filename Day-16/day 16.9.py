print("16. DICTIONARY METHODS – COPY & fromkeys")
original = {"a": 1, "b": 2}
copied = original.copy()
print("copy():", copied)
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print("fromkeys():", new_dict)
print("17. NESTED DICTIONARIES")
students = {
    "s1": {"name": "Ravi", "age": 22},
    "s2": {"name": "Teja", "age": 21}
}
print("students['s1']['name']:", students["s1"]["name"])



