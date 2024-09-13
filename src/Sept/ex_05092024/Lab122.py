class MyClass:
    # public var (instance)
    public_var = "I M public"
    balance = 100

    # Private variable
    __private_variable = "I am private"
    __password = "1234"
    # Protected variable
    _protected_variable = "I m protected"
    b = 10
    _c = 12
    __d = 15
    college = "BLDE"
    preeti = "TTA"
    __preeti_bal = 2000000


object1 = MyClass()
print(object1.public_var)
print(object1.balance)
print(object1._protected_variable)
# print(object1.__password)
