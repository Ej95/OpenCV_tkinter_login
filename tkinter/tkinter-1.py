import tkinter as tk
import sys
sys.path.append(r"C:\Users\ej381\Tkiner\openCV_py")
import face
import cv2 

def detect():
    face.facedetect()



win = tk.Tk() #建立主視窗

#標題
win.title("tkinter test")

#大小
win.geometry("800x900") #寬 X 高

#win.minsize(width= 800,height= 200) 
#win.maxsize(width= 400,height= 200)

win.resizable(0,0) # 1 = True, 0 = False

#icon
win.iconbitmap(r"C:\Users\ej381\Tkiner\tkinter\icon.ico") #ico

#顏色
win.config(background="skyblue")

#透明度
win.attributes("-alpha", 0.9) # 1~0 1 = 100% 0 = 0%

#置頂
win.attributes('-topmost', 0) # 1 = True, 0 = False

#Image
img = tk.PhotoImage(file=r"C:\Users\ej381\Tkiner\tkinter\button.png")


#def submit():
    #text = en.get()
    #lb_3.config(text=text)

#Button
btn = tk.Button(text="Click me")
btn.config(width=200,height=200)
btn.config(image= img)
btn.config(command= detect) #func 連結到 opencv 的人臉識別
btn.place(anchor="center",x=400,y=400)

#btn2 = tk.Button(text="Submit",command= submit)
#btn2.pack()


#labbel
lb_1 = tk.Label(text="點我打開人臉辨識", font=("微軟正黑體", 20))
lb_1.place(x=290,y=520)

lb_2 = tk.Label(text="按 q 即可關閉人臉辨識視窗",font=("微軟正黑體", 20))
lb_2.place(x=240,y=600)

'''
#entry
en = tk.Entry()
en.pack()
'''

win.mainloop() #常駐主視窗