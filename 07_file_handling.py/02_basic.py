# file handling is the key function for working  with files in python 
# there are different mode some of them are 

# 'r' => Read mode (default value)
# Open file for reading, error if the does not exist 

# 'a' => append 
# open a file for appending, create the file it does not exist 

# 'w' => write 
# open a file for writing, create the if does not exits 

# 'x' => create
# create the specified file, returns an error if the file exists

# 't' text mode 
# default value 

# 'b' binary mode (example: image)

# #syntax 
# f = open('filename.txt')

# # or 
# f = open('filename.txt', 'rt')

# open file
# we can open file with open() function 
# opening file and read with read function
f = open('E:/#LearningPython/07_file_handling.py/02_basic.txt','r')
# print(f.read())


# readline()
# this function return single line form file 

# print(f.readline())

# looping in file 
# for text in f:
#     print(text)
    
# f.close()



# write in file 


# To write in an existing file, we have to add mode or parameter in open function 

# 'a' => append will append text to the end of the file 
# 'w' => write will over write any existing content 

file = open('E:/#LearningPython/07_file_handling.py/02_basic.txt','w')
file.write('Overwrite all data')
# print(file.read()) # this will not support in write mode 
file.close()

#  to do so you have to re open file in read mode 
file = open('E:/#LearningPython/07_file_handling.py/02_basic.txt','r')
print(file.read())
file.close()



# both w and a mode create file if it is not exist in the same folder where the program
# file located 
# append mode 
file2 = open('02_basic_file2.txt','a')
file2.write('Appending text in file2 \n')
file2.close()

# reopen
file2= open('02_basic_file2.txt','r')
print(file2.read())
file2.close()


