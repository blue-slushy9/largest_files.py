# os.path.getsize() allows us, in this case, to find the files that take up
# the most space on our system;
from os import path

# This is the filepath from which we will begin our scan;
path = 'C:\\users\\slushy\\'

# getsize() method will be used to retrieve the size of every file in our
# path, one by one;
file_size = path.getsize()



#print(file_size)



