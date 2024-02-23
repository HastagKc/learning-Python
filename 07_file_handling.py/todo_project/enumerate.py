
# enumerate is a built-in Python function that allows you to loop over an iterable 
# (such as a list, tuple, or string) while also keeping track of the index of each 
# item in the iterable. It returns an enumerate object, which yields pairs containing 
# the index and the value from the iterable.


fruits = ['Banana', 'Apple','Orange','Grapes']
for i,fruit in enumerate(fruits,1):
    print(f'{i}: {fruit}')

# strip()
# The strip() method in Python is used to remove leading and trailing whitespace characters 
# (such as spaces, tabs, and newline characters) from a string. It doesn't remove whitespace
# within the string, only at the beginning and end. 
    
message = "    good morning           "
print("Before strip functon" ,len(message))
print("After strip functon",len(message.strip()))