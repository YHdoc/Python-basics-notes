# 기본 정규표현식

import re

def demonstrate_basic_regex():
    """기본 정규표현식을 보여주는 함수"""
    print("=== 기본 정규표현식 ===")
    
    # 기본 매칭
    pattern = r"hello"
    text = "hello world"
    match = re.search(pattern, text)
    print(f"패턴: {pattern}")
    print(f"텍스트: {text}")
    print(f"매칭 결과: {match}")
    if match:
        print(f"매칭된 문자열: '{match.group()}'")
        print(f"매칭 위치: {match.start()}-{match.end()}")
    
    # match vs search
    print(f"\nmatch(): {re.match(pattern, text)}")
    print(f"search(): {re.search(pattern, text)}")
    
    # findall
    text2 = "hello world hello python"
    matches = re.findall(pattern, text2)
    print(f"findall(): {matches}")

if __name__ == "__main__":
    demonstrate_basic_regex()
