# 12. Program to print Fibonacci series up to n terms. 
term = int(input("Enter the term you want to print:"))
# initial value of an variable 
n1 = 0
n2 = 1
count = 0

if(term < 0):
    print("Please enter positive number: ")
else: 
    print("Fibonacci series ")
    while count < term:
        print(n1)
        nth = n1 + n2 
        n1 = n2 
        n2 = nth
        count += 1
 