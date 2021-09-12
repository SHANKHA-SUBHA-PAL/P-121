import cv2
import time
import numpy as np



# Starting the webcam
video = cv2.VideoCapture(0)

image = cv2.imread("Projects\P-121\Tom-in-Bangkok.jpg")


while True:
    ret,frame = video.read()
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))

    u_black = np.array([104,153,70])
    l_black= np.array([30,30,0])

    mask = cv2.inRange(frame,u_black,l_black)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    f= frame - res
    f= np.where(f==0, image, f)

    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

video.release() 
cv2.destroyAllWindows() 
