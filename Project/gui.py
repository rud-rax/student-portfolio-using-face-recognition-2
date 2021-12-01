import mysql.connector as myc
from tkinter import *
import dbConnection as dbc
import Information as inf


root = Tk()
root.title("GUI")
root.geometry("900x600")

database_name = "STUDENT_PORTFOLIO_DATABASE"


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

    lhost = "localhost"
    luser = "root"
    lpasswd = "rudu101519"

    # database name can be changed below the import statements

    student_db_connection = myc.connect(
        host=lhost, user=luser, passwd=lpasswd, database=database_name
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

    fr = inf.FaceRecognition(path=r"Project/ImageInfo")
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

buttonTryFR = Button(root, text="Try Face Recognition", command=facerecognition).grid(
    row=11, column=0, columnspan=2
)
buttonGetUser = Button(root, text="Get User", command=getuser).grid(
    row=12, column=0, columnspan=2
)

idlabel = Label(root, text="Id", width=20).grid(row=0, column=0)
e0 = Entry(root, width=20)
e0.grid(row=0, column=2)

namelabel = Label(root, text="Name", width=20).grid(row=1, column=0)
e1 = Entry(root, width=20)
e1.grid(row=1, column=2)

agelabel = Label(root, text="Age", width=20).grid(row=2, column=0)
e2 = Entry(root, width=20)
e2.grid(row=2, column=2)

phonelabel = Label(root, text="Phone No ", width=20).grid(row=3, column=0)
e3 = Entry(root, width=20)
e3.grid(row=3, column=2)

emaillabel = Label(root, text="Email Id", width=20).grid(row=4, column=0)
e4 = Entry(root, width=20)
e4.grid(row=4, column=2)

addresslabel = Label(root, text="Address", width=20).grid(row=5, column=0)
e5 = Entry(root, width=20)
e5.grid(row=5, column=2)

githublabel = Label(root, text="Github", width=20).grid(row=6, column=0)
e6 = Entry(root, width=20)
e6.grid(row=6, column=2)

linkedinlabel = Label(root, text="LinkedIn", width=20).grid(row=7, column=0)
e7 = Entry(root, width=20)
e7.grid(row=7, column=2)

hrlabel = Label(root, text="Hackerrank", width=20).grid(row=8, column=0)
e8 = Entry(root, width=20)
e8.grid(row=8, column=2)


root.mainloop()
