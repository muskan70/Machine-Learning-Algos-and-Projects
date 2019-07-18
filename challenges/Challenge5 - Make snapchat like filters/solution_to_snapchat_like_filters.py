import cv2
import numpy as np
import pandas as pd

eye_cascade=cv2.CascadeClassifier("./Train/third-party/frontalEyes35x16.xml")
nose_cascade=cv2.CascadeClassifier("./Train/third-party/Nose18x15.xml")

face_frame=cv2.imread('Test/Before.png')
glass_frame=cv2.imread('Train/glasses.png',-1)
mustache_frame=cv2.imread('Train/mustache.png',-1)
print(face_frame.shape)
print(glass_frame.shape)
print(mustache_frame.shape)

eyes=eye_cascade.detectMultiScale(face_frame,1.5,5)
nose=nose_cascade.detectMultiScale(face_frame,1.5,5)

for (ex, ey, ew, eh) in eyes:
    #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)
    roi_eyes = face_frame[ey: ey + eh, ex: ex + ew]
    glass_frame = cv2.resize(glass_frame,(roi_eyes.shape[0],roi_eyes.shape[1]))

    gw, gh, gc = glass_frame.shape
    for i in range(0, gw):
        for j in range(0, gh):
            #print(glasses[i, j]) #RGBA
            if glass_frame[i, j][3] != 0: # alpha 0
                face_frame[ey + i, ex + j] = glass_frame[i, j][:3]


        for (nx, ny, nw, nh) in nose:
            #cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 3)
            roi_nose = face_frame[ny: ny + nh, nx: nx + nw]
            mustache2 = cv2.resize(mustache_frame,(roi_nose.shape[0],roi_nose.shape[1]))

            mw, mh, mc = mustache2.shape
            for i in range(0, mw):
                for j in range(0, mh):
                    #print(glasses[i, j]) #RGBA
                    if mustache2[i, j][3] != 0: # alpha 0
                        face_frame[ny +int(nh/2.0) + i, nx + j] = mustache2[i, j][:3]

        
cv2.imshow("Frame",face_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
frame=face_frame.reshape((-1,3))
ans=pd.DataFrame(frame,columns=['Channel 1','Channel 2','Channel 3'])
ans.to_csv('submit.csv',index=False)     