'''1.Create a Class:
Write a class Mobile with attributes brand and price.
Create two objects of the class and display their attributes using a method.'''

class mobile: #class
    def __init__(self,brand,price): #attributes
        self.brand = brand
        self.price = price

    def display_details(self): #method
        print(f"Brand:{self.brand}, price: {self.price}")

mobile1 = mobile("samsung",45000) #objects
mobile2 = mobile("apple", 90000)

mobile1.display_details() #displaying attributes
mobile2.display_details()

print("                                         ")
'''2.Method Definition:
Define a class Student with attributes name and marks.
Write a method display_info() that prints the student's name and marks.
Create multiple objects of the Student class and call the method on each.'''

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"Name:{self.name}, Marks:{self.marks}")

student1 = student("Nikhil", 95)
student2 = student("Akhil", 90)
student3 = student("Meera", 88)

student1.display_info()
student2.display_info()
student3.display_info()
        

    
