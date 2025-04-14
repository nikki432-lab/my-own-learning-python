num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > 10 and num2 > 10:
   print("Both numbers are greater than 10.")
else:
    print("Both numbers are NOT graeter than 10.")

if num1 < 5 or num2 < 5:
    print("At least one of the numbers is less than 5.")
else:
    print("Neither number is less than 5.")

if not num1 > num2:
    print("The first number is NOT greater than the second")
else:
    print("The first number is greater than the second")
    
             
             
