# DAY 26 - INHERITANCE IN PYTHON
print("1. SINGLE INHERITANCE")
class User:
    def login(self):
        print("every user must be login")
class Manager(User):
    def manage_users(self):
        print("manager can manage the users")
m = Manager()
m.login()
m.manage_users()
