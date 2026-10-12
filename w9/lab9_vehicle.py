# Lab 9 : Inheritance (Vehicle -> Car, Truck)
class Vehicle:                                   # คลาสแม่
    def __init__(self, plate, brand, daily_rate):
        self.plate = plate
        self.brand = brand
        self.daily_rate = daily_rate

    def show_info(self):
        print(self.plate, self.brand, "rate/day:", self.daily_rate)

    def calculate_rental_cost(self, days):
        return self.daily_rate * days


class Car(Vehicle):                              # รถยนต์นั่ง
    def __init__(self, plate, brand, daily_rate, seats):
        super().__init__(plate, brand, daily_rate)
        self.seats = seats

    def show_info(self):
        super().show_info()
        print("seats:", self.seats)

    def calculate_rental_cost(self, days):       # override: เช่า 7 วัน จ่าย 5
        free = (days // 7) * 2
        return self.daily_rate * (days - free)


class Truck(Vehicle):                            # รถบรรทุก
    def __init__(self, plate, brand, daily_rate, payload):
        super().__init__(plate, brand, daily_rate)
        self.payload = payload

    def show_info(self):
        super().show_info()
        print("payload:", self.payload, "ton")
    # ไม่ override calculate_rental_cost -> ใช้ของแม่ (คิดปกติ)


car = Car("1กข 1234", "Toyota", 1500, 5)
truck = Truck("2คง 5678", "Isuzu", 2500, 3)
car.show_info()
print("7 days =", car.calculate_rental_cost(7))
truck.show_info()
print("7 days =", truck.calculate_rental_cost(7))
