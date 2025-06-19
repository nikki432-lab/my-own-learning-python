#1.S-Single responsibility priciple(SRP)
'''ex:-SRP Practice: Create a Book class that only stores details.
 Create another class that prints book details.'''

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.year = year
        self.author = author

class Bookprinter:
    def print_book(self, book):
        print(f"Ttile: {book.title}")
        print(f"Author: {book.author}")
        print(f"Year: {book.year}")

b = Book("To kill a mocking bird", "Harper Lee", 1960)
printer = Bookprinter()
printer.print_book(b)

#2. Open/Closed principle(OCP)
'''OCP Practice: Build a billing system that calculates tax based on ProductType.
 Add Food, Electronics, etc., using subclasses.'''

from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, name ,price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_tax(self):
        pass

class Food(Product):
    def calculate_tax(self):
        return self.price * 0.05
    
class Electronics(Product):
    def calculate_tax(self):
        return self.price * 0.18
    
class Clothing(Product):
    def calculate_tax(self):
        return self.price * 0.12
    
class Billingsystem:
    def generate_bill(self, product):
        tax = product.calculate_tax()
        total = product.price + tax
        print(f"product: {product.name}")
        print(f"price: ${product.price}")
        print(f"tax: ${tax}")
        print(f"Total: ${total}")

items = [
    Food("Bread", 40),
    Electronics("Headphones", 1500),
    Clothing("T-shirt", 500)
]
  
bill = Billingsystem()
for item in items:
    print("--------")
    bill.generate_bill(item)

print("-----------------------------------")

#3.LSP - Liskov substitution principle(LSP)
'''LSP Practice: Write a class Vehicle and subclasses like Bike, Boat.
 Avoid breaking behavior.'''

class Vehicle(ABC):
    def __init__(self, name):
        self.name= name 
    
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Bike(Vehicle):
    def start_engine(self):
        print(f"{self.name}: Starting the engine with a kick or button.")

    def move(self):
        print(f"{self.name}: Riding on the road")

class Boat(Vehicle):
    def start_engine(self):
        print(f"{self.name}: Starting the boat's engine")
    
    def move(self):
        print(f"{self.name}: Sailing in water")
        
if __name__ == "__main__":
    Yamaha = Bike("Yamaha R15")
    Yamaha.start_engine()
    Yamaha.move()

    ferry = Boat("City ferry")
    ferry.start_engine()
    ferry.move()

print("______________________________")

#4. Interface segregation priniciple(ISP)

#Example

from abc import ABC, abstractmethod

class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass
class Sailable(ABC):
    @abstractmethod
    def sail(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Car(Drivable):
    def drive(self):
        print("Driving on the road")

class Boat(Sailable):
    def sail(self):
        print("Sailing on the water")

class Plane(Flyable, Drivable):
    def drive(self):
        print("Taxiing on the runway")
    
    def fly(self):
        print("Flying in the sky")

if __name__ == "__main__":
    honda = Car()
    honda.drive()

    Yacht = Boat()
    Yacht.sail()

    boeing = Plane()
    boeing.drive()
    boeing.fly()

print("---------------------------------")

#5. Dependency inversion principle(DIP)
'''ex:-DIP Practice: Make a HomeAppliance system where high-level 
class Remote works with abstract Appliance, and you can pass TV, AC, etc.'''

from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class TV(Appliance):
    def turn_on(self):
        print("TV is now ON")

    def turn_off(self):
        print("TV is now OFF") 

class AC(Appliance):
    def turn_on(self):
        print("AC is now COOLONG.")

    def turn_off(self):
         print("AC is now OFF")

class Remote:
    def __init__(self, appliance:Appliance):
        self.appliance = appliance

    def press_on_button(self):
        self.appliance.turn_on()
    
    def press_off_button(self):
        self.appliance.turn_off()

if __name__ == "__main__":
    living_room_tv = TV()
    bedroom_ac = AC()

    remote_for_tv = Remote(living_room_tv)
    remote_for_ac = Remote(bedroom_ac)

    remote_for_tv.press_on_button()
    remote_for_tv.press_off_button()

    remote_for_ac.press_on_button()
    remote_for_ac.press_off_button()