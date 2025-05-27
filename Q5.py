# Q5. Static Variables and Static Methods                             Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return  a + b

s1 = MathUtils
print("The output of sum is:",s1.add(1,4))