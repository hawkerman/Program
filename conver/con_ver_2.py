import os
import codecs
#import encodcs
filePathSrc="D:/Program/aa" # Path to the folder with files to convert

fo_new_root= "D:/Program/bb" # Path to the folder with files to convert finish
i=1
for root, dirs, files in os.walk(filePathSrc):
	for fn in files: 
		#print("Name of the root: ",root)
		#print("Name of the dirs: ",dirs)
		#print("Name of the files: ",files)
		if fn[-4:] == '.txt':
			print(fn)
			fpath = root + "/" + fn  #Path for gb2312_novel
			fo_new=fo_new_root+ "/" + fn 
			#gb2312看起來不適用全部的小說，所以用了gbk，
			#看來效果十足，沒有一個錯誤
			
			gb2312_novel = codecs.open(fpath, mode='r+',encoding='gbk', errors='strict')
			utf8_novel   = codecs.open(fo_new, mode='w',encoding='utf-8', errors='strict')
			
			for line in gb2312_novel.readlines():
				utf8_novel.write(line)
			gb2312_novel.close()
			utf8_novel.close()