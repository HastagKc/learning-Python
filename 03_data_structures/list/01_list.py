
'''
In Python, a list is a collection of items enclosed within square brackets [ ]. Lists are ordered and mutable, meaning you can change, add, and remove elements after the list is created. Lists can contain elements of different data types, including integers, floats, strings, and even other lists. 

'''

# create list 
fruits_list = ['apple','banana','grapes']

# adding value in the list 
fruits_list.append('orange')
fruits_list.extend(['football','cricket','hokey'])

# diplaying value from list 
print('before:===============>')
for i in fruits_list:
    print(i)

# update 
fruits_list[0] = 'baseball'
print('after:====================>')
for i in fruits_list:
    print(i)


# remove from list 
fruits_list.remove('banana')
fruits_list[0] = 'baseball'
print('after removing :====================>')
for i in fruits_list:
    print(i,end=" ")


