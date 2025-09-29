"""
기본 클래스와 객체 예제
클래스 정의와 객체 생성 방법을 학습합니다.
"""

# TODO: 기본 클래스 정의
# class Person:
#     """사람을 나타내는 클래스"""
#     
#     def __init__(self, name, age):
#         """생성자 - 객체 초기화"""
#         self.name = name
#         self.age = age
#     
#     def introduce(self):
#         """자기소개 메서드"""
#         return f"안녕하세요, 저는 {self.name}이고 {self.age}살입니다."
#     
#     def have_birthday(self):
#         """생일을 맞아 나이 증가"""
#         self.age += 1
#         print(f"{self.name}의 생일! 이제 {self.age}살이 되었습니다.")

# TODO: 객체 생성
# person1 = Person("홍길동", 25)
# person2 = Person("김철수", 30)

# TODO: 객체의 속성 접근
# print("이름:", person1.name)
# print("나이:", person1.age)

# TODO: 메서드 호출
# print(person1.introduce())
# print(person2.introduce())

# TODO: 속성 값 변경
# person1.age = 26
# print("변경된 나이:", person1.age)

# TODO: 메서드를 통한 속성 변경
# person1.have_birthday()

# TODO: 클래스 변수와 인스턴스 변수
# class Student:
#     """학생을 나타내는 클래스"""
#     
#     # 클래스 변수 (모든 인스턴스가 공유)
#     school_name = "Python 고등학교"
#     
#     def __init__(self, name, student_id):
#         """생성자"""
#         self.name = name  # 인스턴스 변수
#         self.student_id = student_id  # 인스턴스 변수
#     
#     def get_info(self):
#         """학생 정보 반환"""
#         return f"이름: {self.name}, 학번: {self.student_id}, 학교: {self.school_name}"

# TODO: 클래스 변수 접근
# print("학교명:", Student.school_name)

# TODO: 객체 생성 및 사용
# student1 = Student("이영희", "2023001")
# student2 = Student("박민수", "2023002")

# print(student1.get_info())
# print(student2.get_info())

# TODO: 클래스 변수 변경
# Student.school_name = "Python 대학교"
# print("변경된 학교명:", Student.school_name)
# print(student1.get_info())  # 모든 객체에 영향

# TODO: 은행 계좌 클래스 (캡슐화 예제)
# class BankAccount:
#     """은행 계좌 클래스"""
#     
#     def __init__(self, account_number, initial_balance=0):
#         """계좌 초기화"""
#         self.account_number = account_number
#         self.__balance = initial_balance  # private 변수
#     
#     def get_balance(self):
#         """잔액 조회"""
#         return self.__balance
#     
#     def deposit(self, amount):
#         """입금"""
#         if amount > 0:
#             self.__balance += amount
#             print(f"{amount}원 입금. 잔액: {self.__balance}원")
#         else:
#             print("입금액은 0보다 커야 합니다.")
#     
#     def withdraw(self, amount):
#         """출금"""
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             print(f"{amount}원 출금. 잔액: {self.__balance}원")
#             return True
#         else:
#             print("출금할 수 없습니다.")
#             return False

# TODO: 은행 계좌 사용
# account = BankAccount("123-456-789", 10000)
# print("초기 잔액:", account.get_balance())
# 
# account.deposit(5000)
# account.withdraw(2000)
# account.withdraw(20000)  # 잔액 부족

if __name__ == "__main__":
    print("기본 클래스와 객체 예제를 실행합니다.")
    print("TODO 부분을 완성한 후 실행해보세요!")
