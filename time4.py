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
            start_of_lesson=input("Start: (HH:MM:SS")
            start=datetime.strptime(start_of_lesson, "%H:%M:%S").time()
            time_take=input("Duration: (HH:MM:SS)")
            time_taken=f"{time_take}:00:00"
            duration = datetime.strptime(time_taken, "%H:%M:%S").time()
            print(type(duration))
            End_of_sesion=start+duration
            details["Unit"]=unit
            details["LecName"]=lecturer
            details["RoomNO"]=room
            details["Start"]=str(start)
            details["Duration"]=str(time_taken)
            details["End"]=End_of_sesion
        j=json.dumps(details)
        print(j)

c1=Bell_intervals()
c1.Time()