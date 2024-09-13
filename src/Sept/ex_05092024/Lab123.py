class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_me_account_number(self, is_auth):
        if is_auth:
            print(self.__account_number)
        else:
            print("not allowed")


icici = Bank(9874554554, 100)
icici.deposit(100)
icici.check_balance()
icici.show_me_account_number(False)
