# User Defined are of 4 types
# 1. They will not return anything -> no return type
# 2.They can return something
# 3. They have parameters
# 4. They don't parameters / arguments

# 1. They will not return anything -> no return type
# or No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello World")


result = greet()
print(result)


# # 2. # No Return Type and with Argument
def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Preeti")


# # 3. No Return Type and with Default Argument
def say_hello_default_args(name="Pramod"):
    print("hello,", name)


say_hello_default_args("Amit")
say_hello_default_args()
say_hello_default_args(name="Swara")  # positional argument


def multiple_args(name1="Priya", name2="Preeti", name3="Shweta"):
    print("multiple-args", name1, name2, name3)


multiple_args(name1="Amar", name2="Akbar", name3="Antony")
multiple_args(name2="Rani")  # only name2 will replaced with this


# 4. Argument + return Type
def sum_of_two_num(num1, num2):
    return num1 + num2


# result = sum_of_two_num(12, 12)
def sum_of_two_number(num1, num2):
    return num1 + num2


def sum_of_two_number_with_default(num1=100, num2=200):
    return num1 + num2


# result = sum_of_two_number(10, 34)
result = sum_of_two_number(num1=34, num2=34)
result = sum_of_two_number_with_default()
print(result)
