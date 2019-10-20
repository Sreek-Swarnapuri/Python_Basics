#Text files are easiest to manipulate
myfile = open("openfile.txt")

#We can specify a mode when opening a file, this would be a second parameter for open function
# r -- read - reads files, default if no second argument is provided
# w -- write  - writes to files and rewrites over existing data
# a -- append - adds data to the end of the file.
# Adding "b" to the mode opens the file in binary mode for non text files

open("openfile.txt","r")

open("openfile.txt","w")

open("openfile.txt","a")

open("openfile.txt","rb")


#Once the file is open we should close it using close method.
file = open("openfile.txt","r")

file.close()
