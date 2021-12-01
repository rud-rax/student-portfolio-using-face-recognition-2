from logging import exception
from logging import error
import mysql.connector as myc
from mysql.connector.errors import Error
from random import choice

# IF WANT TO MODIFY THE DATABASE NAME CHANGE IT HERE AS WELL AS IN THE SQL FILE
database_name = "STUDENT_PORTFOLIO_DATABASE"


class User:

    """User Class is a base class. To perform any action on the database or the users details, it is necessary to make an object of this class.
    All User Actions are defined in this class"""

    total_users = None

    # change the database name according to you

    student_table = "student_details"

    def __init__(self, id=None, cursor=None):

        try:
            if cursor:
                self.student_cursor = cursor
            else:
                raise NoCursorFound

            cquery = f"select id from {User.student_table}"
            self.student_cursor.execute(cquery)
            usedIds = {i[0] for i in self.student_cursor.fetchall()}
            User.total_users = len(usedIds)

        except Exception as e:
            print(e)
        except NoCursorFound:
            print("Insert a Cursor")

        # print(usedIds)

        allIds = set([i for i in range(10)])
        availableIds = allIds.difference(usedIds)

        # print(availableIds)

        # print('TOTAL USERS = ',User.total_users)

        if id:
            self.id = id
        else:
            self.id = choice(list(availableIds))

        self.details = {
            "id": self.id,
            "name": "",
            "age": 0,
            "phoneno": 0,
            "emailid": "",
            "address": "",
            "githublink": "",
            "linkedinlink": "",
            "hackerrank": "",
        }

    def getDetails(self):

        if not self.checkUser():
            return

        query = f'select * from {User.student_table} where id = "{self.id}"'
        self.student_cursor.execute(query)
        details = self.student_cursor.fetchall()[0]
        # print(details)
        self.parseData(details)

        return self.details

    def parseData(self, details):

        i = 0
        for key in self.details.keys():
            self.details[key] = details[i]
            # print("key : ", self.details[key])
            i += 1

        print(self.details)
        # print('-')

    def checkUser(self):

        try:
            query = f'select id from {User.student_table} where id = "{self.id}"'
            self.student_cursor.execute(query)
            id = self.student_cursor.fetchall()

            # print(id)

            if id:
                return True
            else:
                raise NoUserFound

            id = self.student_cursor.fetchall()[0][0]

        except NoUserFound:
            print(NoUserFound.__doc__)

    def userEntry(self):

        self.details["id"] = self.id
        self.details["name"] = input("NAME --> ")
        # self.details["name"] = self.name
        self.details["age"] = int(input("AGE --> "))
        self.details["phoneno"] = int(input("PHONE NUMBER --> "))
        self.details["emailid"] = input("EMAIL --> ")
        self.details["address"] = input("ADDRESS --> ")
        self.details["githublink"] = input("GITHUB LINK --> ")
        self.details["linkedinlink"] = input("LINKEDIN LINK --> ")
        self.details["hackerrank"] = input("HACKERRANK LINK --> ")

    def addUser(self):

        self.userEntry()

        try:
            if not 15 < self.details["age"] < 120:
                raise AgeError

            if not 1000000000 <= self.details["phoneno"] <= 9999999999:
                raise PhoneNoError

            query = (
                f"insert into {User.student_table} values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            )
            print(tuple(self.details.values()))
            self.student_cursor.execute(query, tuple(self.details.values()))
            student_db_connection.commit()

            User.total_users += 1

        except AgeError:
            print(AgeError.__doc__)
            print(f'Age entered {self.details["age"] } ')

        except PhoneNoError:
            print(PhoneNoError.__doc__)
            print(f'Phone Number entered {self.details["phoneno"]}')

        except Exception as e:
            print(e)

    def updateUser(self):

        try:

            if self.checkUser():

                self.getDetails()

                for op, name in enumerate(list(self.details.keys())[1:]):
                    print(f"{op} - {name}")

                updateKeys = [
                    list(self.details.keys())[1:][i]
                    for i in list(
                        map(
                            int,
                            input("Enter fields you want to update --> ")
                            .rstrip()
                            .split(),
                        )
                    )
                ]

                for key in updateKeys:
                    self.details[key] = input(f"{key} --> ")

                    if key == "age" or key == "phoneno":
                        self.details[key] = int(self.details[key])

                        if not 15 < self.details["age"] < 120:
                            raise AgeError

                        if not 1000000000 <= self.details["phoneno"] <= 9999999999:
                            raise PhoneNoError

                        query = f"update {User.student_table} set {key} = {self.details[key]} where id = {self.id}"
                        self.student_cursor.execute(query)

                    else:
                        query = f'update {User.student_table} set {key} = "{self.details[key]}" where id = {self.id}'
                        self.student_cursor.execute(query)

                student_db_connection.commit()

        except AgeError:
            print(AgeError.__doc__)
            print(f'Age entered {self.details["age"] } ')

        except PhoneNoError:
            print(PhoneNoError.__doc__)
            print(f'Phone Number entered {self.details["phoneno"]}')

        except Exception as e:
            print(e)

    def deleteUser(self):

        try:

            query = f"delete from {User.student_table} where id = {self.id}"
            self.student_cursor.execute(query)
            student_db_connection.commit()

            User.total_users -= 1

        except Exception as e:
            print(e)


class AgeError(Error):
    """Invalid Age is entered. The age value must be between 16 to 120."""


class PhoneNoError(Error):
    """Phone Number Entered is Invalid. You must enter a 10 digit phone number."""


class NoUserFound(Error):
    """No such user is found in the database. Please check the values again."""


class NoCursorFound(Error):
    """No cursor available !"""


if __name__ == "__main__":

    # make sure to change the below values based on your MySQL authentication details
    lhost = "localhost"
    luser = "root"
    lpasswd = ""

    # database name can be changed below the import statements

    student_db_connection = myc.connect(
        host=lhost, user=luser, passwd=lpasswd, database=database_name
    )
    student_cursor = student_db_connection.cursor()
    # student_cursor = student_db_connection.cursor()

    # ALWAYS MAKE AN OBJECT OF A USER TO PERFORM ANY ACTION
    # THE BELOW LINE WILL CREATE AN OBJECT WITH ITS id AS A PARAMETER
    # u1 = User(7)

    # UNCOMMENT THE BELOW CODE TO ADD THE USER TO THE DATABASE
    # u1.addUser()

    # UNCOMMENT THE BELOW CODE TO UPDATE AND EXISTING USER
    # u1.updateUser()

    # UNCOMMENT THE BELOW CODE TO DELETE THE EXISTING USER
    # u1.deleteUser()

    # UNCOMMENT TO CHECK WHETHER THE USER EXIST IN THE DATABASE OR NOT
    # print(u1.checkUser())

    # UNCOMMENT TO GET THE DETAILS OF EXISTING USER
    # print(u1.getDetails())

    student_db_connection.close()
