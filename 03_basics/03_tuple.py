# tuple in python are ordered collections of elements similar to lists, but they are 
# immutable, meaning thier element cannot be changed after creation 

# tuples are commonly used to stored related piece of information together 

#creating my tuple 
my_tuple = (12,32,'python',False)
print(my_tuple)

#insertion and updation cannot be happen, because tuple is immutable so once it was create it will not change of insert value
next_tuple = (10,30,50,5,5)
updated_tuple = my_tuple + next_tuple
print(updated_tuple)

for x in updated_tuple:
    print(x)

# Accessing element from tuple 
print(next_tuple[0])
print(next_tuple[4])


# method in python 
# count()
# count() method count the total number of occurrence of any number in tuples 

tuple_example = (12,22,23,"kshittiz", "ram",22)
print(f'count method of tuple: {tuple_example.count(22)}')

#  index() this method reture index of first occurence of elements

print(f'index of 22: {tuple_example.index(22)}')

# len() method will return length of tuple 
print(f'length of tuple: {len(tuple_example)}')

# slicing method used to slice the tuple or extract elment from tuple 
print(tuple_example[1:3])

# concatenation method 
# we can add two tuple 
tuple1 = (22,25,23,45,85)
tuple2 = (25,85,65,45,75)

modifiy_tuple = tuple1 + tuple2
print(modifiy_tuple)

