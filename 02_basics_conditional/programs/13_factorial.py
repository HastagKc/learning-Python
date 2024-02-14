# 13. Program to find the factorial of a number using for loop.
n = int(input("Enter the number to calculate factorial: "))
fact = 1
for i in range(1,n):
    n = i * n # 120
    fact = n # 120
    i += 1

print(fact)
