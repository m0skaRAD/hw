class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

car = Car("BMW", "i7", 2022, 4)
motorcycle = Motorcycle("YANAHA", "DRAG STAR 1100", 2021, "500cc")

print(f"Car: {car.make} {car.model} {car.year}, {car.num_doors} doors")
print(f"Motorcycle: {motorcycle.make} {motorcycle.model} {motorcycle.year}, {motorcycle.engine_size}")

