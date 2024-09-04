# find out the max between two numbers

# Logic Building Formula

# 1 . user inputs -> two integers
# 2. o/ p ->  int 1 which ever is grater max number it will return.
# 3. - input method
# 31.4 or 45.34

num1 = float(input("enter num1\n"))
num2 = float(input("enter num2\n"))

if num1 > num2:
    print(f"Max is {num1}")
else:
    print("Max is: num2")  # both are print() are fine
    print(f"Max is: {num2}")
