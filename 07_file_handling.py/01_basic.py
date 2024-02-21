# opening file 
file = open('E:/#LearningPython/07_file_handling.py/01_basic.txt', 'r')
# print(file)

# Reading from a file 
content = file.read()
print(content)

# write to a file 
# to use write method we should open with write mode 
#  write mode overide existing content 
file = open('E:/#LearningPython/07_file_handling.py/01_basic.txt', 'w') 
file.write('Hello from kc ')


# append mode 
# append method will not replace existing file content 
file = open('E:/#LearningPython/07_file_handling.py/01_basic.txt', 'a') 
file.write('I am from kathmandu')

# close file 
file.close()