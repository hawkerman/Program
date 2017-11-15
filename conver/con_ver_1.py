import codecs
fn="04.txt"
filePathSrc="D:/Program/aa/"+fn

fo_new = "D:/Program/aa/new_"+fn

a=codecs.open(filePathSrc, mode='r+',encoding='gbk', errors='strict')
c=codecs.open(fo_new, mode='w',encoding='utf-8', errors='strict')


i=1
for line in a.readlines():
	print("this is ",i)
	i+=1
	c.write(line)

	
c.close()
a.close()