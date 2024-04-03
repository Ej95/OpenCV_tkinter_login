import cv2
import numpy as np


name = {
    "1" : "EJ",
    "2" : "I love Bei"
}

def facedetect():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  
    recognizer.read('face.yml')                               

    video = cv2.VideoCapture(0)

    ret, frame = video.read()
    faceCascade = cv2.CascadeClassifier(r"C:\Users\ej381\Tkiner\openCV_py\FaceDetect.xml")

    while ret == True:
        ret, frame = video.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        facerect = faceCascade.detectMultiScale(gray, 1.1, 15) #最後的代表偵測到幾次
        
        for (x,y,w,h) in facerect:
            cv2.rectangle(frame,(x, y) , (x+w , y+h), (0,255,0) , 3)

            #判定身分
            idnum,confidence = recognizer.predict(gray[y:y+h,x:x+w]) #得到 ID & 信心指數
            if confidence < 70:
                text = name[str(idnum)]
            else:
                text = "WTF?"

            cv2.putText(frame, text, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA) # x, y 原點在左上角
        
        cv2.imshow("Face_detect",frame)
        
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()










