import chardet
File content = open("02.txt","r")# str类型
source_encoding = chardet.detect(content)


print(source_encoding)
if source_encoding == None:
    print("can not detect")
