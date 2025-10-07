# 실무에서 자주 사용되는 연산자 패턴

def calculator():
    """간단한 계산기"""
    print("=== 계산기 ===")
    # TODO: 사용자 입력을 받아 사칙연산을 수행하는 계산기를 구현해보세요
    num1 = float(input("첫 번째 숫자: "))
    operator = input("연산자 (+, -, *, /): ").strip();
    num2 = float(input("두 번째 숫자 : "))
    
     # 연산 처리
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # 0으로 나누기 예외 처리
        if num2 == 0:
            print("❌ 0으로 나눌 수 없습니다.")
            return
        result = num1 / num2
    else:
        print("❌ 지원하지 않는 연산자입니다.")
        return

    print(f"결과: {result}")
    pass

def grade_calculator():
    """성적 계산기"""
    print("=== 성적 계산기 ===")
    # TODO: 점수를 입력받아 등급을 계산하는 프로그램을 구현해보세요
    pass

def age_classifier():
    """나이대 분류기"""
    print("=== 나이대 분류기 ===")
    # TODO: 나이를 입력받아 어린이/청소년/성인/노인으로 분류하는 프로그램을 구현해보세요
    pass

def password_validator():
    """비밀번호 검증기"""
    print("=== 비밀번호 검증기 ===")
    # TODO: 비밀번호의 길이와 특수문자 포함 여부를 확인하는 프로그램을 구현해보세요
    pass

if __name__ == "__main__":
    calculator()
    grade_calculator()
    age_classifier()
    password_validator()
