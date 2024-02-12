# Dictionaries 
# are an unordered collection of key-value pairs
# mutable 

my_dict = {"key1":"Value1", "key2": "value2"}

person = {"name":"kshittiz", "address":"Kathmandu"}

# accessing key value from my_dict
print(my_dict["key1"])

print(f'Name: {person["name"]}')
print(f'Address: {person["address"]}')

# insertion
person['gender'] = 'male'

print(person) 

# update 
person['address'] = 'kalanki'
print(f'Update address: {person["address"]}')

# deletion in dict 
del person["address"]
print(person)

removed_value = my_dict.pop('key2')
print(removed_value)
print(my_dict) 


# methods in dictionaries



new_dict = {'name':'jhon', 'age':22, 'address':'New york', 'gender':'male'}

keys_list = new_dict.keys()       # Returns a view of all keys in the dictionary
values_list = new_dict.values()   # Returns a view of all values in the dictionary
items_list = new_dict.items()     # Returns a view of all key-value pairs (tuples) in the dictionary

for i in keys_list:
    print(i)

for i in items_list:
    print(i)
    print(type(i))