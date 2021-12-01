import cv2

# import cv2.cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# THE BELOW MODULE CONTAINS THE CODE FOR CONNECTING THE FACE RECOGNITION IDs TO DATABASE
# MAKE SURE Information.py AND dbConnection.py ARE IN THE SAME DIRECTORIES / FOLDERS
import dbConnection

# IF YOU ARE FACING PROBLEM WITH THE BELOW MODULE RUN THE FOLLOWING COMMANDS IN THE BELOW MODULE
# BEWARE !!! THIS WILL UNINSTALL THE mysql.connector MODULE AND REPLACE WITH THE mysql.connector.python MODULE
# HENCE IT IS BETTER TO USE A VIRTUAL ENVIRONMENT INSTEAD OF LOCAL INTERPRETER
# COMMANDS TO RUN IN TERMINAL / CMD :-
# pip uninstall mysql.connector
# pip install mysql.connector.python

import mysql.connector as myc

# IF WANT TO MODIFY THE DATABASE NAME CHANGE IT HERE AS WELL AS IN THE SQL FILE
database_name = "STUDENT_PORTFOLIO_DATABASE"


class FaceRecognition:
    def __init__(self, path):

        self.path = path
        self.images = []
        self.classNames = []

    def extractClassNames(self):
        self.myList = os.listdir(self.path)
        # print(myList)

        for cls in self.myList:
            curImage = cv2.imread(f"{self.path}/{cls}")
            self.images.append(curImage)
            self.classNames.append(os.path.splitext(cls)[0])
        # print(classNames)

    # THE BELOW FUNCTION IS USED TO CREATE ENCODING OF THE FACES AND RETURN THE ENCODINGS
    def findEncodings(self):
        encodeList = []
        for img in self.images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            print(face_recognition.face_encodings(img))
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    # THE BELOW FUNCTION DISPLAYS INFORMATION OF THE RECOGNISED FACE LINKED TO A DATABASE
    def displayInfo(self, id):
        # print(id)

        # MAKE SURE TO CHANGE THE BELOW VALUES FOR DATABASE AUTHENTICATION
        # mysql.connector.python MODULE IS REQUIRED TO RUN THE CODE IN THIS FUNCTION
        # YOU NEED TO UNINSTALL mqsql.connector OR ELSE YOU WILL GET AN ERROR
        lhost = "localhost"
        luser = "root"
        lpasswd = "rudu101519"

        student_db_connection = myc.connect(
            host=lhost,
            user=luser,
            passwd=lpasswd,
            database=database_name,
            auth_plugin="mysql_native_password",
        )
        student_cursor = student_db_connection.cursor()

        u1 = dbConnection.User(id, student_cursor)
        return u1.getDetails()

        student_db_connection.close()

    # CAPTURE VIDEO USING WEBCAM AND RECOGNIZE THE FACE
    def captureAndRecognize(self, encodeListKnown):

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            # images to be kept small ,fast process
            imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgs)
            encodeCurFrame = face_recognition.face_encodings(imgs, facesCurFrame)

            # compare face wrt encode

            for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = self.classNames[matchIndex].upper()
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(
                        img,
                        name,
                        (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        2,
                    )
                    # print('name --> ',name , f'{type(name)}')
                    # print('className --> ',classNames)

                    if name in self.classNames:
                        # disInfo(name)
                        cap.release()
                        return name

            cv2.imshow("Webcam", img)
            cv2.waitKey(1)


if __name__ == "__main__":

    fr = FaceRecognition(path=r"Project/ImageInfo")
    fr.extractClassNames()
    encodeList = fr.findEncodings()
    print("Encoding Complete")

    id = fr.captureAndRecognize(encodeList)
    print(f"Recognized Id {id}")

    fr.displayInfo(id)
