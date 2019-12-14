#written by jorge orlando  miranda ñahui
#import necessary modules into python
import numpy as np
import cv2
import time
#build an object to capture images from the camera
cam=cv2.VideoCapture(0)
#reference time t1
t1=time.time()
#build the VideoWriter_fourcc object and pass to it the codec format
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
#build the VideoWriter object and pass to it the name ,the fourcc, frame_rate,shape
video_=cv2.VideoWriter("jorge_video_opencv.avi",fourcc,20.0,(640,480))
#while True
while True:
    #determine if 10 seconds have passed or the 'q' letter has been pressed
    if (time.time()-t1)>15 or cv2.waitKey(1)==ord('q'):
        break
    #read the images from the camera and save to the frame variable
    ret,frame=cam.read()
    #show the image captured by the camera
    cv2.imshow("IMAGEN ",frame)
    #save each frame to the video´s file
    video_.write(frame)
#release the camera
cam.release()
#release the object of VideoWriter
video_.release()
#destroy All Windows opened
cv2.destroyAllWindows()



