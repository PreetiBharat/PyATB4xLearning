# Method Overriding - Same method name in the parent and child class
# Child will always override the parent functions
# super means call my parent function

class Grandfather:
    x = 10

    def home(self):
        print("Old home")


class Father(Grandfather):
    a = 12

    def home(self):
        print("1BHK")
        print(self.a)
        print(super.x)


class Son(Father):
    b = 15

    def home(self):
        print("No House")
        print(self.b)
        print(super().a)
        print(super().x)


Pramod = Son()
Pramod.home()
print(Pramod.x)
