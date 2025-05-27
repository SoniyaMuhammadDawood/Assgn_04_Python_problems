# Q15. Method Resolution Order (MRO) and Diamond Inheritance
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("I am A, It's show time")

class B(A):
    def B_Methf(self):
        print("I am B")

class C(A):
    def C_methd(self):
        print("I am C")

class D(B, C):
    def show():
        pass


d = D
d.show()
print(d.__mro__)

