import os


db_params = []
path = r'E:\face reco\student-portfolio-using-face-recognition-2\Project\dbDetails'


try : 

    with open(path) as dbfile :
        for line in dbfile.readlines() :
            db_params.append(line.rstrip().split(' = ')[1])

    print(db_params)

except FileNotFoundError :


    print('The file which contains Database Details does not exist. Please manually hardcode the Database Details.')


    raise FileNotFoundError
