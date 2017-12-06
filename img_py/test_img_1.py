from PIL import Image
from PIL import ImageTk
import tkinter as tk
import os 

def moveit():
	my_canvas.move(rect,0,5)
	
def my_line():
	x0,y0,x1,y1=50,50,80,800
	line=my_canvas.create_line(x0,y0,x1,y1)
	
	
	
my_window=tk.Tk()
my_window.title("me window")
my_window.geometry('1000x800')

my_canvas = tk.Canvas(my_window , bg='blue' , height = 700 , width = 800)

#im= Image.open( "pokemon-attributes_2.jpg" )
#print(im.size[0],im.size[1])



image_open_file = Image.open( "pokemon-attributes_2.jpg" )
#網路上查詢到的是先打開圖片
image_file=ImageTk.PhotoImage(image_open_file)
#再用PIL裡的ImageTk的指令
image = my_canvas.create_image(10, 10 , anchor='nw' ,image=image_file)
#就可以成功了

rect=my_canvas.create_rectangle(100,30,100+20,30+20)



my_canvas.pack()#pack 放前放後(圖片創建的前後)好像都能成功執行




b = tk.Button(my_window, text='move' , command=moveit)
b.pack()

my_window.mainloop()






#print(im.format, im.size, im.mode)
#im.save( "01/fileout.jpg")


#resize_image = im.resize( (200, 300), Image.BILINEAR )
#resize_image.save( "01/Resize.jpg")