# 특수 메서드 (Magic Methods) ✨

> Python의 특수 메서드들을 학습하고 클래스를 더욱 강력하고 직관적으로 만드는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 특수 메서드의 개념과 __init__, __str__, __repr__ 이해
- [ ] 산술 연산자 오버로딩 (__add__, __sub__, __mul__ 등)
- [ ] 비교 연산자 오버로딩 (__eq__, __lt__, __gt__ 등)
- [ ] 컨테이너 메서드 (__len__, __getitem__, __setitem__ 등)
- [ ] 컨텍스트 매니저 (__enter__, __exit__)
- [ ] 속성 접근 메서드 (__getattr__, __setattr__, __delattr__)
- [ ] 실무에서 자주 사용되는 특수 메서드 패턴 익히기

## 📚 핵심 개념

### 1. 기본 특수 메서드
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
```

### 2. 산술 연산자 오버로딩
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
```

### 3. 비교 연산자 오버로딩
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade
```

### 4. 컨테이너 메서드
```python
class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
```

## 📁 예제 파일

- `basic_magic_methods.py` - 기본 특수 메서드들
- `arithmetic_operators.py` - 산술 연산자 오버로딩
- `comparison_operators.py` - 비교 연산자 오버로딩
- `container_methods.py` - 컨테이너 메서드들
- `context_managers.py` - 컨텍스트 매니저
- `attribute_access.py` - 속성 접근 메서드들
- `practical_examples.py` - 실무에서 자주 사용되는 특수 메서드 패턴

## 🏃‍♂️ 실습 과제

1. **벡터 클래스**: 수학적 벡터 연산을 지원하는 클래스
2. **분수 클래스**: 분수 연산을 지원하는 클래스
3. **스마트 리스트**: 추가 기능이 있는 리스트 클래스
4. **데이터베이스 연결 클래스**: 컨텍스트 매니저를 활용한 연결 클래스

## 💡 실무 팁

### ✅ 좋은 예시
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
```

### ❌ 피해야 할 예시
```python
# 불필요한 특수 메서드 오버로딩
class SimpleClass:
    def __add__(self, other):
        return "Hello"  # 의미없는 연산
    
    def __str__(self):
        return "Simple"  # 디버깅에 도움이 되지 않음
```

## 🔗 관련 주제

- [클래스와 객체](./classes-and-objects/) - 특수 메서드의 기초가 되는 클래스
- [상속과 다형성](./inheritance-polymorphism/) - 상속에서 특수 메서드 활용
- [연산자](../../01-basics/operators/) - 오버로딩할 연산자들

## 📖 추가 학습 자료

- [Python 공식 문서 - 특수 메서드](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [PEP 8 - 특수 메서드 가이드](https://pep8.org/#method-names-and-instance-variables)

---

**다음 단계**: [자료구조](../../05-data-structures/) 학습하기
