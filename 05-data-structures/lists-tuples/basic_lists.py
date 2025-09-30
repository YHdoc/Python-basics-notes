# 리스트 기본 사용법

def demonstrate_list_creation():
    """리스트 생성 방법들을 보여주는 함수"""
    print("=== 리스트 생성 방법들 ===")
    
    # 빈 리스트 생성
    empty_list = []
    empty_list2 = list()
    print(f"빈 리스트: {empty_list}, {empty_list2}")
    
    # 직접 생성
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "orange"]
    mixed = [1, "hello", 3.14, True]
    print(f"숫자 리스트: {numbers}")
    print(f"문자열 리스트: {fruits}")
    print(f"혼합 리스트: {mixed}")
    
    # range()를 사용한 생성
    range_list = list(range(5))
    range_list2 = list(range(2, 10, 2))
    print(f"range(5): {range_list}")
    print(f"range(2, 10, 2): {range_list2}")
    
    # 문자열을 리스트로 변환
    string_list = list("Hello")
    print(f"문자열을 리스트로: {string_list}")

def demonstrate_list_access():
    """리스트 접근 방법들을 보여주는 함수"""
    print("\n=== 리스트 접근 방법들 ===")
    
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"원본 리스트: {numbers}")
    
    # 인덱스로 접근
    print(f"첫 번째 요소: {numbers[0]}")
    print(f"두 번째 요소: {numbers[1]}")
    print(f"마지막 요소: {numbers[-1]}")
    print(f"뒤에서 두 번째: {numbers[-2]}")
    
    # 슬라이싱
    print(f"처음 3개: {numbers[:3]}")
    print(f"마지막 3개: {numbers[-3:]}")
    print(f"중간 3개 (인덱스 2-4): {numbers[2:5]}")
    print(f"모든 요소 (2씩 건너뛰기): {numbers[::2]}")
    print(f"역순: {numbers[::-1]}")
    
    # 리스트 길이
    print(f"리스트 길이: {len(numbers)}")

def demonstrate_list_modification():
    """리스트 수정 방법들을 보여주는 함수"""
    print("\n=== 리스트 수정 방법들 ===")
    
    numbers = [1, 2, 3, 4, 5]
    print(f"원본: {numbers}")
    
    # 인덱스로 수정
    numbers[0] = 10
    print(f"첫 번째 요소 수정: {numbers}")
    
    # 슬라이싱으로 수정
    numbers[1:3] = [20, 30]
    print(f"슬라이싱으로 수정: {numbers}")
    
    # 여러 요소를 하나로 수정
    numbers[1:3] = [100]
    print(f"여러 요소를 하나로: {numbers}")
    
    # 빈 슬라이스에 삽입
    numbers[1:1] = [200, 300]
    print(f"빈 슬라이스에 삽입: {numbers}")

def demonstrate_list_operations():
    """리스트 연산들을 보여주는 함수"""
    print("\n=== 리스트 연산들 ===")
    
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    
    # 연결
    combined = list1 + list2
    print(f"리스트 연결: {list1} + {list2} = {combined}")
    
    # 반복
    repeated = list1 * 3
    print(f"리스트 반복: {list1} * 3 = {repeated}")
    
    # 멤버십 확인
    print(f"2가 list1에 있는가? {2 in list1}")
    print(f"7이 list1에 있는가? {7 in list1}")
    
    # 리스트 비교
    list3 = [1, 2, 3]
    print(f"list1 == list3? {list1 == list3}")
    print(f"list1 is list3? {list1 is list3}")

def demonstrate_nested_lists():
    """중첩 리스트를 보여주는 함수"""
    print("\n=== 중첩 리스트 ===")
    
    # 2차원 리스트 (행렬)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"2차원 리스트: {matrix}")
    
    # 접근
    print(f"첫 번째 행: {matrix[0]}")
    print(f"첫 번째 행의 두 번째 요소: {matrix[0][1]}")
    print(f"두 번째 열: {[row[1] for row in matrix]}")
    
    # 3차원 리스트
    cube = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ]
    print(f"3차원 리스트: {cube}")
    print(f"cube[0][1][0]: {cube[0][1][0]}")

def demonstrate_list_iteration():
    """리스트 순회 방법들을 보여주는 함수"""
    print("\n=== 리스트 순회 방법들 ===")
    
    fruits = ["apple", "banana", "orange", "grape"]
    
    # 기본 for문
    print("기본 for문:")
    for fruit in fruits:
        print(f"  {fruit}")
    
    # enumerate 사용
    print("\nenumerate 사용:")
    for i, fruit in enumerate(fruits):
        print(f"  {i}: {fruit}")
    
    # range와 인덱스 사용
    print("\nrange와 인덱스 사용:")
    for i in range(len(fruits)):
        print(f"  {i}: {fruits[i]}")
    
    # 역순 순회
    print("\n역순 순회:")
    for fruit in reversed(fruits):
        print(f"  {fruit}")

if __name__ == "__main__":
    demonstrate_list_creation()
    demonstrate_list_access()
    demonstrate_list_modification()
    demonstrate_list_operations()
    demonstrate_nested_lists()
    demonstrate_list_iteration()
