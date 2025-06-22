'''1.Create a File and Write
Ask user for 3 friend names.
Write them into friends.txt, one per line.'''

friends = []
for i in range(3):
    name = input(f'Enter the name of friend {i + 1}: ')
    friends.append(name)

with open ("friends.txt", "w") as file:
    for friend in friends:
        file.write(friend + "\n")

print("Friend names have been saved to friends.txt.")

'''2. Append Marks
Ask for student name and marks.
Append the info to marks.txt in this format: Ravi - 85'''

student_name = input("Enter the students name: ")
marks = input("Enter the marks: ")

with open("marks.txt", "a") as file:
    file.write(f"{student_name} - {marks}\n")

print("Student info appended to marks.txt")


'''3. Read and Count Lines
Read any file and count how many lines it has.
Example: How many students are listed?
'''

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()
        line_count = len(lines)
    
    print(f"The file '{filename}' has {line_count} lines.")

except FileNotFoundError:
    print(f"file '{filename}' not found. Please check the name and try again!")


'''4. Search From File
Write a program that searches for a name in friends.txt
If found, print "Found!" else "Not Found!"'''

search_name = input("Enter the name to search: ")

try:
    with open("friends.txt", "r") as file:
        friends = [line.strip() for line in file]

        if search_name in friends:
            print("Found!")
        else:
            print("Not Found!")

except FileNotFoundError:
    print("friends.txt not found. Please make sure the file exist.")