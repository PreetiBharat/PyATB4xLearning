# Ternary operators
# if-else

# if condition then do this
# else do that

# if my age is > 18 then I can watch reels
# else I cannot watch
my_age = 18
print("I will go to Goa" if my_age > 18 else "I cant go. Stay home")

# OR
if my_age > 18:
    print("GO Goa")
else:
    print("I cant go. Stay home")


print("GO Goa" if int(input("Enter your age")) > 18 else "Cant go. stay home")

# OR

user_age = int(input("enter your age"))
if user_age > 18:
    print("GO Goa")
else:
    print("Cant go. stay home")
