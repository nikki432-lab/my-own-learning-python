'''1. Age Verifier:
Ask the user for their age.
If age is valid (number), show in how many years they will be 100 years old.
Handle invalid input gracefully.
'''

def age_verifier():
    age_input= input("Please Enter your age: ")
    try:
        age = int(age_input)
        if age < 0:
            print("Age can't be negative. Please try again.")
        elif age > 150:
            print("That age seems a bit unrealistic. Please enter a valid age.")
        else:
            years_left = 100 - age
            if years_left > 0:
                print(f" You will turn 100 in {years_left} years.")
            elif years_left == 0:
                print("Wow, You're 100 years old this year.!")
            else:
                print(f"You turned 100 {-years_left} years ago.")
    except ValueError:
        print("Invalid input. Please enter your age as a number")

age_verifier()

print("--------------------------------")

'''2.Safe Divider:
Ask two numbers from the user and divide them.
Handle ZeroDivisionError and ValueError.
'''

def safe_divider():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a/b
        print(f"The result of {a}/{b} is {result}.")
    except ZeroDivisionError:
        print("OOPS! Division by zero is not allowed")
    except ValueError:
        print("Invalid input! please enter a numeric value.")

safe_divider()    

'''3.File Reader:
Ask the user for a file name and try to open it.
Show error message if file doesn't exist.
Use finally to print “Program End”.'''

def file_reader():
    try:
        filename = input("Enter the name of the file you want to open: ")
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:\n")
            print("content")
    except FileNotFoundError:
        print("Error: File not found. please make sure the filename is correct")
    finally:
        print("\nProgram End.")

file_reader()