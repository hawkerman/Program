#import os
#import sys
import codecs



#print(text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
#fo = open("D:/Program/aa/new_02.txt", "w")
filePathSrc="D:/Program/aa/02.txt"
fo_new = "D:/Program/aa/new_02.txt"

a=codecs.open(filePathSrc, mode='r+',encoding='gb2312', errors='strict')
c=codecs.open(fo_new, mode='w',encoding='utf-8', errors='strict')

#b=codecs.encode(filePathSrc,encoding='gb2312', errors='strict')
#print(type(b))
#print(b)
i=1
for line in a.readlines():
	print("this is ",i)
	i+=1
	c.write(line)

	
c.close()
a.close()
#b=codecs.open(filePathSrc, mode='w+',encoding='gb2312', errors='strict')




#b=codecs.decode(a, encoding='utf-8', errors='strict')
#print(a)
#print(b)
#fo.close()