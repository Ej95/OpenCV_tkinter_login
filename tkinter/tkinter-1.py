import tkinter
import customtkinter
from CTkMessagebox import CTkMessagebox as ctkmsg
from PIL import ImageTk,Image
import sys

sys.path.append(r"openCV_py")
import face

sys.path.append(r"sql")
import face_data


font = "微軟正黑體"
login_success = False
info_success = False
detect_id = -2
detect_result = False



customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green")  


app = customtkinter.CTk()  #建立 tkinter 視窗
app.geometry("600x440")
app.title('Login')


#雙步驟驗證成功窗口
def two_step_function():
    app.destroy()            # 將視窗關閉
    w = customtkinter.CTk()  
    w.geometry("1280x720")
    w.title('Welcome')
    l1=customtkinter.CTkLabel(master=w, text="歡迎登入",font=(font,60))
    l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
    w.mainloop()


#輸入成功確認、接著做人臉辨識
def show_checkmark():
    global login_success

    if detect_result == True:
        two_step_function()

    elif login_success == True and detect_result == False:
        show_error3()

    elif len(face_data.get_student_id_by_student_name(entry_stud_name.get())) == 0:
        show_error2()

    elif entry_stud_number.get() == face_data.get_student_id_by_student_name(entry_stud_name.get())[0][0] and entry_stud_name.get() == face_data.get_name_by_student_id(entry_stud_number.get())[0][0]: #將輸入的姓名丟到資料庫裡並回傳資料庫的學生ID，如果與輸入的符合，則成立
        ctkmsg(message="學號、姓名認證成功！請關閉此視窗點選人臉辨識 ",icon= r"tkinter\picture\check.png", option_1="我知道了",title="認證成功",font=(font,16))
        login_success = True

    else:
        login_success = False
        show_error2()


#還未驗證學號、姓名，錯誤窗口
def show_error1():
    # Show some error message
    ctkmsg(title="無法執行", message="請先認證學號、姓名，再進行人臉辨識", icon=r"tkinter\picture\cancel.png",font=(font,16))

#學號、姓名輸入錯誤
def show_error2():
    ctkmsg(title="無法執行", message="輸入的學號或姓名有誤，如果還未註冊，請點選註冊", icon=r"tkinter\picture\cancel.png",font=(font,16))

def show_error3():
    ctkmsg(title="無法執行", message="人臉辨識尚未成功", icon=r"tkinter\picture\cancel.png",font=(font,16))

#注意事項，人臉辨識使用手冊
def show_info():
    # Default messagebox for showing some information
    msg = ctkmsg(title="使用教學", message="請將臉對準在鏡頭上，偵測正確後再按 Q 關閉視窗",font=(font,16), option_1="我知道了")

    if msg.get() == "我知道了": #判斷是否有讀過訊息
        global info_success
        info_success = True

def show_face_result(result):

    if result == 0:
        ctkmsg(title="偵測結果", message="無此人臉資料，請至學務處申請", icon=r"tkinter\picture\cancel.png",font=(font,16))

    elif result == 1:
        ctkmsg(title="偵測結果", message="沒有偵測到臉", icon=r"tkinter\picture\cancel.png",font=(font,16))

    elif result == 2:
        ctkmsg(title="偵測結果", message="人臉辨識成功，請再按一次登入", icon=r"tkinter\picture\check.png",font=(font,16))
        global detect_result
        detect_result = True

    else:
        ctkmsg(title="偵測結果", message="人臉辨識失敗", icon=r"tkinter\picture\cancel.png",font=(font,16))


#核對人臉與學號、姓名
def success(detect_id):

    if detect_id == -1:
        return 0 #無此人臉資料、請至學務處申請

    elif len(face_data.get_name_by_face_id(detect_id)) == 0 or len(face_data.get_student_id_by_face_id(detect_id)) == 0:
        return 1 #沒有偵測到臉

    elif entry_stud_name.get() == face_data.get_name_by_face_id(detect_id)[0][0] and entry_stud_number.get() == face_data.get_student_id_by_face_id(detect_id)[0][0]:
        return 2 #人臉辨識認證成功
    
    else:
        return 3 #人臉認證失敗
    

#人臉辨識按鈕
def face_detect_button_function():
    if login_success == False: #還未驗證學號、姓名，跳出錯誤窗口
        show_error1()
    elif info_success == False:
        show_info()
    else:
        detect_id = face.facedetect() #回傳 -1 無此人臉資料，回傳 0 沒有偵測到臉
        result = success(detect_id=detect_id)
        show_face_result(result)






img1=ImageTk.PhotoImage(Image.open(r"tkinter\picture\pattern.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="興大附中圖書館登入系統",font=(font,20))
l2.place(x=50, y=45)

entry_stud_name=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='student_name')
entry_stud_name.place(x=50, y=110)

entry_stud_number=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='student_number', show="*")
entry_stud_number.place(x=50, y=165)


#Create custom button
button_login = customtkinter.CTkButton(master=frame, width=220, text="登入", font=(font,14) , height=30 ,command= show_checkmark, corner_radius=6)
button_login.place(x=50, y=230)



button_face_detect= customtkinter.CTkButton(master=frame, text="人臉辨識", font=(font,14) , width=100, height=30, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF',command=face_detect_button_function)
button_face_detect.place(x=50, y=280)

button_sign_up= customtkinter.CTkButton(master=frame, text="註冊", font=(font,14) , width=100, height=30, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button_sign_up.place(x=170, y=280)










app.mainloop()