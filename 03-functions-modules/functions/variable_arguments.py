# 가변 인수

def sum_all(*numbers):
    """여러 숫자의 합을 계산하는 함수"""
    return sum(numbers)

def find_max(*values):
    """여러 값 중 최대값을 찾는 함수"""
    if not values:
        return None
    return max(values)

def print_items(*items, separator=", "):
    """여러 항목을 출력하는 함수"""
    print(separator.join(str(item) for item in items))

def create_dictionary(**kwargs):
    """키워드 인수로 딕셔너리를 생성하는 함수"""
    return kwargs

def process_user_data(*args, **kwargs):
    """위치 인수와 키워드 인수를 모두 처리하는 함수"""
    print("위치 인수:")
    for i, arg in enumerate(args):
        print(f"  {i}: {arg}")
    
    print("키워드 인수:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

def flexible_calculator(operation, *numbers, **options):
    """유연한 계산기 함수"""
    if not numbers:
        return 0
    
    if operation == "add":
        result = sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "average":
        result = sum(numbers) / len(numbers)
    else:
        return "지원하지 않는 연산입니다."
    
    # 옵션 처리
    if options.get("round", False):
        result = round(result)
    
    return result

def format_string(template, *args, **kwargs):
    """문자열 포맷팅 함수"""
    try:
        return template.format(*args, **kwargs)
    except (IndexError, KeyError) as e:
        return f"포맷팅 오류: {e}"

if __name__ == "__main__":
    # *args 사용
    total = sum_all(1, 2, 3, 4, 5)
    print(f"합계: {total}")
    
    maximum = find_max(10, 5, 8, 15, 3)
    print(f"최대값: {maximum}")
    
    print_items("사과", "바나나", "오렌지")
    print_items("A", "B", "C", separator=" | ")
    
    # **kwargs 사용
    user_dict = create_dictionary(name="김철수", age=30, city="서울")
    print(f"사용자 딕셔너리: {user_dict}")
    
    # *args와 **kwargs 함께 사용
    process_user_data("첫 번째", "두 번째", name="김철수", age=30)
    
    # 유연한 계산기
    result1 = flexible_calculator("add", 1, 2, 3, 4, 5)
    result2 = flexible_calculator("multiply", 2, 3, 4)
    result3 = flexible_calculator("average", 85, 92, 78, 96, round=True)
    print(f"덧셈: {result1}, 곱셈: {result2}, 평균: {result3}")
    
    # 문자열 포맷팅
    msg1 = format_string("안녕하세요, {}님!", "김철수")
    msg2 = format_string("이름: {name}, 나이: {age}", name="이영희", age=25)
    print(msg1)
    print(msg2)
