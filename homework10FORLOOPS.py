                   #HomeWORK 10 (FOR LOOPS)
'''1.Multiples of 3:

Write a for loop that prints all multiples of 3 between 1 and 30.(start,stop,step)method
'''
for num in range(3,31,3):
    print(num)

'''2.Sum of First 10 Numbers:

Write a program using a for loop that calculates the sum of numbers from 1 to 10.
'''

total_sum=0
for num in range(1,11):
    total_sum+=num
print("sum of numbers from 1 to 10:",total_sum)

'''
3.Print Your Name Letter by Letter:

Write a program that takes your name as input and prints each letter of your name using a for loop.
'''

name=input("Enter your name: ")
for letter in name:
    print(letter)

'''4.Count Vowels in a String:

Write a program that counts how many vowels are in a given string using a for loop.
'''

text=input("Enter a string: ")
vowels="aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count+=1
print("Numbers of vowels in the string: ", vowel_count)
