#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 02:48:11 2024

@author: gaurav
"""
"""
Screen recording implementation code and saving the file,

"""
    
import cv2  
import pyautogui as pgui   #control the mouse and keyboard library
import numpy as np   #arrays library

# create resolution
s_reso = pgui.size()   #creating the resolution

#enter the filename and its path by user

file_name = input("Enter the output filename and it's path: ") 
fps = 20.0  #frames per secondq

# creating output object which used for saving the file

#XVID is the codecc which are used to create the videos and XVID is good and recommended. XVID is 4 bytes in size.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(file_name,fourcc, fps, s_reso)
# file_name, s_reso, fps, fourcc all are used for only the saving video parameter, this is not diplaying parameter on runtime, we need to add now for diplaying parameters.

#creating recording module

cv2.namedWindow("Live Recording", cv2.WINDOW_GUI_NORMAL) #WINDOW_NORMAL is cv2 function which uses normal window
cv2.resizeWindow("Live Recording", (600,400)) #resizeWindow is used to resize the resolution of window.

while True:
    img = pgui.screenshot() #it captures the screenshots of window, they create a video.
    img_arr = np.array(img) #image stored in 2d-array(pixels value)
    print(img_arr)
    img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2RGB) #it convert the color array which opencv store in BGR format into RGB format.
    output.write(img_arr)
    cv2.imshow("Live Recording", img_arr)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
#release the memory

output.release()
cv2.destroyAllWindows()



"""
#Break video into multiple frames(images) and store in folder

videocap = cv2.VideoCapture("/home/gaurav/Documents/computer_vision/screen_recording_implementation/trailer.mp4")
ret, frames = videocap.read()   #capture the frames of video 
count = 0   #counting variable

while True:
    if ret == True:
        cv2.imwrite("/home/gaurav/Documents/computer_vision/screen_recording_implementation/frames/ImgN%d.jpg"%count, frames)  #saving the frames in a loop with counting no. of frames using count
        #videocap.set(cv2.CAP_PROP_POS_MSEC,(count**100)) #setting the capturing speed of frames in milisecond.captue_prop_position_milisecond.
        ret , frames = videocap.read() #this is again because first one captue only one frame but input for inside the loop, this statement has no. of frames.
        cv2.imshow("frame capturing", frames)
        count+=1
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
            cv2.destroyAllWindows()

videocap.release()
cv2.destroyAllWindows() 
        
"""    


