# def and call
# user defined function

def greet_to_all_of_you():
    print("Hello Everyone")


def greet():
    print("Yes")
    greet_to_all_of_you()  # you can call this function inside another func


greet()
greet_to_all_of_you()
