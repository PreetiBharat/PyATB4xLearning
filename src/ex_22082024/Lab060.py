user_type = input("enter your user type admin, manager, guest\n")
user_type = user_type.lower()  # we are matching the lower case with text entered in o/p))
match user_type:
    case "admin" | "manager":
        print("hello Sir")
    case "guest":
        print("hello Guest")
    case _:
        print("Hello there")
