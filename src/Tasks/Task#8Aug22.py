# Triangle Classifier:

# equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal)

a = float(input("enter the side a: "))
b = float(input("enter the side b: "))
c = float(input("enter the side c: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or c == a:
    print("Isosceles")
else:
    print("Scalene")
