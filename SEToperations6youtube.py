#SETS OPERATIONS

#1 create two sets:

my_fruits = {"apple", "banana", "mango", "orange"}
friend_fruits = {"apple", "kiwi", "mango", "grape"}
print(type(my_fruits))
print(type(friend_fruits))
print(my_fruits)
print(friend_fruits)

#2 Find the union (all unique elements from both sets)

union_set = my_fruits.union(friend_fruits)
print("Union:", union_set)

#3 find the intersection(common values)

intersection_set = my_fruits.intersection(friend_fruits)
print("Intersection:", intersection_set)

#4 find the difference(elements in my_fruits but not in freind_fruits)

difference_set = my_fruits.difference(friend_fruits)
print("Difference:", difference_set)


difference_set1= friend_fruits.difference(my_fruits)
print("Difference 1:", difference_set1)

#5 find the symmetrical difference

symmetrical_diff = my_fruits.symmetric_difference(friend_fruits)
print("Symmetrical Difference:", symmetrical_diff)

symmetrical_diff1 = friend_fruits.symmetric_difference(my_fruits)
print("Symmetrical Difference 1:", symmetrical_diff1)

#6 add a new fruit to my_fruits:

my_fruits.add("pineapple")
print("Updated my fruits:", my_fruits)

#7 remove a fruits using remove() and discard()

my_fruits.remove("banana")
print("After remove :", my_fruits)

my_fruits.discard("orange")
print("After discard :", my_fruits)

'''
my_fruits.remove("peach")
print("After remove :", my_fruits) #Error occurs if fruit not found in set
'''
my_fruits.discard("peach")
print("After discard :", my_fruits) #No Error if fruit not found
