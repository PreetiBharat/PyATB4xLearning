public_toilet = "PB"  # global variable


def home():
    private_toilet = "PT"  # local variable
    print(public_toilet)
    print(private_toilet)


home()


def stranger():
    print(public_toilet)
    # print(private_toilet)  # Bcz it is a local variable, cant call it outside the function


# stranger()
print(public_toilet)
# print(private_toilet)
