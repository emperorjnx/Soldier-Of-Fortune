#adding all fuction in onefile
import cv2
import numpy as np
import winsound
import sys
import time
import random
import os 

def videoplayer(x):
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(x + '.mp4')
 
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening file")
 
    # Read until video is completed
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
 
        # Display the resulting frame
            cv2.imshow(x + '.mp4',frame)
 
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
 
        # Break the loop
        else: 
            break
 
    # When everything done, release the video capture object
    cap.release()
 
    # Closes all the frames
    cv2.destroyAllWindows()
    return 

def imageplayer(x):
    img = cv2.imread(x)
    cv2.imshow = (x,img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return 

def audioplayer(x):
    winsound.PlaySound(x + '.wav',winsound.SND_ASYNC | winsound.SND_LOOP)
    return

def audiostop():
    winsound.PlaySound(None,winsound.SND_ASYNC)
    return

def play(x):
    winsound.PlaySound(x + '.wav',winsound.SND_ASYNC)
    videoplayer(x)
    return


def slow_type(x,s=0.15):
    for l in x:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*s)
    print()
    return

def clearscreen():
    data=os.system('cls')
    return data


