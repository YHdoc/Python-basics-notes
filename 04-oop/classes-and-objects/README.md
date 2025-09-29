# 클래스와 객체 🏗️

> 객체지향 프로그래밍의 핵심인 클래스와 객체를 학습하고, 실무에서 활용할 수 있는 클래스 설계 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 클래스와 객체의 개념 이해
- [ ] 클래스 정의와 객체 생성 방법 학습
- [ ] 속성(Attribute)과 메서드(Method) 구현
- [ ] 생성자(__init__)와 소멸자(__del__) 이해
- [ ] 클래스 변수와 인스턴스 변수 구분
- [ ] 캡슐화와 정보 은닉 개념 학습

## 📚 핵심 개념

### 1. 클래스 정의
```python
class ClassName:
    """클래스에 대한 설명"""
    
    # 클래스 변수
    class_variable = "공통 값"
    
    def __init__(self, parameter1, parameter2):
        """생성자 - 객체 초기화"""
        self.instance_variable1 = parameter1
        self.instance_variable2 = parameter2
    
    def instance_method(self):
        """인스턴스 메서드"""
        return f"인스턴스 변수: {self.instance_variable1}"
    
    @classmethod
    def class_method(cls):
        """클래스 메서드"""
        return f"클래스 변수: {cls.class_variable}"
    
    @staticmethod
    def static_method():
        """정적 메서드"""
        return "정적 메서드 호출"
```

### 2. 객체 생성과 사용
```python
# 객체 생성
obj = ClassName("값1", "값2")

# 속성 접근
print(obj.instance_variable1)

# 메서드 호출
result = obj.instance_method()
```

### 3. 캡슐화 (Encapsulation)
```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # private 변수
    
    def get_balance(self):
        """잔액 조회"""
        return self.__balance
    
    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        """출금"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
```

## 📁 예제 파일

- `basic_class.py` - 기본 클래스 정의와 객체 생성
- `constructor_destructor.py` - 생성자와 소멸자 예제
- `class_instance_variables.py` - 클래스 변수와 인스턴스 변수
- `encapsulation.py` - 캡슐화와 정보 은닉
- `class_methods.py` - 다양한 메서드 타입
- `practical_examples.py` - 실무에서 사용되는 클래스 예제

## 🏃‍♂️ 실습 과제

1. **학생 클래스**: 이름, 나이, 학번을 가진 학생 클래스를 만들어보세요
2. **계산기 클래스**: 사칙연산을 수행하는 계산기 클래스를 구현해보세요
3. **도서 관리 시스템**: 도서 정보를 관리하는 클래스를 설계해보세요
4. **은행 계좌 시스템**: 입출금 기능이 있는 계좌 클래스를 만들어보세요

## 💡 실무 팁

### ✅ 좋은 예시
```python
class User:
    """사용자 정보를 관리하는 클래스"""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.now()
    
    def get_display_name(self):
        """표시용 이름 반환"""
        return f"{self.name} ({self.email})"
    
    def is_valid_email(self):
        """이메일 유효성 검사"""
        return "@" in self.email and "." in self.email.split("@")[1]
```

### ❌ 피해야 할 예시
```python
# 클래스명이 소문자로 시작
class user:  # User로 해야 함

# 의미없는 메서드명
def do_something(self):  # 구체적인 이름 사용

# 모든 변수를 public으로 선언
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # private으로 해야 함
```

## 🔗 관련 주제

- [상속과 다형성](./inheritance-polymorphism/) - 클래스 간의 관계
- [특수 메서드](./magic-methods/) - __init__, __str__ 등의 특수 메서드
- [함수 정의와 호출](../../03-functions-modules/functions/) - 메서드 작성의 기초

## 📖 추가 학습 자료

- [Python 공식 문서 - 클래스](https://docs.python.org/3/tutorial/classes.html)
- [PEP 8 - 클래스 명명 규칙](https://pep8.org/#class-names)

---

**다음 단계**: [상속과 다형성](./inheritance-polymorphism/) 학습하기
