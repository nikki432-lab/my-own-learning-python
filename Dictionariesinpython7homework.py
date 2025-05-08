#Homework-7   #Dictionaries in pyhton
#Basic dictionaries Operations

#step 1 - craete a dictionary with 5 cities and their famous dishes

karnataka_dishes = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore pak",
    "Mangaluru": "Neer Dose",
    "Hubballi": "Girmit",
    "Shivamogga": "ragi Mudde"
}
print(type(karnataka_dishes))

dictionary = dict(karnataka_dishes)
print(dictionary)

#step 2 - Add a new city and its dish

karnataka_dishes["Udupi"] = "Masala Dosa"
print(karnataka_dishes)

#Step 3 - update the dish for bangalore

karnataka_dishes["Bengaluru"] = "Benne Masala Dosa"
print(karnataka_dishes)

#Step 4 - Remove one city from the dictionary

karnataka_dishes.pop("Hubballi")
print(karnataka_dishes)

#Step 5 - print all city names using keys() method

print("karnataka_dishes:", karnataka_dishes.keys())

#step 6 - print all dishes using the values() method

print("karnataka_dishes:", karnataka_dishes.values())

print("                             ")

#Nested Dictionary Practise(simple)
#Create a dictionary storing details of two friends

friends_info = {
    "friend1": {"Name":"Aryan", "Favorite subject": "Mathematics", "Favorite food": "Paneer tikka"},
    "friend2": {"Name":"Meera", "Favorite subject": "Science", "Favorite food": "Masala Dosa"}
}
print(friends_info)

#Step 2- Acess and print the favorite food of one friend

print("Favorite food:" , friends_info["friend2"]["Favorite food"])
print("Favorite food:" , friends_info["friend1"]["Favorite food"])


