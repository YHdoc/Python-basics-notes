# 기본 상속 사용법

class Animal:
    """동물 기본 클래스"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return "동물이 소리를 냅니다."
    
    def get_info(self):
        return f"{self.name}는 {self.age}살입니다."

class Dog(Animal):
    """개 클래스 - Animal을 상속"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self):
        return f"{self.name}가 멍멍 짖습니다."
    
    def get_info(self):
        return f"{self.name}는 {self.age}살 {self.breed}입니다."

class Cat(Animal):
    """고양이 클래스 - Animal을 상속"""
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        return f"{self.name}가 야옹 웁니다."
    
    def get_info(self):
        return f"{self.name}는 {self.age}살 {self.color} 고양이입니다."

class Bird(Animal):
    """새 클래스 - Animal을 상속"""
    
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species
    
    def speak(self):
        return f"{self.name}가 짹짹 웁니다."
    
    def fly(self):
        return f"{self.name}가 날아갑니다."

if __name__ == "__main__":
    print("=== 기본 상속 예제 ===")
    
    # 동물 객체들 생성
    dog = Dog("멍멍이", 3, "골든 리트리버")
    cat = Cat("야옹이", 2, "검은색")
    bird = Bird("짹짹이", 1, "카나리아")
    
    # 정보 출력
    print(dog.get_info())
    print(cat.get_info())
    print(bird.get_info())
    
    # 소리 내기
    print(f"\n소리:")
    print(dog.speak())
    print(cat.speak())
    print(bird.speak())
    
    # 새만의 특별한 메서드
    print(f"\n{bird.fly()}")
    
    # isinstance 확인
    print(f"\n타입 확인:")
    print(f"dog는 Animal인가? {isinstance(dog, Animal)}")
    print(f"dog는 Dog인가? {isinstance(dog, Dog)}")
    print(f"dog는 Cat인가? {isinstance(dog, Cat)}")
    
    # issubclass 확인
    print(f"\n상속 관계 확인:")
    print(f"Dog는 Animal의 자식인가? {issubclass(Dog, Animal)}")
    print(f"Cat은 Animal의 자식인가? {issubclass(Cat, Animal)}")
    print(f"Dog는 Cat의 자식인가? {issubclass(Dog, Cat)}")
