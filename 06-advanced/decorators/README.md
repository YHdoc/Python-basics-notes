# 데코레이터 🎨

> Python의 데코레이터를 학습하고 함수와 클래스를 확장하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 데코레이터의 개념과 기본 사용법 이해
- [ ] 함수 데코레이터 작성 방법
- [ ] 클래스 데코레이터 활용
- [ ] 매개변수가 있는 데코레이터 작성
- [ ] 여러 데코레이터 조합 사용
- [ ] functools.wraps를 활용한 메타데이터 보존
- [ ] 실무에서 자주 사용되는 데코레이터 패턴

## 📚 핵심 개념

### 1. 기본 데코레이터
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("함수 실행 전")
        result = func(*args, **kwargs)
        print("함수 실행 후")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

### 2. 매개변수가 있는 데코레이터
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
```

### 3. 클래스 데코레이터
```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    pass
```

### 4. functools.wraps 사용
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## 📁 예제 파일

- `basic_decorators.py` - 기본 데코레이터
- `parameterized_decorators.py` - 매개변수가 있는 데코레이터
- `class_decorators.py` - 클래스 데코레이터
- `functools_wraps.py` - functools.wraps 활용
- `multiple_decorators.py` - 여러 데코레이터 조합
- `practical_examples.py` - 실무에서 자주 사용되는 패턴

## 🏃‍♂️ 실습 과제

1. **로깅 데코레이터**: 함수 실행을 로깅하는 데코레이터
2. **캐싱 데코레이터**: 함수 결과를 캐싱하는 데코레이터
3. **타이밍 데코레이터**: 함수 실행 시간을 측정하는 데코레이터
4. **권한 검사 데코레이터**: 사용자 권한을 검사하는 데코레이터

## 💡 실무 팁

### ✅ 좋은 예시
```python
from functools import wraps
import time

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 실행 시간: {end - start:.2f}초")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "완료"
```

### ❌ 피해야 할 예시
```python
# functools.wraps 없이 사용
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper  # 메타데이터 손실

# 복잡한 데코레이터 체인
@decorator1
@decorator2
@decorator3
@decorator4
def function():  # 너무 복잡
    pass
```

## 🔗 관련 주제

- [함수 정의와 호출](../../03-functions-modules/functions/) - 데코레이터의 기초
- [클래스와 객체](../../04-oop/classes-and-objects/) - 클래스 데코레이터
- [고급 기능](../../06-advanced/generators/) - 제너레이터와 데코레이터 조합

## 📖 추가 학습 자료

- [Python 공식 문서 - 데코레이터](https://docs.python.org/3/glossary.html#term-decorator)
- [PEP 318 - 데코레이터](https://peps.python.org/pep-0318/)

---

**다음 단계**: [제너레이터](../../06-advanced/generators/) 학습하기
