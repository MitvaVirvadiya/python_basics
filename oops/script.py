class Car: 
    car_count = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.car_count += 1
        
    def print_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    def set_brand(self, brand):
        self.__brand = brand
    
    def fuel_type(self):
        return "Petrol"
    
    @staticmethod
    def general_details():
        return "This is a car"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery
        
    def battery_info(self):
        return f"Battery is {self.battery}"
    
    def fuel_type(self):
        return "Electric"
    
my_car = Car("Honda", "Jazz")

# print(f"Brand: {my_car.get_brand()}\nModel: {my_car.model}")
# print(my_car.print_name())
# print(my_car.fuel_type())
print(Car.general_details())
print(my_car.model)

my_car.set_brand("Hundai")
print(my_car.get_brand())

my_electric_car = ElectricCar("Tesla", "Model x", "165KWH")

# print(my_electric_car.battery_info())
# print(my_electric_car.get_brand())
# print(my_electric_car.fuel_type())

# print(Car.car_count)

print(isinstance(my_electric_car, Car))
print(isinstance(my_electric_car, ElectricCar))

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())