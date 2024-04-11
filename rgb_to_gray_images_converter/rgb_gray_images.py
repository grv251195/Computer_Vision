#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:33:42 2024

@author: gaurav
"""

import cv2 #import the opencv

'''
# this is rgb image
#imread has two parametere path and flag so the flag has two parameters 0 and 1, default is 1, which shows rgb image and 0 show gray image
img1 = cv2.imread('/home/gaurav/Documents/computer vision/images/avengers.jpg', flags=1)
img1 = cv2.resize(img1,(1280,700)) #width, height
print('image in rgb colors ===',img1)
cv2.imshow('rgb image', img1)

# gray image 

img2 = cv2.imread('/home/gaurav/Documents/computer vision/images/avengers.jpg', flags=0)
img2 = cv2.resize(img2,(1280,700)) #width, height
print('image in gray color===',img2)
cv2.imshow('gray scale', img2)

#unchanged flag= -1
# this is same as original but its alpha channel(contrast is high in image) to the original image. 
img3 = cv2.imread('/home/gaurav/Documents/computer vision/images/avengers.jpg', flags=-1)
img3 = cv2.resize(img3,(1280,700)) #width, height
print('image in gray color===',img3)
cv2.imshow('unchanged image', img3)

cv2.waitKey(0) #cv2.waitkey(5000)
# waitkey(), default is 0, this value shows in how many time to close the window, measure in milisecod
#like 5000 pass so 5000 milisecond means 5 second, this image window close after 5 second.

cv2.destroyAllWindows() #use to free the window memory

'''
# now we convert rgb image to gray scale and save the gray image

path = input(r'enter the path of image')
print('the path is ', path)

img1 = cv2.imread(path, flags=0)  #0 is for gray scale
img1 = cv2.resize(img1, (560, 700))
img1 = cv2.flip(img1, 1) #it accept 3 parameters 0,1,-1
cv2.imshow('grayscale', img1)
cv2.imwrite("//home//gaurav//Documents//computer_vision//images//output.png", img1)
cv2.waitKey()
cv2.destroyAllWindows()
