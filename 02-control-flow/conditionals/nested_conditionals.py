# 중첩 조건문

def demonstrate_basic_nested_conditionals():
    """기본 중첩 조건문 예제"""
    print("=== 기본 중첩 조건문 ===")
    
    age = 20
    has_license = True
    
    if age >= 18:
        print("성인입니다.")
        if has_license:
            print("  운전면허가 있습니다.")
            print("  운전할 수 있습니다.")
        else:
            print("  운전면허가 없습니다.")
            print("  운전할 수 없습니다.")
    else:
        print("미성년자입니다.")
        print("운전할 수 없습니다.")

def demonstrate_grade_calculation():
    """성적 계산 중첩 조건문"""
    print("\n=== 성적 계산 ===")
    
    def calculate_grade(score, attendance_rate):
        if attendance_rate >= 80:  # 출석률 체크
            if score >= 90:
                return "A+"
            elif score >= 85:
                return "A"
            elif score >= 80:
                return "B+"
            elif score >= 75:
                return "B"
            elif score >= 70:
                return "C+"
            elif score >= 65:
                return "C"
            elif score >= 60:
                return "D"
            else:
                return "F"
        else:
            return "F (출석률 부족)"
    
    # 테스트
    test_cases = [
        (95, 90),  # A+
        (88, 85),  # A
        (82, 75),  # B+
        (78, 80),  # B
        (72, 70),  # C+
        (68, 65),  # C
        (62, 60),  # D
        (55, 90),  # F
        (95, 70),  # F (출석률 부족)
    ]
    
    for score, attendance in test_cases:
        grade = calculate_grade(score, attendance)
        print(f"점수: {score}, 출석률: {attendance}% -> {grade}")

def demonstrate_user_authentication():
    """사용자 인증 중첩 조건문"""
    print("\n=== 사용자 인증 ===")
    
    def authenticate_user(username, password, role="user"):
        # 첫 번째 레벨: 사용자명 확인
        if username:
            # 두 번째 레벨: 비밀번호 확인
            if password:
                # 세 번째 레벨: 역할 확인
                if role == "admin":
                    return "관리자로 로그인 성공"
                elif role == "moderator":
                    return "모더레이터로 로그인 성공"
                elif role == "user":
                    return "일반 사용자로 로그인 성공"
                else:
                    return "알 수 없는 역할"
            else:
                return "비밀번호가 필요합니다"
        else:
            return "사용자명이 필요합니다"
    
    # 테스트
    test_cases = [
        ("admin", "password123", "admin"),
        ("user1", "mypass", "user"),
        ("mod1", "modpass", "moderator"),
        ("", "password", "user"),  # 사용자명 없음
        ("user2", "", "user"),     # 비밀번호 없음
        ("user3", "pass", "unknown"),  # 알 수 없는 역할
    ]
    
    for username, password, role in test_cases:
        result = authenticate_user(username, password, role)
        print(f"사용자: {username or 'None'}, 역할: {role} -> {result}")

def demonstrate_file_processing():
    """파일 처리 중첩 조건문"""
    print("\n=== 파일 처리 ===")
    
    def process_file(filename, file_size, file_type, is_readable=True):
        # 파일 존재 확인
        if filename:
            # 파일 크기 확인
            if file_size > 0:
                # 파일 타입 확인
                if file_type in ['txt', 'csv', 'json']:
                    # 읽기 권한 확인
                    if is_readable:
                        # 파일 크기별 처리
                        if file_size < 1024:  # 1KB 미만
                            return f"작은 {file_type} 파일 처리 완료"
                        elif file_size < 1024 * 1024:  # 1MB 미만
                            return f"중간 크기 {file_type} 파일 처리 완료"
                        else:
                            return f"큰 {file_type} 파일 처리 완료"
                    else:
                        return "파일 읽기 권한이 없습니다"
                else:
                    return f"지원하지 않는 파일 형식: {file_type}"
            else:
                return "빈 파일입니다"
        else:
            return "파일명이 제공되지 않았습니다"
    
    # 테스트
    test_cases = [
        ("data.txt", 512, "txt", True),
        ("large.csv", 2048 * 1024, "csv", True),
        ("config.json", 1024, "json", True),
        ("", 1024, "txt", True),  # 파일명 없음
        ("data.txt", 0, "txt", True),  # 빈 파일
        ("data.pdf", 1024, "pdf", True),  # 지원하지 않는 형식
        ("data.txt", 1024, "txt", False),  # 읽기 권한 없음
    ]
    
    for filename, size, file_type, readable in test_cases:
        result = process_file(filename, size, file_type, readable)
        print(f"파일: {filename or 'None'}, 크기: {size}, 타입: {file_type} -> {result}")

def demonstrate_shopping_cart():
    """쇼핑 카트 중첩 조건문"""
    print("\n=== 쇼핑 카트 ===")
    
    def calculate_discount(total_amount, user_type, has_coupon=False):
        # 사용자 타입별 기본 할인
        if user_type == "vip":
            base_discount = 0.15  # 15%
        elif user_type == "premium":
            base_discount = 0.10  # 10%
        elif user_type == "regular":
            base_discount = 0.05  # 5%
        else:
            base_discount = 0.0   # 할인 없음
        
        # 쿠폰 할인 추가
        if has_coupon:
            if total_amount >= 100000:  # 10만원 이상
                coupon_discount = 0.1   # 10% 추가 할인
            elif total_amount >= 50000:  # 5만원 이상
                coupon_discount = 0.05  # 5% 추가 할인
            else:
                coupon_discount = 0.02  # 2% 추가 할인
        else:
            coupon_discount = 0.0
        
        # 총 할인율 계산 (최대 30%)
        total_discount = min(base_discount + coupon_discount, 0.3)
        
        return total_discount
    
    # 테스트
    test_cases = [
        (150000, "vip", True),    # VIP + 쿠폰 + 고액
        (80000, "premium", True), # Premium + 쿠폰 + 중액
        (30000, "regular", True), # Regular + 쿠폰 + 저액
        (200000, "vip", False),   # VIP + 쿠폰 없음
        (10000, "guest", True),   # Guest + 쿠폰
    ]
    
    for amount, user_type, has_coupon in test_cases:
        discount = calculate_discount(amount, user_type, has_coupon)
        discounted_amount = amount * (1 - discount)
        print(f"금액: {amount:,}원, 사용자: {user_type}, 쿠폰: {has_coupon}")
        print(f"  할인율: {discount:.1%}, 할인 후: {discounted_amount:,.0f}원")

def demonstrate_weather_conditions():
    """날씨 조건 중첩 조건문"""
    print("\n=== 날씨 조건 ===")
    
    def get_activity_recommendation(temperature, humidity, is_sunny, wind_speed):
        # 온도별 기본 활동
        if temperature >= 30:
            if humidity > 70:
                return "실내 활동을 권장합니다 (고온다습)"
            elif is_sunny:
                return "수영이나 실내 스포츠를 권장합니다"
            else:
                return "실내 활동을 권장합니다"
        elif temperature >= 20:
            if is_sunny:
                if wind_speed < 10:
                    return "야외 활동에 최적입니다"
                else:
                    return "바람이 강하니 주의하세요"
            else:
                return "야외 활동 가능하지만 날씨를 확인하세요"
        elif temperature >= 10:
            if is_sunny and wind_speed < 15:
                return "가벼운 야외 활동을 권장합니다"
            else:
                return "실내 활동을 권장합니다"
        else:
            return "실내 활동을 권장합니다 (추위)"

    # 테스트
    test_cases = [
        (35, 80, True, 5),   # 고온다습
        (32, 50, True, 3),   # 고온건조
        (25, 60, True, 8),   # 적당한 날씨
        (25, 60, False, 8),  # 흐린 날씨
        (15, 70, True, 20),  # 바람 강함
        (5, 80, False, 10),  # 추운 날씨
    ]
    
    for temp, humidity, sunny, wind in test_cases:
        recommendation = get_activity_recommendation(temp, humidity, sunny, wind)
        print(f"온도: {temp}°C, 습도: {humidity}%, 맑음: {sunny}, 바람: {wind}m/s")
        print(f"  권장사항: {recommendation}")

def demonstrate_avoiding_deep_nesting():
    """깊은 중첩을 피하는 방법"""
    print("\n=== 깊은 중첩을 피하는 방법 ===")
    
    # 나쁜 예: 깊은 중첩
    def bad_nested_example(data):
        if data:
            if isinstance(data, dict):
                if "name" in data:
                    if data["name"]:
                        if len(data["name"]) > 0:
                            return f"이름: {data['name']}"
                        else:
                            return "이름이 비어있습니다"
                    else:
                        return "이름이 None입니다"
                else:
                    return "이름 키가 없습니다"
            else:
                return "딕셔너리가 아닙니다"
        else:
            return "데이터가 없습니다"
    
    # 좋은 예: 가드 절 사용
    def good_nested_example(data):
        # 가드 절들
        if not data:
            return "데이터가 없습니다"
        
        if not isinstance(data, dict):
            return "딕셔너리가 아닙니다"
        
        if "name" not in data:
            return "이름 키가 없습니다"
        
        if not data["name"]:
            return "이름이 None입니다"
        
        if len(data["name"]) == 0:
            return "이름이 비어있습니다"
        
        # 정상 처리
        return f"이름: {data['name']}"
    
    # 테스트
    test_data = [
        None,
        "not a dict",
        {},
        {"name": None},
        {"name": ""},
        {"name": "김철수"},
    ]
    
    print("나쁜 예:")
    for data in test_data:
        result = bad_nested_example(data)
        print(f"  {data} -> {result}")
    
    print("\n좋은 예:")
    for data in test_data:
        result = good_nested_example(data)
        print(f"  {data} -> {result}")

if __name__ == "__main__":
    demonstrate_basic_nested_conditionals()
    demonstrate_grade_calculation()
    demonstrate_user_authentication()
    demonstrate_file_processing()
    demonstrate_shopping_cart()
    demonstrate_weather_conditions()
    demonstrate_avoiding_deep_nesting()
