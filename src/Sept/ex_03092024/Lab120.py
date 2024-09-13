# Web Automation - Selenium
# Page - You are going automate

class VWOLoginPage():

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def confirm_login(self):
        if self.email == "pramod@gmail.com" and self.password == "pass123":
            print("Login allowed")
        else:
            print("not allowed")


# This is the end of the class
email = input("enter the email\n")
password = input("enter the password\n")
vwo_obj = VWOLoginPage(email, password)
vwo_obj.confirm_login()

pramod = VWOLoginPage("pramod@gmail.com", "Pass123")
pramod.confirm_login()
