#1.Greet Function: Write a function greet() that takes no arguments and prints a greeting message.

def greet():
    print("Hello! Hope you're having a good day.")
greet()

print("                                       ")
#2.Parameterized Greet: Write a function greet_user() that takes a name as input and prints a custom greeting.

def greet_user(name):
    print(f"Hello {name}! Welcome! hope you're having a fantastic day")

greet_user("Nikhil")
print("                                       ")
#3.Sum Function: Write a function add_numbers(a, b) that returns the sum of two numbers. Call this function with different values.

def add_numbers(a,b):
    return a+b
sum1=add_numbers(5,3)
sum2=add_numbers(-2,7)
sum3 = add_numbers(10.5,4.5)

print(sum1)
print(sum2)
print(sum3)
