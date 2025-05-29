    #Homework(part13)lambda functions Recursion and args and kwargs
#1.Lambda Function: Write a lambda function that multiplies two numbers.

multi = lambda x,y:x*y

result = multi(5,3)
print(result)
print("                                          ")
#2.Recursive Function: Write a recursive function that calculates the sum of the first n numbers.

def recursive_sum(n):
    if n==1:
        return 1
    return n + recursive_sum(n-1)

result = recursive_sum(4)
print(result) 

      #factorial(n)
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

result = factorial(5)
print(result)
print("                         ")

#3.Variable-Length Arguments: Write a function that accepts any number of arguments and returns their average.

def average(*args):
    if not args:
        return 0
    return sum(args)/len(args)

result = average(4,8,15,16,23,42)
print(result)

print("                                    ")
     #  and for **kwargs(keyword arguments)

def person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}:{value}")
person(name="Alice", age = 30, profession = "Engineetr")