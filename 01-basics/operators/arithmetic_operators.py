# 산술 연산자 예제

def basic_arithmetic():
    """기본 산술 연산자 사용법"""
    a = 10
    b = 3
    
    print("=== 기본 산술 연산자 ===")
    print(f"a = {a}, b = {b}")
    print(f"덧셈: a + b = {a + b}")
    print(f"뺄셈: a - b = {a - b}")
    print(f"곱셈: a * b = {a * b}")
    print(f"나눗셈: a / b = {a / b}")
    print(f"나머지: a % b = {a % b}")
    print(f"거듭제곱: a ** b = {a ** b}")
    print(f"몫: a // b = {a // b}")

def floating_point_operations():
    """실수 연산 예제"""
    print("\n=== 실수 연산 ===")
    x = 7.5
    y = 2.3
    
    print(f"x = {x}, y = {y}")
    print(f"덧셈: {x + y}")
    print(f"뺄셈: {x - y}")
    print(f"곱셈: {x * y}")
    print(f"나눗셈: {x / y}")
    print(f"나머지: {x % y}")
    print(f"몫: {x // y}")

def order_of_operations():
    """연산 순서 예제"""
    print("\n=== 연산 순서 ===")
    result1 = 2 + 3 * 4
    result2 = (2 + 3) * 4
    result3 = 2 ** 3 * 4
    result4 = 2 ** (3 * 4)
    
    print(f"2 + 3 * 4 = {result1}")
    print(f"(2 + 3) * 4 = {result2}")
    print(f"2 ** 3 * 4 = {result3}")
    print(f"2 ** (3 * 4) = {result4}")

def practical_examples():
    """실무에서 자주 사용되는 산술 연산"""
    print("\n=== 실무 예제 ===")
    
    # 할인 계산
    original_price = 10000
    discount_rate = 0.15
    discounted_price = original_price * (1 - discount_rate)
    print(f"원가: {original_price}원, 할인가: {discounted_price}원")
    
    # 평균 계산
    scores = [85, 92, 78, 96, 88]
    average = sum(scores) / len(scores)
    print(f"점수들: {scores}, 평균: {average}")
    
    # 시간 계산
    total_seconds = 3661
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print(f"{total_seconds}초 = {hours}시간 {minutes}분 {seconds}초")

if __name__ == "__main__":
    basic_arithmetic()
    floating_point_operations()
    order_of_operations()
    practical_examples()
