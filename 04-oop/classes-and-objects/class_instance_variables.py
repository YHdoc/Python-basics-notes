# 클래스 변수와 인스턴스 변수

class Student:
    """학생 클래스 - 클래스 변수와 인스턴스 변수 예제"""
    
    # 클래스 변수 (모든 인스턴스가 공유)
    school_name = "Python 고등학교"
    total_students = 0
    
    def __init__(self, name, student_id, grade):
        """생성자 - 인스턴스 변수 초기화"""
        # 인스턴스 변수 (각 인스턴스마다 독립적)
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.subjects = []
        
        # 클래스 변수 수정
        Student.total_students += 1
    
    def add_subject(self, subject):
        """과목 추가"""
        self.subjects.append(subject)
    
    def get_info(self):
        """학생 정보 반환"""
        return f"이름: {self.name}, 학번: {self.student_id}, 학년: {self.grade}, 과목: {self.subjects}"
    
    @classmethod
    def get_school_info(cls):
        """클래스 메서드 - 클래스 변수 접근"""
        return f"학교: {cls.school_name}, 총 학생 수: {cls.total_students}"
    
    @classmethod
    def change_school_name(cls, new_name):
        """클래스 메서드 - 클래스 변수 수정"""
        cls.school_name = new_name
        print(f"학교명이 '{new_name}'으로 변경되었습니다")

def demonstrate_basic_class_instance_variables():
    """기본 클래스 변수와 인스턴스 변수 예제"""
    print("=== 기본 클래스 변수와 인스턴스 변수 ===")
    
    # 학생 객체 생성
    student1 = Student("김철수", "2023001", 1)
    student2 = Student("이영희", "2023002", 2)
    student3 = Student("박민수", "2023003", 1)
    
    # 인스턴스 변수 사용
    student1.add_subject("수학")
    student1.add_subject("영어")
    student2.add_subject("과학")
    
    print("학생 정보:")
    print(student1.get_info())
    print(student2.get_info())
    print(student3.get_info())
    
    # 클래스 변수 접근
    print(f"\n클래스 변수 접근:")
    print(f"학교명: {Student.school_name}")
    print(f"총 학생 수: {Student.total_students}")
    
    # 클래스 메서드 사용
    print(f"\n클래스 메서드:")
    print(Student.get_school_info())

class BankAccount:
    """은행 계좌 클래스 - 클래스 변수 활용 예제"""
    
    # 클래스 변수
    bank_name = "Python Bank"
    interest_rate = 0.02  # 2% 이자율
    total_accounts = 0
    
    def __init__(self, account_holder, initial_balance=0):
        """생성자"""
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = f"ACC{BankAccount.total_accounts + 1:06d}"
        
        # 클래스 변수 증가
        BankAccount.total_accounts += 1
    
    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.balance += amount
            print(f"{self.account_holder}님 {amount}원 입금. 잔액: {self.balance}원")
    
    def withdraw(self, amount):
        """출금"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder}님 {amount}원 출금. 잔액: {self.balance}원")
        else:
            print("출금할 수 없습니다.")
    
    def add_interest(self):
        """이자 추가"""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"{self.account_holder}님 이자 {interest:.2f}원 추가. 잔액: {self.balance}원")
    
    @classmethod
    def change_interest_rate(cls, new_rate):
        """이자율 변경"""
        cls.interest_rate = new_rate
        print(f"이자율이 {new_rate:.1%}로 변경되었습니다")
    
    @classmethod
    def get_bank_info(cls):
        """은행 정보"""
        return f"{cls.bank_name} - 총 계좌 수: {cls.total_accounts}, 이자율: {cls.interest_rate:.1%}"

def demonstrate_bank_account_example():
    """은행 계좌 예제"""
    print("\n=== 은행 계좌 예제 ===")
    
    # 계좌 생성
    account1 = BankAccount("김철수", 10000)
    account2 = BankAccount("이영희", 50000)
    account3 = BankAccount("박민수", 0)
    
    print(f"계좌 정보:")
    print(f"계좌1: {account1.account_number} - {account1.account_holder}")
    print(f"계좌2: {account2.account_number} - {account2.account_holder}")
    print(f"계좌3: {account3.account_number} - {account3.account_holder}")
    
    # 거래 수행
    account1.deposit(5000)
    account2.withdraw(10000)
    account3.deposit(20000)
    
    # 이자 추가
    print(f"\n이자 추가:")
    account1.add_interest()
    account2.add_interest()
    account3.add_interest()
    
    # 은행 정보
    print(f"\n{BankAccount.get_bank_info()}")
    
    # 이자율 변경
    BankAccount.change_interest_rate(0.03)
    print(f"변경 후: {BankAccount.get_bank_info()}")

class Counter:
    """카운터 클래스 - 클래스 변수와 인스턴스 변수 구분"""
    
    # 클래스 변수
    total_count = 0
    instance_count = 0
    
    def __init__(self, name):
        """생성자"""
        self.name = name
        self.count = 0  # 인스턴스 변수
        Counter.instance_count += 1
    
    def increment(self):
        """카운트 증가"""
        self.count += 1
        Counter.total_count += 1
        print(f"{self.name}: {self.count} (총: {Counter.total_count})")
    
    def decrement(self):
        """카운트 감소"""
        if self.count > 0:
            self.count -= 1
            Counter.total_count -= 1
            print(f"{self.name}: {self.count} (총: {Counter.total_count})")
    
    @classmethod
    def get_total_count(cls):
        """총 카운트 반환"""
        return cls.total_count
    
    @classmethod
    def get_instance_count(cls):
        """인스턴스 수 반환"""
        return cls.instance_count

def demonstrate_counter_example():
    """카운터 예제"""
    print("\n=== 카운터 예제 ===")
    
    # 카운터 생성
    counter1 = Counter("카운터1")
    counter2 = Counter("카운터2")
    counter3 = Counter("카운터3")
    
    print(f"총 인스턴스 수: {Counter.get_instance_count()}")
    
    # 카운트 증가
    counter1.increment()
    counter1.increment()
    counter2.increment()
    counter3.increment()
    counter3.increment()
    counter3.increment()
    
    print(f"총 카운트: {Counter.get_total_count()}")
    
    # 카운트 감소
    counter1.decrement()
    counter3.decrement()
    
    print(f"최종 총 카운트: {Counter.get_total_count()}")

class Configuration:
    """설정 클래스 - 클래스 변수로 설정 관리"""
    
    # 클래스 변수로 설정 저장
    database_url = "localhost:5432"
    debug_mode = False
    max_connections = 100
    timeout = 30
    
    def __init__(self, app_name):
        """생성자"""
        self.app_name = app_name
        self.local_settings = {}  # 인스턴스 변수
    
    def set_local_setting(self, key, value):
        """로컬 설정 추가"""
        self.local_settings[key] = value
    
    def get_setting(self, key):
        """설정 값 가져오기"""
        # 먼저 로컬 설정 확인
        if key in self.local_settings:
            return self.local_settings[key]
        
        # 클래스 변수에서 확인
        if hasattr(Configuration, key):
            return getattr(Configuration, key)
        
        return None
    
    @classmethod
    def update_global_setting(cls, key, value):
        """전역 설정 업데이트"""
        setattr(cls, key, value)
        print(f"전역 설정 업데이트: {key} = {value}")
    
    @classmethod
    def get_all_settings(cls):
        """모든 설정 반환"""
        settings = {}
        for attr in dir(cls):
            if not attr.startswith('_') and not callable(getattr(cls, attr)):
                settings[attr] = getattr(cls, attr)
        return settings

def demonstrate_configuration_example():
    """설정 관리 예제"""
    print("\n=== 설정 관리 예제 ===")
    
    # 설정 객체 생성
    config1 = Configuration("앱1")
    config2 = Configuration("앱2")
    
    # 로컬 설정 추가
    config1.set_local_setting("cache_size", 1000)
    config2.set_local_setting("cache_size", 2000)
    
    # 설정 값 가져오기
    print(f"앱1 데이터베이스 URL: {config1.get_setting('database_url')}")
    print(f"앱1 캐시 크기: {config1.get_setting('cache_size')}")
    print(f"앱2 캐시 크기: {config2.get_setting('cache_size')}")
    
    # 전역 설정 업데이트
    Configuration.update_global_setting("debug_mode", True)
    Configuration.update_global_setting("max_connections", 200)
    
    print(f"앱1 디버그 모드: {config1.get_setting('debug_mode')}")
    print(f"앱2 최대 연결 수: {config2.get_setting('max_connections')}")
    
    # 모든 설정 출력
    print(f"\n모든 전역 설정:")
    for key, value in Configuration.get_all_settings().items():
        print(f"  {key}: {value}")

class Singleton:
    """싱글톤 패턴 - 클래스 변수 활용"""
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        """객체 생성 제어"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """생성자 - 한 번만 초기화"""
        if not Singleton._initialized:
            self.data = {}
            Singleton._initialized = True
    
    def set_data(self, key, value):
        """데이터 설정"""
        self.data[key] = value
    
    def get_data(self, key):
        """데이터 가져오기"""
        return self.data.get(key)

def demonstrate_singleton_example():
    """싱글톤 예제"""
    print("\n=== 싱글톤 예제 ===")
    
    # 여러 번 생성해도 같은 인스턴스
    s1 = Singleton()
    s2 = Singleton()
    s3 = Singleton()
    
    print(f"s1 is s2: {s1 is s2}")
    print(f"s2 is s3: {s2 is s3}")
    
    # 데이터 설정
    s1.set_data("name", "싱글톤")
    s2.set_data("value", 42)
    
    # 데이터 가져오기
    print(f"이름: {s3.get_data('name')}")
    print(f"값: {s3.get_data('value')}")

if __name__ == "__main__":
    demonstrate_basic_class_instance_variables()
    demonstrate_bank_account_example()
    demonstrate_counter_example()
    demonstrate_configuration_example()
    demonstrate_singleton_example()
