import os
import codecs

filePathSrc = "D:/Program/take_ol"	#要被抓取的檔案位置
fo_new_root = "D:/Program/ddr_4_input"	#匯出的檔案位置
fo_new = fo_new_root+"/"+"aaa.txt"

for root, dirs, files in os.walk(filePathSrc):
	#這邊是要匯出的檔案，用W模式開啟
	title_novel = codecs.open(fo_new, mode='w',encoding='utf-8', errors='strict')
	for fn in files:
		#print(fn)
		#file's Path
		fnPath=root+'/'+fn
		#open file 原始檔案
		opfi = codecs.open(fnPath, mode='r+',encoding='utf-8', errors='strict')
		#opfi=open(fnPath,'r') 	#這個會無法使用，因為使用到了控制台的開啟，裡面必須為cp950
		
		a=opfi.readline()
		print(a)
		#而目前我要轉換的裡面是gbk或是gb2312，所以會無法使用
		#而且也無法讀取，因為會使用到控制台，所以只好把文字直接扔出去到另外一個文件裡
		#上面那行出錯了，實際上是我已經轉好gbk成utf8，結果我還用gbk開啟
		#難怪會出錯
		#所以如果之後有其他需要做這項動作的時候，出錯時可以去檢查一下文件到底是哪個碼編譯的
		#可以減少他娘的去debug的時間
		title_novel.write(a)#這邊是指寫入一行，也就是文件的第一行
		
		opfi.close()
		
	title_novel.close()