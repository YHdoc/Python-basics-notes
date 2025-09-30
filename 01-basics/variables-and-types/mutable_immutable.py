# Mutable vs Immutable 정리

def demonstrate_basic_concept():
    """Mutable과 Immutable의 기본 개념"""
    print("=== Mutable vs Immutable 기본 개념 ===")
    
    # Immutable 예시 (int)
    print("\n1. Immutable 타입 (int):")
    x = 5
    print(f"초기값: x = {x}, id: {id(x)}")
    
    x = 6  # 새로운 객체 생성
    print(f"변경후: x = {x}, id: {id(x)}")
    print("→ id가 다름! 새로운 객체가 생성됨")
    
    # Mutable 예시 (list)
    print("\n2. Mutable 타입 (list):")
    lst = [1, 2, 3]
    print(f"초기값: lst = {lst}, id: {id(lst)}")
    
    lst[0] = 10  # 기존 객체 수정
    print(f"변경후: lst = {lst}, id: {id(lst)}")
    print("→ id가 같음! 같은 객체를 수정함")

def demonstrate_type_classification():
    """타입별 분류"""
    print("\n=== 타입별 분류 ===")
    
    print("📦 Immutable 타입들:")
    immutable_types = [
        ("int", 42),
        ("float", 3.14),
        ("bool", True),
        ("str", "hello"),
        ("tuple", (1, 2, 3)),
        ("frozenset", frozenset([1, 2, 3])),
        ("bytes", b"hello")
    ]
    
    for type_name, value in immutable_types:
        print(f"  - {type_name}: {value}")
    
    print("\n📦 Mutable 타입들:")
    mutable_types = [
        ("list", [1, 2, 3]),
        ("dict", {"key": "value"}),
        ("set", {1, 2, 3}),
        ("bytearray", bytearray(b"hello"))
    ]
    
    for type_name, value in mutable_types:
        print(f"  - {type_name}: {value}")

def demonstrate_id_experiment():
    """id() 함수로 메모리 주소 확인"""
    print("\n=== id() 함수로 메모리 주소 확인 ===")
    
    # Immutable 실험
    print("1. Immutable (str) 실험:")
    s1 = "hello"
    s2 = "hello"
    print(f"s1 = '{s1}', id: {id(s1)}")
    print(f"s2 = '{s2}', id: {id(s2)}")
    print(f"같은 문자열이므로 같은 객체: {s1 is s2}")
    
    s1 += " world"  # 새로운 문자열 생성
    print(f"s1 += ' world' 후: '{s1}', id: {id(s1)}")
    print("→ 새로운 객체가 생성됨!")
    
    # Mutable 실험
    print("\n2. Mutable (list) 실험:")
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    print(f"lst1 = {lst1}, id: {id(lst1)}")
    print(f"lst2 = {lst2}, id: {id(lst2)}")
    print(f"같은 내용이지만 다른 객체: {lst1 is lst2}") #안 같으니까 False 리턴
    
    lst1.append(4)  # 기존 객체 수정
    print(f"lst1.append(4) 후: {lst1}, id: {id(lst1)}")
    print("→ 같은 객체를 수정함!")

def demonstrate_reference_behavior():
    """참조 동작 차이"""
    print("\n=== 참조 동작 차이 ===")
    
    # Immutable 참조
    print("1. Immutable 참조:")
    a = 10
    b = a  # 같은 객체를 참조
    print(f"a = {a}, b = {b}")
    print(f"a is b: {a is b}")
    
    a = 20  # a는 새로운 객체를 참조
    print(f"a = {a}, b = {b}")
    print(f"a is b: {a is b}")
    print("→ a가 새 객체를 참조해도 b는 영향 없음")
    
    # Mutable 참조
    print("\n2. Mutable 참조:")
    list1 = [1, 2, 3]
    list2 = list1  # 같은 객체를 참조
    print(f"list1 = {list1}, list2 = {list2}")
    print(f"list1 is list2: {list1 is list2}")
    
    list1.append(4)  # 같은 객체를 수정
    print(f"list1 = {list1}, list2 = {list2}")
    print(f"list1 is list2: {list1 is list2}")
    print("→ 같은 객체를 수정하므로 둘 다 변경됨!")

def demonstrate_function_parameters():
    """함수 매개변수에서의 동작"""
    print("\n=== 함수 매개변수에서의 동작 ===")
    
    def modify_immutable(x):
        print(f"함수 내부 - 수정 전: x = {x}, id: {id(x)}")
        x = x + 1  # 새로운 객체 생성
        print(f"함수 내부 - 수정 후: x = {x}, id: {id(x)}")
        return x
    
    def modify_mutable(lst):
        print(f"함수 내부 - 수정 전: lst = {lst}, id: {id(lst)}")
        lst.append(999)  # 기존 객체 수정
        print(f"함수 내부 - 수정 후: lst = {lst}, id: {id(lst)}")
        return lst
    
    # Immutable 매개변수
    print("1. Immutable 매개변수 (int):")
    num = 10
    print(f"함수 호출 전: num = {num}, id: {id(num)}")
    result = modify_immutable(num)
    print(f"함수 호출 후: num = {num}, result = {result}")
    print("→ 원본 num은 변경되지 않음")
    
    # Mutable 매개변수
    print("\n2. Mutable 매개변수 (list):")
    numbers = [1, 2, 3]
    print(f"함수 호출 전: numbers = {numbers}, id: {id(numbers)}")
    result = modify_mutable(numbers)
    print(f"함수 호출 후: numbers = {numbers}, result = {result}")
    print("→ 원본 numbers도 변경됨!")

def demonstrate_dangerous_default_values():
    """위험한 기본값 사용"""
    print("\n=== 위험한 기본값 사용 ===")
    
    # 나쁜 예시
    def bad_function(items=[]):  # 위험! 왜? 파이썬의 함수 기본값은 "함수 정의 시점에 한 번만 평가"되기 때문.
        items.append("new item") # 이런점은 C# 과 다르다. C# 에서 기본값은 함수 호출 시점에 평가되기 때문에 호출할 때마다 새 값이 들어가진다.
        return items             # 근데 C#은 컴파일 시간에 확정된 값만 기본값에 들어가지므로 상수만 됨. 리스트 같이 new 써야 되는 건 기본값이 못된다.
    
    print("❌ 나쁜 예시 (mutable 기본값):")
    result1 = bad_function()    #즉, 여기서 이미 기본값 리스트를 생성했다는 거임
    print(f"첫 번째 호출: {result1}")
    
    result2 = bad_function()    #인자가 또 생략된 채로 들어오면, 매번 새로운 리스트가 아니라 그때 만들어진 리스트(같은 주소)가 재사용되는 것
    print(f"두 번째 호출: {result2}")   #그래서 기본값이 누적되는거임ㅇㅇ
    print("→ 기본값이 계속 누적됨!")
    
    # 좋은 예시
    def good_function(items=None): # 그래서 기본값에 가변객체(Mutable)을 직접 쓰지 않고 None 을 써서 처리하는 게 정석이다.
        if items is None:
            items = []
        items.append("new item")    # 이제 늘 새 리스트가 만들어져서 안전하다
        return items
    
    print("\n✅ 좋은 예시 (None 기본값):")
    result1 = good_function()
    print(f"첫 번째 호출: {result1}")
    
    result2 = good_function()
    print(f"두 번째 호출: {result2}")
    print("→ 매번 새로운 리스트 생성!")

def demonstrate_copy_behavior():
    """복사 동작 차이"""
    print("\n=== 복사 동작 차이 ===")
    
    # 얕은 복사 vs 깊은 복사
    print("1. 얕은 복사 (shallow copy):")
    # 파이썬에서 list.copy() (혹은 list() 생성자, [:] 슬라이싱) 으로 만든 것은 얕은 복사(shallow copy)임.
    # 얕은 복사는 리스트 자체(“껍데기”)만 새로 만들고 그 안에 들어있는 내용물은 같은 주소를 참조시킴.
    original = [[1, 2], [3, 4]]
    shallow = original.copy()  # 또는 list(original)    
    
    print(f"원본: {original}")
    print(f"얕은 복사: {shallow}")
    print(f"원본 is 얕은 복사: {original is shallow}")
    print(f"원본[0] is 얕은 복사[0]: {original[0] is shallow[0]}")
    
    shallow[0].append(5)  # 내부 객체 수정
    print(f"얕은 복사[0] 수정 후:")
    print(f"원본: {original}")
    print(f"얕은 복사: {shallow}")
    print("→ 내부 객체는 같은 참조이므로 둘 다 변경!")
    
    # 깊은 복사
    print("\n2. 깊은 복사 (deep copy):")
    import copy
    # 깊은 복사는 내부 객체까지 전부 새로 복사하는 것. 
    # 내용물까지 새로운 객체로 복사되어서 원본과 값만 같지 완전 다른 게 된다.
    original = [[1, 2], [3, 4]]
    deep = copy.deepcopy(original)
    
    print(f"원본: {original}")
    print(f"깊은 복사: {deep}")
    print(f"원본 is 깊은 복사: {original is deep}")
    print(f"원본[0] is 깊은 복사[0]: {original[0] is deep[0]}")
    
    deep[0].append(5)  # 내부 객체 수정
    print(f"깊은 복사[0] 수정 후:")
    print(f"원본: {original}")
    print(f"깊은 복사: {deep}")
    print("→ 완전히 독립적인 객체!")

def demonstrate_performance_considerations():
    """성능 고려사항"""
    print("\n=== 성능 고려사항 ===")
    
    import sys
    
    # 메모리 사용량 비교
    print("1. 메모리 사용량 비교:")
    
    # Immutable (str)
    s1 = "hello"
    s2 = "hello"
    print(f"같은 문자열: s1 id={id(s1)}, s2 id={id(s2)}")
    print(f"같은 객체 참조: {s1 is s2}")
    
    # Mutable (list)
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    print(f"같은 내용 리스트: lst1 id={id(lst1)}, lst2 id={id(lst2)}")
    print(f"다른 객체: {lst1 is not lst2}")
    
    # 메모리 사용량
    print(f"\n문자열 메모리: {sys.getsizeof(s1)} bytes")
    print(f"리스트 메모리: {sys.getsizeof(lst1)} bytes")
    
    print("\n2. 성능 특성:")
    print("Immutable 장점:")
    print("  - 메모리 효율적 (같은 값은 같은 객체)")
    print("  - 스레드 안전")
    print("  - 해시 가능 (딕셔너리 키로 사용 가능)")
    
    print("\nMutable 장점:")
    print("  - 메모리 효율적 (in-place 수정)")
    print("  - 유연한 데이터 구조")
    print("  - 성능상 이점 (새 객체 생성 불필요)")

def demonstrate_practical_tips():
    """실무 팁"""
    print("\n=== 실무 팁 ===")
    
    print("1. 함수 기본값:")
    print("   ❌ def func(items=[]):")
    print("   ✅ def func(items=None):")
    print("       if items is None: items = []")
    
    print("\n2. 복사 방법:")
    print("   - 얕은 복사: list.copy(), list()")
    print("   - 깊은 복사: copy.deepcopy()")
    
    print("\n3. 동등성 비교:")
    print("   - == : 값 비교")
    print("   - is : 객체 동일성 비교")
    
    print("\n4. 성능 최적화:")
    print("   - 문자열 연결: ''.join() 사용")
    print("   - 리스트 수정: in-place 메서드 활용")
    
    print("\n5. 디버깅 팁:")
    print("   - id() 함수로 객체 추적")
    print("   - is 연산자로 참조 확인")

if __name__ == "__main__":
    demonstrate_basic_concept()
    demonstrate_type_classification()
    demonstrate_id_experiment()
    demonstrate_reference_behavior()
    demonstrate_function_parameters()
    demonstrate_dangerous_default_values()
    demonstrate_copy_behavior()
    demonstrate_performance_considerations()
    demonstrate_practical_tips()
