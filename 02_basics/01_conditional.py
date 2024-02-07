# conditional statement 
# conditional statement in python allow you to execute different block 
# based on certain conditions

# if statement 
x = -90
if(x > 0): 
    print("X is positive number")


# if-else 
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