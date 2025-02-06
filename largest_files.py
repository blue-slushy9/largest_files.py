# os.path.getsize() allows us, in this case, to find the files that take up
# the most space on our system;
from os import walk, path

def find_largest_files(path, num=10):

    file_sizes = {}

    for root, dirs, files in walk(path):
        for file in files:
            filepath = path.join(root, file)
            size = path.getsize(file)
            file_sizes[size] = path 




# This is the filepath from which we will begin our scan;
path = 'C:\\users\\slushy\\'

# getsize() method will be used to retrieve the size of every file in our
# path, one by one;
file_size = path.getsize()

print(file_sizes)



