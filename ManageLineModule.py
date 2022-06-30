from LineModule import Line

def ManageLines(TotalLines):
    while(True):
        print("\n\t\t\t\tManage lines from here.\nWhat do you want to do\t\tList all lines(l)\t\tCreate new line(c)\t\texit(e)")
        
        choice = input()
        if(choice in ['l', 'L', "list", "List", "LIST"]):
            i = 1
            for line in TotalLines:
                print(f"\nLine{i} is for Patient of {line.Name} state.")
                print(f"It has Total {line.MaxBeds} of which {line.OcupiedBeds} are already ocupied.")
                i += 1

        elif(choice in ['c', 'C', "create", "Create", "CREATE"]):
            name = input("Enter the Patients for which line is to be created : ")
            beds = int(input("Enter total number of beds in line : "))
            
            line = Line(name, beds, TotalLines=TotalLines)


        elif(choice in ['e', 'E', "exit", "Exit", "Exit"]):
            break
        else:
            print("Enter a valid option.")
