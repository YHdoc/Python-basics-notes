# 연산자 우선순위 예제

def basic_precedence():
    """기본 연산자 우선순위"""
    print("=== 연산자 우선순위 ===")
    
    # 산술 연산자 우선순위
    # ** (거듭제곱) 은 오른쪽 결합이라 2 ** 3 ** 2 는 2 ** (3 ** 2) 로 계산됨
    # 단항 -x 가 ** 보다 우선할 것 같지만, 실제로는 ** 가 더 먼저임 → -3 ** 2 = -(3 ** 2) = -9
    # *, /, //, % 는 같은 우선순위, 왼쪽에서 오른쪽 순서대로
    # +, - (이항 연산) 은 가장 낮은 산술 연산자 우선순위 
    result1 = 2 + 3 * 4
    result2 = (2 + 3) * 4
    print(f"2 + 3 * 4 = {result1}")
    print(f"(2 + 3) * 4 = {result2}")
    
    # 거듭제곱 우선순위
    # 거듭제곱 ** 은 오른쪽 결합 (ex: 2 ** 3 ** 2 → 2 ** (3 ** 2))
    result3 = 2 ** 3 * 4
    result4 = 2 ** (3 * 4)
    print(f"2 ** 3 * 4 = {result3}")
    print(f"2 ** (3 * 4) = {result4}")

def practical_examples():
    """실무 예제"""
    print("\n=== 실무 예제 ===")
    
    # 할인 계산
    price = 1000
    discount = 0.1
    tax = 0.08
    
    # 올바른 계산
    final_price = price * (1 - discount) * (1 + tax)
    print(f"최종 가격: {final_price}")
    
    # 잘못된 계산 (우선순위 무시)
    wrong_price = price * 1 - discount * 1 + tax
    print(f"잘못된 계산: {wrong_price}")

if __name__ == "__main__":
    basic_precedence()
    practical_examples()
