import json
from datetime import datetime
class Timing():
    def schedule(self):
        myTime={

        }
        BusName=input("Bus Name:")
        fare=input("Fare:")
        bus_stop=input("Bus Stop:")
        departure=input("Departure, HH:MM:SS:")
        print(type(departure))
        departure_time=datetime.strptime(departure, "%H:%M:%S") #Coverting string to datetime object
        print(type(departure_time))
        arrival=input("Arrival, HH:MM:SS:")
        arrival_time=datetime.strptime(arrival, "%H:%M:%S")
        print(type(arrival_time))
        duration=arrival_time-departure_time
        print(duration)

        myTime["Bus Name"]=BusName
        myTime["Fare"]=fare
        myTime["Bus Stop"]=bus_stop
        myTime["Departure"]=str(departure)
        myTime["Arrival"]=str(arrival)
        myTime["Duration"]=f"{duration}"
        T=json.dumps(myTime,indent=4)
        print(T)
t1=Timing()
t1.schedule()


