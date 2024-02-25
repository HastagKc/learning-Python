
# 1. Reverse a String: Program to reverse a given string.

msg = 'hello'
reversed_str =''
for i in msg:
    reversed_str =  i + reversed_str
print(reversed_str)


reversed_str2 =''
reversed_str2 = reversed_str2.join(reversed(msg))
print(reversed_str2)


# slicing 
reversed_str3 = ''
reversed_str3 = reversed_str3 + msg[::-1]
print(reversed_str3)