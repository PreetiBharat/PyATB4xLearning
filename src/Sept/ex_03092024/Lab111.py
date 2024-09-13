class Calc:
    def __init__(self):  # default constructor
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


calc1 = Calc()
a = input("enter the value of the a ")
b = input("enter the value of the b ")

output_sum = calc1.sum(a, b)
output_sub = calc1.sub(a, b)
output_mul = calc1.mul(a, b)
output_div = calc1.div(a, b)
print(output_sum, output_sub, output_mul, output_div)
