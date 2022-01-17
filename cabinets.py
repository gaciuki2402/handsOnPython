import json
class Current_Cabinet(object):
    def CabinetSecretaries(self):
        self.name_of_the_cabinet=input("Enter name of the cabinet:").title()

        Cabinet_of_KE={
        "Pro Amina":{
                "cabinet secretary":"Amina Mohamed",
                "office":"Sports and Heritage",
                "year":2017,
                "nationality":"Kenyan"},

            "Pro Keter": {
                "cabinet secretary":"Charles Keter",
                "office":"Devolution and ASAL Areas",
                "year":2013,
                "nationality":"Kenyan"},

            "Pro John": {
                "cabinet secretary":"John Munyes",
                "office":"Petroleum and Mining",
                "year":2007,
                "nationality":"Kenyan"},
            "Pro Munya": {
                "cabinet secretary":"Peter Munya",
                "office":"Agriculture,Livestock,Fisheries and Coop",
                "year": 2013,
                "nationality":"Kenyan"}
        }
        details=Cabinet_of_KE[self.name_of_the_cabinet]
        jsonDetails=json.dumps(details,indent=4)
        print(jsonDetails)

c1=Current_Cabinet()
c1.CabinetSecretaries()




