from os import name
import cv2
import dropbox
import time
import random

start_time=time.time()
def takesnapshot():
    number=random.randint(0,100)
    #initialize cv2
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        #Read the frames while the camera is on
        ret,frame=videocaptureobject.read()
        #cv2.imwrite()is a method used to save an image to any storage device
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshottaken")
    #releases the camera
    videocaptureobject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()



def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=takesnapshot()
            uploadfile(name)

main()