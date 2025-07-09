class person:
    # Attributes
    id = None
    Name = None
    age = None
    email = None
    height = None
    Weight = None
    gender = None
    phone_no = None
    address = None

    # Behaviour
    def talk(self):  # NRNA  # self('this' in java) self will be first argument in every behaviour.
        print("I can Talk")

    def sleep(self, name):  # Arg with No Return
        print("I am a method!")
        print("sleep", name)

    def sleep2(self, name):  # Arg with Return
        print("I am a method!")
        return None

    def walk(self):
        print("I m walking")

    def walk_return(self):  # No Arg with Return
        return "I am walking"


# Create an Object of the Class
# ObjectRef = ClassName() -> Object
tushar = person()
tushar.Name = "Tushar"
print(tushar.Name)
tushar.talk()

rajyalakshmi = person()
rajyalakshmi.Name = "rajyalakshmi"
print(rajyalakshmi.Name)
rajyalakshmi.talk()
