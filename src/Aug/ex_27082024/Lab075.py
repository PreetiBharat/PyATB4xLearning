# function scope
global_b = 12  # global variable


def my_function():
    a = 10  # local variable
    print(a)
    print(global_b)  # we can use global variable in a function


def f1():
    print(global_b)


# print(a)  # a is defined withing the above function and we cant call it outside the function.
my_function()
print(global_b)
f1()
