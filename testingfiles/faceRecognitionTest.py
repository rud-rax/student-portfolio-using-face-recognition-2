import cv2
import face_recognition as fr
from face_recognition.api import face_landmarks


cap = cv2.VideoCapture('dataset/video1.mp4')


while cap.isOpened():
    success, image = cap.read()



    if not success:
        continue

    face_landmarks_list = fr.face_landmarks(image)
    print(face_landmarks_list)
    #print(face_landmarks_list[0]['left_eye'])

    #image.flags.writeable = False
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #image.flags.writeable = True
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    cv2.imshow("Webcam Feed", cv2.flip(image, 1))
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cap.release()
