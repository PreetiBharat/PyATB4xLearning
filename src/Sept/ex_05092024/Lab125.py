# Single Inheritance
class Parent:
    gold = "20kg"

    def bhk2(self):
        print("2BHK")


class Child(Parent):
    diamond = "Diamond"
    def bhk3(self):
        print("3BHK")


child_obj = Child()
child_obj.gold
child_obj.bhk2()
child_obj.bhk3()


father_obj_reference = Parent()
father_obj_reference.bhk2()
# father_obect_ref.BHK3() # AttributeError: 'Parent' object has no attribute 'BHK3'. Did you mean: 'BHK2'?
# print(father_obect_ref.diamond)