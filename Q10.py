# 10. Instance Methods                                                   Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print("woof! My name is", self.name, "and i'm from breed:", self.breed)

d1 = Dog("Tommy","Labrador")
d1.bark()

d2 = Dog("Bruno", "Golden Retriever")
d2.bark()