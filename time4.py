import json
from datetime import datetime,timedelta
class Bell_intervals():
    def Time(self):
        details={

        }
        for lesson in range(1):
            unit=input("Enter Unit name:")
            lecturer=input("LecName:")
            room=input("RoomNo:")
            start_of_lesson=input("Start: (HH:MM:SS)")
            start=datetime.strptime(start_of_lesson, "%H:%M:%S")
            print(type(start))
            time_taken=input("Duration: (HH:MM)")
            if time_taken.__contains__(":"):
                t=time_taken.split(":")
                #t=['2','30']
                hour=int(t[0])
                minute=int(t[1])
            else:
                minute = 0
                hour = int(time_taken)
            duration=timedelta(hours=hour,minutes=minute)
            print(type(duration))
            End_of_session= start+duration


            details["Unit"]=unit
            details["LecName"]=lecturer
            details["RoomNO"]=room
            details["Start"]=str(start.time())
            details["Duration"]=str(duration)
            details["End"]=str(End_of_session.time())
        j=json.dumps(details,indent=4)
        print(j)

c1=Bell_intervals()
c1.Time()