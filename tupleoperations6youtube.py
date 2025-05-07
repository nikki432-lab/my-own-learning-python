#homework6(youtube)
#TUPLES AND SETS IN PYTHPO
#Tuple Operations
#create a tuple with 5 elements

my_tuple = (1,2,3,4,5)
print(my_tuple)

#Try to modify one of the elements (ERROR occurs because tuple cant be modified)
'''
my_tuple[1] = 25
print(my_tuple)
'''

#perform slicing on the tuple to extract the second and third elements

sliced_tuple = my_tuple[1:3]
print(sliced_tuple)

#concatenate the tuple wiht another tuple

new_tuple = my_tuple + (6,7,8,9,10)
print(new_tuple)
