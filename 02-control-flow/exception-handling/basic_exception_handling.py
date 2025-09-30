# 기본 예외 처리

def basic_try_except():
    """기본 try-except 사용법"""
    print("=== 기본 try-except ===")
    
    # ZeroDivisionError 처리
    try:
        result = 10 / 0
        print(f"결과: {result}")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    
    # ValueError 처리
    try:
        number = int("abc")
        print(f"숫자: {number}")
    except ValueError:
        print("올바른 숫자가 아닙니다.")
    
    # IndexError 처리
    try:
        numbers = [1, 2, 3]
        print(f"인덱스 5의 값: {numbers[5]}")
    except IndexError:
        print("리스트 인덱스가 범위를 벗어났습니다.")

def exception_with_message():
    """예외 메시지와 함께 처리"""
    print("\n=== 예외 메시지와 함께 처리 ===")
    
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"예외 발생: {e}")
        print(f"예외 타입: {type(e).__name__}")
    
    try:
        number = int("abc")
    except ValueError as e:
        print(f"예외 발생: {e}")
        print(f"예외 타입: {type(e).__name__}")

def multiple_exceptions():
    """여러 예외 처리"""
    print("\n=== 여러 예외 처리 ===")
    
    # 각각 다른 except 블록
    try:
        user_input = input("숫자를 입력하세요: ")
        number = int(user_input)
        result = 10 / number
        print(f"결과: {result}")
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except Exception as e:
        print(f"예상치 못한 오류: {e}")

def exception_hierarchy():
    """예외 계층 구조"""
    print("\n=== 예외 계층 구조 ===")
    
    # ArithmeticError는 ZeroDivisionError의 부모 클래스
    try:
        result = 10 / 0
    except ArithmeticError as e:
        print(f"산술 오류: {e}")
    except ZeroDivisionError as e:
        print(f"0으로 나누기 오류: {e}")  # 이 블록은 실행되지 않음
    
    # 더 구체적인 예외를 먼저 처리
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"0으로 나누기 오류: {e}")
    except ArithmeticError as e:
        print(f"산술 오류: {e}")

def practical_examples():
    """실무 예제"""
    print("\n=== 실무 예제 ===")
    
    # 파일 처리
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    except PermissionError:
        print("파일 접근 권한이 없습니다.")
    except Exception as e:
        print(f"파일 처리 중 오류: {e}")
    
    # 딕셔너리 키 접근
    person = {"name": "김철수", "age": 25}
    
    try:
        city = person["city"]
        print(f"도시: {city}")
    except KeyError:
        print("'city' 키가 존재하지 않습니다.")
        city = "알 수 없음"
    
    # 리스트 인덱스 접근
    numbers = [1, 2, 3, 4, 5]
    
    try:
        index = int(input("인덱스를 입력하세요 (0-4): "))
        value = numbers[index]
        print(f"인덱스 {index}의 값: {value}")
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
    except IndexError:
        print("인덱스가 범위를 벗어났습니다.")
    except Exception as e:
        print(f"예상치 못한 오류: {e}")

def exception_in_loops():
    """반복문에서 예외 처리"""
    print("\n=== 반복문에서 예외 처리 ===")
    
    numbers = ["10", "20", "abc", "30", "def", "40"]
    valid_numbers = []
    
    for num_str in numbers:
        try:
            num = int(num_str)
            valid_numbers.append(num)
            print(f"유효한 숫자: {num}")
        except ValueError:
            print(f"유효하지 않은 값: {num_str}")
    
    print(f"유효한 숫자들: {valid_numbers}")

def exception_with_functions():
    """함수에서 예외 처리"""
    print("\n=== 함수에서 예외 처리 ===")
    
    def safe_divide(a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
            return None
        except TypeError:
            print("숫자만 나눌 수 있습니다.")
            return None
    
    # 함수 호출
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print(f"10 / 'abc' = {safe_divide(10, 'abc')}")

def exception_handling_best_practices():
    """예외 처리 모범 사례"""
    print("\n=== 예외 처리 모범 사례 ===")
    
    # 1. 구체적인 예외 처리
    print("1. 구체적인 예외 처리:")
    try:
        number = int("abc")
    except ValueError as e:
        print(f"  ValueError: {e}")
    
    # 2. 예외 정보 활용
    print("\n2. 예외 정보 활용:")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"  오류 메시지: {e}")
        print(f"  오류 타입: {type(e).__name__}")
    
    # 3. 적절한 예외 처리 범위
    print("\n3. 적절한 예외 처리 범위:")
    try:
        # 예외가 발생할 수 있는 코드만 포함
        user_input = input("숫자를 입력하세요: ")
        number = int(user_input)
    except ValueError:
        print("  올바른 숫자를 입력해주세요.")
        number = 0
    
    # 예외가 발생하지 않을 코드는 try 블록 밖에
    print(f"  입력된 숫자: {number}")

if __name__ == "__main__":
    basic_try_except()
    exception_with_message()
    multiple_exceptions()
    exception_hierarchy()
    practical_examples()
    exception_in_loops()
    exception_with_functions()
    exception_handling_best_practices()
