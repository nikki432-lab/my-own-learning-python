#Conditional statements (if elif and else)homework 8(youtube)
#Nested IF statements

gender = input("Enter your gender: ")
age = int(input("Enter your age: "))



if gender == "female":
     print("Eligible for a free bus ticket")
else:
    if age<=5 :
        print("Eligible for a free bus ticket")
    elif age>=60:
        print("Eligible for seinor citizen discount")
    else:
        print("You must pay the full price")

print("                               ")

#2 Get ticket price based on age

age = int(input("Enter your age: "))

if age <= 5:
          print("Eligible for a free bus ticket")

elif age>=60:
     print("Eligible for seinor citizen discount")

else:
    print("You must pay the full price")


print("                               ")
#3Meal time checker

time = int(input("Enter your time: "))

if time == 8 :
    print("Its breakfast time")
elif time==13 :
    print("Its lunch time")
elif time== 20:
    print("Its dinner time")
else:
    print("Its not eating time")
print("                               ")
#4Simple Eligibility Check

age = int(input("Enter your age: "))

if age <=18:
    print("Student Membership")
elif age>=60:
    print("Senior Citizen Membership")
else:
    print("Regular Membership")


    


    


    
    

    
