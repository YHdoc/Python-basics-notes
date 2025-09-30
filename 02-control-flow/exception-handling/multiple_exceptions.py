# 여러 예외 처리

def multiple_except_blocks():
    """여러 except 블록 사용"""
    print("=== 여러 except 블록 사용 ===")
    
    def process_number(num_str):
        try:
            number = int(num_str)
            result = 100 / number
            return result
        except ValueError:
            print(f"'{num_str}'는 올바른 숫자가 아닙니다.")
            return None
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
            return None
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return None
    
    # 테스트
    test_inputs = ["10", "0", "abc", "5.5"]
    for inp in test_inputs:
        result = process_number(inp)
        if result is not None:
            print(f"결과: {result}")

def single_except_multiple_types():
    """하나의 except 블록에서 여러 예외 타입 처리"""
    print("\n=== 하나의 except 블록에서 여러 예외 타입 처리 ===")
    
    def safe_operation(a, b):
        try:
            result = a / b
            return result
        except (ZeroDivisionError, TypeError) as e:
            print(f"연산 오류: {e}")
            return None
    
    # 테스트
    test_cases = [
        (10, 2),    # 정상
        (10, 0),    # ZeroDivisionError
        (10, "abc"), # TypeError
        ("abc", 2)  # TypeError
    ]
    
    for a, b in test_cases:
        result = safe_operation(a, b)
        if result is not None:
            print(f"{a} / {b} = {result}")

def exception_chain():
    """예외 체인 처리"""
    print("\n=== 예외 체인 처리 ===")
    
    def read_config_file(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                # JSON 파싱 시뮬레이션
                if not content.strip():
                    raise ValueError("빈 파일입니다.")
                return content
        except FileNotFoundError:
            print(f"설정 파일 '{filename}'을 찾을 수 없습니다.")
            return None
        except PermissionError:
            print(f"설정 파일 '{filename}'에 접근할 권한이 없습니다.")
            return None
        except ValueError as e:
            print(f"설정 파일 오류: {e}")
            return None
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return None
    
    # 테스트
    config = read_config_file("config.txt")
    if config:
        print("설정 파일을 성공적으로 읽었습니다.")

def nested_exception_handling():
    """중첩된 예외 처리"""
    print("\n=== 중첩된 예외 처리 ===")
    
    def process_data(data_list):
        results = []
        
        for i, data in enumerate(data_list):
            try:
                # 첫 번째 단계: 숫자 변환
                try:
                    number = int(data)
                except ValueError:
                    print(f"인덱스 {i}: '{data}'는 숫자가 아닙니다.")
                    continue
                
                # 두 번째 단계: 계산
                try:
                    result = 100 / number
                    results.append(result)
                    print(f"인덱스 {i}: {data} -> {result}")
                except ZeroDivisionError:
                    print(f"인덱스 {i}: 0으로 나눌 수 없습니다.")
                    continue
                    
            except Exception as e:
                print(f"인덱스 {i}: 예상치 못한 오류 - {e}")
                continue
        
        return results
    
    # 테스트
    test_data = ["10", "0", "abc", "5", "2.5", "3"]
    results = process_data(test_data)
    print(f"처리 결과: {results}")

def exception_with_logging():
    """로깅과 함께 예외 처리"""
    print("\n=== 로깅과 함께 예외 처리 ===")
    
    import logging
    
    # 로깅 설정
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    def process_user_input(user_input):
        try:
            number = int(user_input)
            result = 100 / number
            logging.info(f"사용자 입력 '{user_input}' 처리 성공: {result}")
            return result
        except ValueError:
            logging.warning(f"사용자 입력 '{user_input}'는 유효하지 않은 숫자입니다.")
            return None
        except ZeroDivisionError:
            logging.error(f"사용자 입력 '{user_input}'로 인한 0으로 나누기 오류")
            return None
        except Exception as e:
            logging.critical(f"예상치 못한 오류 발생: {e}")
            return None
    
    # 테스트
    test_inputs = ["10", "0", "abc", "5"]
    for inp in test_inputs:
        result = process_user_input(inp)

def exception_with_retry():
    """재시도와 함께 예외 처리"""
    print("\n=== 재시도와 함께 예외 처리 ===")
    
    def risky_operation(max_retries=3):
        for attempt in range(max_retries):
            try:
                # 가상의 위험한 연산 (랜덤하게 실패)
                import random
                if random.random() < 0.7:  # 70% 확률로 실패
                    raise ConnectionError("연결 실패")
                
                print("연산 성공!")
                return "성공"
                
            except ConnectionError as e:
                print(f"시도 {attempt + 1} 실패: {e}")
                if attempt < max_retries - 1:
                    print("재시도 중...")
                else:
                    print("최대 재시도 횟수 초과")
                    return None
            except Exception as e:
                print(f"예상치 못한 오류: {e}")
                return None
        
        return None
    
    # 테스트
    result = risky_operation()
    print(f"최종 결과: {result}")

def exception_with_context():
    """컨텍스트와 함께 예외 처리"""
    print("\n=== 컨텍스트와 함께 예외 처리 ===")
    
    def process_file_with_context(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                # 파일 내용 처리 시뮬레이션
                if len(content) > 1000:
                    raise ValueError("파일이 너무 큽니다.")
                return content
        except FileNotFoundError:
            print(f"파일 '{filename}'을 찾을 수 없습니다.")
            return None
        except PermissionError:
            print(f"파일 '{filename}'에 접근할 권한이 없습니다.")
            return None
        except ValueError as e:
            print(f"파일 처리 오류: {e}")
            return None
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return None
    
    # 테스트
    content = process_file_with_context("test.txt")
    if content:
        print("파일을 성공적으로 처리했습니다.")

def exception_handling_patterns():
    """예외 처리 패턴들"""
    print("\n=== 예외 처리 패턴들 ===")
    
    # 1. EAFP (Easier to Ask for Forgiveness than Permission)
    print("1. EAFP 패턴:")
    data = {"name": "김철수", "age": 25}
    
    try:
        city = data["city"]
    except KeyError:
        city = "알 수 없음"
    
    print(f"도시: {city}")
    
    # 2. LBYL (Look Before You Leap)
    print("\n2. LBYL 패턴:")
    if "city" in data:
        city = data["city"]
    else:
        city = "알 수 없음"
    
    print(f"도시: {city}")
    
    # 3. 예외 변환
    print("\n3. 예외 변환:")
    def convert_to_number(value):
        try:
            return int(value)
        except ValueError:
            raise TypeError(f"'{value}'는 숫자로 변환할 수 없습니다.")
    
    try:
        result = convert_to_number("abc")
    except TypeError as e:
        print(f"변환 오류: {e}")

if __name__ == "__main__":
    multiple_except_blocks()
    single_except_multiple_types()
    exception_chain()
    nested_exception_handling()
    exception_with_logging()
    exception_with_retry()
    exception_with_context()
    exception_handling_patterns()
