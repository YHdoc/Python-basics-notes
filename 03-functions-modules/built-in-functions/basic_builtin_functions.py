# 기본 내장 함수들

def demonstrate_basic_functions():
    """기본 내장 함수들을 보여주는 함수"""
    print("=== 기본 내장 함수들 ===")
    
    # print 함수
    print("Hello, World!")
    print("여러", "값을", "출력", sep="-", end="!\n")
    
    # input 함수
    # name = input("이름을 입력하세요: ")
    # print(f"안녕하세요, {name}님!")
    
    # len 함수
    text = "Python"
    numbers = [1, 2, 3, 4, 5]
    print(f"'{text}'의 길이: {len(text)}")
    print(f"리스트의 길이: {len(numbers)}")
    
    # type 함수
    print(f"42의 타입: {type(42)}")
    print(f"'Hello'의 타입: {type('Hello')}")
    print(f"[1, 2, 3]의 타입: {type([1, 2, 3])}")
    
    # id 함수
    x = 42
    y = 42
    print(f"x의 id: {id(x)}")
    print(f"y의 id: {id(y)}")
    print(f"x와 y가 같은 객체인가? {x is y}")

def demonstrate_type_conversion():
    """타입 변환 함수들을 보여주는 함수"""
    print("\n=== 타입 변환 함수들 ===")
    
    # int 함수
    print(f"int('123'): {int('123')}")
    print(f"int(3.14): {int(3.14)}")
    print(f"int('1010', 2): {int('1010', 2)}")  # 2진수
    
    # float 함수
    print(f"float('3.14'): {float('3.14')}")
    print(f"float(42): {float(42)}")
    
    # str 함수
    print(f"str(123): {str(123)}")
    print(f"str(3.14): {str(3.14)}")
    print(f"str([1, 2, 3]): {str([1, 2, 3])}")
    
    # bool 함수
    print(f"bool(1): {bool(1)}")
    print(f"bool(0): {bool(0)}")
    print(f"bool(''): {bool('')}")
    print(f"bool('Hello'): {bool('Hello')}")
    print(f"bool([]): {bool([])}")
    print(f"bool([1, 2, 3]): {bool([1, 2, 3])}")

def demonstrate_iteration_functions():
    """반복 관련 함수들을 보여주는 함수"""
    print("\n=== 반복 관련 함수들 ===")
    
    # range 함수
    print("range(5):", list(range(5)))
    print("range(2, 8):", list(range(2, 8)))
    print("range(0, 10, 2):", list(range(0, 10, 2)))
    
    # enumerate 함수
    fruits = ["apple", "banana", "orange"]
    print("enumerate(fruits):")
    for i, fruit in enumerate(fruits):
        print(f"  {i}: {fruit}")
    
    # zip 함수
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    print("zip(names, ages):")
    for name, age in zip(names, ages):
        print(f"  {name}: {age}세")

def demonstrate_utility_functions():
    """유틸리티 함수들을 보여주는 함수"""
    print("\n=== 유틸리티 함수들 ===")
    
    # all 함수
    print(f"all([True, True, True]): {all([True, True, True])}")
    print(f"all([True, False, True]): {all([True, False, True])}")
    print(f"all([]): {all([])}")  # 빈 리스트는 True
    
    # any 함수
    print(f"any([False, False, False]): {any([False, False, False])}")
    print(f"any([False, True, False]): {any([False, True, False])}")
    print(f"any([]): {any([])}")  # 빈 리스트는 False
    
    # sorted 함수
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"원본: {numbers}")
    print(f"sorted(numbers): {sorted(numbers)}")
    print(f"sorted(numbers, reverse=True): {sorted(numbers, reverse=True)}")
    
    # reversed 함수
    print(f"reversed(numbers): {list(reversed(numbers))}")

if __name__ == "__main__":
    demonstrate_basic_functions()
    demonstrate_type_conversion()
    demonstrate_iteration_functions()
    demonstrate_utility_functions()
