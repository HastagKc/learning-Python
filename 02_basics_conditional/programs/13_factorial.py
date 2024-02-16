# 13. Program to find the factorial of a number using for loop.
n = int(input("Enter the number to calculate factorial: "))
for i in range(1,n+1):
    n = i * n # 120
    i += 1

print(n)
