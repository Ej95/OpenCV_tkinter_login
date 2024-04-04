import cv2
import numpy as np

detector = cv2.CascadeClassifier(r"openCV_py\FaceDetect.xml")  # 載入人臉追蹤模型
recog = cv2.face.LBPHFaceRecognizer.create()    # 啟用訓練人臉模型方法
faces = []   # 儲存人臉位置大小的串列
ids = []     # 記錄該人臉 id 的串列

#EJ
for i in range(1,56):
    img = cv2.imread(f'openCV_py\\my_head\\face01\\{i}.JPG')           # 依序開啟每一張的照片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    face = detector.detectMultiScale(gray)        # 擷取人臉區域
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄人臉的位置和大小內像素的數值
        ids.append(1)                             # 記錄人臉對應的 id，只能是整數，都是 1 表示的 id 為 1

#I LOVE bei
for i in range(1,23):
    img = cv2.imread(f'openCV_py\\my_head\\face02\\{i}.JPG')           # 依序開啟每一張的照片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    face = detector.detectMultiScale(gray)        # 擷取人臉區域
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄人臉的位置和大小內像素的數值
        ids.append(2)                             # 記錄人臉對應的 id，只能是整數，都是 2 表示的 id 為 2


print('training...')                              # 提示開始訓練
recog.train(faces,np.array(ids))                  # 開始訓練
recog.save('face.yml')                            # 訓練完成儲存為 face.yml
print('ok!')