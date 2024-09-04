# Decorators in Python

def add_extra_security(func):
    # two parts in decorator . 1 wrapper and call
    def wrapper():
        print("1.Before the function is called.")
        print("2.helmet", "safeguards", "gloves")
        func()
        print("3. after the function is called.")
        print("4. secure driving")

    return wrapper()


# definition
# @my_decorator
# def drive_bike():
#     print("i m driving")


@add_extra_security
def drive_scooty():
    print("Normal Function")
