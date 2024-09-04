# There are many types of decorators
# staticmethod
# classmethod
# property
# function.wraps
# these will be used in OOPS concept

# we can add multiple decorators called as Chaining decorators

def decorator1(func):
    def wrapper():
        print("decorator1")
        func()

    return wrapper


def decorator2(func):
    def wrapper():
        print("decorator2")
        func()

    return wrapper()


@decorator1
@decorator2
def say_hello():
    print("hello")


say_hello()
