class dog:
    # A
    name = None
    breed = None
    color = None

    #B
    def sleep(self):
        print("sleeping")

    def bark(self):
        print("barking")

    def eat(self):
        print("eating")


dog1 = dog()
print(dog1.name)
dog1.name = "chow"
print(dog1.name)
dog1.sleep()

print("------------------------")

dog2 = dog()
print(dog2.name)
dog2.name = "mow"
print(dog2.name)

