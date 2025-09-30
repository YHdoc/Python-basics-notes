# 반환값과 return 문

def add_numbers(a, b):
    """두 숫자를 더하고 결과를 반환하는 함수"""
    result = a + b
    return result

def get_user_info():
    """사용자 정보를 반환하는 함수"""
    return {
        "name": "김철수",
        "age": 30,
        "email": "kim@example.com"
    }

def check_even_odd(number):
    """짝수/홀수를 확인하고 문자열을 반환하는 함수"""
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"

def calculate_statistics(numbers):
    """숫자 리스트의 통계를 계산하는 함수"""
    if not numbers:
        return None
    
    stats = {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }
    return stats

def find_element_index(items, target):
    """리스트에서 특정 요소의 인덱스를 찾는 함수"""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1  # 찾지 못한 경우

def process_data(data):
    """데이터를 처리하고 여러 값을 반환하는 함수"""
    if not data:
        return None, None, None
    
    processed = [item * 2 for item in data if item > 0]
    count = len(processed)
    total = sum(processed)
    
    return processed, count, total

def validate_input(value, min_val=0, max_val=100):
    """입력값을 검증하고 결과를 반환하는 함수"""
    if not isinstance(value, (int, float)):
        return False, "숫자가 아닙니다"
    
    if value < min_val:
        return False, f"최소값 {min_val}보다 작습니다"
    
    if value > max_val:
        return False, f"최대값 {max_val}보다 큽니다"
    
    return True, "유효한 값입니다"

if __name__ == "__main__":
    # 단일 값 반환
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    # 딕셔너리 반환
    user = get_user_info()
    print(f"사용자: {user['name']}, 나이: {user['age']}")
    
    # 조건부 반환
    print(f"8은 {check_even_odd(8)}입니다")
    print(f"7은 {check_even_odd(7)}입니다")
    
    # 복잡한 데이터 반환
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stats = calculate_statistics(numbers)
    if stats:
        print(f"통계: {stats}")
    
    # 인덱스 찾기
    fruits = ["사과", "바나나", "오렌지", "포도"]
    index = find_element_index(fruits, "오렌지")
    print(f"오렌지의 인덱스: {index}")
    
    # 여러 값 반환
    data = [1, -2, 3, -4, 5]
    processed, count, total = process_data(data)
    print(f"처리된 데이터: {processed}")
    print(f"개수: {count}, 합계: {total}")
    
    # 검증 결과 반환
    is_valid1, message1 = validate_input(50)
    is_valid2, message2 = validate_input(150)
    is_valid3, message3 = validate_input("abc")
    
    print(f"50 검증: {is_valid1}, {message1}")
    print(f"150 검증: {is_valid2}, {message2}")
    print(f"'abc' 검증: {is_valid3}, {message3}")
