# 각 데이터 타입별 예제

def demonstrate_integer_type():
    """정수 타입 예제"""
    print("=== 정수 타입 (int) ===")
    
    # 기본 정수
    positive_int = 42
    negative_int = -17
    zero = 0
    
    print(f"양수: {positive_int}, 타입: {type(positive_int)}")
    print(f"음수: {negative_int}, 타입: {type(negative_int)}")
    print(f"영: {zero}, 타입: {type(zero)}")
    
    # 진법 변환
    binary = 0b1010  # 2진수
    octal = 0o777    # 8진수
    hexadecimal = 0xFF  # 16진수
    
    print(f"2진수 1010: {binary}")
    print(f"8진수 777: {octal}")
    print(f"16진수 FF: {hexadecimal}")
    
    # 큰 정수
    big_number = 123456789012345678901234567890
    print(f"큰 정수: {big_number}")

def demonstrate_float_type():
    """실수 타입 예제"""
    print("\n=== 실수 타입 (float) ===")
    
    # 기본 실수
    pi = 3.14159
    negative_float = -2.5
    scientific = 1.23e4  # 과학적 표기법
    
    print(f"파이: {pi}, 타입: {type(pi)}")
    print(f"음수 실수: {negative_float}, 타입: {type(negative_float)}")
    print(f"과학적 표기법: {scientific}")
    
    # 특수 값
    infinity = float('inf')
    negative_infinity = float('-inf')
    not_a_number = float('nan')
    
    print(f"무한대: {infinity}")
    print(f"음의 무한대: {negative_infinity}")
    print(f"NaN: {not_a_number}")

def demonstrate_string_type():
    """문자열 타입 예제"""
    print("\n=== 문자열 타입 (str) ===")
    
    # 기본 문자열
    single_quote = 'Hello, World!'
    double_quote = "Python Programming"
    triple_quote = """여러 줄
    문자열입니다."""
    
    print(f"작은따옴표: {single_quote}")
    print(f"큰따옴표: {double_quote}")
    print(f"삼중따옴표: {triple_quote}")
    
    # 이스케이프 문자
    escape_string = "줄바꿈:\n탭:\t따옴표:\""
    print(f"이스케이프 문자: {escape_string}")
    
    # raw 문자열
    raw_string = r"C:\Users\Name\Documents"
    print(f"Raw 문자열: {raw_string}")

def demonstrate_boolean_type():
    """불린 타입 예제"""
    print("\n=== 불린 타입 (bool) ===")
    
    # 기본 불린 값
    true_value = True
    false_value = False
    
    print(f"True: {true_value}, 타입: {type(true_value)}")
    print(f"False: {false_value}, 타입: {type(false_value)}")
    
    # 불린 변환
    print(f"bool(1): {bool(1)}")
    print(f"bool(0): {bool(0)}")
    print(f"bool(''): {bool('')}")
    print(f"bool('Hello'): {bool('Hello')}")
    print(f"bool([]): {bool([])}")
    print(f"bool([1, 2, 3]): {bool([1, 2, 3])}")

def demonstrate_type_checking():
    """타입 확인 예제"""
    print("\n=== 타입 확인 ===")
    
    variables = [
        42,           # int
        3.14,         # float
        "Hello",      # str
        True,         # bool
        [1, 2, 3],    # list
        (1, 2, 3),    # tuple
        {1, 2, 3},    # set
        {"a": 1}      # dict
    ]
    
    for var in variables:
        print(f"{var} -> {type(var).__name__}")

def demonstrate_type_conversion():
    """타입 변환 예제"""
    print("\n=== 타입 변환 ===")
    
    # 문자열을 숫자로
    str_num = "123"
    int_num = int(str_num)
    float_num = float(str_num)
    
    print(f"문자열 '{str_num}' -> 정수: {int_num}")
    print(f"문자열 '{str_num}' -> 실수: {float_num}")
    
    # 숫자를 문자열로
    num = 456
    str_from_num = str(num)
    print(f"정수 {num} -> 문자열: '{str_from_num}'")
    
    # 불린 변환
    print(f"int(True): {int(True)}")
    print(f"int(False): {int(False)}")
    print(f"float(True): {float(True)}")
    print(f"str(True): {str(True)}")

if __name__ == "__main__":
    demonstrate_integer_type()
    demonstrate_float_type()
    demonstrate_string_type()
    demonstrate_boolean_type()
    demonstrate_type_checking()
    demonstrate_type_conversion()
