# 리스트 컴프리헨션

def demonstrate_basic_comprehension():
    """기본 리스트 컴프리헨션을 보여주는 함수"""
    print("=== 기본 리스트 컴프리헨션 ===")
    
    # 기본 형태: [expression for item in iterable]
    squares = [x**2 for x in range(10)]
    print(f"제곱수: {squares}")
    
    # 문자열 처리
    words = ["hello", "world", "python"]
    upper_words = [word.upper() for word in words]
    print(f"대문자 변환: {upper_words}")
    
    # 길이 계산
    lengths = [len(word) for word in words]
    print(f"단어 길이: {lengths}")
    
    # 수학 연산
    numbers = [1, 2, 3, 4, 5]
    doubled = [x * 2 for x in numbers]
    print(f"2배: {doubled}")

def demonstrate_conditional_comprehension():
    """조건부 리스트 컴프리헨션을 보여주는 함수"""
    print("\n=== 조건부 리스트 컴프리헨션 ===")
    
    # 기본 조건: [expression for item in iterable if condition]
    even_numbers = [x for x in range(20) if x % 2 == 0]
    print(f"짝수: {even_numbers}")
    
    # 복잡한 조건
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered = [x for x in numbers if x > 5 and x % 2 == 0]
    print(f"5보다 크고 짝수: {filtered}")
    
    # 문자열 필터링
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    long_words = [word for word in words if len(word) > 5]
    print(f"5글자 이상 단어: {long_words}")
    
    # 특정 문자 포함
    a_words = [word for word in words if 'a' in word]
    print(f"'a' 포함 단어: {a_words}")

def demonstrate_nested_comprehension():
    """중첩 리스트 컴프리헨션을 보여주는 함수"""
    print("\n=== 중첩 리스트 컴프리헨션 ===")
    
    # 2차원 리스트 생성
    matrix = [[i + j for j in range(3)] for i in range(3)]
    print(f"3x3 행렬: {matrix}")
    
    # 평면화 (flatten)
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [item for sublist in nested_list for item in sublist]
    print(f"중첩 리스트: {nested_list}")
    print(f"평면화: {flattened}")
    
    # 조건부 중첩
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
    print(f"원본 행렬: {matrix}")
    print(f"짝수만: {even_matrix}")

def demonstrate_complex_comprehension():
    """복잡한 리스트 컴프리헨션을 보여주는 함수"""
    print("\n=== 복잡한 리스트 컴프리헨션 ===")
    
    # 여러 조건과 변환
    numbers = range(1, 21)
    result = [x**2 for x in numbers if x % 2 == 0 if x > 10]
    print(f"10보다 크고 짝수인 수의 제곱: {result}")
    
    # 삼항 연산자 사용
    numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
    absolute = [x if x >= 0 else -x for x in numbers]
    print(f"절댓값: {absolute}")
    
    # 문자열 처리
    sentences = ["Hello World", "Python Programming", "Data Science"]
    words = [word.lower() for sentence in sentences for word in sentence.split()]
    print(f"모든 단어 (소문자): {words}")

def demonstrate_performance_comparison():
    """성능 비교를 보여주는 함수"""
    print("\n=== 성능 비교 ===")
    
    # 전통적인 방법 vs 컴프리헨션
    print("전통적인 방법:")
    squares_traditional = []
    for x in range(10):
        squares_traditional.append(x**2)
    print(f"결과: {squares_traditional}")
    
    print("컴프리헨션:")
    squares_comprehension = [x**2 for x in range(10)]
    print(f"결과: {squares_comprehension}")
    
    # 필터링 비교
    numbers = list(range(20))
    
    print("\n전통적인 필터링:")
    even_traditional = []
    for x in numbers:
        if x % 2 == 0:
            even_traditional.append(x)
    print(f"결과: {even_traditional}")
    
    print("컴프리헨션 필터링:")
    even_comprehension = [x for x in numbers if x % 2 == 0]
    print(f"결과: {even_comprehension}")

def demonstrate_practical_examples():
    """실무에서 자주 사용되는 컴프리헨션 예제"""
    print("\n=== 실무 예제 ===")
    
    # 데이터 정제
    raw_data = ["  apple  ", "banana", "  cherry  ", "date", "  elderberry  "]
    cleaned_data = [item.strip() for item in raw_data]
    print(f"원본 데이터: {raw_data}")
    print(f"정제된 데이터: {cleaned_data}")
    
    # 데이터 변환
    prices = [10.5, 20.3, 15.7, 8.9, 12.4]
    prices_with_tax = [price * 1.1 for price in prices]
    print(f"원가: {prices}")
    print(f"세금 포함: {[f'{price:.2f}' for price in prices_with_tax]}")
    
    # 조건부 데이터 처리
    scores = [85, 92, 78, 96, 88, 91, 75, 83, 90, 87]
    passed_scores = [score for score in scores if score >= 80]
    print(f"모든 점수: {scores}")
    print(f"합격 점수 (80점 이상): {passed_scores}")
    
    # 딕셔너리에서 리스트 생성
    student_data = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 96
    }
    top_students = [name for name, score in student_data.items() if score >= 90]
    print(f"우수 학생 (90점 이상): {top_students}")
    
    # 파일명 처리
    filenames = ["document.txt", "image.jpg", "data.csv", "script.py"]
    python_files = [filename for filename in filenames if filename.endswith('.py')]
    print(f"Python 파일: {python_files}")

def demonstrate_advanced_patterns():
    """고급 패턴들을 보여주는 함수"""
    print("\n=== 고급 패턴들 ===")
    
    # 중복 제거 (순서 유지)
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique_numbers = []
    [unique_numbers.append(x) for x in numbers if x not in unique_numbers]
    print(f"중복 제거: {unique_numbers}")
    
    # 그룹화
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    grouped = {}
    [grouped.setdefault(len(word), []).append(word) for word in words]
    print(f"길이별 그룹화: {grouped}")
    
    # 조건부 변환
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    processed = [x**2 if x % 2 == 0 else x*2 for x in data]
    print(f"조건부 변환: {processed}")

if __name__ == "__main__":
    demonstrate_basic_comprehension()
    demonstrate_conditional_comprehension()
    demonstrate_nested_comprehension()
    demonstrate_complex_comprehension()
    demonstrate_performance_comparison()
    demonstrate_practical_examples()
    demonstrate_advanced_patterns()
