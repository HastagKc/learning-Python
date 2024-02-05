# Number types in python 
# integer, float and complex types 

# int
int_type = 22

# float 
float_type = 22.000

# complex type
complex_type = 3+5j 

print(type (int_type)) # <class 'int'>
print(type(float_type)) # float type 
print(type(complex_type)) # complex type 

# mathmatical operation 
addition_result = 22 + 22.05
print(addition_result)

subtraction_result = 75 - 22.5
print(subtraction_result) 

multiplication_result = 10 * 22
print(multiplication_result) 

division_result = 22 / 2
print(division_result)

modulus_result = 22 % 3 
print(modulus_result)

exponentation_result = 2**3
print(exponentation_result)


# type conversion 
int_value = 22 
int_to_float = float(int_value)
print(int_to_float) # 22.0

float_value = 25.075
float_to_int = int(float_value) # decimal part get remove 
print(float_to_int) # 25



# int and float to complex 
int_num = 22
int_to_complex = complex(int_num)
print("Int to complex :", int_to_complex) # 22+0j 


float_num = 22.05
float_to_complex = complex(float_num)
print("Float to complex : ", float_to_complex)

'''

When converting a complex number to an integer or a float in Python, 
you usually extract the real or imaginary part depending on your needs.
Here's an example demonstrating both conversions:

'''


complex_value = 2+3j
complex_to_float = float(complex_value.imag)
print(complex_to_float)


complex_to_int = int(complex_value.real)
print(complex_to_int)


# Built-in Functions
abs_result = abs(-5)
rounded_num = round(3.54149, 3)
max_value = max(4, 8, 2, 200)
min_value = min(4, 8, 2, -10)

print("abs_result: ", abs_result)
print("rounded_num: ",rounded_num)
print("max_value: ",max_value)
print("min_value: ",min_value)