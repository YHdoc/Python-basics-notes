# 예외 계층 구조

def demonstrate_exception_hierarchy():
    """예외 계층 구조 예제"""
    print("=== 예외 계층 구조 ===")
    
    # BaseException (최상위)
    print("BaseException (최상위 예외)")
    print("├── SystemExit")
    print("├── KeyboardInterrupt")
    print("├── GeneratorExit")
    print("└── Exception")
    print("    ├── StopIteration")
    print("    ├── StopAsyncIteration")
    print("    ├── ArithmeticError")
    print("    │   ├── FloatingPointError")
    print("    │   ├── OverflowError")
    print("    │   └── ZeroDivisionError")
    print("    ├── AssertionError")
    print("    ├── AttributeError")
    print("    ├── BufferError")
    print("    ├── EOFError")
    print("    ├── ImportError")
    print("    │   └── ModuleNotFoundError")
    print("    ├── LookupError")
    print("    │   ├── IndexError")
    print("    │   └── KeyError")
    print("    ├── MemoryError")
    print("    ├── NameError")
    print("    │   └── UnboundLocalError")
    print("    ├── OSError")
    print("    │   ├── BlockingIOError")
    print("    │   ├── ChildProcessError")
    print("    │   ├── ConnectionError")
    print("    │   │   ├── BrokenPipeError")
    print("    │   │   ├── ConnectionAbortedError")
    print("    │   │   ├── ConnectionRefusedError")
    print("    │   │   └── ConnectionResetError")
    print("    │   ├── FileExistsError")
    print("    │   ├── FileNotFoundError")
    print("    │   ├── InterruptedError")
    print("    │   ├── IsADirectoryError")
    print("    │   ├── NotADirectoryError")
    print("    │   ├── PermissionError")
    print("    │   ├── ProcessLookupError")
    print("    │   └── TimeoutError")
    print("    ├── ReferenceError")
    print("    ├── RuntimeError")
    print("    │   ├── NotImplementedError")
    print("    │   └── RecursionError")
    print("    ├── SyntaxError")
    print("    │   └── IndentationError")
    print("    │       └── TabError")
    print("    ├── SystemError")
    print("    ├── TypeError")
    print("    ├── ValueError")
    print("    │   └── UnicodeError")
    print("    │       ├── UnicodeDecodeError")
    print("    │       ├── UnicodeEncodeError")
    print("    │       └── UnicodeTranslateError")
    print("    └── Warning")
    print("        ├── DeprecationWarning")
    print("        ├── PendingDeprecationWarning")
    print("        ├── RuntimeWarning")
    print("        ├── SyntaxWarning")
    print("        ├── UserWarning")
    print("        ├── FutureWarning")
    print("        ├── ImportWarning")
    print("        ├── UnicodeWarning")
    print("        └── BytesWarning")

def demonstrate_exception_inheritance():
    """예외 상속 관계 예제"""
    print("\n=== 예외 상속 관계 ===")
    
    # 예외 클래스들의 상속 관계 확인
    exceptions_to_check = [
        (ZeroDivisionError, ArithmeticError),
        (IndexError, LookupError),
        (KeyError, LookupError),
        (FileNotFoundError, OSError),
        (PermissionError, OSError),
        (ValueError, Exception),
        (TypeError, Exception),
        (NameError, Exception),
    ]
    
    for child, parent in exceptions_to_check:
        is_subclass = issubclass(child, parent)
        print(f"{child.__name__} is subclass of {parent.__name__}: {is_subclass}")
    
    # MRO (Method Resolution Order) 확인
    print(f"\nZeroDivisionError MRO: {ZeroDivisionError.__mro__}")
    print(f"FileNotFoundError MRO: {FileNotFoundError.__mro__}")

def demonstrate_catching_parent_exceptions():
    """부모 예외로 자식 예외 잡기"""
    print("\n=== 부모 예외로 자식 예외 잡기 ===")
    
    def test_arithmetic_operations():
        try:
            result = 10 / 0
        except ArithmeticError as e:
            print(f"ArithmeticError로 잡힘: {type(e).__name__}: {e}")
    
    def test_lookup_operations():
        try:
            my_list = [1, 2, 3]
            result = my_list[10]
        except LookupError as e:
            print(f"LookupError로 잡힘: {type(e).__name__}: {e}")
        
        try:
            my_dict = {"a": 1, "b": 2}
            result = my_dict["c"]
        except LookupError as e:
            print(f"LookupError로 잡힘: {type(e).__name__}: {e}")
    
    def test_os_operations():
        try:
            with open("nonexistent_file.txt", "r") as f:
                content = f.read()
        except OSError as e:
            print(f"OSError로 잡힘: {type(e).__name__}: {e}")
    
    test_arithmetic_operations()
    test_lookup_operations()
    test_os_operations()

def demonstrate_exception_specificity():
    """예외 처리의 구체성"""
    print("\n=== 예외 처리의 구체성 ===")
    
    def handle_exceptions_specifically():
        try:
            # 여러 종류의 예외가 발생할 수 있는 코드
            data = {"numbers": [1, 2, 3]}
            result = data["numbers"][10] / 0
        except KeyError as e:
            print(f"KeyError 처리: {e}")
        except IndexError as e:
            print(f"IndexError 처리: {e}")
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError 처리: {e}")
        except Exception as e:
            print(f"일반 Exception 처리: {type(e).__name__}: {e}")
    
    def handle_exceptions_generally():
        try:
            # 여러 종류의 예외가 발생할 수 있는 코드
            data = {"numbers": [1, 2, 3]}
            result = data["numbers"][10] / 0
        except Exception as e:
            print(f"일반 Exception 처리: {type(e).__name__}: {e}")
    
    print("구체적인 예외 처리:")
    handle_exceptions_specifically()
    
    print("\n일반적인 예외 처리:")
    handle_exceptions_generally()

def demonstrate_custom_exception_hierarchy():
    """커스텀 예외 계층 구조"""
    print("\n=== 커스텀 예외 계층 구조 ===")
    
    # 기본 커스텀 예외
    class CustomError(Exception):
        """기본 커스텀 예외"""
        pass
    
    # 구체적인 커스텀 예외들
    class ValidationError(CustomError):
        """검증 오류"""
        def __init__(self, message, field=None):
            super().__init__(message)
            self.field = field
    
    class DatabaseError(CustomError):
        """데이터베이스 오류"""
        def __init__(self, message, query=None):
            super().__init__(message)
            self.query = query
    
    class ConnectionError(DatabaseError):
        """연결 오류"""
        pass
    
    class QueryError(DatabaseError):
        """쿼리 오류"""
        pass
    
    # 예외 사용 예제
    def validate_user_data(data):
        if not data.get("name"):
            raise ValidationError("이름은 필수입니다", field="name")
        if not data.get("email"):
            raise ValidationError("이메일은 필수입니다", field="email")
        return True
    
    def connect_to_database():
        # 연결 실패 시뮬레이션
        raise ConnectionError("데이터베이스 연결에 실패했습니다")
    
    def execute_query():
        # 쿼리 오류 시뮬레이션
        raise QueryError("잘못된 SQL 쿼리입니다", query="SELECT * FROM invalid_table")
    
    # 예외 처리 테스트
    try:
        validate_user_data({"name": "김철수"})  # 이메일 누락
    except ValidationError as e:
        print(f"ValidationError: {e} (필드: {e.field})")
    
    try:
        connect_to_database()
    except ConnectionError as e:
        print(f"ConnectionError: {e}")
    except DatabaseError as e:
        print(f"DatabaseError: {e}")
    
    try:
        execute_query()
    except QueryError as e:
        print(f"QueryError: {e} (쿼리: {e.query})")
    except DatabaseError as e:
        print(f"DatabaseError: {e}")

def demonstrate_exception_chaining():
    """예외 체이닝"""
    print("\n=== 예외 체이닝 ===")
    
    def low_level_function():
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            # 새로운 예외를 발생시키면서 원래 예외를 체이닝
            raise ValueError("계산 중 오류가 발생했습니다") from e
    
    def middle_level_function():
        try:
            low_level_function()
        except ValueError as e:
            # 또 다른 예외로 체이닝
            raise RuntimeError("중간 레벨에서 오류 처리 중 문제가 발생했습니다") from e
    
    def high_level_function():
        try:
            middle_level_function()
        except RuntimeError as e:
            print(f"최상위 예외: {e}")
            print(f"원인: {e.__cause__}")
            print(f"원인의 원인: {e.__cause__.__cause__}")
    
    high_level_function()

def demonstrate_exception_context():
    """예외 컨텍스트"""
    print("\n=== 예외 컨텍스트 ===")
    
    def function_with_context():
        try:
            # 첫 번째 예외 발생
            raise ValueError("첫 번째 오류")
        except ValueError as e:
            try:
                # 두 번째 예외 발생 (컨텍스트로 설정됨)
                raise TypeError("두 번째 오류")
            except TypeError as e2:
                print(f"현재 예외: {e2}")
                print(f"예외 컨텍스트: {e2.__context__}")
                print(f"예외 원인: {e2.__cause__}")  # None (from을 사용하지 않았으므로)
    
    function_with_context()

def demonstrate_built_in_exception_usage():
    """내장 예외 사용법"""
    print("\n=== 내장 예외 사용법 ===")
    
    # ValueError - 잘못된 값
    def validate_age(age):
        if not isinstance(age, int):
            raise TypeError("나이는 정수여야 합니다")
        if age < 0 or age > 150:
            raise ValueError(f"나이는 0-150 사이여야 합니다: {age}")
        return age
    
    # TypeError - 잘못된 타입
    def add_numbers(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("숫자만 더할 수 있습니다")
        return a + b
    
    # KeyError - 딕셔너리 키 없음
    def get_user_info(users, user_id):
        if user_id not in users:
            raise KeyError(f"사용자 ID {user_id}를 찾을 수 없습니다")
        return users[user_id]
    
    # IndexError - 리스트 인덱스 범위 초과
    def get_list_item(lst, index):
        if index < 0 or index >= len(lst):
            raise IndexError(f"인덱스 {index}는 범위를 벗어났습니다 (0-{len(lst)-1})")
        return lst[index]
    
    # 테스트
    try:
        validate_age(-5)
    except (TypeError, ValueError) as e:
        print(f"나이 검증 오류: {e}")
    
    try:
        add_numbers("10", 20)
    except TypeError as e:
        print(f"타입 오류: {e}")
    
    try:
        users = {"user1": "김철수", "user2": "이영희"}
        get_user_info(users, "user3")
    except KeyError as e:
        print(f"키 오류: {e}")
    
    try:
        my_list = [1, 2, 3, 4, 5]
        get_list_item(my_list, 10)
    except IndexError as e:
        print(f"인덱스 오류: {e}")

if __name__ == "__main__":
    demonstrate_exception_hierarchy()
    demonstrate_exception_inheritance()
    demonstrate_catching_parent_exceptions()
    demonstrate_exception_specificity()
    demonstrate_custom_exception_hierarchy()
    demonstrate_exception_chaining()
    demonstrate_exception_context()
    demonstrate_built_in_exception_usage()
