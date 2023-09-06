#M03 Lab - Case Study: Lists, Functions, and Classes
#Peyton Chitwood

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
    
    def display(self):
        print(f'Vehicle type: {self.vehicle_type}')

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def display(self):
        super().display()
        print(f'Year: {self.year}')
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
        print(f'Doors: {self.doors}')
        print(f'Roof: {self.roof}')

inputYear = input('Enter year: ')
inputMake = input('Enter make: ')
inputModel = input('Enter model: ')
inputDoors = input('Enter doors: ')
inputRoof = input('Enter roof: ')

car = Automobile("car", inputYear, inputMake, inputModel, inputDoors, inputRoof)
car.display()