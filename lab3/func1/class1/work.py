class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Car is starting")

class ElectroCar(Car):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def newStart(self):
        print(f"new {self.brand} is working now")

car1 = Car("ms","new")
car2 = ElectroCar("bmw","old")
#print(car2.newStart())
car1.start()