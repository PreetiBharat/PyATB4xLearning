# Create a program to sum of three number from the user input

num1 = int(input("Enter the the number 1\n"))  # 100
num2 = int(input("Enter the the number 2\n"))  # 200
num3 = int(input("Enter the the number 3\n"))  # 300


def sum_of_three_numbers(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_three_numbers(num1, num2, num3)
print(result)
