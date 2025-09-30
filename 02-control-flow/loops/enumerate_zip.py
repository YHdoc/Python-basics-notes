# enumerate()와 zip() 활용

def basic_enumerate():
    """기본 enumerate() 사용법"""
    print("=== 기본 enumerate() 사용법 ===")
    
    # 리스트와 함께 사용
    fruits = ["apple", "banana", "orange", "grape"]
    print("인덱스와 함께 출력:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    # 시작값 지정
    print("\n시작값 1로 지정:")
    for index, fruit in enumerate(fruits, 1):
        print(f"  {index}: {fruit}")

def enumerate_with_conditions():
    """조건문과 함께 사용하는 enumerate()"""
    print("\n=== 조건문과 함께 사용하는 enumerate() ===")
    
    numbers = [10, 25, 30, 45, 50, 65, 70, 85, 90]
    
    # 특정 조건을 만족하는 요소의 인덱스 찾기
    print("30보다 큰 수의 인덱스:")
    for index, num in enumerate(numbers):
        if num > 30:
            print(f"  인덱스 {index}: {num}")
    
    # 짝수 인덱스의 요소만 출력
    print("\n짝수 인덱스의 요소:")
    for index, num in enumerate(numbers):
        if index % 2 == 0:
            print(f"  인덱스 {index}: {num}")

def basic_zip():
    """기본 zip() 사용법"""
    print("\n=== 기본 zip() 사용법 ===")
    
    # 두 리스트를 함께 반복
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    
    print("이름과 나이:")
    for name, age in zip(names, ages):
        print(f"  {name}: {age}세")
    
    # 세 개 이상의 리스트
    cities = ["Seoul", "Busan", "Daegu"]
    print("\n이름, 나이, 도시:")
    for name, age, city in zip(names, ages, cities):
        print(f"  {name}: {age}세, {city}")

def zip_with_different_lengths():
    """길이가 다른 시퀀스와 zip()"""
    print("\n=== 길이가 다른 시퀀스와 zip() ===")
    
    # 길이가 다른 리스트들
    short_list = [1, 2, 3]
    long_list = [10, 20, 30, 40, 50]
    
    print("짧은 리스트 기준으로 zip:")
    for a, b in zip(short_list, long_list):
        print(f"  {a} + {b} = {a + b}")
    
    # itertools.zip_longest 사용 (모든 요소 처리)
    from itertools import zip_longest
    print("\n모든 요소 처리 (zip_longest):")
    for a, b in zip_longest(short_list, long_list, fillvalue=0):
        print(f"  {a} + {b} = {a + b}")

def enumerate_with_zip():
    """enumerate()와 zip() 조합"""
    print("\n=== enumerate()와 zip() 조합 ===")
    
    students = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    grades = ["B", "A", "C"]
    
    print("학생 성적표:")
    for i, (name, score, grade) in enumerate(zip(students, scores, grades), 1):
        print(f"  {i}. {name}: {score}점 ({grade}등급)")

def practical_enumerate_examples():
    """실무에서 자주 사용되는 enumerate() 예제"""
    print("\n=== 실무 enumerate() 예제 ===")
    
    # 리스트에서 특정 값의 모든 인덱스 찾기
    numbers = [1, 3, 2, 3, 4, 3, 5]
    target = 3
    
    print(f"{target}의 모든 인덱스:")
    indices = []
    for index, num in enumerate(numbers):
        if num == target:
            indices.append(index)
    
    print(f"  인덱스들: {indices}")
    
    # 리스트에서 최대값의 인덱스 찾기
    print("\n최대값의 인덱스:")
    max_value = max(numbers)
    max_index = numbers.index(max_value)
    print(f"  최대값: {max_value}, 인덱스: {max_index}")
    
    # enumerate로 최대값의 인덱스 찾기
    max_index = 0
    for index, num in enumerate(numbers):
        if num > numbers[max_index]:
            max_index = index
    
    print(f"  최대값: {numbers[max_index]}, 인덱스: {max_index}")

def practical_zip_examples():
    """실무에서 자주 사용되는 zip() 예제"""
    print("\n=== 실무 zip() 예제 ===")
    
    # 딕셔너리 생성
    keys = ["name", "age", "city"]
    values = ["김철수", 25, "서울"]
    
    person_dict = dict(zip(keys, values))
    print(f"딕셔너리 생성: {person_dict}")
    
    # 두 리스트를 딕셔너리로 변환
    products = ["노트북", "마우스", "키보드"]
    prices = [1500000, 25000, 80000]
    
    price_dict = dict(zip(products, prices))
    print(f"가격표: {price_dict}")
    
    # 리스트 전치 (행렬의 행과 열 바꾸기)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("\n원본 행렬:")
    for row in matrix:
        print(f"  {row}")
    
    print("전치된 행렬:")
    transposed = list(zip(*matrix))
    for row in transposed:
        print(f"  {list(row)}")

def advanced_enumerate_zip():
    """고급 enumerate()와 zip() 사용법"""
    print("\n=== 고급 enumerate()와 zip() 사용법 ===")
    
    # enumerate로 리스트 수정
    numbers = [1, 2, 3, 4, 5]
    print(f"원본: {numbers}")
    
    # 각 요소에 인덱스 더하기
    for i, num in enumerate(numbers):
        numbers[i] = num + i
    
    print(f"수정 후: {numbers}")
    
    # zip으로 여러 리스트 동시 처리
    list1 = [1, 2, 3, 4]
    list2 = [10, 20, 30, 40]
    list3 = [100, 200, 300, 400]
    
    print("\n여러 리스트 동시 처리:")
    results = []
    for a, b, c in zip(list1, list2, list3):
        result = a + b + c
        results.append(result)
        print(f"  {a} + {b} + {c} = {result}")
    
    print(f"결과 리스트: {results}")

def performance_comparison():
    """성능 비교"""
    print("\n=== 성능 비교 ===")
    
    # enumerate vs range + len
    items = list(range(1000))
    
    print("enumerate 사용:")
    for i, item in enumerate(items[:5]):  # 처음 5개만
        print(f"  {i}: {item}")
    
    print("\nrange + len 사용:")
    for i in range(len(items[:5])):  # 처음 5개만
        print(f"  {i}: {items[i]}")
    
    # zip vs 인덱스 접근
    list_a = [1, 2, 3, 4, 5]
    list_b = [10, 20, 30, 40, 50]
    
    print("\nzip 사용:")
    for a, b in zip(list_a, list_b):
        print(f"  {a} + {b} = {a + b}")
    
    print("\n인덱스 접근:")
    for i in range(len(list_a)):
        print(f"  {list_a[i]} + {list_b[i]} = {list_a[i] + list_b[i]}")

def common_mistakes():
    """자주 하는 실수들"""
    print("\n=== 자주 하는 실수들 ===")
    
    # enumerate 결과를 리스트로 변환하지 않고 사용
    print("enumerate 결과 확인:")
    result = enumerate(["a", "b", "c"])
    print(f"  enumerate 객체: {result}")
    print(f"  리스트로 변환: {list(result)}")
    
    # zip 결과를 리스트로 변환하지 않고 사용
    print("\nzip 결과 확인:")
    result = zip([1, 2, 3], [4, 5, 6])
    print(f"  zip 객체: {result}")
    print(f"  리스트로 변환: {list(result)}")
    
    # 한 번 사용한 후 다시 사용하려고 시도
    print("\n한 번 사용한 후 다시 사용:")
    items = enumerate(["a", "b", "c"])
    print(f"  첫 번째 사용: {list(items)}")
    print(f"  두 번째 사용: {list(items)}")  # 빈 리스트

if __name__ == "__main__":
    basic_enumerate()
    enumerate_with_conditions()
    basic_zip()
    zip_with_different_lengths()
    enumerate_with_zip()
    practical_enumerate_examples()
    practical_zip_examples()
    advanced_enumerate_zip()
    performance_comparison()
    common_mistakes()
