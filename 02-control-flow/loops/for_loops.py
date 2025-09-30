# for문 기본 사용법

def basic_for_loop():
    """기본 for문 사용법"""
    print("=== 기본 for문 ===")
    
    # 리스트 반복
    fruits = ["apple", "banana", "orange", "grape"]
    print("과일 목록:")
    for fruit in fruits:
        print(f"- {fruit}")
    
    # 문자열 반복
    word = "Python"
    print(f"\n'{word}'의 각 문자:")
    for char in word:
        print(f"- {char}")

def for_with_range():
    """range() 함수와 함께 사용하는 for문"""
    print("\n=== range() 함수와 for문 ===")
    
    # 기본 range 사용
    print("0부터 4까지:")
    for i in range(5):
        print(f"i = {i}")
    
    # 시작값과 끝값 지정
    print("\n5부터 9까지:")
    for i in range(5, 10):
        print(f"i = {i}")
    
    # 시작값, 끝값, 간격 지정
    print("\n0부터 10까지 2씩 증가:")
    for i in range(0, 11, 2):
        print(f"i = {i}")
    
    # 역순으로 반복
    print("\n10부터 0까지 역순:")
    for i in range(10, -1, -1):
        print(f"i = {i}")

def for_with_dictionaries():
    """딕셔너리와 함께 사용하는 for문"""
    print("\n=== 딕셔너리와 for문 ===")
    
    person = {
        "name": "김철수",
        "age": 25,
        "city": "서울",
        "job": "개발자"
    }
    
    # 키만 반복
    print("키들:")
    for key in person:
        print(f"- {key}")
    
    # 키와 값 함께 반복
    print("\n키와 값:")
    for key, value in person.items():
        print(f"{key}: {value}")
    
    # 값만 반복
    print("\n값들:")
    for value in person.values():
        print(f"- {value}")

def for_with_tuples():
    """튜플과 함께 사용하는 for문"""
    print("\n=== 튜플과 for문 ===")
    
    # 기본 튜플 반복
    coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
    print("좌표들:")
    for coord in coordinates:
        print(f"- {coord}")
    
    # 튜플 언패킹
    print("\n좌표 언패킹:")
    for x, y in coordinates:
        print(f"x: {x}, y: {y}")
    
    # 여러 튜플 동시 처리
    students = [
        ("Alice", 85, "A"),
        ("Bob", 92, "A"),
        ("Charlie", 78, "B")
    ]
    
    print("\n학생 성적:")
    for name, score, grade in students:
        print(f"{name}: {score}점 ({grade}등급)")

def for_with_sets():
    """집합과 함께 사용하는 for문"""
    print("\n=== 집합과 for문 ===")
    
    colors = {"red", "green", "blue", "yellow", "red"}  # 중복 제거됨
    print("색상들:")
    for color in colors:
        print(f"- {color}")
    
    # 집합 연산과 함께
    primary_colors = {"red", "blue", "yellow"}
    secondary_colors = {"green", "orange", "purple"}
    
    print("\n기본 색상:")
    for color in primary_colors:
        print(f"- {color}")
    
    print("\n보조 색상:")
    for color in secondary_colors:
        print(f"- {color}")

def practical_for_examples():
    """실무에서 자주 사용되는 for문 예제"""
    print("\n=== 실무 for문 예제 ===")
    
    # 리스트 처리
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 짝수만 출력
    print("짝수들:")
    for num in numbers:
        if num % 2 == 0:
            print(f"- {num}")
    
    # 제곱 계산
    print("\n제곱들:")
    for num in numbers:
        square = num ** 2
        print(f"{num}² = {square}")
    
    # 문자열 리스트 처리
    words = ["hello", "world", "python", "programming"]
    print("\n대문자로 변환:")
    for word in words:
        print(f"{word} -> {word.upper()}")
    
    # 파일명 처리 (가상의 예제)
    filenames = ["document.txt", "image.jpg", "data.csv", "script.py"]
    print("\n파일 확장자별 분류:")
    
    txt_files = []
    other_files = []
    
    for filename in filenames:
        if filename.endswith('.txt'):
            txt_files.append(filename)
        else:
            other_files.append(filename)
    
    print(f"텍스트 파일: {txt_files}")
    print(f"기타 파일: {other_files}")

def for_loop_patterns():
    """for문 패턴들"""
    print("\n=== for문 패턴들 ===")
    
    # 카운터 패턴
    print("카운터 패턴:")
    count = 0
    items = ["a", "b", "c", "d", "e"]
    for item in items:
        count += 1
        print(f"{count}. {item}")
    
    # 누적 패턴
    print("\n누적 패턴:")
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for num in numbers:
        total += num
        print(f"현재 합계: {total}")
    
    # 최대/최소 찾기 패턴
    print("\n최대/최소 찾기:")
    scores = [85, 92, 78, 96, 88, 91]
    max_score = scores[0]
    min_score = scores[0]
    
    for score in scores:
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
    
    print(f"최고 점수: {max_score}")
    print(f"최저 점수: {min_score}")

if __name__ == "__main__":
    basic_for_loop()
    for_with_range()
    for_with_dictionaries()
    for_with_tuples()
    for_with_sets()
    practical_for_examples()
    for_loop_patterns()
