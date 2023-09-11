import cv2 as cv
cv2=cv
import dlib
import mousecontrol_eye
from win32.win32api import GetSystemMetrics
import time
from pynput.mouse import Listener,Button,Controller
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from imutils.video import WebcamVideoStream
import numpy as np
class eye_mouse:
    def __init__(self,camerainput,cameracheck,aspectratio169,illumination):
            self.camerainput=int(camerainput)
            self.blinking_frames=0
            self.mousecontrol=mousecontrol_eye.mousecontrol()
            self.cameracheck=cameracheck
            self.aspectratio169=aspectratio169
            width = GetSystemMetrics(0)
            height = GetSystemMetrics(1)
            middlepoint1=width/2
            middlepoint2=height/2
            self.mousecontrol.firstpos(middlepoint1,middlepoint2)
            self.illumination=illumination
            if self.illumination==None:
                self.illumination=1
    def rescaleFrame(self,frame):
        dimension=(320,240)
        return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
    def midlinepoint(self,p1,p2):
        return int((p1.x+p2.x)/2),int((p1.y+p2.y)/2)
    def aspectratiochanger(self,ratio,frame):
        if ratio=="16by9":
            # src = self.frame
            # new_width = 450
            # dsize = (new_width, src.shape[0])
            # self.frame= cv2.resize(src, dsize, interpolation = cv2.INTER_AREA)
            dimension=(426,240)
            return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
            # frame=cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
    def adjust_gamma(self,frame, gamma=1.0):
        if gamma==1:
            return frame
        else:
            invGamma = 1.0 / gamma
            table = np.array([((i / 255.0) ** invGamma) * 255
               for i in np.arange(0, 256)]).astype("uint8")
            return cv2.LUT(frame, table)
    def eyetrack(self):
        blinking_frames=self.blinking_frames
        blinking_frames1=self.blinking_frames
        self.cap=WebcamVideoStream(src=self.camerainput-1).start()
        #self.cap=cv.VideoCapture(self.camerainput-1,cv.CAP_DSHOW)
        cameracheck=self.cameracheck
        self.detector=dlib.get_frontal_face_detector()
        self.predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        mouse=Controller()
        # self.interfaceclass.changestatus(self.interfaceclass,"good")
        while True:
            try:
                errornumber=0
                if cameracheck==False:
                    #_,frame=self.cap.read()
                    frame=self.cap.read()
                    frame=self.adjust_gamma(frame,self.illumination)
                    
                    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
                    self.aspectratioranned=False#this is false until aspectratiofunction runs
                    if self.aspectratio169==True:
                        
                        gray=self.aspectratiochanger("16by9",gray)
                        frame=self.aspectratiochanger("16by9",frame)
                        self.aspectratioranned=True#this wil determine if aspectratioranned or not for further use
                    else:
                        gray=self.rescaleFrame(gray)
                        frame=self.rescaleFrame(frame)
                    
                    faces=self.detector(gray)
                else:#this will flip the camera if checkbox is clicked
                    frame=self.cap.read()
                    #_,frame=self.cap.read()
                    frame=self.adjust_gamma(frame,self.illumination)
                    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
                    
                    if self.aspectratio169==True:
                        gray=cv.flip(self.aspectratiochanger("16by9",gray),1)#flipping if cameracheck is checked
                        frame=cv.flip(self.aspectratiochanger("16by9",frame),1)
                        self.aspectratioranned=True
                    else:
                        gray=cv.flip(self.rescaleFrame(gray),1)
                        frame=cv.flip(self.rescaleFrame(frame),1)
                        
                    faces=self.detector(gray)
                
                cv.putText(frame,"Q to exit",(120,50),cv.FONT_HERSHEY_DUPLEX,0.5,(255,255,255),1)
                for face in faces:
                    x,y=face.left(),face.right()
                    x1,y1=face.top(),face.bottom()
                    
                    facerect=cv2.rectangle(frame,(x,x1),(y,y1),(255,255,255),1)
                    landmarks=self.predictor(gray,face)
                    noselandmark=(landmarks.part(30).x,landmarks.part(30).y)
                    
                    eyestonosepointx,eyestonosepointy=landmarks.part(30).x,landmarks.part(30).y
                    if self.aspectratioranned==True:#this if else is for changing midpoint of camera
                        nose_to_cursorx=213
                        nose_to_cursory=150
                    else:#this will run if there aspectratio button is not clicked 
                        nose_to_cursorx=160
                        nose_to_cursory=150
                    cv.rectangle(frame,(eyestonosepointx,eyestonosepointy),(eyestonosepointx,eyestonosepointy),(255,255,255),thickness=4)
                    cv.rectangle(frame,(nose_to_cursorx,nose_to_cursory),(nose_to_cursorx,nose_to_cursory),(0,0,0),thickness=5)
                    cv.line(frame,(eyestonosepointx,eyestonosepointy),(nose_to_cursorx,nose_to_cursory),(255,255,255),thickness=1)
                    center_coordinates = (325, 270)
                    # Radius of circle
                    radius = 30
                    # Blue color in BGR
                    color = (220,220,220)
                    
                    # cv2.circle(frame, center_coordinates, radius, color, thickness=-1,lineType=cv.FILLED)
                    
                    # cv2.circle(frame, center_coordinates,50, color, thickness=2,lineType=cv.FILLED)#here 50 is radius
                    # cv2.circle(frame, center_coordinates,70, color, thickness=2,lineType=cv.FILLED)
                    positivecursorvalue=15
                    negativesursorvalue=-15
                    if((eyestonosepointx-nose_to_cursorx)>positivecursorvalue):#this is for gradually increasing speed
                        if((eyestonosepointx-nose_to_cursorx)>60):
                            mouse.move(10,0)                        
                            #this is for gradually increasing the speed
                        elif((eyestonosepointx-nose_to_cursorx)>30):
                            mouse.move(6,0)
                        elif((eyestonosepointx-nose_to_cursorx)>15):
                            mouse.move(2,0)#this is moving right
                    if((eyestonosepointx-nose_to_cursorx)<negativesursorvalue):
                        if((eyestonosepointx-nose_to_cursorx)<-60):
                            mouse.move(-10,0) #this is for gradually increasing the speed
                        elif((eyestonosepointx-nose_to_cursorx)<-30):
                            mouse.move(-6,0)
                        elif((eyestonosepointx-nose_to_cursorx)<-15):
                            mouse.move(-2,0)#this is moving left
                    if(eyestonosepointy-nose_to_cursory)<positivecursorvalue:
                        if(eyestonosepointy-nose_to_cursory)<30:
                            mouse.move(0,-8)#this is moving up
                        elif(eyestonosepointy-nose_to_cursory)<15:
                            mouse.move(0,-4)#this is moving up
                    if(eyestonosepointy-nose_to_cursory)>negativesursorvalue:
                        if(eyestonosepointy-nose_to_cursory)>-30:
                            mouse.move(0,8)# this is moving down
                        elif(eyestonosepointy-nose_to_cursory)>-15:
                            mouse.move(0,4)# this is moving down
                    left_point=(landmarks.part(36).x,landmarks.part(36).y)
                    right_point=(landmarks.part(39).x,landmarks.part(39).y)
                    hor_line=cv.line(frame,left_point,right_point,(255,255,255),1)
                    up_point=(self.midlinepoint(landmarks.part(37),landmarks.part(38)))
                    down_point=(self.midlinepoint(landmarks.part(41),landmarks.part(40)))
                    ver_line=cv.line(frame,up_point,down_point,(255,255,255),1)
                    left_point_r=(landmarks.part(42).x,landmarks.part(42).y)
                    right_point_r=(landmarks.part(45).x,landmarks.part(45).y)
                    hor_line_r=cv.line(frame,left_point_r,right_point_r,(255,255,255),1)
                    up_point_r=(self.midlinepoint(landmarks.part(43),landmarks.part(44)))
                    down_point_r=(self.midlinepoint(landmarks.part(47),landmarks.part(46)))            
                    ver_line_r=cv.line(frame,up_point_r,down_point_r,(255,255,255),1)
                    value_of_blink=-3#this is for distance about 1 feet
                    
                    if((y1-x1)>123):
                        value_of_blink=-5
                        #value_of_blink=-7
                    elif((y1-x1)>102):
                        value_of_blink=-4
                        #value_of_blink=-6
                    elif((y1-x1)>85):
                        value_of_blink=-3
                        #value_of_blink=-5
                    elif((y1-x1)>71):
                        value_of_blink=-2
                        cv.putText(frame,"dont go far than this",(50,70),cv.FONT_HERSHEY_DUPLEX,0.5,(255,255,255),1)
                        #value_of_blink=-4
                    elif((y1-x1)<73):
                        cv.putText(frame,"come close to the camera",(50,70),cv.FONT_HERSHEY_DUPLEX,0.5,(255,255,255),1)
                        value_of_blink=10
                    
                    if((up_point[1]-down_point[1])>=value_of_blink):
                        blinking_frames+=1
                        if (blinking_frames>3):
                            blinking_frames=0#this will reduce multiple clicks
                            cv.putText(frame,"Left click",(125,65),cv.FONT_HERSHEY_DUPLEX,0.5,(0,0,0),1)
                            self.mousecontrol.left_click()
                    else:
                        while blinking_frames!=0:
                            blinking_frames-=1
                    if((up_point_r[1]-down_point_r[1])>=value_of_blink):
                        blinking_frames1+=1
                        if (blinking_frames1>3):
                            blinking_frames1=0#this will reduce multiple clicks
                            cv.putText(frame,"Right click",(125,65),cv.FONT_HERSHEY_DUPLEX,0.5,(0,0,0),1)
                            self.mousecontrol.right_click()
                    else:
                        while blinking_frames1!=0:
                            blinking_frames1-=1
                cv.imshow("frame",frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    # self.cap.release()
                    cv2.destroyAllWindows()
                    self.cap.stop()
                    break
            except:
                cv2.destroyAllWindows()
                self.cap.stop()
                break

cv2.destroyAllWindows()
