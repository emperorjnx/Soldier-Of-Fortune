import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('Taki Taki.mp4')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Taki Taki',frame)
 
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


#Opening an image file
#reading the image from source
img = cv2.imread('conflict.png')
#printing the image
cv2.imshow('Image',img)
#making sure it doesn't close
cv2.waitKey()
cv2.destroyAllWindows()


#clear the screen
import os
a=os.system('cls')
