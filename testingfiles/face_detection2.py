import cv2
import mediapipe
import time


print("STARTING..")
for i in range(4,1,-1):
    print(i)
    time.sleep(1)

cap = cv2.VideoCapture(0)

while cap.isOpened():

    success , image = cap.read()

    if not success : continue

    
