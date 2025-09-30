# 변수 명명 규칙과 관례

def demonstrate_naming_rules():
    """변수 명명 규칙 예제"""
    print("=== 변수 명명 규칙 ===")
    
    # 올바른 변수명
    user_name = "김철수"          # snake_case
    user_age = 30                # 숫자 포함 가능
    is_active = True             # 불린 변수는 is_로 시작
    has_permission = False       # has_로 시작
    max_retry_count = 3          # 의미있는 이름
    
    print(f"사용자 이름: {user_name}")
    print(f"사용자 나이: {user_age}")
    print(f"활성 상태: {is_active}")
    print(f"권한 있음: {has_permission}")
    print(f"최대 재시도 횟수: {max_retry_count}")
    
    # 상수 (대문자)
    MAX_CONNECTIONS = 100
    DEFAULT_TIMEOUT = 30
    API_BASE_URL = "https://api.example.com"
    
    print(f"최대 연결 수: {MAX_CONNECTIONS}")
    print(f"기본 타임아웃: {DEFAULT_TIMEOUT}")
    print(f"API 기본 URL: {API_BASE_URL}")

def demonstrate_good_naming():
    """좋은 변수명 예제"""
    print("\n=== 좋은 변수명 예제 ===")
    
    # 명확하고 의미있는 이름
    student_count = 25
    average_score = 85.5
    is_graduated = True
    graduation_year = 2023
    
    # 계산 결과를 명확하게 표현
    total_price = 1000
    discount_rate = 0.1
    final_price = total_price * (1 - discount_rate)
    
    print(f"학생 수: {student_count}")
    print(f"평균 점수: {average_score}")
    print(f"졸업 여부: {is_graduated}")
    print(f"졸업 연도: {graduation_year}")
    print(f"최종 가격: {final_price}")

def demonstrate_bad_naming():
    """나쁜 변수명 예제 (주석으로 설명)"""
    print("\n=== 나쁜 변수명 예제 ===")
    
    # 의미없는 이름들
    a = 10          # 무엇을 의미하는지 모름
    b = 20          # 무엇을 의미하는지 모름
    x = "hello"     # 무엇을 의미하는지 모름
    
    # 축약된 이름들
    usr_nm = "김철수"    # user_name이 더 명확
    age = 30            # user_age가 더 명확
    cnt = 5             # count가 더 명확
    
    # 일관성 없는 명명
    userName = "이영희"  # snake_case와 camelCase 혼용
    user_age = 25       # 일관성 없음
    
    print("나쁜 예시들 (실제로는 사용하지 말 것):")
    print(f"a = {a}, b = {b}, x = {x}")
    print(f"usr_nm = {usr_nm}, age = {age}, cnt = {cnt}")

def demonstrate_naming_conventions():
    """명명 관례 예제"""
    print("\n=== 명명 관례 ===")
    
    # 불린 변수
    is_valid = True
    has_data = True
    can_edit = False
    should_retry = True
    
    # 함수/메서드명
    def get_user_info():
        return "사용자 정보"
    
    def calculate_total():
        return 1000
    
    def is_even_number(num):
        return num % 2 == 0
    
    # 클래스명 (PascalCase)
    class UserManager:
        pass
    
    class DatabaseConnection:
        pass
    
    print(f"유효함: {is_valid}")
    print(f"데이터 있음: {has_data}")
    print(f"편집 가능: {can_edit}")
    print(f"재시도 해야 함: {should_retry}")
    
    print(f"함수 호출: {get_user_info()}")
    print(f"계산 결과: {calculate_total()}")
    print(f"짝수 확인: {is_even_number(8)}")

def demonstrate_private_variables():
    """비공개 변수 명명 예제"""
    print("\n=== 비공개 변수 명명 ===")
    
    class BankAccount:
        def __init__(self, initial_balance):
            self.balance = initial_balance      # 공개 변수
            self._account_number = "12345"      # 내부 사용 (단일 언더스코어)
            self.__pin_code = "0000"           # 비공개 (이중 언더스코어)
        
        def get_balance(self):
            return self.balance
        
        def get_account_number(self):
            return self._account_number
    
    account = BankAccount(1000)
    print(f"잔액: {account.get_balance()}")
    print(f"계좌번호: {account.get_account_number()}")
    # print(account.__pin_code)  # 에러 발생

def demonstrate_context_specific_naming():
    """상황별 명명 예제"""
    print("\n=== 상황별 명명 ===")
    
    # 반복문에서의 변수명
    for index in range(5):
        print(f"인덱스: {index}")
    
    for item in ["사과", "바나나", "오렌지"]:
        print(f"과일: {item}")
    
    # 임시 변수
    temp_result = 10 * 5
    print(f"임시 결과: {temp_result}")
    
    # 루프 변수
    for i in range(3):
        for j in range(3):
            print(f"({i}, {j})", end=" ")
        print()
    
    # 함수 매개변수
    def process_data(data_list, max_items=10):
        return data_list[:max_items]
    
    result = process_data([1, 2, 3, 4, 5], max_items=3)
    print(f"처리된 데이터: {result}")

if __name__ == "__main__":
    demonstrate_naming_rules()
    demonstrate_good_naming()
    demonstrate_bad_naming()
    demonstrate_naming_conventions()
    demonstrate_private_variables()
    demonstrate_context_specific_naming()
