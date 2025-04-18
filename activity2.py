# Base class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Subclass: Car (overrides move method)
class Car(Vehicle):
    def move(self):
        print(" The car drives on the road.")

# Subclass: Plane (overrides move method)
class Plane(Vehicle):
    def move(self):
        print(" The plane flies through the sky.")

# Subclass: Boat (overrides move method)
class Boat(Vehicle):
    def move(self):
        print("The boat sails across the sea.")

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat()]

# Loop through each and call the polymorphic move() method
for vehicle in vehicles:
    vehicle.move()
