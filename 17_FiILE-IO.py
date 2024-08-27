# Chapter - 17 FILE in python

#----------- python File handling

#----------- creating a new file

import os
# delete a file
os.remove("demo.txt")

f = open("demo.txt", "r")
# writting a file
# f.write("I Love Python\n")
# f.write("I Love JavaScript")

# append/add a new file
# f.write(" and javascript")

# read a file
# x = f.read()
# print(x)

# readline
# first_readline = f.readline()
# second_readline = f.readline()
# print(first_readline)
# print(second_readline)

f.close()


# "x" - Create - will create a file, returns an error if the file exist
# "w" - Write - will overwrite any existing content
# "r" - Read the file
# "a" - Append - will append to the end of the file
# import os
# To delete an entire folder, use the os.rmdir() method