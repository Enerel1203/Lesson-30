class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"


class Ferrari:
    def fuel_type(self):
        return "Petrol (High Octane)"

    def max_speed(self):
        return "340 km/h"


# Polymorphism example
for car in (BMW(), Ferrari()):
    print(f"Car: {car.__class__.__name__}")
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
    print()