# try , except and finally

try:
    num1 = int(input("enter your num1\n"))
    num2 = int(input("enter your num2\n"))
    result = num1 / num2

except ValueError as ve:
    print("Value error, You have entered the string instead of int")

except ZeroDivisionError as zde:
    print("Zero Division Error, Do not use 0 in Num2")

else:
    print("Result: ", result)

finally:  # finally means this line of code will be always executed
    print("This code will be always executed!")

