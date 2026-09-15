print("6. MRO (Method Resolution Order)")
class A:
    def m1(self):
        print("i am m1 in class-A")
class B:
    def m1(self):
        print("i am m1 in class-B")
class C(A, B):
    pass
obj = C()
obj.m1()
print(C.__mro__)
