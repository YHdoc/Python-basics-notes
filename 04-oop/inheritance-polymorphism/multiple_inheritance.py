# 다중 상속

class Flyable:
    """날 수 있는 능력을 가진 클래스"""
    
    def __init__(self):
        self.altitude = 0
    
    def take_off(self):
        self.altitude = 100
        return "이륙했습니다."
    
    def land(self):
        self.altitude = 0
        return "착륙했습니다."
    
    def fly(self, distance):
        return f"{distance}km를 날아갔습니다."

class Swimmable:
    """수영할 수 있는 능력을 가진 클래스"""
    
    def __init__(self):
        self.depth = 0
    
    def dive(self, depth):
        self.depth = depth
        return f"{depth}m 깊이로 잠수했습니다."
    
    def surface(self):
        self.depth = 0
        return "수면으로 올라왔습니다."
    
    def swim(self, distance):
        return f"{distance}m를 수영했습니다."

class Animal:
    """동물 기본 클래스"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        return f"{self.name}가 먹이를 먹습니다."
    
    def sleep(self):
        return f"{self.name}가 잠을 잡니다."

class Bird(Animal, Flyable):
    """새 클래스 - Animal과 Flyable을 다중 상속"""
    
    def __init__(self, name, species, wing_span):
        Animal.__init__(self, name, species)
        Flyable.__init__(self)
        self.wing_span = wing_span
    
    def chirp(self):
        return f"{self.name}가 짹짹 웁니다."

class Duck(Animal, Flyable, Swimmable):
    """오리 클래스 - Animal, Flyable, Swimmable을 다중 상속"""
    
    def __init__(self, name, species, wing_span):
        Animal.__init__(self, name, species)
        Flyable.__init__(self)
        Swimmable.__init__(self)
        self.wing_span = wing_span
    
    def quack(self):
        return f"{self.name}가 꽥꽥 웁니다."

class Penguin(Animal, Swimmable):
    """펭귄 클래스 - Animal과 Swimmable을 다중 상속"""
    
    def __init__(self, name, species):
        Animal.__init__(self, name, species)
        Swimmable.__init__(self)
    
    def waddle(self):
        return f"{self.name}가 뒤뚱뒤뚱 걷습니다."

# 다이아몬드 문제 해결 예제
class A:
    def method(self):
        return "A의 메서드"

class B(A):
    def method(self):
        return "B의 메서드"

class C(A):
    def method(self):
        return "C의 메서드"

class D(B, C):
    pass

if __name__ == "__main__":
    print("=== 다중 상속 예제 ===")
    
    # 새 객체 생성
    bird = Bird("짹짹이", "카나리아", 20)
    print(f"새: {bird.name} ({bird.species})")
    print(bird.eat())
    print(bird.chirp())
    print(bird.take_off())
    print(bird.fly(10))
    print(bird.land())
    
    # 오리 객체 생성
    duck = Duck("도날드", "청둥오리", 30)
    print(f"\n오리: {duck.name} ({duck.species})")
    print(duck.eat())
    print(duck.quack())
    print(duck.take_off())
    print(duck.fly(5))
    print(duck.land())
    print(duck.dive(3))
    print(duck.swim(20))
    print(duck.surface())
    
    # 펭귄 객체 생성
    penguin = Penguin("펭펭이", "아델리펭귄")
    print(f"\n펭귄: {penguin.name} ({penguin.species})")
    print(penguin.eat())
    print(penguin.waddle())
    print(penguin.dive(10))
    print(penguin.swim(50))
    print(penguin.surface())
    
    # MRO 확인
    print(f"\n=== MRO (Method Resolution Order) ===")
    print(f"Bird MRO: {Bird.__mro__}")
    print(f"Duck MRO: {Duck.__mro__}")
    print(f"Penguin MRO: {Penguin.__mro__}")
    
    # 다이아몬드 문제 해결
    print(f"\n=== 다이아몬드 문제 해결 ===")
    d = D()
    print(f"D().method(): {d.method()}")
    print(f"D MRO: {D.__mro__}")
    
    # super()를 사용한 다중 상속
    print(f"\n=== super()를 사용한 다중 상속 ===")
    
    class Base1:
        def __init__(self):
            print("Base1.__init__")
    
    class Base2:
        def __init__(self):
            print("Base2.__init__")
    
    class Derived(Base1, Base2):
        def __init__(self):
            super().__init__()
            print("Derived.__init__")
    
    derived = Derived()
    print(f"Derived MRO: {Derived.__mro__}")
