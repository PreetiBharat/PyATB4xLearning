# Inheritance

class Father:
    key = "2BHK"

    def Car(self):
        print("Father, car!!", "ALTO", self.key)


class Son(Father):
    key = "3BHK"

    def home(self):
        print("3BHK")

    def Car2(self):
        print("Son Car")


father_obj = Father()
father_obj.Car()

son_obj = Son()
son_obj.Car()
