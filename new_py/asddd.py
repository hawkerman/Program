import os
import sys
import Npp
filePathSrc="D:\\Program\\aa" # Path to the folder with files to convert
for root, dirs, files in os.walk(filePathSrc):
    for fn in files: 
        if fn[-4:] == '.txt': # Specify type of the files
            Npp.notepad.open(root + "\\" + fn)      
            Npp.notepad.runMenuCommand("Encoding", "Convert to UTF-8")
            Npp.notepad.save()
            Npp.notepad.close()