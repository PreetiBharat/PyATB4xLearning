# How to handle exceptions
# using try, except, else, finally

print("-- Start of the Program --")
try:
    a = int(input("enter your num1"))  # ValueError: invalid literal for int()
    b = int(input("enter your num2"))  # Lab150.py", line 4, ValueError
    c = a / b  # ZeroDivisionError: division by zero(when any value is 0)
    #  ValueError: invalid literal for int() with base 10: 'preeti'(when any value entered is preeti)

    print("Result Div is ", c)

except Exception as e:  # alias , Exception is what Class - multiple classes
    print(e)
    print("Please check your program, It should not be a zero or string")

print("-- End of the Program --")
