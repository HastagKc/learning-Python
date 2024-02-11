# Armstrong number is a number that is equal to the sum 
# of cubes of its digits

def is_armstrong_num(num):
    temp = 0
    sum = 0
    while num > 0:
      temp = num % 10 
      temp = temp**3
      sum = sum + temp
      num = int(num / 10)
      
    return sum



num = 153
if(num == is_armstrong_num(num)):
   print("Armstrong Number")
else: 
   print("Not a armstrong Number")



        
