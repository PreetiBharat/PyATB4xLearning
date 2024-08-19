# Task #2
# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}

num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))

# print(max(num1, num2))
print(f"Maximum number is: {max(num1, num2)}")  # Print using formatting f"{}"

# print(pow(num1, num2))
print(f"num1 to the power of num2 is: {pow(num1, num2)}")  # Print using formatting f"{}"

# print("Sum=", num1 + num2)
print(f"Sum of num1 and num2 is: {num1 + num2}")  # Print using formatting f"{4}"

# print("Subtraction=", num1 - num2)
print(f"Subtraction of num1 and num2 is: {num1 - num2}")

# print("Multiplication=", num1 * num2)
print(f"Multiplication of num1 and num2 is: {num1 * num2}")  # Print using formatting f"{}"

# print("Division=", num1/num2)
print(f"Division of num1 by num2 is: {num1 / num2}")  # Print using formatting f"{}"
