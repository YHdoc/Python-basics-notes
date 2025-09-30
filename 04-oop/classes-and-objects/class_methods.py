# 클래스 메서드와 정적 메서드

class Date:
    """날짜 클래스 - 클래스 메서드와 정적 메서드 예제"""
    
    def __init__(self, year, month, day):
        """생성자"""
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        """문자열 표현"""
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    @classmethod
    def from_string(cls, date_string):
        """문자열로부터 날짜 객체 생성 (클래스 메서드)"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """오늘 날짜 객체 생성 (클래스 메서드)"""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)
    
    @classmethod
    def from_timestamp(cls, timestamp):
        """타임스탬프로부터 날짜 객체 생성 (클래스 메서드)"""
        import datetime
        dt = datetime.datetime.fromtimestamp(timestamp)
        return cls(dt.year, dt.month, dt.day)
    
    @staticmethod
    def is_leap_year(year):
        """윤년 확인 (정적 메서드)"""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    @staticmethod
    def days_in_month(year, month):
        """해당 월의 일수 (정적 메서드)"""
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if Date.is_leap_year(year) else 28
        else:
            return 0
    
    @staticmethod
    def is_valid_date(year, month, day):
        """유효한 날짜인지 확인 (정적 메서드)"""
        if month < 1 or month > 12:
            return False
        if day < 1 or day > Date.days_in_month(year, month):
            return False
        return True

def demonstrate_date_example():
    """날짜 클래스 예제"""
    print("=== 날짜 클래스 예제 ===")
    
    # 일반 생성자 사용
    date1 = Date(2023, 12, 25)
    print(f"일반 생성: {date1}")
    
    # 클래스 메서드 사용
    date2 = Date.from_string("2023-12-25")
    print(f"문자열로 생성: {date2}")
    
    date3 = Date.today()
    print(f"오늘 날짜: {date3}")
    
    # 정적 메서드 사용
    print(f"2024년은 윤년: {Date.is_leap_year(2024)}")
    print(f"2023년은 윤년: {Date.is_leap_year(2023)}")
    print(f"2023년 2월 일수: {Date.days_in_month(2023, 2)}")
    print(f"2024년 2월 일수: {Date.days_in_month(2024, 2)}")
    print(f"2023-12-25 유효한 날짜: {Date.is_valid_date(2023, 12, 25)}")
    print(f"2023-02-29 유효한 날짜: {Date.is_valid_date(2023, 2, 29)}")

class MathUtils:
    """수학 유틸리티 클래스 - 정적 메서드 예제"""
    
    @staticmethod
    def add(a, b):
        """덧셈"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """뺄셈"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """곱셈"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """나눗셈"""
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return a / b
    
    @staticmethod
    def power(base, exponent):
        """거듭제곱"""
        return base ** exponent
    
    @staticmethod
    def factorial(n):
        """팩토리얼"""
        if n < 0:
            raise ValueError("음수의 팩토리얼은 정의되지 않습니다.")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def is_prime(n):
        """소수 확인"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def demonstrate_math_utils_example():
    """수학 유틸리티 예제"""
    print("\n=== 수학 유틸리티 예제 ===")
    
    # 정적 메서드 사용
    print(f"10 + 5 = {MathUtils.add(10, 5)}")
    print(f"10 - 5 = {MathUtils.subtract(10, 5)}")
    print(f"10 * 5 = {MathUtils.multiply(10, 5)}")
    print(f"10 / 5 = {MathUtils.divide(10, 5)}")
    print(f"2^8 = {MathUtils.power(2, 8)}")
    print(f"5! = {MathUtils.factorial(5)}")
    
    # 소수 확인
    numbers = [2, 3, 4, 5, 17, 25, 29]
    for num in numbers:
        print(f"{num}은 소수: {MathUtils.is_prime(num)}")

class DatabaseConnection:
    """데이터베이스 연결 클래스 - 클래스 메서드 예제"""
    
    _instance = None
    _connection_count = 0
    
    def __init__(self, host, port, database):
        """생성자"""
        self.host = host
        self.port = port
        self.database = database
        self.connected = False
        DatabaseConnection._connection_count += 1
    
    @classmethod
    def create_connection(cls, host, port, database):
        """연결 생성 (클래스 메서드)"""
        return cls(host, port, database)
    
    @classmethod
    def create_local_connection(cls, database):
        """로컬 연결 생성 (클래스 메서드)"""
        return cls("localhost", 5432, database)
    
    @classmethod
    def create_production_connection(cls):
        """프로덕션 연결 생성 (클래스 메서드)"""
        return cls("prod-db.example.com", 5432, "production")
    
    @classmethod
    def get_connection_count(cls):
        """연결 수 조회 (클래스 메서드)"""
        return cls._connection_count
    
    @classmethod
    def reset_connection_count(cls):
        """연결 수 초기화 (클래스 메서드)"""
        cls._connection_count = 0
    
    def connect(self):
        """연결"""
        self.connected = True
        print(f"데이터베이스 연결: {self.host}:{self.port}/{self.database}")
    
    def disconnect(self):
        """연결 해제"""
        self.connected = False
        print(f"데이터베이스 연결 해제: {self.host}:{self.port}/{self.database}")

def demonstrate_database_connection_example():
    """데이터베이스 연결 예제"""
    print("\n=== 데이터베이스 연결 예제 ===")
    
    # 클래스 메서드로 연결 생성
    conn1 = DatabaseConnection.create_connection("db1.example.com", 5432, "testdb")
    conn2 = DatabaseConnection.create_local_connection("localdb")
    conn3 = DatabaseConnection.create_production_connection()
    
    # 연결
    conn1.connect()
    conn2.connect()
    conn3.connect()
    
    # 연결 수 확인
    print(f"총 연결 수: {DatabaseConnection.get_connection_count()}")
    
    # 연결 해제
    conn1.disconnect()
    conn2.disconnect()
    conn3.disconnect()

class StringUtils:
    """문자열 유틸리티 클래스 - 정적 메서드 예제"""
    
    @staticmethod
    def is_palindrome(text):
        """회문 확인"""
        text = text.lower().replace(" ", "")
        return text == text[::-1]
    
    @staticmethod
    def reverse_string(text):
        """문자열 뒤집기"""
        return text[::-1]
    
    @staticmethod
    def count_words(text):
        """단어 수 세기"""
        return len(text.split())
    
    @staticmethod
    def remove_duplicates(text):
        """중복 문자 제거"""
        seen = set()
        result = []
        for char in text:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)
    
    @staticmethod
    def is_valid_email(email):
        """이메일 유효성 검사"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def format_phone_number(phone):
        """전화번호 포맷팅"""
        # 숫자만 추출
        digits = ''.join(filter(str.isdigit, phone))
        
        if len(digits) == 10:
            return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
        elif len(digits) == 11:
            return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
        else:
            return phone

def demonstrate_string_utils_example():
    """문자열 유틸리티 예제"""
    print("\n=== 문자열 유틸리티 예제 ===")
    
    # 회문 확인
    texts = ["level", "hello", "A man a plan a canal Panama", "racecar"]
    for text in texts:
        print(f"'{text}'는 회문: {StringUtils.is_palindrome(text)}")
    
    # 문자열 뒤집기
    text = "Hello World"
    print(f"'{text}' 뒤집기: {StringUtils.reverse_string(text)}")
    
    # 단어 수 세기
    text = "Python is a great programming language"
    print(f"'{text}' 단어 수: {StringUtils.count_words(text)}")
    
    # 중복 문자 제거
    text = "programming"
    print(f"'{text}' 중복 제거: {StringUtils.remove_duplicates(text)}")
    
    # 이메일 유효성 검사
    emails = ["user@example.com", "invalid-email", "test@domain.co.kr"]
    for email in emails:
        print(f"'{email}' 유효한 이메일: {StringUtils.is_valid_email(email)}")
    
    # 전화번호 포맷팅
    phones = ["01012345678", "02-1234-5678", "031-123-4567"]
    for phone in phones:
        print(f"'{phone}' 포맷팅: {StringUtils.format_phone_number(phone)}")

class Configuration:
    """설정 클래스 - 클래스 메서드와 정적 메서드 조합 예제"""
    
    _config = {}
    
    @classmethod
    def load_from_file(cls, filename):
        """파일로부터 설정 로드 (클래스 메서드)"""
        try:
            with open(filename, 'r') as f:
                content = f.read()
                # 간단한 설정 파일 파싱 (실제로는 JSON이나 YAML 사용)
                for line in content.split('\n'):
                    if '=' in line and not line.strip().startswith('#'):
                        key, value = line.split('=', 1)
                        cls._config[key.strip()] = value.strip()
            return cls()
        except FileNotFoundError:
            print(f"설정 파일을 찾을 수 없습니다: {filename}")
            return cls()
    
    @classmethod
    def load_from_dict(cls, config_dict):
        """딕셔너리로부터 설정 로드 (클래스 메서드)"""
        cls._config.update(config_dict)
        return cls()
    
    @classmethod
    def get_config(cls):
        """설정 조회 (클래스 메서드)"""
        return cls._config.copy()
    
    @classmethod
    def set_config(cls, key, value):
        """설정 설정 (클래스 메서드)"""
        cls._config[key] = value
    
    @staticmethod
    def validate_config(config):
        """설정 유효성 검사 (정적 메서드)"""
        required_keys = ['host', 'port', 'database']
        missing_keys = [key for key in required_keys if key not in config]
        if missing_keys:
            return False, f"누락된 설정: {missing_keys}"
        return True, "설정이 유효합니다"
    
    @staticmethod
    def merge_configs(config1, config2):
        """설정 병합 (정적 메서드)"""
        merged = config1.copy()
        merged.update(config2)
        return merged

def demonstrate_configuration_example():
    """설정 클래스 예제"""
    print("\n=== 설정 클래스 예제 ===")
    
    # 딕셔너리로부터 설정 로드
    config_data = {
        'host': 'localhost',
        'port': '5432',
        'database': 'mydb',
        'username': 'admin'
    }
    
    config = Configuration.load_from_dict(config_data)
    
    # 설정 조회
    print(f"현재 설정: {Configuration.get_config()}")
    
    # 설정 추가
    Configuration.set_config('password', 'secret123')
    print(f"설정 추가 후: {Configuration.get_config()}")
    
    # 설정 유효성 검사
    is_valid, message = Configuration.validate_config(Configuration.get_config())
    print(f"설정 유효성: {is_valid}, 메시지: {message}")
    
    # 설정 병합
    additional_config = {'timeout': '30', 'debug': 'true'}
    merged = Configuration.merge_configs(Configuration.get_config(), additional_config)
    print(f"병합된 설정: {merged}")

if __name__ == "__main__":
    demonstrate_date_example()
    demonstrate_math_utils_example()
    demonstrate_database_connection_example()
    demonstrate_string_utils_example()
    demonstrate_configuration_example()
