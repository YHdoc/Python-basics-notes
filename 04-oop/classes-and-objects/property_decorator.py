# @property 데코레이터

class Circle:
    """원 클래스 - @property 데코레이터 예제"""
    
    def __init__(self, radius):
        """생성자"""
        self._radius = radius
    
    @property
    def radius(self):
        """반지름 조회"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """반지름 설정"""
        if value < 0:
            raise ValueError("반지름은 0 이상이어야 합니다.")
        self._radius = value
    
    @property
    def diameter(self):
        """지름 (읽기 전용)"""
        return self._radius * 2
    
    @diameter.setter
    def diameter(self, value):
        """지름 설정"""
        if value < 0:
            raise ValueError("지름은 0 이상이어야 합니다.")
        self._radius = value / 2
    
    @property
    def area(self):
        """면적 (읽기 전용)"""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """둘레 (읽기 전용)"""
        import math
        return 2 * math.pi * self._radius

def demonstrate_basic_property():
    """기본 @property 데코레이터 예제"""
    print("=== 기본 @property 데코레이터 ===")
    
    # 원 생성
    circle = Circle(5)
    
    # 속성 접근
    print(f"반지름: {circle.radius}")
    print(f"지름: {circle.diameter}")
    print(f"면적: {circle.area:.2f}")
    print(f"둘레: {circle.circumference:.2f}")
    
    # 속성 변경
    circle.radius = 10
    print(f"\n반지름 변경 후:")
    print(f"반지름: {circle.radius}")
    print(f"지름: {circle.diameter}")
    print(f"면적: {circle.area:.2f}")
    
    # 지름으로 반지름 변경
    circle.diameter = 20
    print(f"\n지름 변경 후:")
    print(f"반지름: {circle.radius}")
    print(f"지름: {circle.diameter}")
    
    # 유효하지 않은 값 설정
    try:
        circle.radius = -5
    except ValueError as e:
        print(f"오류: {e}")

class Temperature:
    """온도 클래스 - 다양한 단위 변환 예제"""
    
    def __init__(self, celsius=0):
        """생성자"""
        self._celsius = celsius
    
    @property
    def celsius(self):
        """섭씨 온도"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """섭씨 온도 설정"""
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """화씨 온도"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """화씨 온도 설정"""
        self._celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """켈빈 온도"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """켈빈 온도 설정"""
        if value < 0:
            raise ValueError("켈빈 온도는 0보다 작을 수 없습니다.")
        self._celsius = value - 273.15
    
    def __str__(self):
        """문자열 표현"""
        return f"{self._celsius:.1f}°C ({self.fahrenheit:.1f}°F, {self.kelvin:.1f}K)"

def demonstrate_temperature_example():
    """온도 클래스 예제"""
    print("\n=== 온도 클래스 예제 ===")
    
    # 온도 객체 생성
    temp = Temperature(25)
    print(f"초기 온도: {temp}")
    
    # 섭씨 온도 변경
    temp.celsius = 30
    print(f"섭씨 30도: {temp}")
    
    # 화씨 온도 변경
    temp.fahrenheit = 86
    print(f"화씨 86도: {temp}")
    
    # 켈빈 온도 변경
    temp.kelvin = 300
    print(f"켈빈 300도: {temp}")
    
    # 유효하지 않은 켈빈 온도
    try:
        temp.kelvin = -10
    except ValueError as e:
        print(f"오류: {e}")

class BankAccount:
    """은행 계좌 클래스 - 보안과 검증 예제"""
    
    def __init__(self, account_holder, initial_balance=0):
        """생성자"""
        self._account_holder = account_holder
        self._balance = initial_balance
        self._transactions = []
    
    @property
    def account_holder(self):
        """계좌 소유자 (읽기 전용)"""
        return self._account_holder
    
    @property
    def balance(self):
        """잔액 (읽기 전용)"""
        return self._balance
    
    @property
    def transactions(self):
        """거래 내역 (읽기 전용)"""
        return self._transactions.copy()
    
    def deposit(self, amount):
        """입금"""
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 합니다.")
        self._balance += amount
        self._transactions.append(f"입금: +{amount}")
        return self._balance
    
    def withdraw(self, amount):
        """출금"""
        if amount <= 0:
            raise ValueError("출금액은 0보다 커야 합니다.")
        if amount > self._balance:
            raise ValueError("잔액이 부족합니다.")
        self._balance -= amount
        self._transactions.append(f"출금: -{amount}")
        return self._balance
    
    def __str__(self):
        """문자열 표현"""
        return f"계좌: {self._account_holder}, 잔액: {self._balance}원"

def demonstrate_bank_account_example():
    """은행 계좌 예제"""
    print("\n=== 은행 계좌 예제 ===")
    
    # 계좌 생성
    account = BankAccount("김철수", 10000)
    print(f"계좌 생성: {account}")
    
    # 입금
    account.deposit(5000)
    print(f"입금 후: {account}")
    
    # 출금
    account.withdraw(2000)
    print(f"출금 후: {account}")
    
    # 거래 내역 조회
    print(f"거래 내역: {account.transactions}")
    
    # 잔액 조회
    print(f"현재 잔액: {account.balance}원")
    
    # 유효하지 않은 거래
    try:
        account.withdraw(20000)
    except ValueError as e:
        print(f"출금 오류: {e}")

class Rectangle:
    """사각형 클래스 - 계산된 속성 예제"""
    
    def __init__(self, width, height):
        """생성자"""
        self._width = width
        self._height = height
    
    @property
    def width(self):
        """너비"""
        return self._width
    
    @width.setter
    def width(self, value):
        """너비 설정"""
        if value <= 0:
            raise ValueError("너비는 0보다 커야 합니다.")
        self._width = value
    
    @property
    def height(self):
        """높이"""
        return self._height
    
    @height.setter
    def height(self, value):
        """높이 설정"""
        if value <= 0:
            raise ValueError("높이는 0보다 커야 합니다.")
        self._height = value
    
    @property
    def area(self):
        """면적 (읽기 전용)"""
        return self._width * self._height
    
    @property
    def perimeter(self):
        """둘레 (읽기 전용)"""
        return 2 * (self._width + self._height)
    
    @property
    def aspect_ratio(self):
        """가로세로 비율 (읽기 전용)"""
        return self._width / self._height
    
    @property
    def is_square(self):
        """정사각형 여부 (읽기 전용)"""
        return self._width == self._height
    
    def __str__(self):
        """문자열 표현"""
        shape = "정사각형" if self.is_square else "사각형"
        return f"{shape}({self._width} x {self._height})"

def demonstrate_rectangle_example():
    """사각형 예제"""
    print("\n=== 사각형 예제 ===")
    
    # 사각형 생성
    rect = Rectangle(5, 3)
    print(f"사각형: {rect}")
    print(f"면적: {rect.area}")
    print(f"둘레: {rect.perimeter}")
    print(f"가로세로 비율: {rect.aspect_ratio:.2f}")
    print(f"정사각형 여부: {rect.is_square}")
    
    # 크기 변경
    rect.width = 6
    rect.height = 6
    print(f"\n크기 변경 후:")
    print(f"사각형: {rect}")
    print(f"면적: {rect.area}")
    print(f"둘레: {rect.perimeter}")
    print(f"가로세로 비율: {rect.aspect_ratio:.2f}")
    print(f"정사각형 여부: {rect.is_square}")

class Person:
    """사람 클래스 - 복합 속성 예제"""
    
    def __init__(self, first_name, last_name, age):
        """생성자"""
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
    
    @property
    def first_name(self):
        """이름"""
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        """이름 설정"""
        if not value or not value.strip():
            raise ValueError("이름은 비어있을 수 없습니다.")
        self._first_name = value.strip()
    
    @property
    def last_name(self):
        """성"""
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        """성 설정"""
        if not value or not value.strip():
            raise ValueError("성은 비어있을 수 없습니다.")
        self._last_name = value.strip()
    
    @property
    def full_name(self):
        """전체 이름 (읽기 전용)"""
        return f"{self._first_name} {self._last_name}"
    
    @full_name.setter
    def full_name(self, value):
        """전체 이름 설정"""
        if not value or not value.strip():
            raise ValueError("전체 이름은 비어있을 수 없습니다.")
        parts = value.strip().split()
        if len(parts) < 2:
            raise ValueError("전체 이름은 이름과 성을 포함해야 합니다.")
        self._first_name = parts[0]
        self._last_name = " ".join(parts[1:])
    
    @property
    def age(self):
        """나이"""
        return self._age
    
    @age.setter
    def age(self, value):
        """나이 설정"""
        if not isinstance(value, int):
            raise ValueError("나이는 정수여야 합니다.")
        if value < 0 or value > 150:
            raise ValueError("나이는 0-150 사이여야 합니다.")
        self._age = value
    
    @property
    def age_group(self):
        """연령대 (읽기 전용)"""
        if self._age < 13:
            return "어린이"
        elif self._age < 20:
            return "청소년"
        elif self._age < 65:
            return "성인"
        else:
            return "노인"
    
    def __str__(self):
        """문자열 표현"""
        return f"{self.full_name} ({self._age}세, {self.age_group})"

def demonstrate_person_example():
    """사람 클래스 예제"""
    print("\n=== 사람 클래스 예제 ===")
    
    # 사람 생성
    person = Person("김", "철수", 25)
    print(f"사람: {person}")
    
    # 이름 변경
    person.first_name = "이"
    person.last_name = "영희"
    print(f"이름 변경 후: {person}")
    
    # 전체 이름 변경
    person.full_name = "박 민수"
    print(f"전체 이름 변경 후: {person}")
    
    # 나이 변경
    person.age = 30
    print(f"나이 변경 후: {person}")
    
    # 유효하지 않은 값 설정
    try:
        person.age = -5
    except ValueError as e:
        print(f"나이 설정 오류: {e}")
    
    try:
        person.full_name = "홍"
    except ValueError as e:
        print(f"이름 설정 오류: {e}")

class LazyProperty:
    """지연 속성 예제"""
    
    def __init__(self, func):
        """생성자"""
        self.func = func
        self.name = func.__name__
    
    def __get__(self, obj, objtype=None):
        """속성 접근 시 호출"""
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.name, value)
        return value

class ExpensiveCalculation:
    """비싼 계산 예제"""
    
    def __init__(self, n):
        """생성자"""
        self.n = n
        self._cache = {}
    
    @LazyProperty
    def fibonacci(self):
        """피보나치 수열 계산 (지연 속성)"""
        print(f"피보나치 수열 계산 중... (n={self.n})")
        if self.n <= 1:
            return self.n
        a, b = 0, 1
        for _ in range(2, self.n + 1):
            a, b = b, a + b
        return b
    
    @LazyProperty
    def factorial(self):
        """팩토리얼 계산 (지연 속성)"""
        print(f"팩토리얼 계산 중... (n={self.n})")
        if self.n <= 1:
            return 1
        result = 1
        for i in range(2, self.n + 1):
            result *= i
        return result

def demonstrate_lazy_property_example():
    """지연 속성 예제"""
    print("\n=== 지연 속성 예제 ===")
    
    # 계산 객체 생성
    calc = ExpensiveCalculation(10)
    
    # 첫 번째 접근 시 계산 수행
    print(f"피보나치 수열: {calc.fibonacci}")
    
    # 두 번째 접근 시 계산하지 않음 (캐시된 값 사용)
    print(f"피보나치 수열 (재접근): {calc.fibonacci}")
    
    # 팩토리얼 계산
    print(f"팩토리얼: {calc.factorial}")
    print(f"팩토리얼 (재접근): {calc.factorial}")

if __name__ == "__main__":
    demonstrate_basic_property()
    demonstrate_temperature_example()
    demonstrate_bank_account_example()
    demonstrate_rectangle_example()
    demonstrate_person_example()
    demonstrate_lazy_property_example()
