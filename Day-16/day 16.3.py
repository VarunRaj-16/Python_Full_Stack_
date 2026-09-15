print("5. SET METHODS – ADDING")
s = {10, 20}
s.add(30)                         # Add single element
print("After add(30):", s)
s.update([40, 50])                # Add multiple elements
print("After update([40,50]):", s)
print("6. SET METHODS – REMOVING")
s = {10, 20, 30, 40}
s.remove(20)                      # Removes element (error if not present)
print("After remove(20):", s)
s.discard(100)                    # No error even if element is absent
print("After discard(100):", s)
popped = s.pop()                  # Removes a random element
print("After pop():", s, "| Popped:", popped)
s.clear()
print("After clear():", s)
