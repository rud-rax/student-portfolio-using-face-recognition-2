
from main import FaceRecognition

import datetime as dt
import os
from tkinter import *

log_path = r'Project/LogData'
image_path = r"Project/ImageInfo"


# CODE FOR FACE RECOGNITION ..
def captureFaceAndLog() :
    id = None

    while not id :

        fr = FaceRecognition(image_path)
        fr.extractClassNames()
        encodeList = fr.findEncodings()

        recordTime = dt.datetime.now()


        id = fr.captureAndRecognize(encodeList)
        print(f'RECOGNIZED ID {id} AT [ {recordTime.hour}:{recordTime.minute} ]')

        student_details = fr.displayInfo(id)
        return student_details

    # CODE AFTER THE FACE RECOGNITION ..
    # UPDATE RECORD INTO TO LOG FILE .. 

    print('Checking for LogData ...')

    try :

        if not os.path.isdir(log_path) : 
            raise FileNotFoundError

        else :
            print('LogData Folder is present.')
            os.chdir(log_path)

            filename = f'log_{recordTime.day}-{recordTime.month}-{recordTime.year}.txt'

            with open(filename,'a+') as logfile :

                entry = f'{id} - {recordTime.hour}:{recordTime.minute} '

                logfile.write(entry + '\n')
                print('Entry Successful !')


    except FileNotFoundError :

        print('No LogData Folder found !')

    finally :
        os.chdir('..')
        return id

class Student():

    def __init__(self,id) :
        self.id = id

    def markPresent(self,file):
        timeList = []

        with open(file) as logfile :
            for line in logfile.readlines():
                rollno, time = line.split('-')
                rollno = int(rollno[1:-2])
                if rollno == self.id :
                    timeList.append(time)

        
        

        #print(timeList)

        ety_time = timeList[0]
        ety_hr , ety_min = map(int,ety_time.split(':'))

        ext_time = timeList[-1]
        ext_hr , ext_min = map(int,ext_time.split(':'))

        print(ety_time,ext_time)
        date = file[file.index('_')+1 : file.index('.')]

        date = list(map(int,date.split('-')))
        yr,month,day = date[2],date[1],date[0]

        print(date)
        print(f'YR : {yr} MON : {month} DAY : {day}')

        dt1 = dt.datetime(yr,month,day,ety_hr, ety_min)
        dt2 = dt.datetime(yr,month,day,ext_hr, ext_min)

        print(f'Time delta = {dt2 - dt1}')

        threshold_time = dt.timedelta(hours = 1 , minutes = 45)

        if dt2 - dt1 > threshold_time : 
            print('Present')

        else : print('Absent')



           
    

    def calculateAttendance(self) :

        os.chdir(log_path)



        for file in os.listdir('.'):
            self.markPresent(file)


#s1 = Student(captureFaceAndLog()['id'])
s1 = Student(3)

s1.calculateAttendance()