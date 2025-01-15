from datetime import date

class People:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    
    def age(self):
        birthdate=date(*map(int,self.dob.split('-'))) #if i write 2004-06-24 it splits when it sees -
        today=date.today()
        return today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
    #subtracts 1 if bday has not came yet



name=str(input("Enter name: "))
country=str(input("Enter country: "))
dob=str(input("Enter date of birth in yyyy-mm-dd format: "))

person=People(name,country,dob)
print(f"{person.name} is {person.age()} years old")
