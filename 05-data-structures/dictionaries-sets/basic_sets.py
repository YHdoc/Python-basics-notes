# 집합 기본 사용법

def demonstrate_set_creation():
    """집합 생성 방법들을 보여주는 함수"""
    print("=== 집합 생성 방법들 ===")
    
    # 빈 집합 생성
    empty_set = set()
    # empty_set = {}  # 이건 딕셔너리!
    print(f"빈 집합: {empty_set}")
    
    # 직접 생성
    fruits = {"apple", "banana", "orange"}
    numbers = {1, 2, 3, 4, 5}
    mixed = {1, "hello", 3.14, True}
    print(f"과일 집합: {fruits}")
    print(f"숫자 집합: {numbers}")
    print(f"혼합 집합: {mixed}")
    
    # set() 생성자 사용
    from_list = set([1, 2, 2, 3, 3, 3, 4])
    from_string = set("hello")
    from_tuple = set((1, 2, 3, 4, 5))
    print(f"리스트에서 생성: {from_list}")  # 중복 제거됨
    print(f"문자열에서 생성: {from_string}")
    print(f"튜플에서 생성: {from_tuple}")

def demonstrate_set_operations():
    """집합 연산들을 보여주는 함수"""
    print("\n=== 집합 연산들 ===")
    
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"set1: {set1}")
    print(f"set2: {set2}")
    
    # 합집합 (union)
    union = set1 | set2
    union_method = set1.union(set2)
    print(f"합집합 (|): {union}")
    print(f"합집합 (union()): {union_method}")
    
    # 교집합 (intersection)
    intersection = set1 & set2
    intersection_method = set1.intersection(set2)
    print(f"교집합 (&): {intersection}")
    print(f"교집합 (intersection()): {intersection_method}")
    
    # 차집합 (difference)
    difference = set1 - set2
    difference_method = set1.difference(set2)
    print(f"차집합 (-): {difference}")
    print(f"차집합 (difference()): {difference_method}")
    
    # 대칭차집합 (symmetric difference)
    symmetric_diff = set1 ^ set2
    symmetric_diff_method = set1.symmetric_difference(set2)
    print(f"대칭차집합 (^): {symmetric_diff}")
    print(f"대칭차집합 (symmetric_difference()): {symmetric_diff_method}")

def demonstrate_set_methods():
    """집합 메서드들을 보여주는 함수"""
    print("\n=== 집합 메서드들 ===")
    
    fruits = {"apple", "banana", "orange"}
    print(f"원본 집합: {fruits}")
    
    # 추가 메서드들
    fruits.add("grape")
    print(f"add('grape'): {fruits}")
    
    fruits.update(["kiwi", "mango"])
    print(f"update(['kiwi', 'mango']): {fruits}")
    
    # 삭제 메서드들
    fruits.remove("banana")
    print(f"remove('banana'): {fruits}")
    
    fruits.discard("kiwi")
    print(f"discard('kiwi'): {fruits}")
    
    # discard()는 키가 없어도 에러가 발생하지 않음
    fruits.discard("nonexistent")
    print(f"discard('nonexistent'): {fruits}")
    
    # pop() - 임의의 요소 제거
    popped = fruits.pop()
    print(f"pop(): {fruits}, 제거된 요소: {popped}")
    
    # clear() - 모든 요소 제거
    fruits.clear()
    print(f"clear(): {fruits}")

def demonstrate_set_comparison():
    """집합 비교 메서드들을 보여주는 함수"""
    print("\n=== 집합 비교 메서드들 ===")
    
    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5}
    set3 = {1, 2, 3}
    set4 = {4, 5, 6}
    
    print(f"set1: {set1}")
    print(f"set2: {set2}")
    print(f"set3: {set3}")
    print(f"set4: {set4}")
    
    # 부분집합 확인
    print(f"set1.issubset(set2): {set1.issubset(set2)}")
    print(f"set1 <= set2: {set1 <= set2}")
    
    # 진부분집합 확인
    print(f"set1 < set2: {set1 < set2}")
    print(f"set1 < set3: {set1 < set3}")
    
    # 상위집합 확인
    print(f"set2.issuperset(set1): {set2.issuperset(set1)}")
    print(f"set2 >= set1: {set2 >= set1}")
    
    # 진상위집합 확인
    print(f"set2 > set1: {set2 > set1}")
    
    # 교집합이 없는지 확인
    print(f"set1.isdisjoint(set4): {set1.isdisjoint(set4)}")
    print(f"set1.isdisjoint(set2): {set1.isdisjoint(set2)}")

def demonstrate_set_iteration():
    """집합 순회 방법들을 보여주는 함수"""
    print("\n=== 집합 순회 방법들 ===")
    
    colors = {"red", "green", "blue", "yellow", "purple"}
    print(f"원본 집합: {colors}")
    
    # 기본 for문
    print("기본 for문:")
    for color in colors:
        print(f"  {color}")
    
    # enumerate 사용
    print("\nenumerate 사용:")
    for i, color in enumerate(colors):
        print(f"  {i}: {color}")
    
    # sorted()로 정렬된 순회
    print("\n정렬된 순회:")
    for color in sorted(colors):
        print(f"  {color}")

def demonstrate_practical_examples():
    """실무에서 자주 사용되는 집합 예제"""
    print("\n=== 실무 예제 ===")
    
    # 중복 제거
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    unique_numbers = set(numbers)
    print(f"원본 리스트: {numbers}")
    print(f"중복 제거: {unique_numbers}")
    
    # 두 리스트의 공통 요소 찾기
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common = set(list1) & set(list2)
    print(f"리스트1: {list1}")
    print(f"리스트2: {list2}")
    print(f"공통 요소: {common}")
    
    # 두 리스트의 차이점 찾기
    only_in_list1 = set(list1) - set(list2)
    only_in_list2 = set(list2) - set(list1)
    print(f"list1에만 있는 요소: {only_in_list1}")
    print(f"list2에만 있는 요소: {only_in_list2}")
    
    # 단어 빈도 분석
    text = "apple banana apple orange banana apple"
    words = text.split()
    unique_words = set(words)
    print(f"텍스트: {text}")
    print(f"고유 단어: {unique_words}")
    print(f"고유 단어 개수: {len(unique_words)}")

if __name__ == "__main__":
    demonstrate_set_creation()
    demonstrate_set_operations()
    demonstrate_set_methods()
    demonstrate_set_comparison()
    demonstrate_set_iteration()
    demonstrate_practical_examples()
