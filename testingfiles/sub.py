import cv2
import numpy as np
import face_recognition
import os

path = r'Project/ImageInfo'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImage = cv2.imread(f'{path}/{cls}')
    images.append(curImage)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)

#create fn to find encoding
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        frtest = face_recognition.face_encodings(img)[0]
        #print("\nface encode --> " , frtest)
        encode = frtest
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
#print("\n\n\nENCODEING LIST --> ",encodeListKnown)
print(len(encodeListKnown))