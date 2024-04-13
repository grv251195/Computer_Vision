#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:07:25 2024

@author: gaurav
"""
"""
Below code is for capture video direct from Youtube
"""

import cv2
import pafy  #this library handle the videos online #youtube_dl library handle the youtube videos

url = "https://youtu.be/3u6lLWGjFLY?si=wXaOv0N-VGl2y6r0"     #pushpa-2 teaser
data = pafy.new(url)        #insert the url to the pafy library
data = data.getbest(preftype="mp4")
cap = cv2.VideoCapture(0)   #0  is for webcam
cap.open(data.url)

#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("/home/gaurav/Documents/computer_vision/Mobile_As_Webcam&Youtube_Video_Direct_Play/output.mp4",fourcc,20.0,(640,480),0)

while cap.isOpened():
    ret,frame = cap.read()  #reading all the frames till value is true
    if ret == True:    
        cv2.resize(frame,(700,700)) #resize the color output window
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #convert rgb2gray 
        cv2.resize(gray, (700,700))
        cv2.imshow("color frame", frame)
        cv2.imshow("gray frame", gray)    
        output.write(gray)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    else:
        break

#release the variables 
cap.release()
output.release()
cv2.destroyAllWindows()
        

""" 
#How to use android device camera as webcam in OPencv.


import cv2
camera = "http://192.168.0.102:8080/video"
#connect your laptop and android device with same network either wifi or hotspot
cap = cv2.VideoCapture(0)   #Here parameter 0 is a path of any video use for webcam
cap.open(camera)
print("check===",cap.isOpened())
#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    if ret == True:
    
        frame = cv2.resize(frame,(700,700))
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    
 
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()

"""



