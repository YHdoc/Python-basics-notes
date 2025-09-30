# 메모리 효율적인 변수 사용

import sys

def demonstrate_memory_usage():
    """메모리 사용량 확인 예제"""
    print("=== 메모리 사용량 확인 ===")
    
    # 기본 타입들의 메모리 사용량
    integer_var = 42
    float_var = 3.14
    string_var = "Hello"
    boolean_var = True
    
    print(f"정수 42: {sys.getsizeof(integer_var)} bytes")
    print(f"실수 3.14: {sys.getsizeof(float_var)} bytes")
    print(f"문자열 'Hello': {sys.getsizeof(string_var)} bytes")
    print(f"불린 True: {sys.getsizeof(boolean_var)} bytes")
    
    # 문자열 길이에 따른 메모리 사용량
    short_string = "Hi"
    long_string = "This is a very long string that takes more memory"
    
    print(f"짧은 문자열: {sys.getsizeof(short_string)} bytes")
    print(f"긴 문자열: {sys.getsizeof(long_string)} bytes")

def demonstrate_memory_efficient_strings():
    """메모리 효율적인 문자열 사용"""
    print("\n=== 메모리 효율적인 문자열 ===")
    
    # 문자열 연결 방법 비교
    # 비효율적인 방법
    result1 = ""
    for i in range(5):
        result1 += str(i)
    print(f"+= 사용: {result1}, 메모리: {sys.getsizeof(result1)} bytes")
    
    # 효율적인 방법
    result2 = "".join(str(i) for i in range(5))
    print(f"join() 사용: {result2}, 메모리: {sys.getsizeof(result2)} bytes")
    
    # f-string 사용
    name = "김철수"
    age = 30
    message = f"안녕하세요, {name}님! {age}세이시군요."
    print(f"f-string: {message}")

def demonstrate_variable_reuse():
    """변수 재사용 예제"""
    print("\n=== 변수 재사용 ===")
    
    # 변수 재사용
    temp_var = 10
    print(f"초기값: {temp_var}")
    
    temp_var = temp_var * 2
    print(f"2배: {temp_var}")
    
    temp_var = temp_var + 5
    print(f"5 더하기: {temp_var}")
    
    # 다른 타입으로 재사용
    temp_var = "이제 문자열"
    print(f"문자열로 변경: {temp_var}")

def demonstrate_memory_optimization():
    """메모리 최적화 예제"""
    print("\n=== 메모리 최적화 ===")
    
    # 큰 리스트 생성
    large_list = list(range(1000))
    print(f"큰 리스트 메모리: {sys.getsizeof(large_list)} bytes")
    
    # 제너레이터 사용 (메모리 효율적)
    # 리스트는 1000개를 다 메모리에 올려두고 있기 때문에 메모리 사용량이 크다
    # yield가 있는 함수는 '제너레이터 함수'로, 호출 시 실행되는 게 아니라 제너레이터 객체를 반환한다
    # 제너레이터 객체를 가지고 있다가 필요할 때만 처리하므로 메모리 효율적이라는 것 
    # 벽돌 1000개를 다 만들어서 들고 다니냐(list) VS 벽돌만드는 기계를 들고 다니냐(Generator) 의 차이임. 그래서 아래에서 gen이 가벼운 것
    # 자세한 설명: 06-advanced/generators/README.md 참고
    def number_generator(n):
        for i in range(n):
            yield i             
    
    gen = number_generator(1000) # gen 안에는 “실행 준비 상태 + 내부 코드 위치(스택 프레임)”가 저장되어 있다
    print(f"제너레이터 메모리: {sys.getsizeof(gen)} bytes")
    
    # 불필요한 변수 제거
    def calculate_sum(numbers):
        # 불필요한 중간 변수
        # temp = sum(numbers)  # 메모리 낭비
        # return temp
        
        # 직접 반환
        return sum(numbers)
    
    result = calculate_sum([1, 2, 3, 4, 5])
    print(f"합계: {result}")

def demonstrate_garbage_collection():
    """가비지 컬렉션 예제"""
    print("\n=== 가비지 컬렉션 ===")
    
    import gc
    
    # 가비지 컬렉션 통계
    print(f"가비지 컬렉션 통계: {gc.get_stats()}")
    
    # 수동 가비지 컬렉션
    large_data = list(range(10000))
    print(f"큰 데이터 생성 후: {sys.getsizeof(large_data)} bytes")
    
    # 변수 삭제
    del large_data
    
    # 가비지 컬렉션 실행
    collected = gc.collect()
    print(f"수집된 객체 수: {collected}")

def demonstrate_memory_efficient_patterns():
    """메모리 효율적인 패턴들"""
    print("\n=== 메모리 효율적인 패턴들 ===")
    
    # 1. 조건부 변수 생성
    def process_data(data, need_validation=True):
        if need_validation:
            # 필요할 때만 생성
            validator = lambda x: x > 0
            return [x for x in data if validator(x)]
        return data
    
    # 2. 지연 초기화
    class LazyInitializer:
        def __init__(self):
            self._data = None
        
        @property
        def data(self):
            if self._data is None:
                self._data = list(range(1000))  # 필요할 때만 생성
            return self._data
    
    lazy = LazyInitializer()
    print(f"초기 메모리: {sys.getsizeof(lazy)} bytes")
    data = lazy.data  # 이때 생성됨
    print(f"데이터 생성 후: {sys.getsizeof(lazy)} bytes")
    
    # 3. 컨텍스트 매니저 사용
    def read_large_file(filename):
        with open(filename, 'r') as file:
            for line in file:  # 한 줄씩 처리
                yield line.strip()
    
    print("파일 처리는 제너레이터로 메모리 효율적으로!")

def demonstrate_memory_profiling():
    """메모리 프로파일링 예제"""
    print("\n=== 메모리 프로파일링 ===")
    
    # 메모리 사용량 모니터링
    def memory_intensive_function():
        data = []
        for i in range(1000):
            data.append(i * i)
        return data
    
    # 함수 실행 전후 메모리 비교
    import tracemalloc
    
    tracemalloc.start()
    result = memory_intensive_function()
    current, peak = tracemalloc.get_traced_memory()
    
    print(f"현재 메모리 사용량: {current / 1024:.2f} KB")
    print(f"최대 메모리 사용량: {peak / 1024:.2f} KB")
    
    tracemalloc.stop()

if __name__ == "__main__":
    demonstrate_memory_usage()
    demonstrate_memory_efficient_strings()
    demonstrate_variable_reuse()
    demonstrate_memory_optimization()
    demonstrate_garbage_collection()
    demonstrate_memory_efficient_patterns()
    demonstrate_memory_profiling()
