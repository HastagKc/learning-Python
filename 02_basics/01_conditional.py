# conditional statement 
# conditional statement in python allow you to execute different block 
# based on certain conditions

# if statement 
x = -90
if(x > 0): 
    print("X is positive number")


# if-else 
# if one condition if checked it will not check other condition in if else
x = 10
if(x>0):
    print(x, "is postive number")
else:
    print(x,"is negative number")



# Example of nested if statements
if x > 0:
    if x % 2 == 0:
        print("x is a positive even number")
    else:
        print("x is a positive odd number")
else:
    print("x is non-positive")

    
# Example of ternary conditional expression
result = "positive" if x > 0 else "non-positive"
print("x is", result)


# Remember
x = 10
if x <= 10:
    print("x is less or equal to 10")
elif x == 10:
    print("x is equal to 10")  # This block will not be executed
else:
    print("x is greater than 10")