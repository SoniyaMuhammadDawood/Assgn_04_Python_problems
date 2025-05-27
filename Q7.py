# 7. Access Modifiers: Public, Private, and Protected
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

var1 = Employee("Soniya", 90000, 234566)
print("Public Varible output is: ",var1.name)
print("Protected variable output is: ", var1._salary)
print("Private variable output is: ", var1.__ssn)  # It's give attribute error.