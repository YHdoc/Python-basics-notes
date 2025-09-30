# 고차 함수

def apply_operation(func, x, y):
    """함수를 인수로 받는 고차 함수"""
    return func(x, y)

def create_multiplier(factor):
    """함수를 반환하는 고차 함수"""
    def multiplier(number):
        return number * factor
    return multiplier

def filter_and_transform(data, filter_func, transform_func):
    """필터링과 변환을 수행하는 고차 함수"""
    filtered = [item for item in data if filter_func(item)]
    transformed = [transform_func(item) for item in filtered]
    return transformed

def compose(f, g):
    """함수 합성을 수행하는 고차 함수"""
    def composed(x):
        return f(g(x))
    return composed

def memoize(func):
    """메모이제이션을 제공하는 데코레이터 함수"""
    cache = {}
    
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    
    return memoized_func

def retry(max_attempts=3):
    """재시도 로직을 제공하는 데코레이터 함수"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"시도 {attempt + 1} 실패: {e}")
            return None
        return wrapper
    return decorator

def with_logging(func):
    """로깅을 추가하는 데코레이터 함수"""
    def wrapper(*args, **kwargs):
        print(f"함수 {func.__name__} 호출 시작")
        result = func(*args, **kwargs)
        print(f"함수 {func.__name__} 호출 완료")
        return result
    return wrapper

if __name__ == "__main__":
    print("=== 함수를 인수로 받는 고차 함수 ===")
    
    # 기본 연산 함수들
    add = lambda x, y: x + y
    multiply = lambda x, y: x * y
    
    result1 = apply_operation(add, 5, 3)
    result2 = apply_operation(multiply, 4, 7)
    print(f"5 + 3 = {result1}")
    print(f"4 * 7 = {result2}")
    
    print("\n=== 함수를 반환하는 고차 함수 ===")
    
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"2 * 5 = {double(5)}")
    print(f"3 * 5 = {triple(5)}")
    
    print("\n=== 필터링과 변환 ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    is_even = lambda x: x % 2 == 0
    square = lambda x: x ** 2
    
    result = filter_and_transform(numbers, is_even, square)
    print(f"짝수의 제곱: {result}")
    
    print("\n=== 함수 합성 ===")
    
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    
    composed_func = compose(add_one, multiply_by_two)
    result = composed_func(5)  # (5 * 2) + 1 = 11
    print(f"합성 함수 결과: {result}")
    
    print("\n=== 메모이제이션 ===")
    
    @memoize
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(f"피보나치(10): {fibonacci(10)}")
    
    print("\n=== 재시도 로직 ===")
    
    @retry(max_attempts=3)
    def risky_operation():
        import random
        if random.random() < 0.7:
            raise Exception("랜덤 오류")
        return "성공"
    
    result = risky_operation()
    print(f"위험한 연산 결과: {result}")
    
    print("\n=== 로깅 데코레이터 ===")
    
    @with_logging
    def sample_function(x):
        return x * 2
    
    result = sample_function(5)
    print(f"결과: {result}")
