#Formatted stings and concatenate strings
print("love")
Boy_Name = input("Boy Name: ")
Boy_age = int(input("Boy age: "))
girl_name = input("girl name: ")
girl_age = int(input("girl age: "))

# using abs because sometimes boy might be younger(single line comment)
"""
using abs because
sometimes boy might be younger(triple quotes for multiline comments)
"""
age_diff = abs(Boy_age - girl_age)#(abs= absolute value)
print(Boy_Name + " Loves " + girl_name + ".age difference is" + str(age_diff))
print(f"{Boy_Name} loves {girl_name}. age difference is {age_diff}")

