import os
import sys
from Npp import notepad # import it first!

filePathSrc="D:\\Program\\aa" # Path to the folder with files to convert
for root, dirs, files in os.walk(filePathSrc):
    for fn in files: 
        if fn[-4:] == '.txt': # Specify type of the files
            notepad.open(root + "\\" + fn)      
            notepad.runMenuCommand("Encoding", "Convert to UTF-8")
            # notepad.save()
            # if you try to save/replace the file, an annoying confirmation window would popup.
            notepad.saveAs("{}{}".format(fn[:-4], '_utf8.txt')) 
            notepad.close()