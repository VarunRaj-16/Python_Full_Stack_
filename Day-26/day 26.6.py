print("7. super() FUNCTION")
class Employee:
    def __init__(self, ename, eid):
        self.ename = ename
        self.eid = eid
class ChildEmployee(Employee):
    def __init__(self, ename, eid, esal):
        super().__init__(ename, eid)
        self.esal = esal
ce = ChildEmployee("rajesh", 102, 20000)
print(ce.ename, ce.eid, ce.esal)
print("8. DOCSTRING")
def greet(name):
    """This function greets the person with the provided name."""
    print("Hello,", name)
print(greet.__doc__)
greet("Varun")

