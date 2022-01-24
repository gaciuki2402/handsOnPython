from datetime import datetime
import json
class Details():
    def myPet(self):
        pets={

        }
        y="2013-02-19 00:45:13"
        y2=datetime.strptime(y,"%Y-%m-%d %H:%M:%S")
        print(y2)
        for pet in range(1):
            name=input("Enter name:")
            species=input("Enter type:")
            Dob=input("Enter D.O.B: (YYYY-mm-dd)")
            Date_of_birth=datetime.strptime(Dob,"%Y-%m-%d")
            print(type(Date_of_birth))
            today=datetime.now()
            age=datetime.now().year-Date_of_birth.year
            pets["Name"]=name
            pets["Type"]=species
            pets["D.O.B"]=str(Date_of_birth) #datetime.datetime(...)
            pets["Age"]=age
        j=json.dumps(pets,indent=4)
        print(j)
w1=Details()
w1.myPet()
