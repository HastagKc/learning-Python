fruits = ['Banana', 'Apple','Orange','Grapes']
for i,fruit in enumerate(fruits,1):
    print(f'{i}: {fruit}')


# strip()
message = "    good morning           "
print("Before strip functon" ,len(message))
print("After strip functon",len(message.strip()))