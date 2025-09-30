# 커스텀 예외 정의

def basic_custom_exception():
    """기본 커스텀 예외 정의"""
    print("=== 기본 커스텀 예외 정의 ===")
    
    # 기본 커스텀 예외
    class CustomError(Exception):
        pass
    
    # 커스텀 예외 발생
    def raise_custom_error():
        raise CustomError("커스텀 오류가 발생했습니다.")
    
    try:
        raise_custom_error()
    except CustomError as e:
        print(f"커스텀 예외 처리: {e}")

def custom_exception_with_message():
    """메시지가 있는 커스텀 예외"""
    print("\n=== 메시지가 있는 커스텀 예외 ===")
    
    class ValidationError(Exception):
        def __init__(self, message, field_name=None):
            super().__init__(message)
            self.field_name = field_name
    
    def validate_age(age):
        if not isinstance(age, int):
            raise ValidationError("나이는 정수여야 합니다.", "age")
        if age < 0:
            raise ValidationError("나이는 0 이상이어야 합니다.", "age")
        if age > 150:
            raise ValidationError("나이는 150 이하여야 합니다.", "age")
        return True
    
    # 테스트
    test_ages = [25, -5, 200, "abc"]
    for age in test_ages:
        try:
            validate_age(age)
            print(f"나이 {age}: 유효함")
        except ValidationError as e:
            print(f"나이 {age}: {e} (필드: {e.field_name})")

def custom_exception_hierarchy():
    """커스텀 예외 계층 구조"""
    print("\n=== 커스텀 예외 계층 구조 ===")
    
    # 기본 예외 클래스
    class DatabaseError(Exception):
        pass
    
    # 구체적인 예외 클래스들
    class ConnectionError(DatabaseError):
        pass
    
    class QueryError(DatabaseError):
        pass
    
    class DataError(DatabaseError):
        pass
    
    # 예외 발생 함수들
    def connect_to_database():
        raise ConnectionError("데이터베이스 연결 실패")
    
    def execute_query():
        raise QueryError("쿼리 실행 실패")
    
    def process_data():
        raise DataError("데이터 처리 실패")
    
    # 예외 처리
    operations = [connect_to_database, execute_query, process_data]
    
    for operation in operations:
        try:
            operation()
        except ConnectionError as e:
            print(f"연결 오류: {e}")
        except QueryError as e:
            print(f"쿼리 오류: {e}")
        except DataError as e:
            print(f"데이터 오류: {e}")
        except DatabaseError as e:
            print(f"데이터베이스 오류: {e}")

def custom_exception_with_attributes():
    """속성이 있는 커스텀 예외"""
    print("\n=== 속성이 있는 커스텀 예외 ===")
    
    class FileProcessingError(Exception):
        def __init__(self, message, filename=None, line_number=None):
            super().__init__(message)
            self.filename = filename
            self.line_number = line_number
        
        def __str__(self):
            base_msg = super().__str__()
            if self.filename:
                base_msg += f" (파일: {self.filename}"
                if self.line_number:
                    base_msg += f", 라인: {self.line_number}"
                base_msg += ")"
            return base_msg
    
    def process_file_line(filename, line_number, content):
        if not content.strip():
            raise FileProcessingError("빈 줄입니다.", filename, line_number)
        if len(content) > 100:
            raise FileProcessingError("줄이 너무 깁니다.", filename, line_number)
        return content.strip()
    
    # 테스트
    test_data = [
        ("test.txt", 1, "정상적인 줄"),
        ("test.txt", 2, ""),
        ("test.txt", 3, "x" * 150)
    ]
    
    for filename, line_num, content in test_data:
        try:
            result = process_file_line(filename, line_num, content)
            print(f"처리 성공: {result}")
        except FileProcessingError as e:
            print(f"처리 실패: {e}")

def custom_exception_with_methods():
    """메서드가 있는 커스텀 예외"""
    print("\n=== 메서드가 있는 커스텀 예외 ===")
    
    class BusinessLogicError(Exception):
        def __init__(self, message, error_code=None, details=None):
            super().__init__(message)
            self.error_code = error_code
            self.details = details or {}
        
        def get_error_info(self):
            return {
                "message": str(self),
                "error_code": self.error_code,
                "details": self.details
            }
        
        def is_critical(self):
            return self.error_code and self.error_code.startswith("CRITICAL")
    
    def process_order(order_data):
        if not order_data.get("customer_id"):
            raise BusinessLogicError(
                "고객 ID가 필요합니다.",
                "MISSING_CUSTOMER_ID",
                {"field": "customer_id", "order_data": order_data}
            )
        
        if order_data.get("amount", 0) <= 0:
            raise BusinessLogicError(
                "주문 금액이 유효하지 않습니다.",
                "CRITICAL_INVALID_AMOUNT",
                {"amount": order_data.get("amount")}
            )
        
        return f"주문 처리 완료: {order_data['customer_id']}"
    
    # 테스트
    test_orders = [
        {"customer_id": "C001", "amount": 1000},
        {"amount": 1000},  # customer_id 누락
        {"customer_id": "C002", "amount": 0},  # 잘못된 금액
        {"customer_id": "C003", "amount": -100}  # 음수 금액
    ]
    
    for order in test_orders:
        try:
            result = process_order(order)
            print(f"주문 성공: {result}")
        except BusinessLogicError as e:
            print(f"주문 실패: {e}")
            print(f"오류 정보: {e.get_error_info()}")
            print(f"치명적 오류: {e.is_critical()}")

def custom_exception_with_context():
    """컨텍스트가 있는 커스텀 예외"""
    print("\n=== 컨텍스트가 있는 커스텀 예외 ===")
    
    class APIError(Exception):
        def __init__(self, message, status_code=None, response_data=None, request_url=None):
            super().__init__(message)
            self.status_code = status_code
            self.response_data = response_data
            self.request_url = request_url
        
        def get_context(self):
            return {
                "message": str(self),
                "status_code": self.status_code,
                "request_url": self.request_url,
                "response_data": self.response_data
            }
    
    def make_api_request(url):
        # 가상의 API 요청
        if "error" in url:
            raise APIError(
                "API 요청 실패",
                status_code=500,
                response_data={"error": "Internal Server Error"},
                request_url=url
            )
        elif "notfound" in url:
            raise APIError(
                "리소스를 찾을 수 없습니다",
                status_code=404,
                response_data={"error": "Not Found"},
                request_url=url
            )
        else:
            return {"data": "성공적인 응답"}
    
    # 테스트
    test_urls = [
        "https://api.example.com/users",
        "https://api.example.com/error",
        "https://api.example.com/notfound"
    ]
    
    for url in test_urls:
        try:
            response = make_api_request(url)
            print(f"API 요청 성공: {response}")
        except APIError as e:
            print(f"API 요청 실패: {e}")
            print(f"컨텍스트: {e.get_context()}")

def custom_exception_best_practices():
    """커스텀 예외 모범 사례"""
    print("\n=== 커스텀 예외 모범 사례 ===")
    
    # 1. 명확한 이름 사용
    class InvalidEmailError(Exception):
        pass
    
    class InsufficientFundsError(Exception):
        pass
    
    # 2. 적절한 상속 구조
    class PaymentError(Exception):
        pass
    
    class CreditCardError(PaymentError):
        pass
    
    class BankTransferError(PaymentError):
        pass
    
    # 3. 유용한 정보 포함
    class ValidationError(Exception):
        def __init__(self, message, field_name, value):
            super().__init__(message)
            self.field_name = field_name
            self.value = value
        
        def __str__(self):
            return f"{super().__str__()} (필드: {self.field_name}, 값: {self.value})"
    
    # 4. 예외 체인 사용
    def process_data(data):
        try:
            result = int(data)
        except ValueError as e:
            raise ValidationError("데이터 변환 실패", "data", data) from e
    
    try:
        process_data("abc")
    except ValidationError as e:
        print(f"검증 오류: {e}")
        print(f"원본 오류: {e.__cause__}")

def practical_custom_exceptions():
    """실무에서 자주 사용되는 커스텀 예외"""
    print("\n=== 실무 커스텀 예외 예제 ===")
    
    # 웹 애플리케이션 예외
    class WebAppError(Exception):
        def __init__(self, message, status_code=500, user_message=None):
            super().__init__(message)
            self.status_code = status_code
            self.user_message = user_message or message
    
    class AuthenticationError(WebAppError):
        def __init__(self, message="인증이 필요합니다"):
            super().__init__(message, 401, "로그인이 필요합니다")
    
    class AuthorizationError(WebAppError):
        def __init__(self, message="권한이 없습니다"):
            super().__init__(message, 403, "접근 권한이 없습니다")
    
    class ValidationError(WebAppError):
        def __init__(self, message="입력 데이터가 유효하지 않습니다"):
            super().__init__(message, 400, "입력한 정보를 확인해주세요")
    
    # 사용 예제
    def check_user_permission(user, resource):
        if not user:
            raise AuthenticationError()
        if not user.has_permission(resource):
            raise AuthorizationError()
        return True
    
    def validate_user_data(data):
        if not data.get("email"):
            raise ValidationError("이메일이 필요합니다")
        if "@" not in data["email"]:
            raise ValidationError("올바른 이메일 형식이 아닙니다")
        return True

if __name__ == "__main__":
    basic_custom_exception()
    custom_exception_with_message()
    custom_exception_hierarchy()
    custom_exception_with_attributes()
    custom_exception_with_methods()
    custom_exception_with_context()
    custom_exception_best_practices()
    practical_custom_exceptions()
