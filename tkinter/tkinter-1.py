import tkinter as tk
import sys
sys.path.append(r"openCV_py")
sys.path.append(r"sql")
import face
import face_data
import time
 
id = 0
do = False


win = tk.Tk() #建立主視窗

#標題
win.title("tkinter test")

#大小
win.geometry() #寬 X 高

#win.minsize(width= 800,height= 200) 
#win.maxsize(width= 400,height= 200)

win.resizable(0,0) # 1 = True, 0 = False

#icon
win.iconbitmap(r"C:\Users\ej381\GitHub\OpenCV_tkinter_login\tkinter\icon.ico") #ico

#顏色
win.config(background="skyblue")

#透明度
win.attributes("-alpha", 0.9) # 1~0 1 = 100% 0 = 0%

#置頂
win.attributes('-topmost', 0) # 1 = True, 0 = False

#Image
img = tk.PhotoImage(file=r"C:\Users\ej381\GitHub\OpenCV_tkinter_login\tkinter\button.png")


def submit():
    text_name = en_name.get()

    text_student_id = str(en_student_id.get())

    #判斷是否資料輸入正確
    if text_name == face_data.get_name_by_student_id(text_student_id)[0][0] and text_student_id == face_data.get_student_id_by_student_name(text_name)[0][0]:
        btn_face.config(text="人臉辨識",command=detect)
        btn_login.config(text="輸入完成，請做臉部辨識",command=None)
    else:
        label_result.config(text="學號 或 名字 輸入錯誤", font=("微軟正黑體", 20))
        label_result.grid(row=3,column=0,columnspan=2)


def detect():
    id = face.facedetect()

    text_name = en_name.get()
    text_student_id = str(en_student_id.get())

    print(face_data.get_name_by_face_id(id))
    print(face_data.get_student_id_by_face_id(id))
    

    if len(face_data.get_name_by_face_id(id)) == 0 and len(face_data.get_student_id_by_face_id(id)) == 0 and id != -1:
        label_result.config(text="未偵測到臉，請在試一次", font=("微軟正黑體", 20))
        label_result.grid(row=3,column=0,columnspan=2)
    elif id != face_data.get_face_id_by_name(text_name)[0][0]:
        label_result.config(text="臉部驗證失敗".format(text_name), font=("微軟正黑體", 20))
        label_result.grid(row=3,column=0,columnspan=2)
    elif text_name == face_data.get_name_by_face_id(id)[0][0] and text_student_id == face_data.get_student_id_by_face_id(id)[0][0]:
        label_result.config(text="臉部驗證成功 歡迎 {}".format(text_name), font=("微軟正黑體", 20))
        label_result.grid(row=3,column=0,columnspan=2)


#Button
btn_login = tk.Button(text="確認輸入", font=("微軟正黑體", 20), command= submit)
btn_login.grid(row=2,column=1)

btn_face = tk.Button(text="人臉辨識(請先認證學號、姓名)", font=("微軟正黑體", 20))
btn_face.grid(row=2,column=0)


#btn2 = tk.Button(text="Submit",command= submit)
#btn2.pack()

'''
#labbel
lb_1 = tk.Label(text="點我打開人臉辨識", font=("微軟正黑體", 20))
lb_1.place(x=290,y=520)

lb_2 = tk.Label(text="確認自己臉擺好偵測到之後，按 q 即可關閉人臉辨識視窗",font=("微軟正黑體", 20))
lb_2.place(x=100,y=600)

login_label = tk.Label(text="請登入",font=("微軟正黑體",16))
login_label.place(x=350, y = 650)
'''


label_login_name = tk.Label(text="姓名",font=("微軟正黑體",20))
label_login_name.grid(row=0,column=0)

label_login_student_id = tk.Label(text="學號",font=("微軟正黑體",20))
label_login_student_id.grid(row=1,column=0)

label_result = tk.Label()

#entry
en_name = tk.Entry(width=40,font=("微軟正黑體",20))
en_name.grid(row=0,column=1)

en_student_id = tk.Entry(width=40,font=("微軟正黑體",20))
en_student_id.grid(row=1,column=1)




win.mainloop() #常駐主視窗