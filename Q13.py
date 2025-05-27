# 13. Composition
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("car started...")

class Car:
    def __init__(self, engine):
        self.engine = engine
    

    def startCar(self):
        return self.engine.start()

myCar = Car(Engine())
myCar.startCar()
