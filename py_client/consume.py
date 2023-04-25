import requests

class Consumption:

    def __init__(self):
        self.sig = "http://127.0.0.1:8000/"

    def __str__(self):
        return self.sig
    
    def simpletext(self):
        signAl = self.sig
        responSe = requests.get(signAl)
        output_sig = responSe.text
        return output_sig
    
    def simpleJson(self):
        signAl = self.sig
        responSe = requests.get(signAl)
        output_sig = responSe.json()
        return output_sig
    

    def sTatsCode(self):
        signAl = self.sig
        response = requests.get(signAl)
        output_sig = response.status_code
        return output_sig
    
def SigOut():
    text = Consumption.simpletext()
    simpleJS = Consumption.simpleJson()
    statusC = Consumption.sTatsCode()

    return str(text, simpleJS, statusC)

sigO = SigOut
print(str(sigO))

