# 기본 문자열 메서드들

def demonstrate_basic_methods():
    """기본 문자열 메서드들을 보여주는 함수"""
    print("=== 기본 문자열 메서드들 ===")
    
    text = "  Hello, World!  "
    print(f"원본: '{text}'")
    
    # 공백 제거
    stripped = text.strip()
    left_stripped = text.lstrip()
    right_stripped = text.rstrip()
    print(f"strip(): '{stripped}'")
    print(f"lstrip(): '{left_stripped}'")
    print(f"rstrip(): '{right_stripped}'")
    
    # 대소문자 변환
    print(f"upper(): '{text.upper()}'")
    print(f"lower(): '{text.lower()}'")
    print(f"title(): '{text.title()}'")
    print(f"capitalize(): '{text.capitalize()}'")
    print(f"swapcase(): '{text.swapcase()}'")

def demonstrate_string_analysis():
    """문자열 분석 메서드들을 보여주는 함수"""
    print("\n=== 문자열 분석 메서드들 ===")
    
    text = "Hello, World! 123"
    print(f"원본: '{text}'")
    
    # 문자 확인
    print(f"isalpha(): {text.isalpha()}")
    print(f"isdigit(): {text.isdigit()}")
    print(f"isalnum(): {text.isalnum()}")
    print(f"isspace(): {text.isspace()}")
    print(f"isupper(): {text.isupper()}")
    print(f"islower(): {text.islower()}")
    
    # 부분 문자열 확인
    print(f"startswith('Hello'): {text.startswith('Hello')}")
    print(f"endswith('123'): {text.endswith('123')}")
    
    # 포함 여부 확인
    print(f"'World' in text: {'World' in text}")
    print(f"'Python' in text: {'Python' in text}")

if __name__ == "__main__":
    demonstrate_basic_methods()
    demonstrate_string_analysis()
