import os
import math
import time
import socket
import cv2 as cv
import numpy as np
import handtracking_module as htm

#----parameters-----
width = 1280
height = 720
#-------------------

#creating a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #IPv4 and UDP
serverAddress = ('127.0.0.1', 4000)  #local host IP address as we are communicating with our own machine and a high port number to avoid clash
#hand detector object 
detector = htm.handDetector(False,2,0.7,0.3)

#webcam input
capture = cv.VideoCapture(0)
capture.set(3,width) #width
capture.set(4,height)  #height

pTime = 0
cTime = 0

while True:
    #reads video frame by frame and flips it
    ifTrue, frame = capture.read()
    frame = cv.flip(frame,1)
    
    data = [] #hand coordinate data that will be streamed in every frame
    img = detector.findHands(frame)
    lmList = detector.findPosition(img) #returns a list of 21 landmarks found in the image frame
    #print(lmList)
    if len(lmList) != 0:
        x,y = lmList[9][1], lmList[9][2]
        x1,y1 = lmList[8][1], lmList[8][2]
        x2,y2 = lmList[4][1], lmList[4][2]

        length = math.hypot(x2-x1, y2-y1)
        #x,y = (x1+x2+x3)//3, (y1+y2+y3)//3
        data.extend([x,height - y,length])
    
        s.sendto(str.encode(str(data)), serverAddress)  #encodes and transmits the data
    else:
        data.extend([640,360])
        s.sendto(str.encode(str(data)), serverAddress)  #encodes and transmits the data
    
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(frame,str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX,3,(255,0,255), 3) 
    
    cv.imshow("camera feed",img)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

capture.release()