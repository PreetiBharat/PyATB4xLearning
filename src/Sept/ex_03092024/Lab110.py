# Take input and create a class in python

class Person:

    def __init__(self):
        self.name = input("enter the name\n")
        self.age = input("enter the age\n")
        self.phone = input("enter the phone\n")
        self.occupation = input("enter the occupation\n")

    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}")
        print(f"age is {self.age}")
        print(f"phone is {self.phone}")
        print(f"occupation is {self.occupation}")

        # print(f"Name is {self.name}", f"Age is {self.age}", f"Phone is {self.phone}",
        #               f"occupation is {self.occupation}")


# Create an Object
person1 = Person()

# Call the display Function
person1.name_of_the_function_to_display()
