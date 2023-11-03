# Banking System using OOP

# Parent Class : User
# Holds details about an user
# Has a function to show user details   

# Parent Class
class User():

    # init function which takes arguements
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # showUserDetails function which print the user details
    def showUserDetails(self):
        print("Personal Details")
        print("")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)



# Child Class : Bank
# Stores details about the account balance
# Stores details about the amount
# Allows for Deposits, Withdraw, View Balance


# Child Class
class Bank(User):

    # init function which takes arguements, and by using the super function we can easily assigned the value to initialised variable
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    # Deposit Function which we used to deposit amount in the account
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account Balance has been updated...")
        print()
        print("Current Balance: ",self.balance)
    

    # Withdraw function which we used to withdraw amount from the account.
    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Balance...")
            print("Available Amount: ", self.balance)
        else:
            print("Amount Deducted...")
            self.balance = self.balance - amount
            print("Available Amount: ", self.balance)

    def viewBalance(self):
        self.showUserDetails()
        print("Available Amount: ", self.balance)



user1 = Bank("Harsh Solanki", 22, "M")
user1.showUserDetails()
user1.deposit(2000)
user1.withdraw(1000)
user1.withdraw(2000)