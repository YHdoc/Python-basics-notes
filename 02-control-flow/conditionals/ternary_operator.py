# 삼항 연산자

def demonstrate_basic_ternary():
    """기본 삼항 연산자 예제"""
    print("=== 기본 삼항 연산자 ===")
    
    age = 20
    
    # 기본 문법: value_if_true if condition else value_if_false
    status = "성인" if age >= 18 else "미성년자"
    print(f"나이 {age}: {status}")
    
    # 숫자 비교
    a, b = 10, 20
    max_value = a if a > b else b
    print(f"max({a}, {b}) = {max_value}")
    
    # 문자열 처리
    name = "김철수"
    greeting = f"안녕하세요, {name}님!" if name else "안녕하세요!"
    print(greeting)

def demonstrate_nested_ternary():
    """중첩 삼항 연산자 예제"""
    print("\n=== 중첩 삼항 연산자 ===")
    
    score = 85
    
    # 중첩 삼항 연산자
    grade = ("A" if score >= 90 else 
             "B" if score >= 80 else 
             "C" if score >= 70 else 
             "D" if score >= 60 else "F")
    
    print(f"점수 {score}: {grade}등급")
    
    # 더 복잡한 예제
    temperature = 25
    weather = "맑음"
    
    activity = ("수영" if temperature >= 30 else
                "야외활동" if temperature >= 20 and weather == "맑음" else
                "실내활동" if temperature < 10 else
                "가벼운 야외활동")
    
    print(f"온도 {temperature}°C, 날씨 {weather} -> {activity}")

def demonstrate_ternary_with_functions():
    """함수와 함께 사용하는 삼항 연산자"""
    print("\n=== 함수와 함께 사용 ===")
    
    def get_discount_rate(user_type):
        return 0.15 if user_type == "vip" else 0.10 if user_type == "premium" else 0.05
    
    def format_price(price, currency="원"):
        return f"{price:,}{currency}" if price > 0 else "무료"
    
    # 사용 예제
    user_types = ["vip", "premium", "regular"]
    for user_type in user_types:
        discount = get_discount_rate(user_type)
        print(f"{user_type} 사용자 할인율: {discount:.1%}")
    
    prices = [0, 1000, 50000, 100000]
    for price in prices:
        formatted = format_price(price)
        print(f"가격: {formatted}")

def demonstrate_ternary_with_lists():
    """리스트와 함께 사용하는 삼항 연산자"""
    print("\n=== 리스트와 함께 사용 ===")
    
    # 리스트가 비어있는지 확인
    def get_list_info(lst):
        return "리스트가 비어있습니다" if not lst else f"리스트 길이: {len(lst)}"
    
    # 리스트 요소 선택
    def get_first_or_default(lst, default="기본값"):
        return lst[0] if lst else default
    
    # 테스트
    test_lists = [
        [],
        [1, 2, 3],
        ["apple", "banana", "cherry"]
    ]
    
    for lst in test_lists:
        info = get_list_info(lst)
        first = get_first_or_default(lst)
        print(f"리스트: {lst} -> {info}, 첫 번째 요소: {first}")

def demonstrate_ternary_with_dictionaries():
    """딕셔너리와 함께 사용하는 삼항 연산자"""
    print("\n=== 딕셔너리와 함께 사용 ===")
    
    def get_user_info(user_data):
        name = user_data.get("name", "익명")
        age = user_data.get("age", 0)
        
        # 삼항 연산자로 정보 포맷팅
        age_info = f"{age}세" if age > 0 else "나이 미상"
        status = "성인" if age >= 18 else "미성년자" if age > 0 else "나이 미상"
        
        return f"이름: {name}, 나이: {age_info}, 상태: {status}"
    
    # 테스트
    test_users = [
        {"name": "김철수", "age": 25},
        {"name": "이영희", "age": 17},
        {"name": "박민수"},  # age 없음
        {}  # 빈 딕셔너리
    ]
    
    for user in test_users:
        info = get_user_info(user)
        print(f"사용자 정보: {info}")

def demonstrate_ternary_vs_if_else():
    """삼항 연산자 vs if-else 비교"""
    print("\n=== 삼항 연산자 vs if-else ===")
    
    # 삼항 연산자 사용
    def using_ternary(x):
        return "양수" if x > 0 else "음수" if x < 0 else "영"
    
    # if-else 사용
    def using_if_else(x):
        if x > 0:
            return "양수"
        elif x < 0:
            return "음수"
        else:
            return "영"
    
    # 테스트
    test_values = [5, -3, 0]
    
    print("삼항 연산자 사용:")
    for x in test_values:
        result = using_ternary(x)
        print(f"  {x} -> {result}")
    
    print("\nif-else 사용:")
    for x in test_values:
        result = using_if_else(x)
        print(f"  {x} -> {result}")

def demonstrate_ternary_best_practices():
    """삼항 연산자 모범 사례"""
    print("\n=== 모범 사례 ===")
    
    # 좋은 예: 간단하고 명확한 조건
    def is_even_good(num):
        return "짝수" if num % 2 == 0 else "홀수"
    
    # 나쁜 예: 복잡한 조건 (가독성이 떨어짐)
    def is_even_bad(num):
        return "짝수" if num % 2 == 0 and num > 0 and isinstance(num, int) else "홀수 또는 유효하지 않은 입력"
    
    # 좋은 예: 간단한 값 할당
    def get_status_good(is_active, is_premium):
        return "활성 프리미엄" if is_active and is_premium else "활성 일반" if is_active else "비활성"
    
    # 나쁜 예: 너무 복잡한 중첩
    def get_status_bad(is_active, is_premium, has_permission, is_verified):
        return ("활성 프리미엄 인증" if is_active and is_premium and is_verified else
                "활성 프리미엄 미인증" if is_active and is_premium else
                "활성 일반 인증" if is_active and is_verified else
                "활성 일반 미인증" if is_active else
                "비활성")
    
    # 테스트
    print("좋은 예:")
    for num in [2, 3, 4, 5]:
        result = is_even_good(num)
        print(f"  {num} -> {result}")
    
    print("\n나쁜 예 (복잡함):")
    for num in [2, 3, 4, 5]:
        result = is_even_bad(num)
        print(f"  {num} -> {result}")

def demonstrate_ternary_with_side_effects():
    """부작용이 있는 삼항 연산자 (주의사항)"""
    print("\n=== 부작용이 있는 삼항 연산자 ===")
    
    # 주의: 삼항 연산자는 두 값 모두 평가됨
    def safe_divide(a, b):
        # 이렇게 하면 b가 0일 때도 b로 나누려고 시도함 (에러 발생)
        # return a / b if b != 0 else 0  # 위험!
        
        # 안전한 방법
        if b != 0:
            return a / b
        else:
            return 0
    
    # 리스트에서 안전하게 요소 가져오기
    def safe_get_item(lst, index, default=None):
        # 삼항 연산자 사용 (안전함)
        return lst[index] if 0 <= index < len(lst) else default
    
    # 테스트
    print("안전한 나눗셈:")
    test_cases = [(10, 2), (10, 0), (15, 3)]
    for a, b in test_cases:
        result = safe_divide(a, b)
        print(f"  {a} / {b} = {result}")
    
    print("\n안전한 리스트 접근:")
    test_list = [1, 2, 3, 4, 5]
    indices = [0, 2, 5, -1]
    for index in indices:
        result = safe_get_item(test_list, index, "인덱스 범위 초과")
        print(f"  인덱스 {index}: {result}")

def demonstrate_ternary_practical_examples():
    """실용적인 삼항 연산자 예제"""
    print("\n=== 실용적인 예제 ===")
    
    # 파일 확장자 확인
    def get_file_type(filename):
        return ("이미지" if filename.lower().endswith(('.jpg', '.png', '.gif')) else
                "문서" if filename.lower().endswith(('.txt', '.pdf', '.doc')) else
                "압축파일" if filename.lower().endswith(('.zip', '.rar', '.7z')) else
                "알 수 없음")
    
    # 사용자 권한 확인
    def get_user_permission(user_role, is_verified):
        return ("모든 권한" if user_role == "admin" and is_verified else
                "읽기/쓰기 권한" if user_role == "user" and is_verified else
                "읽기 권한" if is_verified else
                "권한 없음")
    
    # 테스트
    filenames = ["photo.jpg", "document.pdf", "archive.zip", "unknown.xyz"]
    print("파일 타입 확인:")
    for filename in filenames:
        file_type = get_file_type(filename)
        print(f"  {filename} -> {file_type}")
    
    print("\n사용자 권한 확인:")
    user_roles = [("admin", True), ("user", True), ("user", False), ("guest", True)]
    for role, verified in user_roles:
        permission = get_user_permission(role, verified)
        print(f"  {role} (인증: {verified}) -> {permission}")

if __name__ == "__main__":
    demonstrate_basic_ternary()
    demonstrate_nested_ternary()
    demonstrate_ternary_with_functions()
    demonstrate_ternary_with_lists()
    demonstrate_ternary_with_dictionaries()
    demonstrate_ternary_vs_if_else()
    demonstrate_ternary_best_practices()
    demonstrate_ternary_with_side_effects()
    demonstrate_ternary_practical_examples()
