import cv2 as cv
import numpy as np
import screen_brightness_control as scrbr
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)

hd = HandDetector()
brightnessvalue = 0

while 1:
    success,img=cap.read()
    hands,img = hd.findHands(img)
    

    if hands:
        lm = hands[0]['lmList']
        # print(lm)

        length,info,img = hd.findDistance(lm[8][0:2],lm[4][0:2],img)
        # print(length)
        blevel = np.interp(length,[15,230],[0,100])
        brightnessvalue = np.interp(length,[0, 100],[400,150])
        blevel=int(blevel)
        print(blevel)

        scrbr.set_brightness(blevel)

        cv.rectangle(img,(20,150),(85,400),(0,0,255),4)
        cv.rectangle(img,(20,int(brightnessvalue)),(85,400),(0,0,255),-1)
        cv.putText(img,str(blevel)+'%',(20,430),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)


    cv.imshow('Gesture Brightness Control',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
