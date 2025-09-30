# 메서드 오버라이딩

class Vehicle:
    """차량 기본 클래스"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def start(self):
        return f"{self.brand} {self.model}이 시작됩니다."
    
    def stop(self):
        self.speed = 0
        return f"{self.brand} {self.model}이 정지합니다."
    
    def accelerate(self, amount):
        self.speed += amount
        return f"속도가 {self.speed}km/h로 증가했습니다."
    
    def get_info(self):
        return f"{self.year}년 {self.brand} {self.model}"

class Car(Vehicle):
    """자동차 클래스"""
    
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    
    def start(self):
        return f"{self.brand} {self.model} 자동차가 시동을 겁니다."
    
    def open_trunk(self):
        return f"{self.brand} {self.model}의 트렁크가 열립니다."
    
    def get_info(self):
        return f"{super().get_info()} (문 {self.doors}개)"

class Motorcycle(Vehicle):
    """오토바이 클래스"""
    
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
    
    def start(self):
        return f"{self.brand} {self.model} 오토바이가 시동을 겁니다."
    
    def wheelie(self):
        return f"{self.brand} {self.model}이 휠리를 합니다!"
    
    def get_info(self):
        return f"{super().get_info()} ({self.engine_size}cc)"

class Truck(Vehicle):
    """트럭 클래스"""
    
    def __init__(self, brand, model, year, cargo_capacity):
        super().__init__(brand, model, year)
        self.cargo_capacity = cargo_capacity
        self.cargo = 0
    
    def start(self):
        return f"{self.brand} {self.model} 트럭이 시동을 겁니다."
    
    def load_cargo(self, amount):
        if self.cargo + amount <= self.cargo_capacity:
            self.cargo += amount
            return f"화물 {amount}톤을 적재했습니다. (총 {self.cargo}톤)"
        else:
            return f"화물 적재 한도를 초과했습니다. (최대 {self.cargo_capacity}톤)"
    
    def unload_cargo(self, amount):
        if self.cargo >= amount:
            self.cargo -= amount
            return f"화물 {amount}톤을 하역했습니다. (남은 {self.cargo}톤)"
        else:
            return f"하역할 화물이 부족합니다. (현재 {self.cargo}톤)"
    
    def get_info(self):
        return f"{super().get_info()} (적재량 {self.cargo_capacity}톤)"

if __name__ == "__main__":
    print("=== 메서드 오버라이딩 예제 ===")
    
    # 다양한 차량 객체 생성
    car = Car("현대", "소나타", 2023, 4)
    motorcycle = Motorcycle("혼다", "CBR600", 2023, 600)
    truck = Truck("기아", "봉고", 2023, 5)
    
    vehicles = [car, motorcycle, truck]
    
    # 각 차량의 정보와 시작
    for vehicle in vehicles:
        print(f"\n{vehicle.get_info()}")
        print(vehicle.start())
    
    # 각 차량만의 특별한 기능
    print(f"\n=== 특별한 기능 ===")
    print(car.open_trunk())
    print(motorcycle.wheelie())
    print(truck.load_cargo(3))
    print(truck.load_cargo(2))
    print(truck.unload_cargo(1))
    
    # 가속 기능 (상속받은 메서드)
    print(f"\n=== 가속 기능 ===")
    for vehicle in vehicles:
        print(vehicle.accelerate(20))
        print(vehicle.accelerate(30))
