import cv2 as cv
import numpy as np
import mediapipe as mp
import time
import math

class handDetector():
    def __init__(self,mode = False, maxHands = 2, detection_confidence = 0.6, track_confidence = 0.4):
        self.mode = mode
        self.maxHands = maxHands
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mpHands = mp.solutions.mediapipe.python.solutions.hands  
        self.hands = self.mpHands.Hands(static_image_mode = self.mode , max_num_hands= self.maxHands, min_detection_confidence = self.detection_confidence, min_tracking_confidence = self.track_confidence) 
        self.mpDraw = mp.solutions.drawing_utils   
        self.tipsId = [4,8,12,16,20]

    def findHands(self,img, draw = True):
    
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)  

        if self.results.multi_hand_landmarks :
            for handLms in self.results.multi_hand_landmarks:  
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS) 
        
        return img



    def findPosition(self, img, handNo = 0, draw = True):

        self.lmList = []

        if self.results.multi_hand_landmarks :
            myHand = self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id,cx,cy]) 
                #print(id,cx,cy)
        
        return self.lmList 

    
    def fingers_up(self):

        if len(self.lmList) != 0:
            fingers = []
            
            if self.lmList[self.tipsId[0]][1] < self.lmList[self.tipsId[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):
                if self.lmList[self.tipsId[id]][2] < self.lmList[self.tipsId[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0) 

        return fingers


    def findDistance(self, p1,p2,img,draw = True, r = 15, t = 3):
        x1,y1 = self.lmList[p1][1:]
        x2,y2 = self.lmList[p2][1:]
        cx,cy = (x1+x2)//2, (y1+y2)//2

        if draw:
            cv.line(img, (x1,y1), (x2,y2), (100,100,100), t)
            cv.circle(img, (x1,y1), r, (100,100,100), cv.FILLED)
            cv.circle(img, (x2,y2), r, (100,100,100), cv.FILLED)
            cv.circle(img,(cx,cy),r,(255,0,0),cv.FILLED)
        length = math.hypot(x2-x1,y2-y1)

        return length,img,[x1,y1,x2,y2,cx,cy]



def main():

    capture = cv.VideoCapture(0) #is for web cam access
    
    pTime = 0
    cTime = 0
    detector = handDetector()

    while True:
        ifTrue, frame = capture.read()
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv.putText(frame,str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX,3,(255,0,255), 3)

        cv.imshow("camera_feed", frame)

        if cv.waitKey(1) & 0xFF == ord('d'):
            break



if __name__ == "__main__":
    main()