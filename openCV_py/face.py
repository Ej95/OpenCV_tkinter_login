import cv2
import numpy as np
import sys
sys.path.append(r"sql")
import face_data



def facedetect():
    id = 0

    recognizer = cv2.face.LBPHFaceRecognizer_create()  
    recognizer.read('face.yml')                               

    video = cv2.VideoCapture(0)

    ret, frame = video.read()
    faceCascade = cv2.CascadeClassifier(r"openCV_py\FaceDetect.xml")

    while ret == True:
        ret, frame = video.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        facerect = faceCascade.detectMultiScale(gray, 1.1, 15) #最後的代表偵測到幾次
        
        for (x,y,w,h) in facerect:
            cv2.rectangle(frame,(x, y) , (x+w , y+h), (0,255,0) , 3)

            #判定身分
            idnum,confidence = recognizer.predict(gray[y:y+h,x:x+w]) #得到 ID & confidence
            if confidence < 65:
                text = face_data.get_name_by_face_id(idnum)[0][0]
                id = idnum
                cv2.putText(frame, text, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA) # x, y 原點在左上角
            else:
                text = "WTF?"
                cv2.putText(frame, text, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA) # x, y 原點在左上角
                id = -1 #未驗證的臉，回傳-1
            
        cv2.imshow("Face_detect",frame)
        
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    return id










