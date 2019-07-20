
# 1. Build a new class called `BankAccount`...
class BankAccount:
    def __init__(self, thisName):
        self.name = thisName
        self.balance = 1000
        self.status = "open"
        
    def deposit(self, amount):
        self.balance +=amount
        
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print(f"You can only withdraw {self.balance} dollars.")
            
    def check_balance(self):
        print(self.balance)
        
    def is_valid(self):
        if self.status == "open":
            return True
        else:
            return False
            
    def close_account(self):
        self.status = "closed"



#  ... and instantiate a new account for a user named "Kiran".
kiran_account = BankAccount("Kiran")

# i. Confirm that Kiran's new account is of the type `BankAccount`.
print(type(kiran_account))

# ii. Confirm that the name on Kiran's account is "Kiran".
print(kiran_account.name)

# iii. Confirm that Kiran's account has a balance of $1000.
print(kiran_account.balance)

# iv. Confirm that Kiran's account is `open`.
print(kiran_account.status)

# v. Set Kiran's balance to $2000. Confirm his new account balance.
kiran_account.balance = 2000
print(kiran_account.balance)

# Now you're on your own to write tests for the rest...

stanleyaccount = BankAccount("Stanley")
print(stanleyaccount.is_valid())

lauraaccount = BankAccount("Laura")
print(lauraaccount.is_valid())


amandaaccount = BankAccount("Amanda")
class Transfer:
    def __init__(self, thisSender, thisRecipient, thisAmount):
        self.sender = thisSender
        self.recipient = thisRecipient
        self.amount = thisAmount
        self.status = "pending"
        
    def both_valid(self):
       return(self.sender.is_valid()) and (self.recipient.is_valid())
       
    def execute_transaction(self):
        if (self.sender.balance > self.amount) and (self.both_valid()):
            self.sender.balance -= self.amount
            self.recipient.balance += self.amount
            self.status = "complete"
            print(self.sender.balance, self.recipient.balance, "Transaction complete.", sep="\n")
        elif self.sender.balance < self.amount:
            self.status = "rejected"
            print("Transacion rejected. Please check your account balance.")
    def reverse_transfer(self):
        if self.status == "complete":
            self.sender.balance += self.amount
            self.recipient.balance -= self.amount
            self.status = "reversed"
            print(self.sender.balance)
            print(self.recipient.balance)
            print("Transaction reversed.")
    
        
transfer1 = Transfer(amandaaccount, stanleyaccount, 50)   
transfer1.execute_transaction()
transfer1.reverse_transfer()

