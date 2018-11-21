#adding all fuction in onefile
import cv2
import numpy as np
from playsound import playsound
import sys
import time
import random
import os 

def videoplayer(x):
    cap = cv2.VideoCapture(x)
    if (cap.isOpened()== False): 
        print("Error opening file")
    while( cap.isOpened() ):
        ret , frame = cap.read()
        if ret == True:
            cv2.imshow(x,frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else: 
            break
    cap.release()
    cv2.destroyAllWindows()
    return 

def imageplayer(x):
    img = cv2.imread(x)
    cv2.imshow = (x,img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return 

def audioplayer(x):
    playsound(x,block=False)
    return

def play(x):
    audioplayer(x + '.mp3')
    videoplayer(x + '.mp4')


def slow_type(x,s=0.15):
    for l in x:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*s)
    print()

def clearscreen():
    a=os.system('cls')



