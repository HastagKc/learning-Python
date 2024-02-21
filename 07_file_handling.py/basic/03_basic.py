

# delete file using file handling 
file2 = open('delete.txt','a')

import os
if os.path.exists('delete.txt'):
    os.remove('delete.txt')

else:
    print('file is not exist')