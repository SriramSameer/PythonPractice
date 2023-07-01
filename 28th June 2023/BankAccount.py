class BankAccount:
    def __init__(self):
        self.balance = 0  # Public Attribute

    def deposit(self, amount):
        self.balance += amount

    def _withdraw(self, amount):  # Protected Attribute
        self.balance -= amount

    def __show_balance(self):
        print("Balance is ", self.balance)  # Private Attribute

    def is_Auth_True(self, isAuth):
        if isAuth:
            print("You are authenticated!!")
            self.__show_balance()
        else:
            print("You are not authenticated")

    def is_withdraw_Auth_True(self, isAuth_withdraw, amount):
        if isAuth_withdraw:
            print("You are authenticated!!, withdraw")
            self._withdraw(amount)
        else:
            print("You are not authenticated")


account = BankAccount()
account.deposit(1000)
account.is_withdraw_Auth_True(True, 499)

account.is_Auth_True(False)