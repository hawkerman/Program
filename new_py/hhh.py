import os;
import sys;
filePathSrc="D:/Program/aa" # Path to the folder with files to convert
for root, dirs, files in os.walk(filePathSrc):
    for fn in files: 
        if fn[-4:] == '.txt': # Specify type of the files
            notepad.open(root + "\\" + fn)      
            notepad.runMenuCommand("Encoding", "Convert to UTF-8")
            notepad.save()
            notepad.close()