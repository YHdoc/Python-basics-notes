# 모듈 생성 예제

# 이 파일은 모듈로 사용될 수 있는 예제입니다.
# 다른 파일에서 import하여 사용할 수 있습니다.

# 모듈 레벨 변수
MODULE_VERSION = "1.0.0"
AUTHOR = "Python 학습자"

# 상수 정의
PI = 3.14159
E = 2.71828

# 유틸리티 함수들
def greet(name):
    """인사 함수"""
    return f"안녕하세요, {name}님!"

def calculate_circle_area(radius):
    """원의 넓이 계산"""
    return PI * radius ** 2

def calculate_circle_circumference(radius):
    """원의 둘레 계산"""
    return 2 * PI * radius

def is_prime(number):
    """소수 판별 함수"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_fibonacci(n):
    """피보나치 수열의 n번째 항 반환"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 클래스 정의
class Calculator:
    """간단한 계산기 클래스"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        return self.history

# 모듈이 직접 실행될 때만 실행되는 코드
if __name__ == "__main__":
    print(f"모듈 버전: {MODULE_VERSION}")
    print(f"작성자: {AUTHOR}")
    
    # 함수 테스트
    print(f"\n인사: {greet('김철수')}")
    print(f"원의 넓이 (반지름 5): {calculate_circle_area(5):.2f}")
    print(f"원의 둘레 (반지름 5): {calculate_circle_circumference(5):.2f}")
    print(f"17은 소수인가? {is_prime(17)}")
    print(f"피보나치 10번째 항: {get_fibonacci(10)}")
    
    # 클래스 테스트
    calc = Calculator()
    print(f"\n계산기 테스트:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"계산 기록: {calc.get_history()}")
