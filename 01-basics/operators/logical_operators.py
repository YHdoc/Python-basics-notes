# 논리 연산자 예제

def basic_logical():
    """기본 논리 연산자 사용법"""
    print("=== 기본 논리 연산자 ===")
    
    # and 연산자
    print("AND 연산자 (and):")
    print(f"True and True = {True and True}")
    print(f"True and False = {True and False}")
    print(f"False and True = {False and True}")
    print(f"False and False = {False and False}")
    
    # or 연산자
    print("\nOR 연산자 (or):")
    print(f"True or True = {True or True}")
    print(f"True or False = {True or False}")
    print(f"False or True = {False or True}")
    print(f"False or False = {False or False}")
    
    # not 연산자
    print("\nNOT 연산자 (not):")
    print(f"not True = {not True}")
    print(f"not False = {not False}")

def practical_logical():
    """실무에서 자주 사용되는 논리 연산"""
    print("\n=== 실무 예제 ===")
    
    # 사용자 권한 확인
    user_age = 25
    has_license = True
    is_premium = False
    
    can_drive = user_age >= 18 and has_license
    can_access_premium = is_premium or user_age >= 65
    cannot_use_service = not (user_age >= 18)
    
    print(f"사용자 나이: {user_age}")
    print(f"면허 보유: {has_license}")
    print(f"프리미엄 회원: {is_premium}")
    print(f"운전 가능: {can_drive}")
    print(f"프리미엄 접근 가능: {can_access_premium}")
    print(f"서비스 이용 불가: {cannot_use_service}")
    
    # 로그인 조건
    username = "admin"
    password = "password123"
    is_active = True
    
    valid_username = username == "admin"
    valid_password = len(password) >= 8
    can_login = valid_username and valid_password and is_active
    
    print(f"\n로그인 조건:")
    print(f"유효한 사용자명: {valid_username}")
    print(f"유효한 비밀번호: {valid_password}")
    print(f"계정 활성화: {is_active}")
    print(f"로그인 가능: {can_login}")

def short_circuit_evaluation():
    """단축 평가 (Short-circuit evaluation) 예제"""
    print("\n=== 단축 평가 ===")
    
    def expensive_operation():
        print("비용이 큰 연산 실행됨!")
        return True
    
    # and 연산에서 첫 번째가 False면 두 번째는 실행되지 않음
    print("False and expensive_operation():")
    result1 = False and expensive_operation()
    print(f"결과: {result1}")
    
    # or 연산에서 첫 번째가 True면 두 번째는 실행되지 않음
    print("\nTrue or expensive_operation():")
    result2 = True or expensive_operation()
    print(f"결과: {result2}")
    
    # 실제로 실행되는 경우
    print("\nTrue and expensive_operation():")
    result3 = True and expensive_operation()
    print(f"결과: {result3}")

def complex_conditions():
    """복합 조건 예제"""
    print("\n=== 복합 조건 ===")
    
    # 날씨와 활동 조건
    is_sunny = True
    temperature = 25
    has_umbrella = False
    is_weekend = True
    
    # 복합 조건들
    can_go_picnic = is_sunny and temperature > 20 and is_weekend
    should_stay_home = not is_sunny or temperature < 10
    can_go_with_umbrella = (not is_sunny and has_umbrella) or is_sunny
    
    print(f"날씨가 맑음: {is_sunny}")
    print(f"온도: {temperature}°C")
    print(f"우산 보유: {has_umbrella}")
    print(f"주말: {is_weekend}")
    print(f"피크닉 가능: {can_go_picnic}")
    print(f"집에 있어야 함: {should_stay_home}")
    print(f"우산과 함께 외출 가능: {can_go_with_umbrella}")

def operator_precedence():
    """논리 연산자 우선순위 예제"""
    print("\n=== 연산자 우선순위 ===")
    
    a = True
    b = False
    c = True
    
    # 괄호 없이
    result1 = a and b or c
    print(f"a and b or c = {result1}")
    
    # 괄호로 명확히
    result2 = (a and b) or c
    result3 = a and (b or c)
    
    print(f"(a and b) or c = {result2}")
    print(f"a and (b or c) = {result3}")
    
    # not 연산자 우선순위
    result4 = not a and b
    result5 = not (a and b)
    
    print(f"not a and b = {result4}")
    print(f"not (a and b) = {result5}")

if __name__ == "__main__":
    basic_logical()
    practical_logical()
    short_circuit_evaluation()
    complex_conditions()
    operator_precedence()
