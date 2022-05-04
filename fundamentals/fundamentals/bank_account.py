# class BankAccount:
#     # class attribute
#     bank_name = "First National Dojo"
#     all_accounts = []
#     def __init__(self, int_rate, balance):
#         self.int_rate = int_rate
#         self.balance = balance
#         BankAccount.all_accounts.append(self)
#     # class method to change the name of the bank
#     @classmethod
#     def change_bank_name(cls, name):
#         cls.bank_name = name
#     # class method to get balance of all accounts
#     @classmethod
#     def all_balances(cls):
#         sum = 0
#         # we use cls to refer to the class
#         for account in cls.all_accounts:
#             sum += account.balance
#         return sum


# class BankAccount:
#     # ... _init__ goes here
#     def with_draw(self, amount):
#         # we can use the static method here to evaluate
#         # if we can with draw the funds without going negative
#         if BankAccount.can_withdraw(self.balance, amount):
#             self.balance -= amount
#         else:
#             print("Insufficient Funds")
#         return self
#     # static methods have no access to any attribute
#     # only to what is passed into it
#     @staticmethod
#     def can_withdraw(balance, amount):
#         if (balance - amount) < 0:
#             return False
#         else:
#             return True

class BankAccount:

    def __init__(self, int_rate = 0.02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance = self.balance + interest
        print(f"You made {interest} in interest!")
        return self

test1 = BankAccount(0.02, 500)
test2 = BankAccount(0.01, 1500)


test1.deposit(100).deposit(100).deposit(50).withdraw(200).yield_interest().display_account_info()
# test1.display_account_info()

test2.deposit(100).deposit(100).withdraw(50).withdraw(200).withdraw(100).withdraw(250).yield_interest().display_account_info()
# test2.display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(200)
        print(self.account.balance)

    def make_withdraw(self, amount):
        self.account.withdraw(100)
        print(self.account.balance)

    def make_display_user_balance(self):
        print(self.account.balance)

test1 = User("Geralt", "whitewolf@python.com")
test2 = User("Yennifer", "purpledank@python.com")

class CheckingAccount(BankAccount):
    pass

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance = 0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth

    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self