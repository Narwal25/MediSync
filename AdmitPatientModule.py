from PatientModule import Patient
from LineModule import Line

def AdmitPatient(TotalLines):
    name = str(input("Enter the name of Patient : "))
    age = int(input("Enter the age of Patient : "))
    state = str(input("Enter the state of Patient : "))
    
    patient = Patient(name, age, state)
    found = False
    
    for lines in TotalLines:
        if(state.capitalize() == lines.Name):
            lines.AdmitPatient(patient)
            found = True
    
    if(found):
        pass
    else:
        print(f"{state} is not a valid state.")
        print("Valid states are: ",end="")
        for line in TotalLines:
            print(f"\t{line.Name}",end="")
