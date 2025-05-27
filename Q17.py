# Q17. Class Decorators
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greet(cls):
    def greet(self):
        return "Hello from Decortor!"
    cls.greet = greet
    return cls

@add_greet
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Soniya")
print(p1.name)
print(p1.greet())
