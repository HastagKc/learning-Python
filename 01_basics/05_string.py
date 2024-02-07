# Strings in Python are sequences of characters, enclosed within either single quotes
# (') or double quotes ("). They are immutable, meaning once defined, their contents cannot be 
# changed. Strings support various operations, including concatenation, slicing, formatting, and
# more.

# declaration and initizition of string 
message = "Namaste from Nepal."
discription = "Nepal is beautiful country"

# concatenation 
full_message = message+ " "+ discription
print(full_message)


# String Indexing and Slicing:
user_name = "kshittiz"
print(user_name[0]) # k
print(user_name[-1]) # z

print(user_name[:5]) # kshit
print(user_name[1:]) # shittiz
print(user_name[1:5]) # shit index 5 will not include 
print(user_name[::2]) # print all laternative words 


# String Length
dis = "I like mountain bikes"
print(len(dis))

# string method 
message = "Hello, World!"
uppercase = message.upper()           # "HELLO, WORLD!"
lowercase = message.lower()           # "hello, world!"
capitalized = message.capitalize()    # "Hello, world!"
replaced = message.replace("World", "Python")   # "Hello, Python!"

# string formating 
name = "Kshittiz"
age = 22
formatted_string = f"My name is {name} and I'm {age} years old."
print(formatted_string)

num1 = 22
num2 = 23 
result=f"Sum of {num1} + {num2} = {num1 + num2}"
print(result)

result2 = "The sum of {} + {} = {}".format(num1, num2, num1 + num2)
print(result2)

# Escape Characters:
escaped_string = "This is a newline \nand this is a tab \tcharacter."
print(escaped_string)
