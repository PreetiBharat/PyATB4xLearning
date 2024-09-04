# Conditions and Loops
# Write a program to take a user age and let him know if he can go the club.
# 21

# Logic Building
# 1. user input - data type -> int
# o/p -> String -> user if he can go or not.

# 2. Rough logic
# age  > 21 -> print can go
# age < 21 -> print can't go

# Write the logic

age = (input("Enter your age"))
age = int(age)

if age >= 21:
    print("Can go to club")
else:
    print("Cant go")
