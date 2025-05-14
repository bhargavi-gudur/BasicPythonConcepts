def first():
    print("hello")


second = first
second()


def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before the original function.")
        original_function()
        print("Wrapper executed after the original function.")

    return wrapper_function
# @decorator_function


def say_hello():
    print("Hello!")


new = decorator_function(say_hello)
new()


def add(n):
    return n+10


def mul(n):
    return n*10


def cal(i, val):
    print(i(val))


cal(add, 10)
cal(mul, 18)
