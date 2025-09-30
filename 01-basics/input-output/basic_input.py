# 기본 입력 방법들

def basic_input():
    """기본 input() 함수 사용법"""
    print("=== 기본 입력 ===")
    
    # 문자열 입력
    name = input("이름을 입력하세요: ")
    print(f"안녕하세요, {name}님!")
    
    # 숫자 입력 (문자열로 받은 후 변환)
    age_str = input("나이를 입력하세요: ")
    age = int(age_str)
    print(f"나이: {age}세")

def type_conversion():
    """타입 변환과 함께 입력받기"""
    print("\n=== 타입 변환 ===")
    
    # 정수 입력
    age = int(input("나이를 입력하세요: "))
    print(f"입력받은 나이: {age} (타입: {type(age)})")
    
    # 실수 입력
    height = float(input("키를 입력하세요 (cm): "))
    print(f"입력받은 키: {height}cm (타입: {type(height)})")
    
    # 불린 입력 (간단한 방법)
    is_student = input("학생인가요? (y/n): ").lower() == 'y'
    print(f"학생 여부: {is_student} (타입: {type(is_student)})")

def multiple_inputs():
    """여러 값 입력받기"""
    print("\n=== 여러 값 입력 ===")
    
    # 공백으로 구분된 값들
    values = input("이름과 나이를 입력하세요 (예: 김철수 25): ").split()
    if len(values) == 2:
        name, age = values #언패킹 - ReadMe 참고
        age = int(age)
        print(f"이름: {name}, 나이: {age}세")
    
    # 콤마로 구분된 값들
    scores = input("세 과목 점수를 입력하세요 (예: 85,92,78): ").split(',')
    scores = [int(score.strip()) for score in scores]
    print(f"점수들: {scores}")
    print(f"평균: {sum(scores)/len(scores):.1f}")

def input_validation():
    """입력 검증"""
    print("\n=== 입력 검증 ===")
    
    # 나이 입력 검증
    while True:
        try:
            age = int(input("나이를 입력하세요 (1-120): "))
            if 1 <= age <= 120: 
                break
            else:
                print("나이는 1-120 사이의 숫자여야 합니다.")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")
    
    print(f"입력된 나이: {age}세")
    
    # 이메일 형식 검증 (간단한 버전)
    while True:
        email = input("이메일을 입력하세요: ")
        if "@" in email and "." in email.split("@")[1]:
            break
        else:
            print("올바른 이메일 형식을 입력해주세요.")
    
    print(f"입력된 이메일: {email}")

def practical_examples():
    """실무 예제"""
    print("\n=== 실무 예제 ===")
    
    # 사용자 등록
    print("=== 사용자 등록 ===")
    username = input("사용자명: ")
    password = input("비밀번호: ")
    confirm_password = input("비밀번호 확인: ")
    
    if password == confirm_password:
        print("회원가입이 완료되었습니다!")
    else:
        print("비밀번호가 일치하지 않습니다.")
    
    # 계산기
    print("\n=== 간단한 계산기 ===")
    try:
        num1 = float(input("첫 번째 숫자: "))
        operator = input("연산자 (+, -, *, /): ")
        num2 = float(input("두 번째 숫자: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("0으로 나눌 수 없습니다.")
                return
        else:
            print("지원하지 않는 연산자입니다.")
            return
        
        print(f"{num1} {operator} {num2} = {result}")
        
    except ValueError:
        print("올바른 숫자를 입력해주세요.")

if __name__ == "__main__":
    basic_input()
    type_conversion()
    multiple_inputs()
    input_validation()
    practical_examples()
