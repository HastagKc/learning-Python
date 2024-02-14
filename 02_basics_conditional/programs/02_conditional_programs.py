# 1. Program to check if a number is positive, negative, or zero.

print("Question - 1")
def postiveAndNegative(num):
    if num > 0:
        print('Positive')
    elif num == 0:
        print('Zero')
    else:
        print('Negative')


# 2. Program to find the maximum of three numbers
def programToMaxThreeNumber(num1, num2, num3):
    if num1 > num2 and num1 > num3: 
        print("Num1 is greater")
    elif num2 > num3 and num2 > num1:
        print('Num2 is greater')
    else:
        print('Num3 is greater')


def max_number(num1, num2, num3):
    # lets consider num1 as greater number first 
    max_num = num1
    if num2 > max_num:
        max_num = num2
    elif num3 > max_num:
        max_num = num3
    return max_num

    
# callling function 
# num1 = input("Enter number: ")
# postiveAndNegative(int(num1))
        

num1 = 95
num2 = 22 
num3 = 15
programToMaxThreeNumber(num1, num2, num3)

max_value = max_number(num1=10, num2=30, num3=45)
print("Maximum number: ", max_value)

