# Q3 ___ Public Variables and Methods                                   Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    brand = "Toyota"

    @staticmethod
    def start():
        print("Car is started...")
    
c1 = Car()
print(c1.brand)
c1.start()