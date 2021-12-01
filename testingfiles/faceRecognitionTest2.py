import numpy as np
import face_recognition as fr
import cv2

from face_recognition.api import face_landmarks

image_path = 'dataset/rudraksh.jpeg'
image = fr.load_image_file(image_path)
face_location = fr.face_landmarks(image)

left_eye_location = np.array(face_location[0]['left_eye'],np.int32)
left_eye_location = left_eye_location.reshape((-1, 1, 2))
print(left_eye_location)

cv2.imread(image_path)
cv2.polylines(image,[left_eye_location],False,(0,255,255))

cv2.imshow('Rudraksh',image)
cv2.waitKey(0)
cv2.destroyAllWindows()