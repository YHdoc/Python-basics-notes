# 실무에서 자주 사용되는 조건문 패턴

def demonstrate_user_validation():
    """사용자 입력 검증 패턴"""
    print("=== 사용자 입력 검증 ===")
    
    def validate_user_registration(username, email, password, age):
        errors = []
        
        # 사용자명 검증
        if not username:
            errors.append("사용자명은 필수입니다")
        elif len(username) < 3:
            errors.append("사용자명은 3자 이상이어야 합니다")
        elif not username.isalnum():
            errors.append("사용자명은 영문자와 숫자만 사용 가능합니다")
        
        # 이메일 검증
        if not email:
            errors.append("이메일은 필수입니다")
        elif "@" not in email or "." not in email:
            errors.append("올바른 이메일 형식이 아닙니다")
        
        # 비밀번호 검증
        if not password:
            errors.append("비밀번호는 필수입니다")
        elif len(password) < 8:
            errors.append("비밀번호는 8자 이상이어야 합니다")
        elif not any(c.isdigit() for c in password):
            errors.append("비밀번호에 숫자가 포함되어야 합니다")
        elif not any(c.isalpha() for c in password):
            errors.append("비밀번호에 문자가 포함되어야 합니다")
        
        # 나이 검증
        if not isinstance(age, int) or age < 0:
            errors.append("올바른 나이를 입력해주세요")
        elif age < 13:
            errors.append("13세 이상만 가입 가능합니다")
        elif age > 120:
            errors.append("올바른 나이를 입력해주세요")
        
        return len(errors) == 0, errors
    
    # 테스트
    test_cases = [
        ("user123", "user@example.com", "password123", 25),
        ("ab", "invalid-email", "123", 10),
        ("", "user@test.com", "password", 30),
        ("user456", "user@domain.com", "weak", 20),
    ]
    
    for username, email, password, age in test_cases:
        is_valid, errors = validate_user_registration(username, email, password, age)
        print(f"사용자: {username}, 이메일: {email}")
        print(f"결과: {'유효' if is_valid else '무효'}")
        if errors:
            for error in errors:
                print(f"  - {error}")
        print()

def demonstrate_file_processing():
    """파일 처리 패턴"""
    print("=== 파일 처리 패턴 ===")
    
    def process_file_safely(file_path, operation="read"):
        import os
        
        # 파일 존재 확인
        if not os.path.exists(file_path):
            return False, "파일이 존재하지 않습니다"
        
        # 파일인지 확인
        if not os.path.isfile(file_path):
            return False, "디렉토리입니다. 파일을 선택해주세요"
        
        # 파일 크기 확인
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            return False, "빈 파일입니다"
        
        # 파일 크기 제한 (10MB)
        max_size = 10 * 1024 * 1024  # 10MB
        if file_size > max_size:
            return False, f"파일이 너무 큽니다 ({file_size / (1024*1024):.1f}MB > 10MB)"
        
        # 파일 확장자 확인
        allowed_extensions = ['.txt', '.csv', '.json', '.xml', '.log']
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext not in allowed_extensions:
            return False, f"지원하지 않는 파일 형식입니다: {file_ext}"
        
        # 권한 확인
        if operation == "read" and not os.access(file_path, os.R_OK):
            return False, "파일 읽기 권한이 없습니다"
        elif operation == "write" and not os.access(file_path, os.W_OK):
            return False, "파일 쓰기 권한이 없습니다"
        
        return True, "파일 처리 가능"
    
    # 테스트
    test_files = [
        "data.txt",
        "large_file.zip",
        "nonexistent.txt",
        "config.json"
    ]
    
    for file_path in test_files:
        is_valid, message = process_file_safely(file_path)
        print(f"파일: {file_path}")
        print(f"결과: {'처리 가능' if is_valid else '처리 불가'}")
        print(f"메시지: {message}")
        print()

def demonstrate_api_response_handling():
    """API 응답 처리 패턴"""
    print("=== API 응답 처리 패턴 ===")
    
    def handle_api_response(response_data):
        # 응답 데이터 존재 확인
        if not response_data:
            return {"success": False, "message": "응답 데이터가 없습니다"}
        
        # HTTP 상태 코드 확인
        status_code = response_data.get("status_code", 0)
        if status_code == 0:
            return {"success": False, "message": "상태 코드가 없습니다"}
        
        # 성공 응답 처리
        if 200 <= status_code < 300:
            data = response_data.get("data")
            if data is None:
                return {"success": False, "message": "데이터가 없습니다"}
            
            # 데이터 유효성 검사
            if isinstance(data, dict):
                if "items" in data:
                    items = data["items"]
                    if not isinstance(items, list):
                        return {"success": False, "message": "items가 리스트가 아닙니다"}
                    if len(items) == 0:
                        return {"success": True, "message": "데이터가 비어있습니다", "data": []}
                    return {"success": True, "message": "성공", "data": items}
                else:
                    return {"success": True, "message": "성공", "data": data}
            else:
                return {"success": True, "message": "성공", "data": data}
        
        # 클라이언트 에러 (4xx)
        elif 400 <= status_code < 500:
            error_message = response_data.get("message", "클라이언트 오류")
            if status_code == 401:
                return {"success": False, "message": "인증이 필요합니다"}
            elif status_code == 403:
                return {"success": False, "message": "접근 권한이 없습니다"}
            elif status_code == 404:
                return {"success": False, "message": "요청한 리소스를 찾을 수 없습니다"}
            else:
                return {"success": False, "message": f"클라이언트 오류: {error_message}"}
        
        # 서버 에러 (5xx)
        elif 500 <= status_code < 600:
            return {"success": False, "message": "서버 오류가 발생했습니다"}
        
        # 기타 상태 코드
        else:
            return {"success": False, "message": f"알 수 없는 상태 코드: {status_code}"}
    
    # 테스트
    test_responses = [
        {"status_code": 200, "data": {"items": [1, 2, 3]}},
        {"status_code": 200, "data": {"items": []}},
        {"status_code": 200, "data": None},
        {"status_code": 401, "message": "Unauthorized"},
        {"status_code": 404, "message": "Not Found"},
        {"status_code": 500, "message": "Internal Server Error"},
        {"status_code": 0},
        None
    ]
    
    for i, response in enumerate(test_responses, 1):
        result = handle_api_response(response)
        print(f"테스트 {i}: {result}")
        print()

def demonstrate_configuration_loading():
    """설정 파일 로딩 패턴"""
    print("=== 설정 파일 로딩 패턴 ===")
    
    def load_config_with_defaults(config_data):
        # 기본 설정값
        defaults = {
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "myapp",
                "username": "admin",
                "password": "password"
            },
            "server": {
                "host": "0.0.0.0",
                "port": 8000,
                "debug": False
            },
            "logging": {
                "level": "INFO",
                "file": "app.log",
                "max_size": "10MB"
            }
        }
        
        # 설정 데이터가 없으면 기본값 사용
        if not config_data:
            return defaults
        
        # 설정 병합
        merged_config = defaults.copy()
        
        # 데이터베이스 설정
        if "database" in config_data:
            db_config = config_data["database"]
            if isinstance(db_config, dict):
                merged_config["database"].update(db_config)
        
        # 서버 설정
        if "server" in config_data:
            server_config = config_data["server"]
            if isinstance(server_config, dict):
                merged_config["server"].update(server_config)
        
        # 로깅 설정
        if "logging" in config_data:
            logging_config = config_data["logging"]
            if isinstance(logging_config, dict):
                merged_config["logging"].update(logging_config)
        
        # 설정 검증
        if not isinstance(merged_config["database"]["port"], int):
            merged_config["database"]["port"] = 5432
        
        if not isinstance(merged_config["server"]["port"], int):
            merged_config["server"]["port"] = 8000
        
        if merged_config["server"]["port"] < 1 or merged_config["server"]["port"] > 65535:
            merged_config["server"]["port"] = 8000
        
        return merged_config
    
    # 테스트
    test_configs = [
        None,  # 기본값만 사용
        {"database": {"host": "db.example.com", "port": 3306}},  # 부분 설정
        {"server": {"port": "invalid"}},  # 잘못된 타입
        {"database": {"host": "prod.db.com"}, "server": {"debug": True}},  # 정상 설정
    ]
    
    for i, config in enumerate(test_configs, 1):
        result = load_config_with_defaults(config)
        print(f"테스트 {i}:")
        print(f"  데이터베이스: {result['database']['host']}:{result['database']['port']}")
        print(f"  서버: {result['server']['host']}:{result['server']['port']} (debug: {result['server']['debug']})")
        print()

def demonstrate_error_handling_patterns():
    """에러 처리 패턴"""
    print("=== 에러 처리 패턴 ===")
    
    def safe_divide(a, b):
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                return None, "숫자만 입력 가능합니다"
            
            if b == 0:
                return None, "0으로 나눌 수 없습니다"
            
            result = a / b
            return result, None
            
        except Exception as e:
            return None, f"예상치 못한 오류: {str(e)}"
    
    def safe_list_access(lst, index, default=None):
        try:
            if not isinstance(lst, list):
                return default, "리스트가 아닙니다"
            
            if not isinstance(index, int):
                return default, "인덱스는 정수여야 합니다"
            
            if index < 0 or index >= len(lst):
                return default, f"인덱스 범위 초과 (0-{len(lst)-1})"
            
            return lst[index], None
            
        except Exception as e:
            return default, f"예상치 못한 오류: {str(e)}"
    
    # 테스트
    print("안전한 나눗셈:")
    test_divisions = [(10, 2), (10, 0), ("10", 2), (10, "2")]
    for a, b in test_divisions:
        result, error = safe_divide(a, b)
        if error:
            print(f"  {a} / {b} -> 오류: {error}")
        else:
            print(f"  {a} / {b} = {result}")
    
    print("\n안전한 리스트 접근:")
    test_list = [1, 2, 3, 4, 5]
    test_indices = [0, 2, 5, -1, "invalid"]
    for index in test_indices:
        result, error = safe_list_access(test_list, index, "기본값")
        if error:
            print(f"  인덱스 {index} -> 오류: {error}")
        else:
            print(f"  인덱스 {index} -> {result}")

def demonstrate_business_logic_conditions():
    """비즈니스 로직 조건 패턴"""
    print("=== 비즈니스 로직 조건 패턴 ===")
    
    def calculate_shipping_cost(order_amount, user_type, is_express=False, is_weekend=False):
        # 기본 배송비
        base_shipping = 3000
        
        # 주문 금액에 따른 무료 배송
        if order_amount >= 50000:
            return 0, "무료 배송"
        
        # 사용자 타입별 할인
        if user_type == "vip":
            shipping_discount = 0.5  # 50% 할인
        elif user_type == "premium":
            shipping_discount = 0.3  # 30% 할인
        elif user_type == "regular":
            shipping_discount = 0.1  # 10% 할인
        else:
            shipping_discount = 0    # 할인 없음
        
        # 익스프레스 배송
        if is_express:
            base_shipping *= 2  # 2배
        
        # 주말 배송
        if is_weekend:
            base_shipping *= 1.5  # 1.5배
        
        # 할인 적용
        final_shipping = base_shipping * (1 - shipping_discount)
        
        # 최소 배송비
        if final_shipping < 1000:
            final_shipping = 1000
        
        return int(final_shipping), f"배송비 (할인: {shipping_discount:.0%})"
    
    # 테스트
    test_orders = [
        (30000, "vip", False, False),
        (60000, "regular", False, False),  # 무료 배송
        (25000, "premium", True, False),   # 익스프레스
        (15000, "regular", False, True),   # 주말 배송
        (10000, "guest", True, True),      # 모든 조건
    ]
    
    for amount, user_type, express, weekend in test_orders:
        cost, message = calculate_shipping_cost(amount, user_type, express, weekend)
        print(f"주문금액: {amount:,}원, 사용자: {user_type}, 익스프레스: {express}, 주말: {weekend}")
        print(f"  배송비: {cost:,}원 ({message})")
        print()

if __name__ == "__main__":
    demonstrate_user_validation()
    demonstrate_file_processing()
    demonstrate_api_response_handling()
    demonstrate_configuration_loading()
    demonstrate_error_handling_patterns()
    demonstrate_business_logic_conditions()
