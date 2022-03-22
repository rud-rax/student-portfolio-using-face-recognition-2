from turtle import bgcolor
import mysql.connector as myc
from tkinter import *
from PIL import Image, ImageTk
import dbConnection as dbc
import main as mn
import os
'''root = Tk()
#top = Tk(bgcolor="blue")
root.title("GUI")
root.geometry("500x400")'''



root = Tk()
#root.geometry("700x600")
root.resizable(0,0)
#creating a simple canvas  
#c = Canvas(top,bg = "pink",height = "900")  
#c.pack()  
root.configure(bg='#24AAC9')
#root.resizable(height = None, width = None)
#a_canvas = Canvas(root,width=900,height=600)
#bg = ImageTk.PhotoImage(Image.open("imgdir\\bg.png"))
#a_canvas.pack(fill="both",expand=True)
#a_canvas.pack()
#a_canvas.create_image(0,0,anchor=NW,image=bg)



db_params = []
path = r'E:\face reco\student-portfolio-using-face-recognition-2\Project\dbDetails'


try : 

    with open(path) as dbfile :
        for line in dbfile.readlines() :
            db_params.append(line.rstrip().split(' = ')[1])

    #print(db_params)

    USER = db_params[0]
    PASSWD = db_params[1]
    DB = db_params[2]
    TABLE = db_params[3]

except FileNotFoundError :


    print('The file which contains Database Details does not exist. Please manually hardcode the Database Details.')


    raise FileNotFoundError

# def deluser() :

#    lhost = 'localhost'
#    luser = 'root'
#    lpasswd = 'rudu101519'

#    # database name can be changed below the import statements
#    try :

#        student_db_connection = myc.connect(
#            host=lhost, user=luser, passwd=lpasswd, database=database_name
#        )
#        student_cursor = student_db_connection.cursor()

#        id = int(e0.get())
#        u1 = dbc.User(id,student_cursor)
#        u1.deleteUser()

#        student_db_connection.close()
#    except ValueError :
#        print('Enter proper id !')
#        #messagebox.showerror(title = 'Id Error' , message = 'Invalid User Id !' )

#    except Exception as e :
#        print(e)


def getuser():

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)



    # database name can be changed below the import statements

    student_db_connection = myc.connect(
        host='localhost', user=USER, passwd=PASSWD, database=DB
    )
    student_cursor = student_db_connection.cursor()

    id = int(e0.get())
    u1 = dbc.User(id, student_cursor)
    userdetails = u1.getDetails()

    e1.insert(0, userdetails["name"])
    e2.insert(0, userdetails["age"])
    e3.insert(0, userdetails["phoneno"])
    e4.insert(0, userdetails["emailid"])
    e5.insert(0, userdetails["address"])
    e6.insert(0, userdetails["githublink"])
    e7.insert(0, userdetails["linkedinlink"])
    e8.insert(0, userdetails["hackerrank"])

    student_db_connection.close()


def facerecognition():

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)

    fr = mn.FaceRecognition(path=r"Project/ImageInfo")
    fr.extractClassNames()
    encodeList = fr.findEncodings()
    print("Encoding Complete")

    id = fr.captureAndRecognize(encodeList)
    print(f"Recognized Id {id}")

    e0.insert(0, id)
    getuser()


# label1 = Label(root,text = 'Hello There').grid(row = 0,column = 0 )
# button1 = Button(root,text = 'Click Here',command = func1, width= 20 ).grid(row = 1,column = 0 )

# buttonAddUser = Button(root,text = 'Add User' , command = useradd ).grid(row = 9,column = 0 , columnspan=2 )
# buttonDeleteUser = Button(root , text = 'Delete User' , command = deluser).grid(row = 10 , column = 0, columnspan = 2)
new_frame=Frame(root , bg='#24AAC9')
new_frame.pack(pady=190)
buttonTryFR = Button(new_frame, text="Try Face Recognition", command=facerecognition,width=20,font="Arial ",fg='#24AAC9',bg="white").grid(
    row=24, column=0, columnspan=1
)
buttonGetUser = Button(new_frame, text="Get User", command=getuser,width=20,font="Arial ",fg='#24AAC9',bg="white").grid(
    row=24, column=3, columnspan=2
)

idlabel = Label(new_frame, text="RollNo:", width=20,font="Arial ",fg="white",bg='#24AAC9').grid(row=0, column=0)
e0 = Entry(new_frame, width=30)
e0.grid(row=0, column=3)

#a_canvas.create_text(400,200, text="Welcome",font=("Arial", 50))

namelabel = Label(new_frame, text="Name", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=2, column=0)
e1 = Entry(new_frame, width=30)
e1.grid(row=2, column=3)

agelabel = Label(new_frame, text="Age", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=4, column=0)
e2 = Entry(new_frame, width=30)
e2.grid(row=4, column=3)

phonelabel = Label(new_frame, text="Phone No ", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=6, column=0)
e3 = Entry(new_frame, width=30)
e3.grid(row=6, column=3)

emaillabel = Label(new_frame, text="Email Id", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=8, column=0)
e4 = Entry(new_frame, width=30)
e4.grid(row=8, column=3)

addresslabel = Label(new_frame, text="Class", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=10, column=0)
e5 = Entry(new_frame, width=30)
e5.grid(row=10, column=3)

githublabel = Label(new_frame, text="Time", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=12, column=0)
e6 = Entry(new_frame, width=30)
e6.grid(row=12, column=3)

linkedinlabel = Label(new_frame, text="Status", width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=14, column=0)
e7 = Entry(new_frame, width=30)
e7.grid(row=14, column=3)

hrlabel = Label(new_frame, text="Date",width=30,font="Arial ",fg="white",bg='#24AAC9').grid(row=16, column=0)
e8 = Entry(new_frame, width=30)
e8.grid(row=16, column=3)
root.mainloop()


#top.mainloop()


