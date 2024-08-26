# Match Statement
# Its called Switch in Java
# match the o/p and execute
# This works only when Python version > 3.10

# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block

# Write a program to ask the user which browser he wants to run automation
browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        if browser_name == "firefox":
            print("Hello Hello")
        print("Execute the firefox Code")
    case "chrome":
        print("Execute the Chrome Code")
    case "edge":
        print("Execute the Edge Code")
    case "safari":
        print("Execute the Safari Code")
    case _:
        print("Browser Not Found!")
