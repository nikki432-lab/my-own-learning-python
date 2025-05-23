                        #Part- 11 Homework
# Lists and Dictonaries with for loops , List Comprehension and Dictionary Comprehension

#1.List Manipulation:

#Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

kannada_foods = [ "idly", "dosa", "chitranna", "palou", "ragi mudde", "puri"]

uppercase_foods = [food.upper() for food in kannada_foods]

print(uppercase_foods)

#2.Sum of Prices:

#Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.

items_prices = {
    "mango":30,
    "banana":10,
    "milk":50,
    "bread":40,
    "eggs":60
}
total_price=0

for price in items_prices.values():
    total_price+=price

print("Total price of all items:", total_price)

#3.List of Squares:

#Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.

l=[l**2 for l in range(1,11)]
print(l)

#4.Student Data Task:

#Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.

students = [
    {"name": "Aarav", "age": 16, "marks": 85},
    {"name": "Meera", "age": 17, "marks": 92},
    {"name": "Raj", "age": 15, "marks": 78}
]

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

#5.Dictionary Comprehension:

#Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.

kannada_cities = {
    "bengaluru":85,
    "mysuru":13,
    "mangaluru":5,
    "hubballi":12,
    "belagavi":6,
    "kalaburgi":11,
    "davanagere":5
}

small_cities={city:pop for city, pop in kannada_cities.items() if pop<=10}

print(small_cities)

large_cities={city:pop for city, pop in kannada_cities.items() if pop>=10}

print(large_cities)

#6.Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:
'''
Prints the entire matrix row by row.
Prints the sum of each row in the matrix.
Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Matrix:")
for row in matrix:
    print(row)
print("\nsum of each row:")
for row in matrix:
    print(f"Sum of {row}={sum(row)}")
    




