# Q6. Constructors and Destructors                                    Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger is ready ")

    def __del__(self):
        print("logger is no more..He is dead")

log1 = Logger()
log1.__del__

log2 = Logger()
log2.__del__

