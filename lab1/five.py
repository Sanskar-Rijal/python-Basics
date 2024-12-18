def inputStudent():
    marks=[]
    for n in range(10):
        percentage=float(input("Enter marks of student"))
        marks.append(percentage)
    return marks


studentmarks=inputStudent()
print(studentmarks)