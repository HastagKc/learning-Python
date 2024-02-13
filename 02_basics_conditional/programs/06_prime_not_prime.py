#6. Program to check if a number is prime or not.
num = 16 
flag = False
if(num == 1):
    print(1,"is not a prime number")

elif(num > 1 ):
    for i in range(2, num):
        if(num % i == 0):
            flag = True
            break

if(flag == True):
    print("Not a prime Number:")
else: 
    print("Prime Number: ")

