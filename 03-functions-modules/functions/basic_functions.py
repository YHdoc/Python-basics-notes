# 기본 함수 정의와 호출

def hello_world():
    """간단한 인사 함수"""
    print("Hello, World!")

def greet(name):
    """이름을 받아 인사하는 함수"""
    print(f"안녕하세요, {name}님!")

def add_numbers(a, b):
    """두 숫자를 더하는 함수"""
    return a + b

def calculate_area(length, width):
    """사각형의 넓이를 계산하는 함수"""
    area = length * width
    return area

def is_even(number):
    """짝수인지 확인하는 함수"""
    return number % 2 == 0

def get_max(a, b):
    """두 수 중 큰 값을 반환하는 함수"""
    if a > b:
        return a
    else:
        return b

if __name__ == "__main__":
    # 함수 호출 예제
    hello_world()
    greet("김철수")
    
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    area = calculate_area(10, 5)
    print(f"사각형 넓이: {area}")
    
    print(f"8은 짝수인가? {is_even(8)}")
    print(f"7은 짝수인가? {is_even(7)}")
    
    max_value = get_max(10, 20)
    print(f"10과 20 중 큰 값: {max_value}")
