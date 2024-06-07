
import cv2
import numpy as np
cap=cv2.VideoCapture('VID_20240519_192518.mp4')
#set mediapipe model
#with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
while cap.isOpened():
        #READ FEED
        reT,frame=cap.read()
        #MAKE DETECTION
       # image,results=mediapipe_detection(frame,holistic)
       # print(results)
        #SHOW TO SCREEN
        cv2.imshow('OpenCV',frame)
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()