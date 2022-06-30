from PatientModule import Patient
from LineModule import Line

def DischargePatient(TotalLines):
    name = str(input("Enter the name of Patient : "))
    age = int(input("Enter the age of Patient : "))
    state = str(input("Enter the state of Patient : "))
    found = False
    
    for lines in TotalLines:
        if(state == lines.Name):
            lines.DischargePatient(name)
            found = True
    
    if(found):
        pass
    else:
        print(f"{state} is not a valid state.")