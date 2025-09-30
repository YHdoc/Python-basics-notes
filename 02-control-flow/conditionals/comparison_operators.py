# 비교 연산자 활용

def demonstrate_comparison_operators():
    """기본 비교 연산자 예제"""
    print("=== 기본 비교 연산자 ===")
    
    a = 10
    b = 20
    
    # 등호 비교
    print(f"{a} == {b}: {a == b}")  # False
    print(f"{a} != {b}: {a != b}")  # True
    
    # 크기 비교
    print(f"{a} < {b}: {a < b}")    # True
    print(f"{a} > {b}: {a > b}")    # False
    print(f"{a} <= {b}: {a <= b}")  # True
    print(f"{a} >= {b}: {a >= b}")  # False
    
    # 같은 값 비교
    c = 10
    print(f"{a} == {c}: {a == c}")  # True
    print(f"{a} is {c}: {a is c}")  # True (같은 객체)

def demonstrate_string_comparison():
    """문자열 비교 예제"""
    print("\n=== 문자열 비교 ===")
    
    str1 = "apple"
    str2 = "banana"
    str3 = "apple"
    
    # 문자열 등호 비교
    print(f"'{str1}' == '{str2}': {str1 == str2}")  # False
    print(f"'{str1}' == '{str3}': {str1 == str3}")  # True
    
    # 문자열 사전순 비교
    print(f"'{str1}' < '{str2}': {str1 < str2}")    # True
    print(f"'{str1}' > '{str2}': {str1 > str2}")    # False
    
    # 대소문자 구분
    str4 = "Apple"
    print(f"'{str1}' == '{str4}': {str1 == str4}")  # False
    print(f"'{str1.lower()}' == '{str4.lower()}': {str1.lower() == str4.lower()}")  # True

def demonstrate_numeric_comparison():
    """숫자 비교 예제"""
    print("\n=== 숫자 비교 ===")
    
    # 정수와 실수 비교
    int_num = 5
    float_num = 5.0
    
    print(f"{int_num} == {float_num}: {int_num == float_num}")  # True
    print(f"{int_num} is {float_num}: {int_num is float_num}")  # False
    
    # 복소수 비교
    complex1 = 3 + 4j
    complex2 = 3 + 4j
    print(f"{complex1} == {complex2}: {complex1 == complex2}")  # True
    
    # 특수 값 비교
    infinity = float('inf')
    not_a_number = float('nan')
    
    print(f"infinity == infinity: {infinity == infinity}")  # True
    print(f"NaN == NaN: {not_a_number == not_a_number}")    # False (NaN은 자기 자신과도 다름)

def demonstrate_list_comparison():
    """리스트 비교 예제"""
    print("\n=== 리스트 비교 ===")
    
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    list4 = [1, 2, 3, 4]
    
    # 리스트 등호 비교
    print(f"{list1} == {list2}: {list1 == list2}")  # True
    print(f"{list1} == {list3}: {list1 == list3}")  # False
    print(f"{list1} == {list4}: {list1 == list4}")  # False
    
    # 리스트 크기 비교
    print(f"{list1} < {list4}: {list1 < list4}")    # True
    print(f"{list1} > {list3}: {list1 > list3}")    # False

def demonstrate_boolean_comparison():
    """불린 값 비교 예제"""
    print("\n=== 불린 값 비교 ===")
    
    true_val = True
    false_val = False
    
    # 불린 값 비교
    print(f"True == True: {true_val == true_val}")      # True
    print(f"True == False: {true_val == false_val}")    # False
    print(f"True != False: {true_val != false_val}")    # True
    
    # 불린과 숫자 비교
    print(f"True == 1: {true_val == 1}")                # True
    print(f"False == 0: {false_val == 0}")              # True
    print(f"True == 2: {true_val == 2}")                # False

def demonstrate_chained_comparison():
    """연쇄 비교 예제"""
    print("\n=== 연쇄 비교 ===")
    
    x = 5
    y = 10
    z = 15
    
    # 연쇄 비교 (Python의 특별한 기능)
    print(f"{x} < {y} < {z}: {x < y < z}")              # True
    print(f"{x} < {z} < {y}: {x < z < y}")              # False
    
    # 여러 조건을 하나로
    age = 25
    print(f"18 <= {age} <= 65: {18 <= age <= 65}")      # True
    
    # 복잡한 연쇄 비교
    score = 85
    print(f"80 <= {score} < 90: {80 <= score < 90}")    # True

def demonstrate_identity_vs_equality():
    """동일성 vs 등가성 비교"""
    print("\n=== 동일성 vs 등가성 ===")
    
    # 같은 값, 다른 객체
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    
    print(f"list1 == list2: {list1 == list2}")  # True (등가성)
    print(f"list1 is list2: {list1 is list2}")  # False (동일성)
    
    # 같은 객체
    list3 = list1
    print(f"list1 is list3: {list1 is list3}")  # True (동일성)
    
    # 작은 정수는 캐시됨
    a = 256
    b = 256
    print(f"256 is 256: {a is b}")              # True (Python이 작은 정수를 캐시)
    
    # 큰 정수는 캐시되지 않음
    c = 257
    d = 257
    print(f"257 is 257: {c is d}")              # False (캐시되지 않음)

def demonstrate_practical_examples():
    """실용적인 비교 예제"""
    print("\n=== 실용적인 비교 예제 ===")
    
    # 나이 확인
    def check_age(age):
        if 0 <= age <= 120:
            return "유효한 나이"
        else:
            return "유효하지 않은 나이"
    
    print(f"25세: {check_age(25)}")
    print(f"150세: {check_age(150)}")
    
    # 점수 등급 확인
    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    scores = [95, 85, 75, 65, 55]
    for score in scores:
        print(f"{score}점: {get_grade(score)}등급")
    
    # 문자열 유효성 검사
    def is_valid_username(username):
        return (len(username) >= 3 and 
                len(username) <= 20 and 
                username.isalnum())
    
    usernames = ["user123", "ab", "user@name", "valid_user"]
    for username in usernames:
        print(f"'{username}': {'유효' if is_valid_username(username) else '무효'}")

if __name__ == "__main__":
    demonstrate_comparison_operators()
    demonstrate_string_comparison()
    demonstrate_numeric_comparison()
    demonstrate_list_comparison()
    demonstrate_boolean_comparison()
    demonstrate_chained_comparison()
    demonstrate_identity_vs_equality()
    demonstrate_practical_examples()
