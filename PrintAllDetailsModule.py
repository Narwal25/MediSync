from PatientModule import Patient
from LineModule import Line


def PrintAllDetails(TotalLines):     
    for line in TotalLines:
        print(f"Line {line.Name}")
        print(f"\tTotal Beds = {line.MaxBeds}")
        print(f"\tFree Beds = {line.FreeBeds}")
        print(f"\tOcupiedBeds Beds = {line.OcupiedBeds}")
        print(f"\tAll Patients are: ")
        for patient in line.Beds:
            print(f"\t\tName: {patient.Name}\tAge: {patient.Age}")


if __name__ =="__main__":
    PrintAllDetails(TotalLines= [1,4,5])