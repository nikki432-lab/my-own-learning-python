'''#1.Create a Class with a Constructor:
Write a class Movie with attributes title and rating using the __init__() constructor.
Define a method to display the movie’s title and rating.
'''

class movie:
    def __init__(self,title,rating):
        self.title = title
        self.rating = rating

    def display_info(self):
        print(f"Movie:{self.title}, Rating:{self.rating}")

m1 = movie("Inception", 8.8)
m1.display_info()

print("                                                   ")

'''Add Default Parameters:
Create a class Employee with attributes name, designation, and salary (default value of salary is 30,000).
Write a method that displays the details of each employee.
Create multiple Employee objects with different values for name and designation, and test the default salary behavior.'''

class employee:
    def __init__(self,name,designation,salary=30000):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print(f"Employee:{self.name}, Designation:{self.designation}, Salary:{self.salary}")
        
emp1 = employee("Alice", "Software Engineer")
emp2 = employee("Bob", "Data Analyst", 45000)
emp3 = employee("Charlie", "Product Manager", 35000)

emp1.display_info()
emp2.display_info()
emp3.display_info()


