class Vehicle:
    def __init__(self, brand, model, rental_price):
        self.brand = brand
        self.model = model
        self.rental_price = rental_price

    def calculate_rent(self, days):
        return self.rental_price * days


class Car(Vehicle):
    def calculate_rent(self, days):
        rent = self.rental_price * days

        if days >= 5:
            rent *= 0.90

        return rent


class Bike(Vehicle):
    def calculate_rent(self, days):
        rent = self.rental_price * days

        if days >= 3:
            rent *= 0.95

        return rent


class Truck(Vehicle):
    def calculate_rent(self, days):
        return (self.rental_price + 500) * days


car = Car("Toyota", "Camry", 2000)
bike = Bike("Honda", "Shine", 800)
truck = Truck("Tata", "Prima", 5000)

vehicles = [car, bike, truck]

for vehicle in vehicles:
    print(
        f"{vehicle.brand} {vehicle.model} - "
        f"Rent for 5 days: ₹{vehicle.calculate_rent(5)}"
    )
