# Open a file
import os

fo = open("D:/Program/new_py/02.txt", "r")
print ("Name of the file: " , fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line


print(type(fo))

line = fo.readlines()
print ("Read Line: %s" % (line))

line = fo.readlines(2)
print ("Read Line: %s" % (line))


# Close opend file
fo.close()
