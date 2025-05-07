#Tuple and Set comparison

#1 create a list and convert both into tuple and set:

my_list = [1,2,3,4,5]

my_tuple = tuple(my_list)
my_set = set(my_list)

print("Tuple:" , my_tuple)
print("Set:" , my_set)

#2 Try adding new elements
'''
my_tuple.add(6)
print("Updated tuple:", my_tuple)
Error occurs because Tuples cannot be modified after creating
'''

#adding an element into tuples by using concatenation

my_tuple += (6,)
print("Updated tuple:", my_tuple)# concatenation creates new tuple instead of modifying

#addinf an element in a set

my_set.add(6)
print("Updated Set:", my_set) #sets can be modified after creating but order may be varies(Unordered)


