from datetime import datetime
# name=input("Enter your name:")
# n=input("Enter your age:")
# y=input("Enter your admNo:")
# print("-"*45)
class Details():
    def admissions(self,completion_of_study):
        current_time=datetime.now().date()
        students_graduating={

        }
        for year in range(completion_of_study):
            name=input("Enter name:")
            course=input("CourseName:").title()
            email=input("Email").lower()
            date_of_adm=input("Date of Admission (YYYY-mm-dd)")
            d=datetime.strptime(date_of_adm,"%Y-%m-%d")
            month_of_adm=d.month
            day_of_adm=d.day

            if course=="Mining":
                number_of_years=5
            elif course=="Medicine":
                number_of_years=7
            elif course=="Mcs":
                number_of_years=4
            else:
                number_of_years=None

            if number_of_years is not None:
                new_year = int(d.year) + number_of_years
                new_year=str(new_year)
                new_year=datetime(new_year,"%Y")
                print(type(new_year))
                # y=f"{new_year}-{d.month}-{d.day}"
                # completion_date=datetime(y,"%Y-%m-%d")
                # print(completion_date)
                # years=datetime(numberofyears,"%Y")
                # print(years)
            students_graduating["Name"]=name
            students_graduating["Email Address"]=email
            students_graduating["Course"]=course
            students_graduating["Years"]=number_of_years
        print(students_graduating)

d1=Details()
d1.admissions(1)





