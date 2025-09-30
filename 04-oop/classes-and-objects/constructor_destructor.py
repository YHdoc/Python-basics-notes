# 생성자와 소멸자

class Person:
    """사람 클래스 - 생성자와 소멸자 예제"""
    
    def __init__(self, name, age):
        """생성자 (Constructor)"""
        print(f"Person 객체 생성 중: {name}")
        self.name = name
        self.age = age
        self.created_at = __import__('datetime').datetime.now()
    
    def __del__(self):
        """소멸자 (Destructor)"""
        print(f"Person 객체 소멸: {self.name}")
    
    def introduce(self):
        """자기소개"""
        return f"안녕하세요, 저는 {self.name}이고 {self.age}세입니다."

def demonstrate_basic_constructor_destructor():
    """기본 생성자와 소멸자 예제"""
    print("=== 기본 생성자와 소멸자 ===")
    
    # 객체 생성 (생성자 호출)
    person1 = Person("김철수", 30)
    person2 = Person("이영희", 25)
    
    # 객체 사용
    print(person1.introduce())
    print(person2.introduce())
    
    # 객체 삭제 (소멸자 호출)
    del person1
    del person2
    
    print("함수 종료 - 남은 객체들도 자동으로 소멸됩니다.")

class BankAccount:
    """은행 계좌 클래스 - 리소스 관리 예제"""
    
    def __init__(self, account_number, initial_balance=0):
        """생성자"""
        print(f"계좌 생성: {account_number}")
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []
        self.is_open = True
    
    def __del__(self):
        """소멸자 - 리소스 정리"""
        if hasattr(self, 'is_open') and self.is_open:
            print(f"계좌 {self.account_number} 정리 중...")
            self.close_account()
    
    def deposit(self, amount):
        """입금"""
        if not self.is_open:
            raise ValueError("계좌가 닫혀있습니다")
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 합니다")
        
        self.balance += amount
        self.transactions.append(f"입금: +{amount}")
        print(f"입금 완료: {amount}원, 잔액: {self.balance}원")
    
    def withdraw(self, amount):
        """출금"""
        if not self.is_open:
            raise ValueError("계좌가 닫혀있습니다")
        if amount <= 0:
            raise ValueError("출금액은 0보다 커야 합니다")
        if amount > self.balance:
            raise ValueError("잔액이 부족합니다")
        
        self.balance -= amount
        self.transactions.append(f"출금: -{amount}")
        print(f"출금 완료: {amount}원, 잔액: {self.balance}원")
    
    def close_account(self):
        """계좌 닫기"""
        if self.is_open:
            print(f"계좌 {self.account_number}를 닫습니다. 최종 잔액: {self.balance}원")
            self.is_open = False

def demonstrate_resource_management():
    """리소스 관리 예제"""
    print("\n=== 리소스 관리 ===")
    
    # 계좌 생성
    account = BankAccount("123-456-789", 10000)
    
    # 거래 수행
    account.deposit(5000)
    account.withdraw(2000)
    
    # 계좌 삭제 (소멸자에서 자동으로 정리)
    del account

class FileHandler:
    """파일 핸들러 클래스 - 파일 리소스 관리"""
    
    def __init__(self, filename, mode='r'):
        """생성자"""
        print(f"파일 핸들러 생성: {filename}")
        self.filename = filename
        self.mode = mode
        self.file = None
        self.is_open = False
    
    def __del__(self):
        """소멸자 - 파일 닫기"""
        if self.is_open:
            print(f"파일 {self.filename} 닫는 중...")
            self.close()
    
    def open(self):
        """파일 열기"""
        if not self.is_open:
            try:
                self.file = open(self.filename, self.mode)
                self.is_open = True
                print(f"파일 {self.filename} 열기 성공")
            except FileNotFoundError:
                print(f"파일 {self.filename}을 찾을 수 없습니다")
            except Exception as e:
                print(f"파일 열기 오류: {e}")
    
    def close(self):
        """파일 닫기"""
        if self.is_open and self.file:
            self.file.close()
            self.is_open = False
            print(f"파일 {self.filename} 닫기 완료")
    
    def read(self):
        """파일 읽기"""
        if not self.is_open:
            self.open()
        
        if self.is_open:
            try:
                content = self.file.read()
                return content
            except Exception as e:
                print(f"파일 읽기 오류: {e}")
                return None
        return None

def demonstrate_file_handling():
    """파일 핸들링 예제"""
    print("\n=== 파일 핸들링 ===")
    
    # 파일 핸들러 생성
    file_handler = FileHandler("test.txt", "w")
    
    # 파일 작업
    if file_handler.open():
        file_handler.file.write("테스트 내용입니다.")
        file_handler.close()
    
    # 파일 핸들러 삭제 (소멸자에서 자동으로 정리)
    del file_handler

class DatabaseConnection:
    """데이터베이스 연결 클래스"""
    
    def __init__(self, host, port, database):
        """생성자"""
        print(f"데이터베이스 연결 생성: {host}:{port}/{database}")
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
        self.is_connected = False
    
    def __del__(self):
        """소멸자 - 연결 해제"""
        if self.is_connected:
            print(f"데이터베이스 연결 해제: {self.host}:{self.port}/{self.database}")
            self.disconnect()
    
    def connect(self):
        """데이터베이스 연결"""
        if not self.is_connected:
            # 실제로는 데이터베이스 연결 로직이 여기에 들어감
            self.connection = f"Connection to {self.host}:{self.port}/{self.database}"
            self.is_connected = True
            print(f"데이터베이스 연결 성공: {self.connection}")
    
    def disconnect(self):
        """데이터베이스 연결 해제"""
        if self.is_connected:
            self.connection = None
            self.is_connected = False
            print("데이터베이스 연결 해제 완료")
    
    def execute_query(self, query):
        """쿼리 실행"""
        if not self.is_connected:
            raise RuntimeError("데이터베이스에 연결되지 않았습니다")
        
        print(f"쿼리 실행: {query}")
        return f"Query result for: {query}"

def demonstrate_database_connection():
    """데이터베이스 연결 예제"""
    print("\n=== 데이터베이스 연결 ===")
    
    # 데이터베이스 연결 생성
    db = DatabaseConnection("localhost", 5432, "mydb")
    
    # 연결 및 쿼리 실행
    db.connect()
    result = db.execute_query("SELECT * FROM users")
    print(f"결과: {result}")
    
    # 연결 삭제 (소멸자에서 자동으로 연결 해제)
    del db

class Counter:
    """카운터 클래스 - 객체 생성/소멸 추적"""
    
    _instance_count = 0  # 클래스 변수
    
    def __init__(self, name):
        """생성자"""
        Counter._instance_count += 1
        self.name = name
        self.instance_id = Counter._instance_count
        print(f"Counter 객체 생성: {self.name} (ID: {self.instance_id})")
        print(f"총 인스턴스 수: {Counter._instance_count}")
    
    def __del__(self):
        """소멸자"""
        Counter._instance_count -= 1
        print(f"Counter 객체 소멸: {self.name} (ID: {self.instance_id})")
        print(f"남은 인스턴스 수: {Counter._instance_count}")
    
    def get_count(self):
        """현재 카운트 반환"""
        return Counter._instance_count

def demonstrate_instance_tracking():
    """인스턴스 추적 예제"""
    print("\n=== 인스턴스 추적 ===")
    
    # 여러 객체 생성
    counter1 = Counter("첫 번째")
    counter2 = Counter("두 번째")
    counter3 = Counter("세 번째")
    
    print(f"현재 총 인스턴스 수: {counter1.get_count()}")
    
    # 객체 삭제
    del counter2
    print(f"counter2 삭제 후 총 인스턴스 수: {counter1.get_count()}")
    
    # 함수 종료 시 나머지 객체들도 자동으로 소멸

class Singleton:
    """싱글톤 패턴 - 생성자 제어 예제"""
    
    _instance = None
    _initialized = False
    
    def __new__(cls, *args, **kwargs):
        """객체 생성 제어"""
        if cls._instance is None:
            print("싱글톤 인스턴스 생성")
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name):
        """생성자 - 한 번만 초기화"""
        if not Singleton._initialized:
            print(f"싱글톤 초기화: {name}")
            self.name = name
            Singleton._initialized = True
        else:
            print("싱글톤은 이미 초기화되었습니다")
    
    def __del__(self):
        """소멸자"""
        print("싱글톤 인스턴스 소멸")
        Singleton._instance = None
        Singleton._initialized = False

def demonstrate_singleton_pattern():
    """싱글톤 패턴 예제"""
    print("\n=== 싱글톤 패턴 ===")
    
    # 여러 번 생성해도 같은 인스턴스
    s1 = Singleton("첫 번째")
    s2 = Singleton("두 번째")
    s3 = Singleton("세 번째")
    
    print(f"s1 is s2: {s1 is s2}")
    print(f"s2 is s3: {s2 is s3}")
    print(f"싱글톤 이름: {s1.name}")
    
    # 삭제
    del s1, s2, s3

class LazyInitialization:
    """지연 초기화 예제"""
    
    def __init__(self):
        """생성자 - 지연 초기화"""
        print("LazyInitialization 객체 생성")
        self._data = None
        self._initialized = False
    
    def __del__(self):
        """소멸자"""
        print("LazyInitialization 객체 소멸")
        if self._initialized:
            print("리소스 정리 중...")
    
    @property
    def data(self):
        """지연 초기화된 데이터"""
        if not self._initialized:
            print("데이터 초기화 중...")
            self._data = "초기화된 데이터"
            self._initialized = True
        return self._data

def demonstrate_lazy_initialization():
    """지연 초기화 예제"""
    print("\n=== 지연 초기화 ===")
    
    # 객체 생성 (아직 초기화되지 않음)
    lazy = LazyInitialization()
    
    # 데이터 접근 시 초기화
    print(f"데이터: {lazy.data}")
    print(f"데이터: {lazy.data}")  # 두 번째 접근은 초기화되지 않음
    
    del lazy

if __name__ == "__main__":
    demonstrate_basic_constructor_destructor()
    demonstrate_resource_management()
    demonstrate_file_handling()
    demonstrate_database_connection()
    demonstrate_instance_tracking()
    demonstrate_singleton_pattern()
    demonstrate_lazy_initialization()
