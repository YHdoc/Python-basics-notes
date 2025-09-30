# 기본 데코레이터

def my_decorator(func):
    """기본 데코레이터 예제"""
    def wrapper(*args, **kwargs):
        print("함수 실행 전")
        result = func(*args, **kwargs)
        print("함수 실행 후")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

if __name__ == "__main__":
    say_hello()
