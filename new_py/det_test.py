import chardet

str1=" JAPANトップページの機能を正しくご利用いただくには、下記の環境が必要です。"
str2=str.encode(str1)
a = chardet.detect(str1)

print(a)
