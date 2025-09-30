# 추상 클래스

from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 추상 클래스"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """넓이를 계산하는 추상 메서드"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """둘레를 계산하는 추상 메서드"""
        pass
    
    def get_info(self):
        """도형 정보를 반환하는 일반 메서드"""
        return f"{self.name}: 넓이={self.area():.2f}, 둘레={self.perimeter():.2f}"

class Rectangle(Shape):
    """사각형 클래스 - Shape를 상속"""
    
    def __init__(self, width, height):
        super().__init__("사각형")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """원 클래스 - Shape를 상속"""
    
    def __init__(self, radius):
        super().__init__("원")
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# 추상 메서드가 없는 추상 클래스
class Animal(ABC):
    """동물 추상 클래스"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        return f"{self.name}가 먹이를 먹습니다."
    
    def sleep(self):
        return f"{self.name}가 잠을 잡니다."
    
    @abstractmethod
    def make_sound(self):
        """소리를 내는 추상 메서드"""
        pass
    
    @abstractmethod
    def move(self):
        """움직이는 추상 메서드"""
        pass

class Dog(Animal):
    """개 클래스 - Animal을 상속"""
    
    def __init__(self, name, breed):
        super().__init__(name, "개")
        self.breed = breed
    
    def make_sound(self):
        return f"{self.name}가 멍멍 짖습니다."
    
    def move(self):
        return f"{self.name}가 뛰어갑니다."

class Fish(Animal):
    """물고기 클래스 - Animal을 상속"""
    
    def __init__(self, name, water_type):
        super().__init__(name, "물고기")
        self.water_type = water_type
    
    def make_sound(self):
        return f"{self.name}가 물속에서 소리를 냅니다."
    
    def move(self):
        return f"{self.name}가 헤엄쳐갑니다."

# 여러 추상 메서드를 가진 추상 클래스
class Vehicle(ABC):
    """차량 추상 클래스"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    @abstractmethod
    def start(self):
        """시동을 거는 추상 메서드"""
        pass
    
    @abstractmethod
    def stop(self):
        """정지하는 추상 메서드"""
        pass
    
    @abstractmethod
    def accelerate(self, amount):
        """가속하는 추상 메서드"""
        pass
    
    def get_info(self):
        return f"{self.year}년 {self.brand} {self.model}"

class Car(Vehicle):
    """자동차 클래스 - Vehicle을 상속"""
    
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    
    def start(self):
        return f"{self.brand} {self.model} 자동차가 시동을 겁니다."
    
    def stop(self):
        self.speed = 0
        return f"{self.brand} {self.model} 자동차가 정지합니다."
    
    def accelerate(self, amount):
        self.speed += amount
        return f"속도가 {self.speed}km/h로 증가했습니다."

class Motorcycle(Vehicle):
    """오토바이 클래스 - Vehicle을 상속"""
    
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
    
    def start(self):
        return f"{self.brand} {self.model} 오토바이가 시동을 겁니다."
    
    def stop(self):
        self.speed = 0
        return f"{self.brand} {self.model} 오토바이가 정지합니다."
    
    def accelerate(self, amount):
        self.speed += amount
        return f"속도가 {self.speed}km/h로 증가했습니다."

# 추상 클래스를 상속하지 않은 클래스 (에러 발생)
class IncompleteShape(Shape):
    """완전하지 않은 도형 클래스 - 에러 발생"""
    
    def __init__(self, name):
        super().__init__(name)
    
    def area(self):
        return 0
    # perimeter 메서드가 없어서 에러 발생

if __name__ == "__main__":
    print("=== 추상 클래스 예제 ===")
    
    # 도형 객체들 생성
    shapes = [
        Rectangle(5, 3),
        Circle(4)
    ]
    
    print("=== 도형 정보 ===")
    for shape in shapes:
        print(shape.get_info())
    
    # 동물 객체들 생성
    animals = [
        Dog("멍멍이", "골든 리트리버"),
        Fish("금붕어", "민물")
    ]
    
    print(f"\n=== 동물 행동 ===")
    for animal in animals:
        print(f"{animal.name} ({animal.species}):")
        print(f"  {animal.eat()}")
        print(f"  {animal.sleep()}")
        print(f"  {animal.make_sound()}")
        print(f"  {animal.move()}")
        print()
    
    # 차량 객체들 생성
    vehicles = [
        Car("현대", "소나타", 2023, 4),
        Motorcycle("혼다", "CBR600", 2023, 600)
    ]
    
    print(f"=== 차량 동작 ===")
    for vehicle in vehicles:
        print(f"{vehicle.get_info()}:")
        print(f"  {vehicle.start()}")
        print(f"  {vehicle.accelerate(30)}")
        print(f"  {vehicle.stop()}")
        print()
    
    # 추상 클래스 인스턴스화 시도 (에러 발생)
    try:
        # shape = Shape("도형")  # 에러 발생
        print("추상 클래스는 직접 인스턴스화할 수 없습니다.")
    except TypeError as e:
        print(f"에러: {e}")
    
    # 완전하지 않은 클래스 인스턴스화 시도 (에러 발생)
    try:
        # incomplete = IncompleteShape("불완전한 도형")  # 에러 발생
        print("추상 메서드를 구현하지 않은 클래스는 인스턴스화할 수 없습니다.")
    except TypeError as e:
        print(f"에러: {e}")
    
    # isinstance 확인
    print(f"\n=== 타입 확인 ===")
    for shape in shapes:
        print(f"{shape.name}: Shape인가? {isinstance(shape, Shape)}")
        print(f"  ABC인가? {isinstance(shape, ABC)}")
    
    # 상속 관계 확인
    print(f"\n상속 관계:")
    print(f"Rectangle은 Shape의 자식인가? {issubclass(Rectangle, Shape)}")
    print(f"Shape는 ABC의 자식인가? {issubclass(Shape, ABC)}")
