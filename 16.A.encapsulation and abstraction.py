'''1.Encapsulation:
Create a BankAccount class with private attributes for account_number and balance.
Add methods to check balance, deposit, and withdraw funds.
Try accessing the balance directly and observe the result.'''

class Bankaccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def check_balance(self):
        return f"Balance: { self.__balance}"
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}.{self.check_balance()}"
        return "Invalid deposit amount."
    
    def withdraw(self,amount):
        if 0 < amount <= amount:
            self.__balance -= amount
            return f" withdrew {amount}.{self.check_balance()}"
        return "Insufficient funds or invalid amount."

account = Bankaccount("123456",1000)

print(account.check_balance())
print(account.deposit(500))
print(account.withdraw(200))

print(account.__balance)

print("                                    ")

'''
2.Abstraction:
Design a Phone class with methods to call_contact and take_picture. 
Abstract away any internal processing details and focus on 
creating a user-friendly interface.
'''

from abc import ABC, abstractmethod

class Phone(ABC):
    def __init__(self,model):
        self.model = model

    def call_contact(self,contact_name):
        pass

    def take_picture(self):
        pass

class Smartphone(Phone):
    def __init__(self,model):
        super().__init__(model)

    def call_contact(self,contact_name):
        return f"Calling {contact_name} using {self.model}...."

    def take_picture(self):
        return f"Taking a picture with {self.model}'s camera...."
    
phone = Smartphone("Galaxy X")
print(phone.call_contact("Alice"))
print(phone.take_picture())
      
