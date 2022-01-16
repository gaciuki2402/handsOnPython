from datetime import datetime
class Birthday(object):
    def Friends(self,number_of_birthdays):
        current_date=datetime.now().date()
        my_friends={

        }
        for birth_day in range(1,number_of_birthdays+1):
            name=input("Name:")
            date=str(input("Enter date of birth (yyyy-mm-dd):"))
            date_of_birth=datetime.strptime(date,"%Y-%m-%d").date()
            location=input("Location:")
            age=current_date.year-date_of_birth.year
            hotel=input("Enter the Hotel:")
            my_friends["Name"]=name
            my_friends["DOB"]=f"{date_of_birth.year}-{date_of_birth.month}-{date_of_birth.day}"
            my_friends["Age"]=age
            my_friends["Location"]=location
            my_friends["Hotel"]=hotel
        print(my_friends)
b1=Birthday()
b1.Friends(1)