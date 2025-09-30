# 비교 연산자 예제

def basic_comparison():
    """기본 비교 연산자 사용법"""
    a = 10
    b = 20
    c = 10
    
    print("=== 기본 비교 연산자 ===")
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"a == b: {a == b}")  # 같다
    print(f"a != b: {a != b}")  # 다르다
    print(f"a < b: {a < b}")    # 작다
    print(f"a > b: {a > b}")    # 크다
    print(f"a <= b: {a <= b}")  # 작거나 같다
    print(f"a >= b: {a >= b}")  # 크거나 같다
    print(f"a == c: {a == c}")  # 같다

def string_comparison():
    """문자열 비교 예제"""
    print("\n=== 문자열 비교 ===")
    str1 = "apple"
    str2 = "banana"
    str3 = "apple"
    
    print(f"'{str1}' == '{str2}': {str1 == str2}")
    print(f"'{str1}' != '{str2}': {str1 != str2}")
    print(f"'{str1}' < '{str2}': {str1 < str2}")  # 사전순
    print(f"'{str1}' > '{str2}': {str1 > str2}")
    print(f"'{str1}' == '{str3}': {str1 == str3}")

def boolean_comparison():
    """불린 값 비교 예제"""
    print("\n=== 불린 값 비교 ===")
    true_val = True
    false_val = False
    
    print(f"True == True: {true_val == true_val}")
    print(f"True == False: {true_val == false_val}")
    print(f"True != False: {true_val != false_val}")

def practical_examples():
    """실무에서 자주 사용되는 비교 연산"""
    print("\n=== 실무 예제 ===")
    
    # 나이 확인
    user_age = 25
    min_age = 18
    max_age = 65
    
    can_use_service = min_age <= user_age <= max_age
    print(f"사용자 나이: {user_age}, 서비스 이용 가능: {can_use_service}")
    
    # 점수 등급 확인
    score = 85
    is_excellent = score >= 90
    is_good = 80 <= score < 90
    is_pass = score >= 60
    
    print(f"점수: {score}")
    print(f"우수: {is_excellent}")
    print(f"양호: {is_good}")
    print(f"합격: {is_pass}")
    
    # 문자열 길이 확인
    password = "mypassword123"
    min_length = 8
    max_length = 20
    
    is_valid_length = min_length <= len(password) <= max_length
    print(f"비밀번호 길이 유효: {is_valid_length}")

def chained_comparison():
    """연쇄 비교 예제"""
    print("\n=== 연쇄 비교 ===")
    x = 15
    
    # 일반적인 방법
    result1 = x >= 10 and x <= 20
    
    # 연쇄 비교 (더 간결)
    result2 = 10 <= x <= 20
    
    print(f"x = {x}")
    print(f"10 <= x <= 20: {result2}")
    print(f"x >= 10 and x <= 20: {result1}")

if __name__ == "__main__":
    basic_comparison()
    string_comparison()
    boolean_comparison()
    practical_examples()
    chained_comparison()
