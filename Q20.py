# 20. Creating a Custom Exception
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older to continue")
    else:
        print("You're allowed!")

try:
    user_age = int(input("Type your age: ")) 
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom exception caught:", e)

