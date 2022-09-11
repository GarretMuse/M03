# Garret Muse
# M03_lab 
# This program organizes data about a car input from a user


vehicle_type = input("What type of vehicle are you looking for? ")
year = input("What year? ")
make = input("What make? ")
model = input("What model? ")
doors = input("How many doors? ")
roof = input("Would you like a solid roof or a sun roof? ")

class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display():
        print("")
        print(f"Vehicle type: {vehicle_type}")
        print(f"Year: {year}")
        print(f"Make: {make}")
        print(f"Model: {model}")
        print(f"Number of doors: {doors}")
        print(f"Type of roof: {roof}")

Automobile.display()



