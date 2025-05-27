# Q16. Function Decorators
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(call):
    def wrapper():
        print("Function is being called")
        call()
    return wrapper
    
@log_function_call
def say_hello():
    print("Say Hello")

say_hello()

