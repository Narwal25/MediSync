class Patient:

    def __init__(self, name, age, state):
        self.Name = name
        self.Age = int(age)
        self.State = state

    def details(self):
        print(f"Name of patient is {self.Name}, Age of patient is {self.Age} and state of patient is {self.State}")

    def changeState(self):
        newState = input("Enter new state of patients")
        self.State = newState


