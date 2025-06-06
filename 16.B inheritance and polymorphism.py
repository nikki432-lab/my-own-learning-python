'''1.Inheritance:
Create a base class Vehicle with a start method. Then create a subclass Bike with an additional ride() method.
Demonstrate how the Bike can use both start and ride.'''

class vehicle:
    def start(self):
        return "Vehicle is starting..."
    
class bike(vehicle):
    def ride(self):
        return "Bike is being ridden..."
    
my_bike = bike()
print(my_bike.start())
print(my_bike.ride())

print('                    ')

'''2.Polymorphism:
Implement a Shape class and derive Circle and Rectangle classes with a method calculate_area. Each class should calculate area differently based on its shape.
Create a loop to calculate areas for both Circle and Rectangle objects.'''

import math

class shape:
    def calculate_area(self):
        raise NotImplementedError("Subclass must implement this method")
    
class circle(shape):
    def __init__(self,radius):
        self.radius = radius 

    def calculate_area(self):
        return math.pi * self.radius**2
    
class rectangle(shape):
    def __init__(self,width,height):
        self.width = width 
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
shapes = [circle(5), rectangle(4,6)]

for shape in shapes:
    print(f"Area: {shape.calculate_area():.2f}")

