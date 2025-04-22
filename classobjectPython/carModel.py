# carmodel.py
# This is a class to represent a car model
# It includes attributes for brand, model, colour, and engine type
class carModel:
    message = " car details "

    def __init__(self, brand="unknown", model="generic", colour="unknown", enginetype="unknown"):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.enginetype = enginetype

    def display(self):
        print(carModel.message)
        return f"Brand: {self.brand}, Model: {self.model}, Colour: {self.colour}, Engine Type: {self.enginetype}"


# Example usage of the carModel class
# Creating instances of carModel with different attributes
Toyota_car = carModel("Toyota", "Corolla", "Red", "Petrol")
print(Toyota_car.display())
Honda_car = carModel("Honda", "Civic", "Blue", "Diesel")
print(Honda_car.display())
Ford_car = carModel("Ford", "Mustang", "Black", "Petrol")
print(Ford_car.display())
Chevrolet_car = carModel("Chevrolet", "Camaro", "Yellow", "Petrol")
print(Chevrolet_car.display())
unknown_car = carModel(colour="White", enginetype="Electric")
print(unknown_car.display())
