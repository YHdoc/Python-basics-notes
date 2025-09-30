# 다형성 활용

class Shape:
    """도형 기본 클래스"""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        raise NotImplementedError("하위 클래스에서 구현해야 합니다.")
    
    def perimeter(self):
        raise NotImplementedError("하위 클래스에서 구현해야 합니다.")
    
    def get_info(self):
        return f"{self.name}: 넓이={self.area():.2f}, 둘레={self.perimeter():.2f}"

class Rectangle(Shape):
    """사각형 클래스"""
    
    def __init__(self, width, height):
        super().__init__("사각형")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """원 클래스"""
    
    def __init__(self, radius):
        super().__init__("원")
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Triangle(Shape):
    """삼각형 클래스"""
    
    def __init__(self, base, height, side1, side2):
        super().__init__("삼각형")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.base + self.side1 + self.side2

class Square(Rectangle):
    """정사각형 클래스"""
    
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "정사각형"

# 다형성을 활용한 함수들
def calculate_total_area(shapes):
    """여러 도형의 총 넓이를 계산하는 함수"""
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

def calculate_total_perimeter(shapes):
    """여러 도형의 총 둘레를 계산하는 함수"""
    total = 0
    for shape in shapes:
        total += shape.perimeter()
    return total

def print_shapes_info(shapes):
    """여러 도형의 정보를 출력하는 함수"""
    for shape in shapes:
        print(shape.get_info())

def find_largest_shape(shapes):
    """가장 큰 넓이를 가진 도형을 찾는 함수"""
    if not shapes:
        return None
    
    largest = shapes[0]
    for shape in shapes[1:]:
        if shape.area() > largest.area():
            largest = shape
    return largest

def sort_shapes_by_area(shapes):
    """넓이 순으로 도형들을 정렬하는 함수"""
    return sorted(shapes, key=lambda shape: shape.area())

# 동물 예제
class Animal:
    """동물 기본 클래스"""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        raise NotImplementedError("하위 클래스에서 구현해야 합니다.")
    
    def move(self):
        return f"{self.name}가 움직입니다."

class Dog(Animal):
    def make_sound(self):
        return f"{self.name}가 멍멍 짖습니다."

class Cat(Animal):
    def make_sound(self):
        return f"{self.name}가 야옹 웁니다."

class Bird(Animal):
    def make_sound(self):
        return f"{self.name}가 짹짹 웁니다."
    
    def move(self):
        return f"{self.name}가 날아갑니다."

def animal_concert(animals):
    """동물들의 콘서트 함수"""
    print("=== 동물 콘서트 ===")
    for animal in animals:
        print(animal.make_sound())
        print(animal.move())
        print()

if __name__ == "__main__":
    print("=== 다형성 예제 ===")
    
    # 도형 객체들 생성
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(6, 4, 5, 5),
        Square(4)
    ]
    
    # 다형성을 활용한 함수들 호출
    print("=== 도형 정보 ===")
    print_shapes_info(shapes)
    
    print(f"\n총 넓이: {calculate_total_area(shapes):.2f}")
    print(f"총 둘레: {calculate_total_perimeter(shapes):.2f}")
    
    largest = find_largest_shape(shapes)
    print(f"가장 큰 도형: {largest.get_info()}")
    
    print(f"\n넓이 순 정렬:")
    sorted_shapes = sort_shapes_by_area(shapes)
    for shape in sorted_shapes:
        print(f"  {shape.get_info()}")
    
    # 동물 예제
    print(f"\n=== 동물 다형성 예제 ===")
    animals = [
        Dog("멍멍이"),
        Cat("야옹이"),
        Bird("짹짹이")
    ]
    
    animal_concert(animals)
    
    # isinstance와 issubclass를 활용한 다형성
    print("=== 타입 확인 ===")
    for shape in shapes:
        print(f"{shape.name}: Shape인가? {isinstance(shape, Shape)}")
        print(f"  Rectangle인가? {isinstance(shape, Rectangle)}")
        print(f"  Circle인가? {isinstance(shape, Circle)}")
    
    # 상속 관계 확인
    print(f"\n상속 관계:")
    print(f"Rectangle은 Shape의 자식인가? {issubclass(Rectangle, Shape)}")
    print(f"Square는 Rectangle의 자식인가? {issubclass(Square, Rectangle)}")
    print(f"Square는 Shape의 자식인가? {issubclass(Square, Shape)}")
