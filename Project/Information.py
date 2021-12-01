import cv2
import numpy as np
import face_recognition
import os

# print(os.path.abspath(os.curdir ))

imgOri = face_recognition.load_image_file(r"Project/ImagesBasic/rudraksh0.jpeg")
imgOri = cv2.cvtColor(imgOri, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file(r"Project/ImagesBasic/rudraksh1.jpeg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgOri)[0]
encodeElon = face_recognition.face_encodings(imgOri)[0]
cv2.rectangle(
    imgOri, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2
)


faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(
    imgTest, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2
)

results = face_recognition.compare_faces([encodeElon], encodeTest)
facedistance = face_recognition.face_distance([encodeElon], encodeTest)
print(results, facedistance)
cv2.putText(
    imgTest,
    f"{results}{round(facedistance[0],2)}",
    (50, 50),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    (0, 0, 255),
    2,
)

cv2.imshow("Original Image", imgOri)
cv2.imshow("Test Image", imgTest)
cv2.waitKey(0)
