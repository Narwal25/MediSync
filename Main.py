# Project for predicting the line for covid patients and the availablity of beds state wise

# Impoting all the modules of Project
import dill
from PatientModule import Patient
from LineModule import Line
from AdmitPatientModule import AdmitPatient
from DischargePatientModule import DischargePatient
from ManageLineModule import ManageLines
from PrintAllDetailsModule import PrintAllDetails
from WelcomeModule import Welcome

# Loading Last Session
try:
    dill.load_session("TotalLines.pkl")
except:
    TotalLines = []

while(True):

    Welcome()

    choice = input()
    if(choice in ['a', 'A', "admit", "Admit", "ADMIT"]):
        AdmitPatient(TotalLines=TotalLines) 
       
    elif(choice in ['d', 'D', "discharge", "Discharge", "DISCHARGE"]):
        DischargePatient(TotalLines=TotalLines)
    
    elif(choice in ['m', 'M', "manage", "Manage", "MANAGE"]):
         ManageLines(TotalLines=TotalLines)

    elif(choice in ['p', 'P', "print", "Print", "PRINT", "details", "Details", "print details"]):
        PrintAllDetails(TotalLines = TotalLines)

    elif(choice in ['e', 'E', "exit", "Exit", "Exit"]):
        dill.dump_session("TotalLines.pkl")
        break

    else:
        print("Enter a valid option.")