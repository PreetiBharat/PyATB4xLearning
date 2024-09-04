# This is a function of type "No return type with arguments function"

def print_arguments(*args):
    # print(args[0])
    for i in args:  # to print all the args, use for loop
        print(i)


# list = ["pramod", "amit", "lucky"]

print_arguments("Pramod", "Amit", "Lucky")
print_arguments("Swasti", "Swara")
print_arguments("Bharat", 100, True, False, "PREETI")
# print_arguments()  # this gives error as "tuple index out of range". minimum 1 argument is important


# print() also takes multiple type of agrs

print("amit")
print("pramod", "amit")
print("pramod", "amit", True)
print("pramod", "amit", True, False)
