# 람다 함수 활용

def demonstrate_basic_lambda():
    """기본 람다 함수 예제"""
    print("=== 기본 람다 함수 ===")
    
    # 기본 람다 함수
    square = lambda x: x ** 2
    print(f"5의 제곱: {square(5)}")
    
    # 여러 매개변수
    add = lambda x, y: x + y
    print(f"3 + 4 = {add(3, 4)}")
    
    # 기본값이 있는 매개변수
    multiply = lambda x, y=2: x * y
    print(f"5 * 2 = {multiply(5)}")
    print(f"5 * 3 = {multiply(5, 3)}")

def demonstrate_lambda_with_built_in_functions():
    """내장 함수와 함께 사용하는 람다"""
    print("\n=== 내장 함수와 함께 사용 ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # map()과 함께 사용
    squares = list(map(lambda x: x**2, numbers))
    print(f"제곱수들: {squares}")
    
    # filter()와 함께 사용
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"짝수들: {even_numbers}")
    
    # sorted()와 함께 사용
    words = ["apple", "banana", "cherry", "date"]
    sorted_by_length = sorted(words, key=lambda x: len(x))
    print(f"길이순 정렬: {sorted_by_length}")

def demonstrate_lambda_with_sort():
    """정렬과 함께 사용하는 람다"""
    print("\n=== 정렬과 함께 사용 ===")
    
    # 학생 데이터
    students = [
        {"name": "김철수", "age": 20, "grade": 85},
        {"name": "이영희", "age": 19, "grade": 92},
        {"name": "박민수", "age": 21, "grade": 78},
        {"name": "최지영", "age": 20, "grade": 88}
    ]
    
    # 나이순 정렬
    sorted_by_age = sorted(students, key=lambda x: x["age"])
    print("나이순 정렬:")
    for student in sorted_by_age:
        print(f"  {student['name']}: {student['age']}세")
    
    # 성적순 정렬 (내림차순)
    sorted_by_grade = sorted(students, key=lambda x: x["grade"], reverse=True)
    print("\n성적순 정렬 (내림차순):")
    for student in sorted_by_grade:
        print(f"  {student['name']}: {student['grade']}점")

def demonstrate_lambda_with_reduce():
    """reduce()와 함께 사용하는 람다"""
    print("\n=== reduce()와 함께 사용 ===")
    
    from functools import reduce
    
    numbers = [1, 2, 3, 4, 5]
    
    # 합계 계산
    total = reduce(lambda x, y: x + y, numbers)
    print(f"합계: {total}")
    
    # 최대값 찾기
    maximum = reduce(lambda x, y: x if x > y else y, numbers)
    print(f"최대값: {maximum}")
    
    # 문자열 연결
    words = ["Hello", "World", "Python"]
    sentence = reduce(lambda x, y: x + " " + y, words)
    print(f"문장: {sentence}")

def demonstrate_lambda_with_list_comprehension():
    """리스트 컴프리헨션과 함께 사용하는 람다"""
    print("\n=== 리스트 컴프리헨션과 함께 사용 ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 람다 함수 정의
    is_even = lambda x: x % 2 == 0
    square = lambda x: x ** 2
    
    # 리스트 컴프리헨션에서 람다 사용
    even_squares = [square(x) for x in numbers if is_even(x)]
    print(f"짝수의 제곱: {even_squares}")
    
    # 더 복잡한 예제
    process_number = lambda x: x * 2 if x % 2 == 0 else x * 3
    processed_numbers = [process_number(x) for x in numbers]
    print(f"처리된 숫자들: {processed_numbers}")

def demonstrate_lambda_with_higher_order_functions():
    """고차 함수와 함께 사용하는 람다"""
    print("\n=== 고차 함수와 함께 사용 ===")
    
    def apply_operation(numbers, operation):
        """숫자 리스트에 연산을 적용하는 함수"""
        return [operation(x) for x in numbers]
    
    numbers = [1, 2, 3, 4, 5]
    
    # 다양한 연산 적용
    doubled = apply_operation(numbers, lambda x: x * 2)
    print(f"2배: {doubled}")
    
    squared = apply_operation(numbers, lambda x: x ** 2)
    print(f"제곱: {squared}")
    
    # 조건부 연산
    conditional = apply_operation(numbers, lambda x: x + 10 if x > 3 else x)
    print(f"조건부 연산: {conditional}")

def demonstrate_lambda_with_defaultdict():
    """defaultdict와 함께 사용하는 람다"""
    print("\n=== defaultdict와 함께 사용 ===")
    
    from collections import defaultdict
    
    # 기본값이 리스트인 defaultdict
    list_dict = defaultdict(lambda: [])
    list_dict["fruits"].append("apple")
    list_dict["fruits"].append("banana")
    list_dict["vegetables"].append("carrot")
    
    print("리스트 defaultdict:")
    for key, value in list_dict.items():
        print(f"  {key}: {value}")
    
    # 기본값이 0인 defaultdict
    counter_dict = defaultdict(lambda: 0)
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    
    for word in words:
        counter_dict[word] += 1
    
    print("\n단어 카운터:")
    for word, count in counter_dict.items():
        print(f"  {word}: {count}")

def demonstrate_lambda_with_event_handling():
    """이벤트 처리와 함께 사용하는 람다"""
    print("\n=== 이벤트 처리와 함께 사용 ===")
    
    class Button:
        def __init__(self, name):
            self.name = name
            self.click_handlers = []
        
        def on_click(self, handler):
            self.click_handlers.append(handler)
        
        def click(self):
            print(f"{self.name} 버튼이 클릭되었습니다!")
            for handler in self.click_handlers:
                handler()
    
    # 버튼 생성
    button = Button("저장")
    
    # 람다로 이벤트 핸들러 등록
    button.on_click(lambda: print("  데이터를 저장합니다."))
    button.on_click(lambda: print("  로그를 기록합니다."))
    button.on_click(lambda: print("  사용자에게 알림을 보냅니다."))
    
    # 버튼 클릭
    button.click()

def demonstrate_lambda_pitfalls():
    """람다 함수 사용 시 주의사항"""
    print("\n=== 람다 함수 주의사항 ===")
    
    # 문제가 있는 예제
    print("문제가 있는 예제:")
    functions = []
    for i in range(3):
        functions.append(lambda: i)  # 모든 람다가 같은 i를 참조
    
    for func in functions:
        print(f"  {func()}")  # 모두 2를 출력
    
    # 해결 방법 1: 기본값 사용
    print("\n해결 방법 1 (기본값 사용):")
    functions = []
    for i in range(3):
        functions.append(lambda x=i: x)  # 기본값으로 i의 현재 값 저장
    
    for func in functions:
        print(f"  {func()}")
    
    # 해결 방법 2: 클로저 사용
    print("\n해결 방법 2 (클로저 사용):")
    def create_lambda(x):
        return lambda: x
    
    functions = []
    for i in range(3):
        functions.append(create_lambda(i))
    
    for func in functions:
        print(f"  {func()}")

def demonstrate_lambda_vs_regular_function():
    """람다 vs 일반 함수 비교"""
    print("\n=== 람다 vs 일반 함수 ===")
    
    # 람다 함수
    lambda_square = lambda x: x ** 2
    
    # 일반 함수
    def regular_square(x):
        return x ** 2
    
    # 성능 테스트
    import time
    
    numbers = list(range(1000000))
    
    # 람다 함수 테스트
    start_time = time.time()
    result1 = list(map(lambda_square, numbers))
    lambda_time = time.time() - start_time
    
    # 일반 함수 테스트
    start_time = time.time()
    result2 = list(map(regular_square, numbers))
    regular_time = time.time() - start_time
    
    print(f"람다 함수 시간: {lambda_time:.4f}초")
    print(f"일반 함수 시간: {regular_time:.4f}초")
    print(f"결과 동일: {result1 == result2}")

def demonstrate_practical_lambda_examples():
    """실용적인 람다 예제"""
    print("\n=== 실용적인 람다 예제 ===")
    
    # 1. 데이터 정제
    raw_data = ["  apple  ", "BANANA", "  Cherry  ", "DATE"]
    cleaned_data = list(map(lambda x: x.strip().lower(), raw_data))
    print(f"정제된 데이터: {cleaned_data}")
    
    # 2. 조건부 필터링
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = list(filter(lambda x: x % 3 == 0 and x > 5, numbers))
    print(f"3의 배수이면서 5보다 큰 수: {filtered_numbers}")
    
    # 3. 복잡한 정렬
    people = [
        ("김철수", 25, "개발자"),
        ("이영희", 30, "디자이너"),
        ("박민수", 22, "기획자"),
        ("최지영", 28, "개발자")
    ]
    
    # 직업별, 나이순 정렬
    sorted_people = sorted(people, key=lambda x: (x[2], x[1]))
    print("직업별, 나이순 정렬:")
    for person in sorted_people:
        print(f"  {person[0]} ({person[1]}세, {person[2]})")

if __name__ == "__main__":
    demonstrate_basic_lambda()
    demonstrate_lambda_with_built_in_functions()
    demonstrate_lambda_with_sort()
    demonstrate_lambda_with_reduce()
    demonstrate_lambda_with_list_comprehension()
    demonstrate_lambda_with_higher_order_functions()
    demonstrate_lambda_with_defaultdict()
    demonstrate_lambda_with_event_handling()
    demonstrate_lambda_pitfalls()
    demonstrate_lambda_vs_regular_function()
    demonstrate_practical_lambda_examples()
