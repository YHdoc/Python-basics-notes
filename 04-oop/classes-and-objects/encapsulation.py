# 캡슐화와 정보 은닉

class BankAccount:
    """은행 계좌 클래스 - 캡슐화 예제"""
    
    def __init__(self, account_holder, initial_balance=0):
        """생성자"""
        # 공개 속성
        self.account_holder = account_holder
        
        # 비공개 속성 (이중 언더스코어)
        self.__balance = initial_balance
        self.__account_number = self._generate_account_number()
        self.__transactions = []
    
    def _generate_account_number(self):
        """보호된 메서드 (단일 언더스코어)"""
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    def deposit(self, amount):
        """입금 - 공개 메서드"""
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"입금: +{amount}")
            print(f"{amount}원 입금 완료. 잔액: {self.__balance}원")
        else:
            print("입금액은 0보다 커야 합니다.")
    
    def withdraw(self, amount):
        """출금 - 공개 메서드"""
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                self.__transactions.append(f"출금: -{amount}")
                print(f"{amount}원 출금 완료. 잔액: {self.__balance}원")
            else:
                print("잔액이 부족합니다.")
        else:
            print("출금액은 0보다 커야 합니다.")
    
    def get_balance(self):
        """잔액 조회 - 공개 메서드"""
        return self.__balance
    
    def get_account_number(self):
        """계좌번호 조회 - 공개 메서드"""
        return self.__account_number
    
    def get_transactions(self):
        """거래 내역 조회 - 공개 메서드"""
        return self.__transactions.copy()  # 복사본 반환
    
    def __validate_pin(self, pin):
        """비공개 메서드 (이중 언더스코어)"""
        # 실제로는 암호화된 PIN과 비교
        return len(pin) == 4 and pin.isdigit()

def demonstrate_basic_encapsulation():
    """기본 캡슐화 예제"""
    print("=== 기본 캡슐화 ===")
    
    # 계좌 생성
    account = BankAccount("김철수", 10000)
    
    # 공개 메서드 사용
    print(f"계좌번호: {account.get_account_number()}")
    print(f"잔액: {account.get_balance()}원")
    
    # 거래 수행
    account.deposit(5000)
    account.withdraw(2000)
    
    # 거래 내역 조회
    transactions = account.get_transactions()
    print(f"거래 내역: {transactions}")
    
    # 비공개 속성에 직접 접근 시도 (에러 발생)
    try:
        print(f"비공개 잔액: {account.__balance}")
    except AttributeError as e:
        print(f"비공개 속성 접근 오류: {e}")
    
    # 비공개 메서드 호출 시도 (에러 발생)
    try:
        account.__validate_pin("1234")
    except AttributeError as e:
        print(f"비공개 메서드 호출 오류: {e}")

class Student:
    """학생 클래스 - 속성 접근 제어 예제"""
    
    def __init__(self, name, age, student_id):
        """생성자"""
        self.name = name
        self._age = age  # 보호된 속성
        self.__student_id = student_id  # 비공개 속성
        self.__grades = {}  # 비공개 속성
    
    def get_age(self):
        """나이 조회"""
        return self._age
    
    def set_age(self, age):
        """나이 설정 (검증 포함)"""
        if 0 <= age <= 150:
            self._age = age
            print(f"나이가 {age}세로 변경되었습니다.")
        else:
            print("유효하지 않은 나이입니다.")
    
    def add_grade(self, subject, grade):
        """성적 추가"""
        if 0 <= grade <= 100:
            self.__grades[subject] = grade
            print(f"{subject} 과목에 {grade}점이 추가되었습니다.")
        else:
            print("성적은 0-100 사이여야 합니다.")
    
    def get_grade(self, subject):
        """성적 조회"""
        return self.__grades.get(subject, "성적 없음")
    
    def get_all_grades(self):
        """모든 성적 조회"""
        return self.__grades.copy()
    
    def get_average_grade(self):
        """평균 성적 계산"""
        if self.__grades:
            return sum(self.__grades.values()) / len(self.__grades)
        return 0
    
    def get_student_id(self):
        """학번 조회"""
        return self.__student_id

def demonstrate_property_encapsulation():
    """속성 접근 제어 예제"""
    print("\n=== 속성 접근 제어 ===")
    
    # 학생 생성
    student = Student("이영희", 20, "2023001")
    
    # 공개 속성 접근
    print(f"이름: {student.name}")
    
    # 보호된 속성 접근 (가능하지만 권장하지 않음)
    print(f"나이 (직접 접근): {student._age}")
    
    # 메서드를 통한 안전한 접근
    print(f"나이 (메서드): {student.get_age()}")
    
    # 나이 변경
    student.set_age(21)
    student.set_age(-5)  # 유효하지 않은 나이
    
    # 성적 추가
    student.add_grade("수학", 85)
    student.add_grade("영어", 92)
    student.add_grade("과학", 78)
    
    # 성적 조회
    print(f"수학 성적: {student.get_grade('수학')}")
    print(f"모든 성적: {student.get_all_grades()}")
    print(f"평균 성적: {student.get_average_grade():.1f}")

class Temperature:
    """온도 클래스 - @property 데코레이터 예제"""
    
    def __init__(self, celsius=0):
        """생성자"""
        self._celsius = celsius
    
    @property
    def celsius(self):
        """섭씨 온도 (읽기 전용)"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """섭씨 온도 설정"""
        if value < -273.15:
            raise ValueError("절대 영도(-273.15°C)보다 낮을 수 없습니다.")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """화씨 온도 (읽기 전용)"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """화씨 온도 설정"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """켈빈 온도 (읽기 전용)"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """켈빈 온도 설정"""
        if value < 0:
            raise ValueError("켈빈 온도는 0보다 작을 수 없습니다.")
        self.celsius = value - 273.15

def demonstrate_property_decorator():
    """@property 데코레이터 예제"""
    print("\n=== @property 데코레이터 ===")
    
    # 온도 객체 생성
    temp = Temperature(25)
    
    # 섭씨 온도
    print(f"섭씨: {temp.celsius}°C")
    temp.celsius = 30
    print(f"섭씨 변경 후: {temp.celsius}°C")
    
    # 화씨 온도
    print(f"화씨: {temp.fahrenheit}°F")
    temp.fahrenheit = 86
    print(f"화씨 변경 후: {temp.fahrenheit}°F, 섭씨: {temp.celsius}°C")
    
    # 켈빈 온도
    print(f"켈빈: {temp.kelvin}K")
    temp.kelvin = 300
    print(f"켈빈 변경 후: {temp.kelvin}K, 섭씨: {temp.celsius}°C")
    
    # 유효하지 않은 값 설정 시도
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"오류: {e}")

class Rectangle:
    """사각형 클래스 - 캡슐화와 검증 예제"""
    
    def __init__(self, width, height):
        """생성자"""
        self._width = 0
        self._height = 0
        self.width = width  # setter 호출
        self.height = height  # setter 호출
    
    @property
    def width(self):
        """너비 조회"""
        return self._width
    
    @width.setter
    def width(self, value):
        """너비 설정"""
        if value <= 0:
            raise ValueError("너비는 0보다 커야 합니다.")
        self._width = value
    
    @property
    def height(self):
        """높이 조회"""
        return self._height
    
    @height.setter
    def height(self, value):
        """높이 설정"""
        if value <= 0:
            raise ValueError("높이는 0보다 커야 합니다.")
        self._height = value
    
    @property
    def area(self):
        """면적 (읽기 전용)"""
        return self._width * self._height
    
    @property
    def perimeter(self):
        """둘레 (읽기 전용)"""
        return 2 * (self._width + self._height)
    
    def __str__(self):
        """문자열 표현"""
        return f"Rectangle({self._width} x {self._height})"

def demonstrate_rectangle_example():
    """사각형 예제"""
    print("\n=== 사각형 예제 ===")
    
    # 사각형 생성
    rect = Rectangle(5, 3)
    print(f"사각형: {rect}")
    print(f"면적: {rect.area}")
    print(f"둘레: {rect.perimeter}")
    
    # 크기 변경
    rect.width = 8
    rect.height = 4
    print(f"변경 후: {rect}")
    print(f"면적: {rect.area}")
    print(f"둘레: {rect.perimeter}")
    
    # 유효하지 않은 값 설정 시도
    try:
        rect.width = -5
    except ValueError as e:
        print(f"오류: {e}")

class SecureData:
    """보안 데이터 클래스 - 강력한 캡슐화 예제"""
    
    def __init__(self, data, password):
        """생성자"""
        self.__data = data
        self.__password = password
        self.__access_count = 0
    
    def get_data(self, password):
        """데이터 조회 (비밀번호 필요)"""
        if password == self.__password:
            self.__access_count += 1
            return self.__data
        else:
            raise ValueError("잘못된 비밀번호입니다.")
    
    def set_data(self, new_data, password):
        """데이터 설정 (비밀번호 필요)"""
        if password == self.__password:
            self.__data = new_data
            self.__access_count += 1
            print("데이터가 업데이트되었습니다.")
        else:
            raise ValueError("잘못된 비밀번호입니다.")
    
    def change_password(self, old_password, new_password):
        """비밀번호 변경"""
        if old_password == self.__password:
            self.__password = new_password
            print("비밀번호가 변경되었습니다.")
        else:
            raise ValueError("기존 비밀번호가 올바르지 않습니다.")
    
    def get_access_count(self, password):
        """접근 횟수 조회"""
        if password == self.__password:
            return self.__access_count
        else:
            raise ValueError("잘못된 비밀번호입니다.")

def demonstrate_secure_data_example():
    """보안 데이터 예제"""
    print("\n=== 보안 데이터 예제 ===")
    
    # 보안 데이터 생성
    secure = SecureData("비밀 정보", "1234")
    
    # 올바른 비밀번호로 데이터 접근
    try:
        data = secure.get_data("1234")
        print(f"데이터: {data}")
        print(f"접근 횟수: {secure.get_access_count('1234')}")
    except ValueError as e:
        print(f"오류: {e}")
    
    # 잘못된 비밀번호로 데이터 접근
    try:
        data = secure.get_data("5678")
    except ValueError as e:
        print(f"오류: {e}")
    
    # 데이터 업데이트
    try:
        secure.set_data("업데이트된 정보", "1234")
        print(f"업데이트 후 데이터: {secure.get_data('1234')}")
        print(f"접근 횟수: {secure.get_access_count('1234')}")
    except ValueError as e:
        print(f"오류: {e}")
    
    # 비밀번호 변경
    try:
        secure.change_password("1234", "5678")
        secure.get_data("5678")
        print("비밀번호 변경 후 데이터 접근 성공")
    except ValueError as e:
        print(f"오류: {e}")

if __name__ == "__main__":
    demonstrate_basic_encapsulation()
    demonstrate_property_encapsulation()
    demonstrate_property_decorator()
    demonstrate_rectangle_example()
    demonstrate_secure_data_example()
