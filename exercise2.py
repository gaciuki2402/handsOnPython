#amount Ksh
#input=amount
#1dollar=155ksh
#GDP=140.75KSH
#1YEN=75kSH
#Euro=130.37
#Rand=7.75
#30.5UGX=1KSH
#40.75 TZ=1KSH
class Currency():
    def Currency_Converter(self):
        amount=eval(input("Enter amount in KSH:"))
        currency=input("Enter the currency:").upper()

        Currency_from_other_countries={
                "USD":{
                    1:155
                },
                "GDP":{
                    1:140.75
                },
                "YEN":{
                    1:75
                },
                "EURO":{
                    1:130
                },
                "RAND":{
                    1:7.75
                },
                "UGX":{
                    30.5:1
                },
                "TZ":{
                    40.75:1
                }

        }
        rates=Currency_from_other_countries[currency]
        for key,value in rates.items():
            if key==1:
                converted_output=amount/value
                print(converted_output)
            elif key>1:
                converted_output=amount*key
                print(converted_output)

C1=Currency()
C1.Currency_Converter()