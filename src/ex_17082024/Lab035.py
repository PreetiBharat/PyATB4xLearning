# Write a Python program to calculate  the area of circle given its radius using its formula
# area=pi*r^2  (pi = 3.14)
import math

# Logic building formula
# step 1: figure out the input and output
# input -> r -> data type -> float
# pi = 3.14 or math.pi(this is inbuilt function)
# power = pow or **

# output: float -> area  -> print area

# Step2
# rough logic: area = 3.14 * pow(r, 2)
#
# step 3: write the logic

radius = float(input("enter the radius of the circle\n "))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius, 2)
# area = 3.14 * (radius ** 2)  # Can be
print(f"area of the circle is {area:.2f}")  # Use of formatting and rounding off decimal number
