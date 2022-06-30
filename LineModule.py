from PatientModule import Patient

class Line:

    def __init__(self, name, beds, TotalLines):
        self.Name = name
        self.MaxBeds = int(beds)
        self.Beds = []
        self.OcupiedBeds = int(0)
        self.FreeBeds = self.MaxBeds - self.OcupiedBeds
        TotalLines.append(self)
        

    def AdmitPatient(self, patient):
        if(self.FreeBeds > 0):
            self.Beds.append(patient)
            self.OcupiedBeds += 1
            self.FreeBeds -= 1
        else:
            print("No more free beds in this line. You can check for free Beds in other lines.")


    def DischargePatient(self, patient):
        bednumber = next(filter(lambda x: x[1].Name == patient, enumerate(self.Beds)))[0]
        self.Beds[bednumber] = self.Beds[self.OcupiedBeds - 1]
        self.OcupiedBeds -= 1
        self.FreeBeds += 1
        self.Beds.pop()
