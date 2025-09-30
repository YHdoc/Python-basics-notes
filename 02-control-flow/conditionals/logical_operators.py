# 논리 연산자 활용

def demonstrate_basic_logical_operators():
    """기본 논리 연산자 예제"""
    print("=== 기본 논리 연산자 ===")
    
    # and 연산자
    print("AND 연산자:")
    print(f"True and True: {True and True}")      # True
    print(f"True and False: {True and False}")    # False
    print(f"False and True: {False and True}")    # False
    print(f"False and False: {False and False}")  # False
    
    # or 연산자
    print("\nOR 연산자:")
    print(f"True or True: {True or True}")        # True
    print(f"True or False: {True or False}")      # True
    print(f"False or True: {False or True}")      # True
    print(f"False or False: {False or False}")    # False
    
    # not 연산자
    print("\nNOT 연산자:")
    print(f"not True: {not True}")                # False
    print(f"not False: {not False}")              # True

def demonstrate_short_circuit_evaluation():
    """단축 평가 예제"""
    print("\n=== 단축 평가 (Short Circuit) ===")
    
    def expensive_function():
        print("  비싼 함수가 실행되었습니다!")
        return True
    
    # and 연산자 - 첫 번째가 False면 두 번째는 실행되지 않음
    print("False and expensive_function():")
    result1 = False and expensive_function()
    print(f"결과: {result1}")
    
    # or 연산자 - 첫 번째가 True면 두 번째는 실행되지 않음
    print("\nTrue or expensive_function():")
    result2 = True or expensive_function()
    print(f"결과: {result2}")
    
    # 실제로 실행되는 경우
    print("\nTrue and expensive_function():")
    result3 = True and expensive_function()
    print(f"결과: {result3}")

def demonstrate_truthiness():
    """진실성(Truthiness) 예제"""
    print("\n=== 진실성 (Truthiness) ===")
    
    # False로 평가되는 값들
    falsy_values = [False, 0, 0.0, "", [], {}, None]
    
    print("False로 평가되는 값들:")
    for value in falsy_values:
        print(f"  {repr(value)}: {bool(value)}")
    
    # True로 평가되는 값들
    truthy_values = [True, 1, 3.14, "hello", [1, 2, 3], {"key": "value"}]
    
    print("\nTrue로 평가되는 값들:")
    for value in truthy_values:
        print(f"  {repr(value)}: {bool(value)}")

def demonstrate_complex_conditions():
    """복잡한 조건 예제"""
    print("\n=== 복잡한 조건 ===")
    
    age = 25
    has_license = True
    has_insurance = False
    
    # 복잡한 조건문
    can_drive = age >= 18 and has_license and has_insurance
    print(f"운전 가능: {can_drive}")
    
    # or 조건
    can_rent_car = age >= 21 or (age >= 18 and has_license)
    print(f"차량 렌트 가능: {can_rent_car}")
    
    # not 조건
    is_minor = not (age >= 18)
    print(f"미성년자: {is_minor}")

def demonstrate_practical_examples():
    """실용적인 논리 연산자 예제"""
    print("\n=== 실용적인 예제 ===")
    
    # 사용자 입력 검증
    def validate_user_input(username, password, email):
        return (len(username) >= 3 and 
                len(password) >= 8 and 
                "@" in email and 
                "." in email)
    
    # 로그인 상태 확인
    def can_access_admin(user_role, is_logged_in, has_permission):
        return (is_logged_in and 
                (user_role == "admin" or user_role == "superuser") and 
                has_permission)
    
    # 파일 처리 조건
    def should_process_file(filename, file_size, file_type):
        return (filename.endswith(('.txt', '.csv')) and 
                file_size > 0 and 
                file_size < 10 * 1024 * 1024 and  # 10MB 미만
                file_type in ['text', 'data'])
    
    # 테스트
    print(f"사용자 입력 유효: {validate_user_input('user123', 'password123', 'user@example.com')}")
    print(f"관리자 접근 가능: {can_access_admin('admin', True, True)}")
    print(f"파일 처리 가능: {should_process_file('data.txt', 1024, 'text')}")

def demonstrate_operator_precedence():
    """연산자 우선순위 예제"""
    print("\n=== 연산자 우선순위 ===")
    
    # 괄호 없이
    result1 = True or False and False
    print(f"True or False and False: {result1}")  # True (and가 먼저)
    
    # 괄호로 명확하게
    result2 = (True or False) and False
    print(f"(True or False) and False: {result2}")  # False
    
    result3 = True or (False and False)
    print(f"True or (False and False): {result3}")  # True
    
    # 복잡한 예제
    a, b, c = True, False, True
    result4 = a and b or c
    print(f"a and b or c: {result4}")  # True
    
    result5 = a and (b or c)
    print(f"a and (b or c): {result5}")  # True

def demonstrate_ternary_operator():
    """삼항 연산자 스타일 예제"""
    print("\n=== 삼항 연산자 스타일 ===")
    
    age = 20
    
    # and/or를 이용한 삼항 연산자 스타일
    status = age >= 18 and "성인" or "미성년자"
    print(f"나이 {age}: {status}")
    
    # 더 안전한 방법
    status2 = "성인" if age >= 18 else "미성년자"
    print(f"나이 {age}: {status2}")
    
    # 복잡한 조건
    score = 85
    grade = (score >= 90 and "A" or 
             score >= 80 and "B" or 
             score >= 70 and "C" or 
             score >= 60 and "D" or "F")
    print(f"점수 {score}: {grade}등급")

def demonstrate_guard_clauses():
    """가드 절(Guard Clauses) 예제"""
    print("\n=== 가드 절 (Guard Clauses) ===")
    
    def process_user_data(user_data):
        # 가드 절들
        if not user_data:
            return "데이터가 없습니다"
        
        if not isinstance(user_data, dict):
            return "잘못된 데이터 형식입니다"
        
        if "name" not in user_data or "age" not in user_data:
            return "필수 필드가 누락되었습니다"
        
        if user_data["age"] < 0 or user_data["age"] > 150:
            return "유효하지 않은 나이입니다"
        
        # 정상 처리
        return f"사용자 {user_data['name']} ({user_data['age']}세) 처리 완료"
    
    # 테스트
    test_cases = [
        None,
        "invalid",
        {"name": "김철수"},
        {"name": "이영희", "age": -5},
        {"name": "박민수", "age": 25}
    ]
    
    for data in test_cases:
        result = process_user_data(data)
        print(f"입력: {data} -> 결과: {result}")

if __name__ == "__main__":
    demonstrate_basic_logical_operators()
    demonstrate_short_circuit_evaluation()
    demonstrate_truthiness()
    demonstrate_complex_conditions()
    demonstrate_practical_examples()
    demonstrate_operator_precedence()
    demonstrate_ternary_operator()
    demonstrate_guard_clauses()
