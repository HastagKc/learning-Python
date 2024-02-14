# # 11. Program to find the sum of digits of a number using while loop.

# num = 324 
# sum = 0
# while num > 0:
#   single_digit = num % 10 # 324 % 10 = 4
#   sum = sum + single_digit # 0 + 4
#   num = num // 10 # 324 // 10 => 32 

# print("Sum of Digit:",sum)


# solving by creating function 
def sumOfDigits(number):
  total = 0
  original_num = number
  
  while original_num > 0:
    digit = original_num % 10
    total = total + digit
    original_num = original_num // 10 
  return total
  
num = int(input("Enter any digit number: "))
print("Sum of digits are: ",sumOfDigits(num))
  