#Homework 9     WHILE LOOPS

#1.Basic counting wiht while loop

i = 0
while i<=10:
    print(i)
    i+=1

#2 ODD number printer

i = 1
while i<=20 :
    print("ODD Numbers:", i)
    i+=2


#3 Ticket booking simulation:

available_seats = 8

while available_seats>0:
    print(f"seats available: {available_seats }")
    input("Press Enter to book a seat: ")
    available_seats-=1

print("All seats are booked")


#4 Countdown Time

import time
count=10
while count > 0:
    print(count)
    time.sleep(1)
    count -= 1
print("Happy New Year!")
