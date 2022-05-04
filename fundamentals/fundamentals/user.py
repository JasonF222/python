# # class User:
# #     pass

# # michael = User()
# # anna = User()

# # Declare a class and give it name User

# class User:
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0


# User()
# guido = User()
# monty = User()
# # Accessing the instance's attributes
# print(guido.name)    # output: Michael
# print(monty.name)    # output: Michael

# guido.name = "Guido"
# print(guido.name)    # output: Guido
# monty.name = "Monty"
# print(monty.name)    # output: Monty

# guido = User()
# monty = User()
# guido.bank_name = "Dojo Credit Union"
# print(guido.bank_name)    # output: Dojo Credit Union
# print(monty.bank_name)    # output: First National Dojo

# User.bank_name = "Bank of Dojo"
# print(guido.bank_name)    # output: Bank of Dojo
# print(monty.bank_name)    # output: Bank of Dojo

# class User:
#     # class attributes get defined in the class
#     bank_name = "First National Dojo"
#     # now our method has 2 parameters!
#     def __init__(self, name, email_address):
#         # we assign them accordingly
#         self.name = name
#         self.email = email_address
#         # the account balance is set to $0
#         self.account_balance = 0
# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")



# guido.make_deposit(100)

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account_balance = 0
#     # adding the deposit method
#     def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
#         self.account_balance += amount # the specifc user's account increases by the amount of the value received

# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(50)
# print(guido.account_balance)    # output: 300
# print(monty.account_balance)    # output: 50



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def user_account_balance(self):
        print("User : " + self.name, "Account Balance: " + str(self.account_balance))


milo = User("Milo", "milo@python.com")
tony = User("Tony", "tony@python.com")
lily = User("Lily", "lily@python.com")


# milo.make_deposit(100)
# milo.make_deposit(100)
# milo.make_deposit(100)
# milo.make_withdrawal(50)

milo.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50)
print("User : " + milo.name, "Account Balance: " + str(milo.account_balance))

# tony.make_deposit(500)
# tony.make_deposit(200)
# tony.make_withdrawal(300)
# tony.make_withdrawal(75)

tony.make_deposit(500).make_deposit(200).make_withdrawal(300).make_withdrawal(75)
print("User : " + tony.name, "Account Balance: " + str(tony.account_balance))

# lily.make_deposit(400)
# lily.make_withdrawal(50)
# lily.make_withdrawal(150)
# lily.make_withdrawal(500)

lily.make_deposit(400).make_withdrawal(50).make_withdrawal(150).make_withdrawal(500)
print("User : " + lily.name, "Account Balance: " + str(lily.account_balance))