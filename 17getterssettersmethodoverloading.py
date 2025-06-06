'''Getters and Setters:
Create a class BankAccount with a private attribute balance.
Write a getter method to retrieve the balance and a setter method to update it, 
ensuring the balance never goes below zero.'''

class Bankaccount:
    def __init__(self, initial_balance = 0):
        self.__balance = max(initial_balance, 0)

    @property
    def balance(self):
        "Getter method to retrive the balance"""
        return self.__balance
    
    @balance.setter
    def balance(self,amount):
        """Setter method to update the balance ensuring it never goes below zero"""
        if amount >= 0:
            self.__balance = amount
        else:
            print("Error: Balance cannot be negative!")

account = Bankaccount(100)
print(account.balance)

account.balance = 50
print(account.balance)

account.balance = -20
print("                                   ")

'''2.Method Overloading:
Write a class Calculator with a method multiply(). 
Allow it to take either two or three arguments to multiply two or three numbers.'''

class calculator:
    def multiply(self,a,b,c=1):
        """multiply two or three numbers"""
        return a*b*c
    
calc = calculator()
print(calc.multiply(3,4))
print(calc.multiply(3,4,5))

print("                                        ")

'''3.Method Overriding:
Create a parent class Shape with a method draw() that prints "Drawing shape".
Create a child class Circle that overrides draw() to print "Drawing circle".'''

class Shape:
    def draw(self):
        print("Drawing Shape")

class circle(Shape):
    def draw(self):
        print("Drawing Circle")

Shape = Shape()
Shape.draw()
Circle = circle()
Circle.draw()
print("                                   ")

'''4.Abstract Classes:
Define an abstract class Employee with an abstract method calculate_salary().
Create a subclass Manager that implements calculate_salary() based on working hours and rate per hour.'''

from abc import ABC, abstractmethod

class employee(ABC):
    def calculate_salary(self, hours_worked, rate_per_hour):
        """Abstract method to be implemented in subclasses"""
        pass 

class manager(employee):
    def calculate_salary(self, hours_worked, rate_per_hour):
        return hours_worked * rate_per_hour
    
manager = manager()
print(manager.calculate_salary(40,50))

print("                      ")

'''5.super() function'''

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound")

class dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        super().sound()
        print(f"{self.name} barks")

dog = dog("blacky" ,"labrador")
dog.sound()