# 5. Program to find the largest among three numbers using nested if statements.

def largest_among_three(num1, num2, num3):
    if(num1 > num2):
        if(num1 > num3):
            print("Num1 is largest: ")
        else:
            print("Num3 is largest: ")
    else:
        if(num3 > num2):
            print("Num3 is largest: ")

        else:
            print("Num2 is largest: ")


largest_among_three(num1=1, num2=3, num3= 45)

    