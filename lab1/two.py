def checkDistinction(num:float):
    if(num>=80):
        print("Distinction \n")
    elif(num>=65):
        print(" First Division")
    elif(num>=55):
        print(" Second Division")
    elif(num>=40):
        print(" Third Division")
    elif(num<40):
        print(" Fail")


percentage = float(input("Enter percentage"))
checkDistinction(percentage)
