
import os

#目前這個是拿來轉換小說用的
def conver(path):
	for file in os.listdir(path):
		
		if os.path.isfile(os.path.join(path,file))==True:
			#print(file)
			#print(file.find('.'))
			if file.find('.')<3:	#這裡是利用文件名稱的 . 的位置，來確認此文件是否為3個字
				#print(file)		#如果不是就幫他加一個0，讓文件變成3個字組成
				newname='0'+file  # 該改名稱的地方
				os.rename(os.path.join(path,file),os.path.join(path,newname))
				print(file,'ok')

				
#目前這個是拿來轉換字幕用的
def conver_2(path):
	for root, dirs, files in os.walk(path):
		num=0
		for fn in files: 
			num+=1
			if fn[-4:] == '.ass':
				unknown_kino(path,fn)
			

def configPrint(path):
	for file in os.listdir(path):
		print(file)
		
def configPrint_2(path):
	for root, dirs, files in os.walk(path):
		for fn in files:
			print(root,fn)
	

def change_mp4_name(path):
	for root, dirs, files in os.walk(path):
		num=0
		for fn in files: 
			num+=1
			if fn[-4:] == '.mp4':
				Kyousougiga_big5(path,fn)

def Kyousougiga_big5(path,fn):
	#print(fn)
	#print(fn.find('BIG5'))
	tar_w=fn.find('BIG5')
	if fn[tar_w:tar_w+4] == 'BIG5':
		#print('ok')
		#print(fn[tar_w-10:tar_w-2])#fn[tar_w-7:tar_w-2]==>是確定集數位置的粗概位置  ex: a][05
		mid_find=fn[tar_w-10:tar_w-2]
		end_word=mid_find[mid_find.find('[')+1:]
		#print(end_word)
		#_1_find=len(mid_find)-mid_find.find('[')
		#print(mid_find)
		newname="[Kyousougiga]["+end_word+"][BIG5][1280X720].mp4"
		if end_word=="10.5":
			newname="[Kyousougiga]["+end_word+"][BIG5][END][1280X720].mp4"
		#print(newname)
		rename_all(path,fn,newname)
		
def rename_all(path,fn,newname):
	os.rename(os.path.join(path,fn),os.path.join(path,newname))
	print(fn,'ok')
		

def unknown_kino(path,fn):
	if fn[1:3] == '未知':
		#newname='[未知] 奇諾之旅 01 DVD 720P'
		newname = '[未知] 奇諾之旅 '+fn[10:]
		#print('[未知] 奇諾之旅 '+fn[10:])
		os.rename(os.path.join(path,fn),os.path.join(path,newname))
		print(newname,'ok')

def allgod(path,fn):
	if fn[1:3] == '諸神':				
		#print(fn)
		#print(fn[10:])
		newname='[諸神] 血界戰線 '+fn[10:]
		os.rename(os.path.join(path,fn),os.path.join(path,newname))
		print(newname,'ok')

def YYDM_11FANS(path,fn):
	if fn[7:18] =='YYDM-11FANS':#這邊可以修改為該檔案的共同名稱
		#print(fn[7:18]) #這邊是尋找檔名的的共同名稱
		if num<10:
			newname='K-ON ! BD 720P '+'0'+str(num)+'.ass'
		else:
			newname='K-ON ! BD 720P '+str(num)+'.ass'
		os.rename(os.path.join(path,fn),os.path.join(path,newname))
		print(newname,'ok')
 
if __name__ == '__main__' :
	path = 'D:/change' # 這是需要轉換名字的資料夾
	#configPrint_2(path)
	#conver_2(path)
	change_mp4_name(path)
	#conver(path)