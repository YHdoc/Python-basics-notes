# 문자열 처리 함수들

def demonstrate_string_functions():
    """문자열 처리 함수들을 보여주는 함수"""
    print("=== 문자열 처리 함수들 ===")
    
    # str 함수
    print(f"str(123): {str(123)}")
    print(f"str(3.14): {str(3.14)}")
    print(f"str([1, 2, 3]): {str([1, 2, 3])}")
    print(f"str(True): {str(True)}")
    
    # repr 함수 (디버깅용)
    print(f"repr('Hello'): {repr('Hello')}")
    print(f"repr(123): {repr(123)}")
    print(f"repr([1, 2, 3]): {repr([1, 2, 3])}")
    
    # ord, chr 함수
    print(f"ord('A'): {ord('A')}")
    print(f"chr(65): {chr(65)}")
    print(f"ord('가'): {ord('가')}")
    print(f"chr(44032): {chr(44032)}")
    
    # ascii 함수
    print(f"ascii('Hello'): {ascii('Hello')}")
    print(f"ascii('안녕'): {ascii('안녕')}")

def demonstrate_string_methods():
    """문자열 메서드들을 보여주는 함수"""
    print("\n=== 문자열 메서드들 ===")
    
    text = "  Hello, World!  "
    print(f"원본: '{text}'")
    
    # 공백 제거
    print(f"strip(): '{text.strip()}'")
    print(f"lstrip(): '{text.lstrip()}'")
    print(f"rstrip(): '{text.rstrip()}'")
    
    # 대소문자 변환
    print(f"upper(): '{text.strip().upper()}'")
    print(f"lower(): '{text.strip().lower()}'")
    print(f"title(): '{text.strip().title()}'")
    print(f"capitalize(): '{text.strip().capitalize()}'")
    
    # 문자열 검색
    print(f"find('World'): {text.strip().find('World')}")
    print(f"find('Python'): {text.strip().find('Python')}")
    print(f"count('l'): {text.strip().count('l')}")
    print(f"startswith('Hello'): {text.strip().startswith('Hello')}")
    print(f"endswith('!'): {text.strip().endswith('!')}")
    
    # 문자열 분할과 결합
    words = text.strip().split(', ')
    print(f"split(', '): {words}")
    print(f"join(['Hello', 'Python']): {'-'.join(['Hello', 'Python'])}")

def demonstrate_string_formatting():
    """문자열 포맷팅 함수들을 보여주는 함수"""
    print("\n=== 문자열 포맷팅 ===")
    
    name = "김철수"
    age = 30
    height = 175.5
    
    # f-string (Python 3.6+)
    message1 = f"안녕하세요, {name}님! {age}세이시군요."
    print(f"f-string: {message1}")
    
    # format 메서드
    message2 = "안녕하세요, {}님! {}세이시군요.".format(name, age)
    print(f"format(): {message2}")
    
    # % 포맷팅
    message3 = "안녕하세요, %s님! %d세이시군요." % (name, age)
    print(f"% 포맷팅: {message3}")
    
    # 숫자 포맷팅
    print(f"소수점 2자리: {height:.2f}")
    print(f"천 단위 구분: {1234567:,}")
    print(f"백분율: {0.85:.1%}")

def demonstrate_string_validation():
    """문자열 검증 함수들을 보여주는 함수"""
    print("\n=== 문자열 검증 ===")
    
    test_strings = [
        "Hello123",
        "123456",
        "Hello World",
        "hello",
        "HELLO",
        "  ",
        "",
        "Hello@World"
    ]
    
    for s in test_strings:
        print(f"'{s}':")
        print(f"  isalnum(): {s.isalnum()}")
        print(f"  isalpha(): {s.isalpha()}")
        print(f"  isdigit(): {s.isdigit()}")
        print(f"  islower(): {s.islower()}")
        print(f"  isupper(): {s.isupper()}")
        print(f"  isspace(): {s.isspace()}")
        print(f"  isprintable(): {s.isprintable()}")

if __name__ == "__main__":
    demonstrate_string_functions()
    demonstrate_string_methods()
    demonstrate_string_formatting()
    demonstrate_string_validation()
