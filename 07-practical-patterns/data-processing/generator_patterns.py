# 제너레이터 패턴

def demonstrate_basic_generator():
    """기본 제너레이터 예제"""
    print("=== 기본 제너레이터 ===")
    
    def simple_generator():
        yield 1
        yield 2
        yield 3
    
    # 제너레이터 생성
    gen = simple_generator()
    print(f"제너레이터 타입: {type(gen)}")
    
    # 값 순차적으로 가져오기
    print(f"첫 번째 값: {next(gen)}")
    print(f"두 번째 값: {next(gen)}")
    print(f"세 번째 값: {next(gen)}")
    
    # 더 이상 값이 없으면 StopIteration 예외 발생
    try:
        print(f"네 번째 값: {next(gen)}")
    except StopIteration:
        print("더 이상 값이 없습니다.")

def demonstrate_generator_with_loop():
    """반복문과 함께 사용하는 제너레이터"""
    print("\n=== 반복문과 함께 사용 ===")
    
    def count_up_to(n):
        count = 1
        while count <= n:
            yield count
            count += 1
    
    # for 루프로 제너레이터 사용
    for num in count_up_to(5):
        print(f"숫자: {num}")

def demonstrate_generator_expression():
    """제너레이터 표현식 예제"""
    print("\n=== 제너레이터 표현식 ===")
    
    # 리스트 컴프리헨션 vs 제너레이터 표현식
    numbers = [1, 2, 3, 4, 5]
    
    # 리스트 컴프리헨션 (메모리에 모든 값 저장)
    squares_list = [x**2 for x in numbers]
    print(f"리스트 컴프리헨션: {squares_list}")
    print(f"메모리 사용량: {squares_list.__sizeof__()} bytes")
    
    # 제너레이터 표현식 (필요할 때만 값 생성)
    squares_gen = (x**2 for x in numbers)
    print(f"제너레이터 표현식: {squares_gen}")
    print(f"메모리 사용량: {squares_gen.__sizeof__()} bytes")
    
    # 제너레이터 값 사용
    print("제너레이터 값들:")
    for square in squares_gen:
        print(f"  {square}")

def demonstrate_fibonacci_generator():
    """피보나치 수열 제너레이터"""
    print("\n=== 피보나치 수열 제너레이터 ===")
    
    def fibonacci(n):
        a, b = 0, 1
        count = 0
        while count < n:
            yield a
            a, b = b, a + b
            count += 1
    
    # 피보나치 수열 생성
    fib_gen = fibonacci(10)
    print("피보나치 수열 (처음 10개):")
    for i, num in enumerate(fib_gen, 1):
        print(f"  F{i}: {num}")

def demonstrate_generator_with_condition():
    """조건이 있는 제너레이터"""
    print("\n=== 조건이 있는 제너레이터 ===")
    
    def even_numbers(max_num):
        for i in range(max_num):
            if i % 2 == 0:
                yield i
    
    # 짝수만 생성
    even_gen = even_numbers(20)
    print("20 미만의 짝수들:")
    for num in even_gen:
        print(f"  {num}")

def demonstrate_generator_send():
    """제너레이터에 값 전송하기"""
    print("\n=== 제너레이터에 값 전송 ===")
    
    def accumulator():
        total = 0
        while True:
            value = yield total
            if value is not None:
                total += value
    
    # 제너레이터 생성 및 시작
    acc = accumulator()
    next(acc)  # 제너레이터 시작
    
    # 값 전송
    print(f"초기값: {acc.send(0)}")
    print(f"5 추가 후: {acc.send(5)}")
    print(f"3 추가 후: {acc.send(3)}")
    print(f"10 추가 후: {acc.send(10)}")

def demonstrate_generator_throw():
    """제너레이터에 예외 전송하기"""
    print("\n=== 제너레이터에 예외 전송 ===")
    
    def resilient_generator():
        try:
            yield 1
            yield 2
            yield 3
        except ValueError as e:
            print(f"예외 처리됨: {e}")
            yield "예외 후 값"
    
    gen = resilient_generator()
    print(f"첫 번째 값: {next(gen)}")
    print(f"두 번째 값: {next(gen)}")
    
    # 예외 전송
    result = gen.throw(ValueError, "테스트 예외")
    print(f"예외 후 값: {result}")

def demonstrate_generator_close():
    """제너레이터 종료하기"""
    print("\n=== 제너레이터 종료 ===")
    
    def counting_generator():
        try:
            count = 1
            while True:
                yield count
                count += 1
        except GeneratorExit:
            print("제너레이터가 종료되었습니다.")
    
    gen = counting_generator()
    print(f"첫 번째 값: {next(gen)}")
    print(f"두 번째 값: {next(gen)}")
    
    # 제너레이터 종료
    gen.close()
    print("제너레이터 종료 완료")

def demonstrate_practical_generator():
    """실용적인 제너레이터 예제"""
    print("\n=== 실용적인 제너레이터 예제 ===")
    
    def read_large_file(filename):
        """큰 파일을 한 줄씩 읽는 제너레이터"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {filename}")
    
    def process_data(data_generator):
        """데이터를 처리하는 제너레이터"""
        for item in data_generator:
            if item:  # 빈 줄이 아닌 경우
                yield item.upper()
    
    # 테스트용 데이터
    test_data = ["hello", "world", "", "python", "generator"]
    
    # 데이터 처리 파이프라인
    processed_gen = process_data(iter(test_data))
    
    print("처리된 데이터:")
    for item in processed_gen:
        print(f"  {item}")

def demonstrate_generator_performance():
    """제너레이터 성능 비교"""
    print("\n=== 제너레이터 성능 비교 ===")
    
    import sys
    
    # 큰 데이터 생성
    n = 1000000
    
    # 리스트 컴프리헨션
    squares_list = [x**2 for x in range(n)]
    print(f"리스트 컴프리헨션 메모리: {sys.getsizeof(squares_list)} bytes")
    
    # 제너레이터 표현식
    squares_gen = (x**2 for x in range(n))
    print(f"제너레이터 표현식 메모리: {sys.getsizeof(squares_gen)} bytes")
    
    # 메모리 사용량 비교
    memory_ratio = sys.getsizeof(squares_list) / sys.getsizeof(squares_gen)
    print(f"메모리 사용량 비율: {memory_ratio:.1f}배")

if __name__ == "__main__":
    demonstrate_basic_generator()
    demonstrate_generator_with_loop()
    demonstrate_generator_expression()
    demonstrate_fibonacci_generator()
    demonstrate_generator_with_condition()
    demonstrate_generator_send()
    demonstrate_generator_throw()
    demonstrate_generator_close()
    demonstrate_practical_generator()
    demonstrate_generator_performance()
