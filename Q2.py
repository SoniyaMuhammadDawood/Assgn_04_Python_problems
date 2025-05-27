# Q2.   (Using cls) :                                                Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        print("Number of object creted =", cls.count)

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
Counter.display_count()