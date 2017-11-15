import os
import sys
import encodcs
filePathSrc="D:/Program/aa" # Path to the folder with files to convert
i=1
for root, dirs, files in os.walk(filePathSrc):
	for fn in files: 
		print("this is",i)
		i+=1
		#print("Name of the root: ",root)
		#print("Name of the dirs: ",dirs)
		#print("Name of the files: ",files)
		print("Name of the fn: ",fn)
		if fn[-4:] == '.txt':
			print('yes')
			fpath = root + "/" + fn
			#print(type(fpath)) 
			fa=open(fpath,encoding = 'utf8')
			sss=fa.readlines(2)
			print(sss)
			#codecs.encode(fa, encoding=’utf-8’, errors=’strict’)
			fa.close()

			'''
if fn[-4:] == '.txt': # Specify type of the files  my is txt
notepad.open(root + "\\" + fn)      
notepad.runMenuCommand("Encoding", "Convert to UTF-8")
notepad.save()
notepad.close()
'''
