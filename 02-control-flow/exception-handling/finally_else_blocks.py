# finally와 else 블록

def basic_finally():
    """기본 finally 블록 사용법"""
    print("=== 기본 finally 블록 ===")
    
    # 예외가 발생하지 않는 경우
    try:
        result = 10 / 2
        print(f"결과: {result}")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    finally:
        print("finally 블록이 실행되었습니다.")
    
    print()
    
    # 예외가 발생하는 경우
    try:
        result = 10 / 0
        print(f"결과: {result}")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    finally:
        print("finally 블록이 실행되었습니다.")

def finally_with_file_handling():
    """파일 처리에서 finally 사용"""
    print("\n=== 파일 처리에서 finally 사용 ===")
    
    # finally를 사용한 파일 처리
    file = None
    try:
        file = open("test.txt", "w")
        file.write("Hello, World!")
        print("파일에 데이터를 썼습니다.")
    except IOError as e:
        print(f"파일 처리 오류: {e}")
    finally:
        if file:
            file.close()
            print("파일을 닫았습니다.")
    
    # with 문을 사용한 더 간단한 방법
    try:
        with open("test.txt", "r") as file:
            content = file.read()
            print(f"파일 내용: {content}")
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    except IOError as e:
        print(f"파일 읽기 오류: {e}")

def basic_else_block():
    """기본 else 블록 사용법"""
    print("\n=== 기본 else 블록 ===")
    
    # 예외가 발생하지 않는 경우
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    else:
        print(f"계산 성공: {result}")
    
    print()
    
    # 예외가 발생하는 경우
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    else:
        print(f"계산 성공: {result}")  # 실행되지 않음

def else_with_loops():
    """반복문에서 else 블록"""
    print("\n=== 반복문에서 else 블록 ===")
    
    # for문의 else
    numbers = [1, 2, 3, 4, 5]
    target = 6
    
    for num in numbers:
        if num == target:
            print(f"{target}을 찾았습니다!")
            break
    else:
        print(f"{target}을 찾을 수 없습니다.")
    
    # while문의 else
    count = 0
    while count < 3:
        if count == 2:
            print(f"count가 {count}에 도달했습니다!")
            break
        count += 1
    else:
        print("while문이 정상적으로 완료되었습니다.")

def try_except_else_finally():
    """try-except-else-finally 전체 구조"""
    print("\n=== try-except-else-finally 전체 구조 ===")
    
    def process_number(num_str):
        try:
            number = int(num_str)
            result = 100 / number
        except ValueError:
            print(f"'{num_str}'는 올바른 숫자가 아닙니다.")
            return None
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
            return None
        else:
            print("계산이 성공적으로 완료되었습니다.")
            return result
        finally:
            print("처리 과정이 완료되었습니다.")
    
    # 테스트
    test_inputs = ["10", "0", "abc", "5"]
    for inp in test_inputs:
        print(f"\n입력: {inp}")
        result = process_number(inp)
        if result is not None:
            print(f"결과: {result}")

def finally_with_return():
    """return이 있는 경우의 finally"""
    print("\n=== return이 있는 경우의 finally ===")
    
    def test_finally_with_return():
        try:
            print("try 블록 실행")
            return "try에서 반환"
        except Exception as e:
            print(f"except 블록 실행: {e}")
            return "except에서 반환"
        finally:
            print("finally 블록 실행")
    
    result = test_finally_with_return()
    print(f"반환값: {result}")

def finally_with_exception():
    """finally에서 예외가 발생하는 경우"""
    print("\n=== finally에서 예외가 발생하는 경우 ===")
    
    def test_finally_exception():
        try:
            print("try 블록 실행")
            return "정상 반환"
        except Exception as e:
            print(f"except 블록 실행: {e}")
        finally:
            print("finally 블록 실행")
            # finally에서 예외 발생
            raise ValueError("finally에서 예외 발생")
    
    try:
        result = test_finally_exception()
        print(f"반환값: {result}")
    except ValueError as e:
        print(f"finally에서 발생한 예외: {e}")

def practical_finally_examples():
    """실무에서 자주 사용되는 finally 예제"""
    print("\n=== 실무 finally 예제 ===")
    
    # 데이터베이스 연결 시뮬레이션
    class DatabaseConnection:
        def __init__(self, name):
            self.name = name
            self.connected = False
        
        def connect(self):
            self.connected = True
            print(f"데이터베이스 '{self.name}'에 연결되었습니다.")
        
        def disconnect(self):
            if self.connected:
                self.connected = False
                print(f"데이터베이스 '{self.name}' 연결이 해제되었습니다.")
        
        def execute_query(self, query):
            if not self.connected:
                raise ConnectionError("데이터베이스에 연결되지 않았습니다.")
            print(f"쿼리 실행: {query}")
            return f"결과: {query}"
    
    # finally를 사용한 리소스 관리
    def process_database_operation():
        db = DatabaseConnection("test_db")
        try:
            db.connect()
            result = db.execute_query("SELECT * FROM users")
            return result
        except ConnectionError as e:
            print(f"데이터베이스 오류: {e}")
            return None
        finally:
            db.disconnect()
    
    result = process_database_operation()
    if result:
        print(f"데이터베이스 작업 결과: {result}")

def else_block_practical_examples():
    """실무에서 자주 사용되는 else 블록 예제"""
    print("\n=== 실무 else 블록 예제 ===")
    
    # 파일 처리에서 else 사용
    def process_file(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"파일 '{filename}'을 찾을 수 없습니다.")
            return None
        except IOError as e:
            print(f"파일 읽기 오류: {e}")
            return None
        else:
            print(f"파일 '{filename}'을 성공적으로 읽었습니다.")
            return content
    
    # 사용자 입력 검증에서 else 사용
    def get_valid_number():
        while True:
            try:
                user_input = input("숫자를 입력하세요: ")
                number = int(user_input)
            except ValueError:
                print("올바른 숫자를 입력해주세요.")
            else:
                print("유효한 숫자가 입력되었습니다.")
                return number
    
    # 네트워크 요청 시뮬레이션에서 else 사용
    def make_request(url):
        try:
            # 가상의 네트워크 요청
            if "error" in url:
                raise ConnectionError("연결 실패")
            response = f"응답: {url}"
        except ConnectionError as e:
            print(f"네트워크 오류: {e}")
            return None
        else:
            print("요청이 성공적으로 완료되었습니다.")
            return response

def best_practices():
    """finally와 else 블록 모범 사례"""
    print("\n=== finally와 else 블록 모범 사례 ===")
    
    # 1. finally는 리소스 정리에 사용
    print("1. finally는 리소스 정리에 사용:")
    def safe_file_operation():
        file = None
        try:
            file = open("temp.txt", "w")
            file.write("임시 데이터")
        except IOError as e:
            print(f"파일 쓰기 오류: {e}")
        finally:
            if file:
                file.close()
                print("파일이 정리되었습니다.")
    
    # 2. else는 예외가 발생하지 않았을 때만 실행할 코드에 사용
    print("\n2. else는 예외가 발생하지 않았을 때만 실행할 코드에 사용:")
    def process_data(data):
        try:
            result = int(data)
        except ValueError:
            print("데이터 변환 실패")
            return None
        else:
            print("데이터 변환 성공")
            return result * 2
    
    # 3. with 문과 함께 사용
    print("\n3. with 문과 함께 사용:")
    def process_file_with_with(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"파일 '{filename}'을 찾을 수 없습니다.")
            return None
        else:
            print(f"파일 '{filename}' 처리 완료")
            return content

if __name__ == "__main__":
    basic_finally()
    finally_with_file_handling()
    basic_else_block()
    else_with_loops()
    try_except_else_finally()
    finally_with_return()
    finally_with_exception()
    practical_finally_examples()
    else_block_practical_examples()
    best_practices()
