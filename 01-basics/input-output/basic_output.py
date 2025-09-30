# 기본 출력 방법들

def basic_print():
    """기본 print() 함수 사용법"""
    print("=== 기본 출력 ===")
    
    # 단순 출력
    print("Hello, World!")
    
    # 여러 값 출력
    name = "김철수"
    age = 25
    print("이름:", name, "나이:", age)
    
    # 구분자 변경
    print("Python", "is", "awesome", sep="-")
    
    # 끝 문자 변경
    print("첫 번째 줄", end=" ")
    print("두 번째 줄")

def formatted_output():
    """포맷된 출력"""
    print("\n=== 포맷된 출력 ===")
    
    name = "홍길동"
    age = 30
    height = 175.5
    
    # f-string (Python 3.6+)
    print(f"이름: {name}, 나이: {age}, 키: {height}cm")
    
    # format() 메서드
    print("이름: {}, 나이: {}, 키: {}cm".format(name, age, height))
    
    # % 포맷팅
    print("이름: %s, 나이: %d, 키: %.1fcm" % (name, age, height))

def number_formatting():
    """숫자 포맷팅"""
    print("\n=== 숫자 포맷팅 ===")
    
    number = 1234.5678
    
    # 소수점 자릿수
    print(f"소수점 2자리: {number:.2f}")
    print(f"소수점 4자리: {number:.4f}")
    
    # 천 단위 구분자
    print(f"천 단위 구분: {number:,.2f}")
    
    # 정렬과 패딩
    print(f"오른쪽 정렬: {number:>10.2f}")
    print(f"왼쪽 정렬: {number:<10.2f}")
    print(f"가운데 정렬: {number:^10.2f}")
    
    # 0으로 패딩
    print(f"0으로 패딩: {number:010.2f}")

def table_output():
    """표 형태 출력"""
    print("\n=== 표 형태 출력 ===")
    
    # 간단한 표
    print(f"{'이름':<10} {'나이':<5} {'직업':<10}")
    print("-" * 25)
    print(f"{'김철수':<10} {25:<5} {'개발자':<10}")
    print(f"{'이영희':<10} {30:<5} {'디자이너':<10}")
    print(f"{'박민수':<10} {28:<5} {'기획자':<10}")

if __name__ == "__main__":
    basic_print()
    formatted_output()
    number_formatting()
    table_output()
