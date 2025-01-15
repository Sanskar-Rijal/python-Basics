class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    
    def drive(self):
        print(f"{self.make} {self.model} is now being driven")

class Car(Vehicle):
    def drive(self):
        print(f"{self.make} {self.model} is now being driven and it is a car")


vehicle= Vehicle("tata", "nano")
vehicle.drive()

car = Car("Toyota", "Corolla")
car.drive()