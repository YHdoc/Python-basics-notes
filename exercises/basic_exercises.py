"""
기초 연습 문제
Python 기초를 다지기 위한 연습 문제들입니다.
"""

# TODO: 문제 1 - 변수와 타입 변환
# 사용자로부터 이름, 나이, 키를 입력받아 출력하는 프로그램을 작성하세요.
# 단, 나이는 정수, 키는 실수로 변환하여 저장하세요.

def exercise_1():
    """변수와 타입 변환 연습"""
    print("=== 문제 1: 변수와 타입 변환 ===")
    
    # TODO: 여기에 코드를 작성하세요
    # name = input("이름을 입력하세요: ")
    # age = int(input("나이를 입력하세요: "))
    # height = float(input("키를 입력하세요: "))
    # 
    # print(f"이름: {name}, 나이: {age}세, 키: {height}cm")
    pass

# TODO: 문제 2 - 조건문
# 점수를 입력받아 등급을 출력하는 프로그램을 작성하세요.
# 90점 이상: A, 80점 이상: B, 70점 이상: C, 60점 이상: D, 60점 미만: F

def exercise_2():
    """조건문 연습"""
    print("=== 문제 2: 조건문 ===")
    
    # TODO: 여기에 코드를 작성하세요
    # score = int(input("점수를 입력하세요: "))
    # 
    # if score >= 90:
    #     grade = "A"
    # elif score >= 80:
    #     grade = "B"
    # elif score >= 70:
    #     grade = "C"
    # elif score >= 60:
    #     grade = "D"
    # else:
    #     grade = "F"
    # 
    # print(f"점수: {score}, 등급: {grade}")
    pass

# TODO: 문제 3 - 반복문
# 1부터 100까지의 숫자 중에서 3의 배수만 출력하는 프로그램을 작성하세요.

def exercise_3():
    """반복문 연습"""
    print("=== 문제 3: 반복문 ===")
    
    # TODO: 여기에 코드를 작성하세요
    # for i in range(1, 101):
    #     if i % 3 == 0:
    #         print(i, end=" ")
    # print()  # 줄바꿈
    pass

# TODO: 문제 4 - 함수
# 두 수를 입력받아 사칙연산을 수행하는 함수들을 작성하세요.
# add(a, b), subtract(a, b), multiply(a, b), divide(a, b)

def exercise_4():
    """함수 연습"""
    print("=== 문제 4: 함수 ===")
    
    # TODO: 함수들을 정의하세요
    # def add(a, b):
    #     return a + b
    # 
    # def subtract(a, b):
    #     return a - b
    # 
    # def multiply(a, b):
    #     return a * b
    # 
    # def divide(a, b):
    #     if b != 0:
    #         return a / b
    #     else:
    #         return "0으로 나눌 수 없습니다."
    # 
    # # 함수 테스트
    # a = int(input("첫 번째 숫자: "))
    # b = int(input("두 번째 숫자: "))
    # 
    # print(f"{a} + {b} = {add(a, b)}")
    # print(f"{a} - {b} = {subtract(a, b)}")
    # print(f"{a} * {b} = {multiply(a, b)}")
    # print(f"{a} / {b} = {divide(a, b)}")
    pass

# TODO: 문제 5 - 리스트
# 1부터 10까지의 숫자를 리스트에 저장하고, 
# 짝수만 필터링하여 새로운 리스트를 만드는 프로그램을 작성하세요.

def exercise_5():
    """리스트 연습"""
    print("=== 문제 5: 리스트 ===")
    
    # TODO: 여기에 코드를 작성하세요
    # numbers = list(range(1, 11))
    # even_numbers = [x for x in numbers if x % 2 == 0]
    # 
    # print("원본 리스트:", numbers)
    # print("짝수 리스트:", even_numbers)
    pass

# TODO: 문제 6 - 딕셔너리
# 학생들의 이름과 점수를 딕셔너리로 저장하고,
# 평균 점수를 계산하는 프로그램을 작성하세요.

def exercise_6():
    """딕셔너리 연습"""
    print("=== 문제 6: 딕셔너리 ===")
    
    # TODO: 여기에 코드를 작성하세요
    # student_scores = {
    #     "김철수": 85,
    #     "이영희": 92,
    #     "박민수": 78,
    #     "최지영": 95,
    #     "정수진": 88
    # }
    # 
    # total_score = sum(student_scores.values())
    # average_score = total_score / len(student_scores)
    # 
    # print("학생 점수:", student_scores)
    # print(f"평균 점수: {average_score:.2f}")
    pass

# TODO: 문제 7 - 클래스
# 도서 정보를 관리하는 Book 클래스를 작성하세요.
# 속성: 제목, 저자, 가격, 페이지수
# 메서드: get_info() (도서 정보 출력), apply_discount() (할인 적용)

def exercise_7():
    """클래스 연습"""
    print("=== 문제 7: 클래스 ===")
    
    # TODO: Book 클래스를 정의하세요
    # class Book:
    #     def __init__(self, title, author, price, pages):
    #         self.title = title
    #         self.author = author
    #         self.price = price
    #         self.pages = pages
    #     
    #     def get_info(self):
    #         return f"제목: {self.title}, 저자: {self.author}, 가격: {self.price}원, 페이지: {self.pages}페이지"
    #     
    #     def apply_discount(self, discount_rate):
    #         self.price = int(self.price * (1 - discount_rate))
    #         return self.price
    # 
    # # 클래스 테스트
    # book = Book("파이썬 프로그래밍", "홍길동", 30000, 400)
    # print(book.get_info())
    # 
    # discounted_price = book.apply_discount(0.1)  # 10% 할인
    # print(f"할인 후 가격: {discounted_price}원")
    pass

# TODO: 문제 8 - 예외 처리
# 사용자로부터 숫자를 입력받아 제곱을 계산하는 프로그램을 작성하세요.
# 잘못된 입력이 들어오면 적절한 메시지를 출력하고 다시 입력받으세요.

def exercise_8():
    """예외 처리 연습"""
    print("=== 문제 8: 예외 처리 ===")
    
    # TODO: 여기에 코드를 작성하세요
    # while True:
    #     try:
    #         number = float(input("숫자를 입력하세요: "))
    #         square = number ** 2
    #         print(f"{number}의 제곱은 {square}입니다.")
    #         break
    #     except ValueError:
    #         print("올바른 숫자를 입력해주세요.")
    #     except Exception as e:
    #         print(f"오류가 발생했습니다: {e}")
    pass

# TODO: 문제 9 - 파일 입출력
# 사용자 정보를 파일에 저장하고 읽어오는 프로그램을 작성하세요.

def exercise_9():
    """파일 입출력 연습"""
    print("=== 문제 9: 파일 입출력 ===")
    
    # TODO: 여기에 코드를 작성하세요
    # import json
    # 
    # # 사용자 정보 저장
    # user_info = {
    #     "name": input("이름: "),
    #     "age": int(input("나이: ")),
    #     "email": input("이메일: ")
    # }
    # 
    # # 파일에 저장
    # with open("user_info.json", "w", encoding="utf-8") as f:
    #     json.dump(user_info, f, ensure_ascii=False, indent=2)
    # 
    # print("사용자 정보가 저장되었습니다.")
    # 
    # # 파일에서 읽기
    # with open("user_info.json", "r", encoding="utf-8") as f:
    #     loaded_info = json.load(f)
    # 
    # print("저장된 사용자 정보:", loaded_info)
    pass

# TODO: 문제 10 - 종합 문제
# 간단한 계산기 프로그램을 작성하세요.
# 사용자가 연산자와 두 숫자를 입력하면 결과를 출력하고,
# 'quit'을 입력하면 프로그램을 종료합니다.

def exercise_10():
    """종합 문제"""
    print("=== 문제 10: 계산기 프로그램 ===")
    
    # TODO: 여기에 코드를 작성하세요
    # while True:
    #     print("\n=== 계산기 ===")
    #     print("연산자: +, -, *, /")
    #     print("종료하려면 'quit' 입력")
    #     
    #     operator = input("연산자를 입력하세요: ")
    #     
    #     if operator.lower() == 'quit':
    #         print("계산기를 종료합니다.")
    #         break
    #     
    #     if operator not in ['+', '-', '*', '/']:
    #         print("올바른 연산자를 입력해주세요.")
    #         continue
    #     
    #     try:
    #         num1 = float(input("첫 번째 숫자: "))
    #         num2 = float(input("두 번째 숫자: "))
    #         
    #         if operator == '+':
    #             result = num1 + num2
    #         elif operator == '-':
    #             result = num1 - num2
    #         elif operator == '*':
    #             result = num1 * num2
    #         elif operator == '/':
    #             if num2 == 0:
    #                 print("0으로 나눌 수 없습니다.")
    #                 continue
    #             result = num1 / num2
    #         
    #         print(f"{num1} {operator} {num2} = {result}")
    #         
    #     except ValueError:
    #         print("올바른 숫자를 입력해주세요.")
    #     except Exception as e:
    #         print(f"오류가 발생했습니다: {e}")
    pass

def main():
    """메인 함수 - 모든 연습 문제 실행"""
    print("Python 기초 연습 문제를 시작합니다!")
    print("각 문제의 TODO 부분을 완성한 후 실행해보세요.\n")
    
    # TODO: 원하는 문제만 실행하려면 주석을 해제하세요
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    # exercise_8()
    # exercise_9()
    # exercise_10()

if __name__ == "__main__":
    main()
