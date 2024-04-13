"""
Created on Sat Apr 13 18:15:47 2024

@author: gaurav
"""
"""
Below code, converting the rgb video to gray video code.
""" 

import cv2

"""
cap = cv2.VideoCapture("/home/gaurav/Documents/computer_vision/video_rgb_to_gray/video/Pirates of the Caribbean 6_ Beyond the Horizon - Official Trailer _ Jenna Ortega, Johnny Depp.mp4")
print(cap)

while True:
    ret, frame = cap.read()
    cv2.resize(frame,(100,200))
    cv2.imshow("frame", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    cv2.resize(gray, (100,200))
    k = cv2.waitKey(25)
    if k == ord("q") & 0xFF:
        break
cap.release()
cv2.destroyAllWindows()

"""
# Now capture the video from webcam and save into memory.

#VideoCapture using path for selecting video from memory, 0 for webcam, 1 for external camera device
cap = cv2.VideoCapture(0)   #0 is for webcam
print(cap)

#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("/home/gaurav/Documents/computer_vision/video_rgb_to_gray/video/output.avi",fourcc,20.0,(640,480),0)

#isOpened(), this is use for camera opened is true
while cap.isOpened():
    ret, frame = cap.read() #ret reurn boolean values, frame get image frames
    print(ret)
    if ret == True: 
        #cv2.resize(frame,(100,200)) # already define in output 
        cv2.imshow("frame", frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", gray)
        output.write(gray)
        #cv2.waitkey() value if 0 so its image if 1 its video,
        if cv2.waitKey(1) & 0xFF == ord("q"):   #press q to exit 
            break
    else:
        break
    
cap.release()
output.release()
cv2.destroyAllWindows()
