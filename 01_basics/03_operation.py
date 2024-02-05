# Arithmetics operators 
addition = 5 + 3
subtraction = 10 - 4
multiplication = 2 * 3
division = 8 / 2
modulus = 15 % 7
exponentiation = 2 ** 3

# Displaying Results
print("Arithmetic Operators:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)


# Comparison Operators
# comparison operators provides output in boolean from
equal_to = (5 == 3)
not_equal_to = (10 != 4)
greater_than = (2 > 3)
less_than = (8 < 2)
greater_than_or_equal = (15 >= 7)
less_than_or_equal = (2 <= 3)

print("\nComparison Operators:")
print("Equal to:", equal_to)
print("Not equal to:", not_equal_to)
print("Greater than:", greater_than)
print("Less than:", less_than)
print("Greater than or equal to:", greater_than_or_equal)
print("Less than or equal to:", less_than_or_equal)

# logical operators
# and 
# or 
# not 

and_operator = True and False # False 
or_operator = True or False # True
not_operator = not True # False

print("\nLogical Operators:")
print("And Operator:", and_operator)
print("Or Operator:", or_operator)
print("Not Operator:", not_operator)

# Assignment operators 
num1 = 22
num1 += num1  # num1 = num1 + 3

num2 = 22
num2 -=10
print("\nAssignment Operators:")
print("Value of num1 after increment:", num1)
print("Value of num2 after decrement:",num2)

# Identity Operators:
# Test if two variables reference the same object.

obj = [1, 2, 3]
obj2 = obj
is_same = (obj is obj2)
print(is_same)

# member Operators 
num_list = [2, 3, 85, 500]
is_in_list = (50 in num_list)
print("is in the list: ", is_in_list) # False


# Example of an expression
a = 5
b = 3
result = (a + b) * 2