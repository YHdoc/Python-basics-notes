# 상속과 다형성 🧬

> 객체지향 프로그래밍의 핵심 개념인 상속과 다형성을 학습하고 실무에서 활용하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 상속의 개념과 기본 사용법 이해
- [ ] 부모 클래스와 자식 클래스의 관계 학습
- [ ] 메서드 오버라이딩과 super() 함수 사용법
- [ ] 다중 상속과 MRO (Method Resolution Order) 이해
- [ ] 다형성의 개념과 활용 방법 학습
- [ ] 추상 클래스와 인터페이스 패턴 이해
- [ ] 실무에서 자주 사용되는 상속 패턴 익히기

## 📚 핵심 개념

### 1. 기본 상속
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "동물이 소리를 냅니다."

class Dog(Animal):
    def speak(self):
        return f"{self.name}가 멍멍 짖습니다."

# 사용
dog = Dog("멍멍이")
print(dog.speak())
```

### 2. super() 함수
```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
```

### 3. 다형성
```python
def make_sound(animal):
    return animal.speak()

animals = [Dog("멍멍이"), Cat("야옹이")]
for animal in animals:
    print(make_sound(animal))
```

### 4. 추상 클래스
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
```

## 📁 예제 파일

- `basic_inheritance.py` - 기본 상속 사용법
- `method_overriding.py` - 메서드 오버라이딩
- `super_function.py` - super() 함수 사용법
- `multiple_inheritance.py` - 다중 상속
- `polymorphism.py` - 다형성 활용
- `abstract_classes.py` - 추상 클래스
- `practical_examples.py` - 실무에서 자주 사용되는 상속 패턴

## 🏃‍♂️ 실습 과제

1. **도형 클래스 계층**: 도형들의 상속 관계를 구현한 클래스들
2. **동물 클래스 계층**: 다양한 동물들의 상속 관계 구현
3. **직원 관리 시스템**: 직원들의 상속 관계를 활용한 관리 시스템
4. **게임 캐릭터 시스템**: 게임 캐릭터들의 상속과 다형성 활용

## 💡 실무 팁

### ✅ 좋은 예시
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return f"{self.brand} {self.model}이 시작됩니다."

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def start(self):
        return f"{self.brand} {self.model} 자동차가 시동을 겁니다."
```

### ❌ 피해야 할 예시
```python
# 너무 깊은 상속 계층
class A: pass
class B(A): pass
class C(B): pass
class D(C): pass
class E(D): pass  # 너무 깊음

# 불필요한 상속
class StringUtils(str):  # str을 상속할 필요 없음
    pass
```

## 🔗 관련 주제

- [클래스와 객체](../../04-oop/classes-and-objects/) - 상속의 기초가 되는 클래스
- [특수 메서드](../../04-oop/magic-methods/) - 상속에서 사용되는 특수 메서드들
- [함수 정의와 호출](../../03-functions-modules/functions/) - 메서드 정의의 기초

## 📖 추가 학습 자료

- [Python 공식 문서 - 상속](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [PEP 8 - 클래스 상속 가이드](https://pep8.org/#class-names)

---

**다음 단계**: [특수 메서드](../../04-oop/magic-methods/) 학습하기
