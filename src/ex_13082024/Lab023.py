# string Formating

number = 3.14159265359
formatted_number = f"{number:.3f}"
print(formatted_number)
# formating also consider rounding of the number. In this case formatting is 3 and 1 is rounded of to 2


# String format
num = 90
print("this is the number your working with " f"{num}")

# Table of 9
# 9*1 = 9
# 9*2 = 18"


table = 9
print(f"{table}*1={table}")
print(f"{table}*2={table * 2}")
print(f"{table}*3={table * 3}")
print(f"{table}*10={table * 10}")
