# 비트 연산자 예제

def basic_bitwise():
    """기본 비트 연산자 사용법"""
    print("=== 기본 비트 연산자 ===")
    
    a = 12  # 1100 (이진수)
    b = 10  # 1010 (이진수)
    
    print(f"a = {a} (이진수: {bin(a)})")
    print(f"b = {b} (이진수: {bin(b)})")
    
    # AND 연산자 (&)
    result_and = a & b
    print(f"a & b = {result_and} (이진수: {bin(result_and)})")
    
    # OR 연산자 (|)
    result_or = a | b
    print(f"a | b = {result_or} (이진수: {bin(result_or)})")
    
    # XOR 연산자 (^)
    result_xor = a ^ b
    print(f"a ^ b = {result_xor} (이진수: {bin(result_xor)})")
    
    # NOT 연산자 (~)
    result_not_a = ~a
    print(f"~a = {result_not_a} (이진수: {bin(result_not_a & 0xFF)})")
    
    # 왼쪽 시프트 (<<)
    result_left = a << 2
    print(f"a << 2 = {result_left} (이진수: {bin(result_left)})")
    
    # 오른쪽 시프트 (>>)
    result_right = a >> 2
    print(f"a >> 2 = {result_right} (이진수: {bin(result_right)})")

def practical_bitwise():
    """실무에서 자주 사용되는 비트 연산"""
    print("\n=== 실무 예제 ===")
    
    # 플래그 관리 : 이런 식으로 한 개체에 여러 상태값이 있는 걸 나타낼 때 비트연산이 유용하다
    READ_PERMISSION = 1    # 0001
    WRITE_PERMISSION = 2   # 0010
    EXECUTE_PERMISSION = 4 # 0100
    ADMIN_PERMISSION = 8   # 1000
    
    # 권한 설정
    user_permissions = READ_PERMISSION | WRITE_PERMISSION
    admin_permissions = READ_PERMISSION | WRITE_PERMISSION | EXECUTE_PERMISSION | ADMIN_PERMISSION
    
    print(f"사용자 권한: {user_permissions} (이진수: {bin(user_permissions)})")
    print(f"관리자 권한: {admin_permissions} (이진수: {bin(admin_permissions)})")
    
    # 권한 확인
    def has_permission(user_perm, required_perm):
        return (user_perm & required_perm) == required_perm
    
    print(f"사용자가 읽기 권한 있음: {has_permission(user_permissions, READ_PERMISSION)}")
    print(f"사용자가 실행 권한 있음: {has_permission(user_permissions, EXECUTE_PERMISSION)}")
    print(f"관리자가 모든 권한 있음: {has_permission(admin_permissions, 15)}")

def bit_manipulation():
    """비트 조작 예제"""
    print("\n=== 비트 조작 ===")
    
    def set_bit(number, position):
        """특정 위치의 비트를 1로 설정"""
        return number | (1 << position)
    
    def clear_bit(number, position):
        """특정 위치의 비트를 0으로 설정"""
        return number & ~(1 << position)
    
    def toggle_bit(number, position):
        """특정 위치의 비트를 토글"""
        return number ^ (1 << position)
    
    def get_bit(number, position):
        """특정 위치의 비트 값 확인"""
        return (number >> position) & 1
    
    # 예제
    num = 8  # 1000
    print(f"원본 숫자: {num} (이진수: {bin(num)})")
    
    # 비트 설정
    num = set_bit(num, 1)  # 1010
    print(f"1번 비트 설정: {num} (이진수: {bin(num)})")
    
    # 비트 토글
    num = toggle_bit(num, 0)  # 1011
    print(f"0번 비트 토글: {num} (이진수: {bin(num)})")
    
    # 비트 확인
    print(f"2번 비트: {get_bit(num, 2)}")
    print(f"1번 비트: {get_bit(num, 1)}")
    
    # 비트 클리어
    num = clear_bit(num, 1)  # 1001
    print(f"1번 비트 클리어: {num} (이진수: {bin(num)})")

def shift_operations():
    """시프트 연산 예제"""
    print("\n=== 시프트 연산 ===")
    
    number = 8  # 1000
    print(f"원본: {number} (이진수: {bin(number)})")
    
    # 왼쪽 시프트 (곱셈과 유사)
    left_shift_1 = number << 1  # 16 (10000)
    left_shift_2 = number << 2  # 32 (100000)
    left_shift_3 = number << 3  # 64 (1000000)
    
    print(f"왼쪽 시프트 1: {left_shift_1} (이진수: {bin(left_shift_1)})")
    print(f"왼쪽 시프트 2: {left_shift_2} (이진수: {bin(left_shift_2)})")
    print(f"왼쪽 시프트 3: {left_shift_3} (이진수: {bin(left_shift_3)})")
    
    # 오른쪽 시프트 (나눗셈과 유사)
    right_shift_1 = left_shift_3 >> 1  # 32
    right_shift_2 = left_shift_3 >> 2  # 16
    right_shift_3 = left_shift_3 >> 3  # 8
    
    print(f"오른쪽 시프트 1: {right_shift_1} (이진수: {bin(right_shift_1)})")
    print(f"오른쪽 시프트 2: {right_shift_2} (이진수: {bin(right_shift_2)})")
    print(f"오른쪽 시프트 3: {right_shift_3} (이진수: {bin(right_shift_3)})")

def practical_shift_uses():
    """시프트 연산의 실무 활용"""
    print("\n=== 시프트 연산 실무 활용 ===")
    
    # 2의 거듭제곱 계산
    def power_of_two(n):
        return 1 << n
    
    print("2의 거듭제곱:")
    for i in range(5):
        result = power_of_two(i)
        print(f"2^{i} = {result}")
    
    # 빠른 곱셈/나눗셈
    number = 25
    print(f"\n빠른 연산 (원본: {number}):")
    print(f"2로 곱하기: {number << 1}")
    print(f"4로 곱하기: {number << 2}")
    print(f"8로 곱하기: {number << 3}")
    print(f"2로 나누기: {number >> 1}")
    print(f"4로 나누기: {number >> 2}")
    print(f"8로 나누기: {number >> 3}")
    
    # RGB 색상 분리
    color = 0xFF5733  # 주황색
    red = (color >> 16) & 0xFF
    green = (color >> 8) & 0xFF
    blue = color & 0xFF
    
    print(f"\nRGB 색상 분리 (0x{color:06X}):")
    print(f"Red: {red}")
    print(f"Green: {green}")
    print(f"Blue: {blue}")

if __name__ == "__main__":
    basic_bitwise()
    practical_bitwise()
    bit_manipulation()
    shift_operations()
    practical_shift_uses()
