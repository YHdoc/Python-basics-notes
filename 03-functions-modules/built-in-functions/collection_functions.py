# 컬렉션 관련 함수들

def demonstrate_collection_functions():
    """컬렉션 관련 함수들을 보여주는 함수"""
    print("=== 컬렉션 관련 함수들 ===")
    
    # list 함수
    print(f"list('hello'): {list('hello')}")
    print(f"list(range(5)): {list(range(5))}")
    print(f"list((1, 2, 3)): {list((1, 2, 3))}")
    
    # tuple 함수
    print(f"tuple('hello'): {tuple('hello')}")
    print(f"tuple([1, 2, 3]): {tuple([1, 2, 3])}")
    print(f"tuple(range(3)): {tuple(range(3))}")
    
    # set 함수
    print(f"set('hello'): {set('hello')}")
    print(f"set([1, 2, 2, 3, 3, 4]): {set([1, 2, 2, 3, 3, 4])}")
    
    # dict 함수
    print(f"dict([('a', 1), ('b', 2)]): {dict([('a', 1), ('b', 2)])}")
    print(f"dict(a=1, b=2): {dict(a=1, b=2)}")
    
    # frozenset 함수
    frozen = frozenset([1, 2, 3, 4])
    print(f"frozenset([1, 2, 3, 4]): {frozen}")

def demonstrate_iteration_functions():
    """반복 관련 함수들을 보여주는 함수"""
    print("\n=== 반복 관련 함수들 ===")
    
    # iter 함수
    numbers = [1, 2, 3, 4, 5]
    iterator = iter(numbers)
    print(f"iter(numbers): {iterator}")
    print(f"next(iterator): {next(iterator)}")
    print(f"next(iterator): {next(iterator)}")
    
    # enumerate 함수
    fruits = ["apple", "banana", "orange"]
    print("enumerate(fruits):")
    for i, fruit in enumerate(fruits):
        print(f"  {i}: {fruit}")
    
    # zip 함수
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["Seoul", "Busan", "Daegu"]
    
    print("zip(names, ages, cities):")
    for name, age, city in zip(names, ages, cities):
        print(f"  {name}: {age}세, {city}")
    
    # reversed 함수
    print(f"reversed([1, 2, 3, 4, 5]): {list(reversed([1, 2, 3, 4, 5]))}")

def demonstrate_filtering_functions():
    """필터링 관련 함수들을 보여주는 함수"""
    print("\n=== 필터링 관련 함수들 ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # filter 함수
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"짝수: {even_numbers}")
    
    # map 함수
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"제곱수: {squares}")
    
    # all 함수
    print(f"모든 수가 5보다 작은가? {all(x < 5 for x in numbers)}")
    print(f"모든 수가 10보다 작은가? {all(x < 10 for x in numbers)}")
    
    # any 함수
    print(f"5보다 큰 수가 있는가? {any(x > 5 for x in numbers)}")
    print(f"10보다 큰 수가 있는가? {any(x > 10 for x in numbers)}")

def demonstrate_sorting_functions():
    """정렬 관련 함수들을 보여주는 함수"""
    print("\n=== 정렬 관련 함수들 ===")
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"원본: {numbers}")
    
    # sorted 함수
    print(f"sorted(numbers): {sorted(numbers)}")
    print(f"sorted(numbers, reverse=True): {sorted(numbers, reverse=True)}")
    
    # 문자열 정렬
    words = ["banana", "apple", "cherry", "date"]
    print(f"원본: {words}")
    print(f"sorted(words): {sorted(words)}")
    print(f"sorted(words, key=len): {sorted(words, key=len)}")
    
    # 딕셔너리 정렬
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}
    print(f"원본: {scores}")
    print(f"키로 정렬: {sorted(scores.items())}")
    print(f"값으로 정렬: {sorted(scores.items(), key=lambda x: x[1])}")

def demonstrate_utility_functions():
    """유틸리티 함수들을 보여주는 함수"""
    print("\n=== 유틸리티 함수들 ===")
    
    # len 함수
    data = [1, 2, 3, 4, 5]
    print(f"len([1, 2, 3, 4, 5]): {len(data)}")
    print(f"len('Hello'): {len('Hello')}")
    print(f"len({'a': 1, 'b': 2}): {len({'a': 1, 'b': 2})}")
    
    # sum 함수
    print(f"sum([1, 2, 3, 4, 5]): {sum([1, 2, 3, 4, 5])}")
    print(f"sum(range(10)): {sum(range(10))}")
    
    # min, max 함수
    numbers = [10, 5, 8, 3, 7]
    print(f"min([10, 5, 8, 3, 7]): {min(numbers)}")
    print(f"max([10, 5, 8, 3, 7]): {max(numbers)}")
    
    # range 함수
    print(f"list(range(5)): {list(range(5))}")
    print(f"list(range(2, 8)): {list(range(2, 8))}")
    print(f"list(range(0, 10, 2)): {list(range(0, 10, 2))}")

if __name__ == "__main__":
    demonstrate_collection_functions()
    demonstrate_iteration_functions()
    demonstrate_filtering_functions()
    demonstrate_sorting_functions()
    demonstrate_utility_functions()
