# 제너레이터 ⚡

> Python의 제너레이터를 학습하고 메모리 효율적인 데이터 처리를 구현하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 제너레이터의 핵심 개념과 yield 키워드 이해
- [ ] 제너레이터 함수 vs 일반 함수의 차이점
- [ ] 제너레이터 객체의 동작 원리 (지연 실행)
- [ ] 제너레이터 표현식과 함수형 프로그래밍
- [ ] 제너레이터 메서드들 (send, throw, close) 활용
- [ ] 제너레이터의 메모리 효율성과 성능 최적화
- [ ] 실무에서 자주 사용되는 제너레이터 패턴

## 📚 핵심 개념

### 1. 제너레이터의 핵심 원리

> **yield가 있으면, 이 함수는 일반 함수가 아니라 제너레이터 함수로 바뀐다.**

```python
def number_generator(n):
    for i in range(n):
        yield i

# 호출하면 바로 실행되는 게 아니라, **제너레이터 객체가 반환된다**
gen = number_generator(1000)
print(type(gen))  # <class 'generator'>
print(gen)        # <generator object number_generator at 0x...>

# 👉 즉, gen 안에는 "실행 준비 상태 + 내부 코드 위치(스택 프레임)"가 저장돼 있음.
# 실행은 next() 또는 for 루프에서 자동으로 호출할 때 일어난다.

# 실행 흐름 예시
gen = number_generator(5)

print(next(gen))  # 0
print(next(gen))  # 1  
print(next(gen))  # 2

# 실행 흐름:
# 1) next(gen) → 함수 진입, i=0 → yield 0 반환 (여기서 멈춤)
# 2) next(gen) → 멈춘 지점부터 다시 실행, i=1 → yield 1 반환
# 3) next(gen) → 이어서 실행, i=2 → yield 2 반환
# ...
# 5) 다 끝나면 StopIteration 예외 발생
```

### 2. 제너레이터 vs 일반 함수

```python
# 일반 함수 - 즉시 실행
def normal_function():
    print("함수 시작")
    result = []
    for i in range(3):
        result.append(i)
        print(f"값 생성: {i}")
    print("함수 끝")
    return result

# 제너레이터 함수 - 지연 실행
def generator_function():
    print("제너레이터 시작")
    for i in range(3):
        print(f"값 생성: {i}")
        yield i
    print("제너레이터 끝")

# 비교
print("=== 일반 함수 ===")
result = normal_function()  # 즉시 실행됨
print(f"결과: {result}")

print("\n=== 제너레이터 함수 ===")
gen = generator_function()  # 아직 실행 안됨!
print("제너레이터 객체 생성됨")

print("첫 번째 next() 호출:")
print(next(gen))  # 이제 실행됨

print("두 번째 next() 호출:")
print(next(gen))
```

### 3. for 루프로 제너레이터 사용

제너레이터는 보통 for 문에서 사용된다.

```python
def number_generator(n):
    for i in range(n):
        yield i

# for 루프로 사용 - 더 직관적
for num in number_generator(5):
    print(num)

# 출력:
# 0
# 1
# 2
# 3
# 4

# 👉 for 문이 내부적으로 계속 next(gen)를 호출해주기 때문에 간단하게 순회할 수 있습니다.
```

### 4. 제너레이터의 메모리 효율성

```python
import sys

# 리스트 컴프리헨션 - 모든 값을 메모리에 저장
squares_list = [x**2 for x in range(1000000)]
print(f"리스트 메모리: {sys.getsizeof(squares_list)} bytes")

# 제너레이터 표현식 - 필요할 때만 값 생성
squares_gen = (x**2 for x in range(1000000))
print(f"제너레이터 메모리: {sys.getsizeof(squares_gen)} bytes")

# 벽돌 1000개를 다 만들어서 들고 다니냐(list) 
# VS 벽돌만드는 기계를 들고 다니냐(Generator) 의 차이임
```

### 5. 제너레이터 메서드들

```python
def accumulator():
    total = 0
    while True:
        value = yield total  # yield로 값을 반환하고, 받을 수도 있음
        if value is not None:
            total += value

# 제너레이터 생성 및 시작
acc = accumulator()
next(acc)  # 제너레이터 시작 (첫 번째 yield까지 실행)

# 값 전송
print(acc.send(5))   # 5
print(acc.send(3))   # 8
print(acc.send(10))  # 18

# 예외 전송
try:
    acc.throw(ValueError, "테스트 예외")
except ValueError as e:
    print(f"예외 처리됨: {e}")

# 제너레이터 종료
acc.close()
```

### 6. 제너레이터 체이닝 (파이프라인)

```python
def read_file(filename):
    """파일을 한 줄씩 읽는 제너레이터"""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def filter_lines(lines, keyword):
    """특정 키워드가 포함된 줄만 필터링"""
    for line in lines:
        if keyword in line:
            yield line

def process_lines(lines):
    """줄을 대문자로 변환"""
    for line in lines:
        yield line.upper()

# 체이닝으로 데이터 파이프라인 구성
lines = read_file("data.txt")
filtered = filter_lines(lines, "error")
processed = process_lines(filtered)

# 실제로는 마지막에 소비할 때까지 실행되지 않음
for line in processed:
    print(line)
```

### 7. 제너레이터 표현식

```python
# 리스트 컴프리헨션 vs 제너레이터 표현식
numbers = [1, 2, 3, 4, 5]

# 리스트 컴프리헨션 - 모든 값을 메모리에 저장
squares_list = [x**2 for x in numbers]
print(f"리스트: {squares_list}")

# 제너레이터 표현식 - 필요할 때만 값 생성
squares_gen = (x**2 for x in numbers)
print(f"제너레이터: {squares_gen}")

# 제너레이터 값 사용
for square in squares_gen:
    print(square)
```

## 🔄 제너레이터의 동작 원리

### 지연 실행 (Lazy Evaluation)
```python
def fibonacci_generator(n):
    print(f"피보나치 제너레이터 시작 (n={n})")
    a, b = 0, 1
    for i in range(n):
        print(f"yield 전: {a}")
        yield a
        print(f"yield 후: {a}")
        a, b = b, a + b
    print("피보나치 제너레이터 끝")

# 제너레이터 생성 - 아직 실행 안됨
fib_gen = fibonacci_generator(5)
print("제너레이터 객체 생성 완료")

# 첫 번째 next() 호출 - 이제 실행 시작
print("\n첫 번째 next() 호출:")
print(f"결과: {next(fib_gen)}")

# 두 번째 next() 호출
print("\n두 번째 next() 호출:")
print(f"결과: {next(fib_gen)}")

# for 루프로 나머지 소비
print("\nfor 루프로 나머지 소비:")
for num in fib_gen:
    print(f"결과: {num}")
```

### 제너레이터의 상태 관리
```python
def stateful_generator():
    print("제너레이터 시작")
    count = 0
    while count < 3:
        print(f"yield 전: count={count}")
        received = yield count
        print(f"yield 후: received={received}, count={count}")
        if received is not None:
            count = received
        else:
            count += 1
    print("제너레이터 끝")

gen = stateful_generator()
print(f"초기 상태: {gen.gi_frame.f_locals}")  # 제너레이터 내부 상태

next(gen)  # 첫 번째 yield까지 실행
print(f"첫 번째 yield 후: {gen.gi_frame.f_locals}")

gen.send(10)  # 값 전송
print(f"send(10) 후: {gen.gi_frame.f_locals}")
```

## 📁 예제 파일

- `basic_generators.py` - 기본 제너레이터와 동작 원리
- `generator_expressions.py` - 제너레이터 표현식
- `generator_methods.py` - 제너레이터 메서드들 (send, throw, close)
- `generator_chaining.py` - 제너레이터 체이닝과 파이프라인
- `memory_efficiency.py` - 메모리 효율성 비교
- `practical_examples.py` - 실무에서 자주 사용되는 패턴

## 🏃‍♂️ 실습 과제

1. **파일 처리기**: 대용량 파일을 효율적으로 처리하는 제너레이터
2. **데이터 파이프라인**: 여러 단계의 데이터 처리를 연결하는 파이프라인
3. **무한 시퀀스**: 무한한 데이터 시퀀스를 생성하는 제너레이터
4. **배치 처리기**: 데이터를 배치 단위로 처리하는 제너레이터
5. **상태 관리**: 제너레이터의 상태를 활용한 복잡한 로직 구현

## 💡 실무 팁

### ✅ 좋은 예시
```python
def read_large_file(filename):
    """대용량 파일을 메모리 효율적으로 읽기"""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def process_data(data):
    """데이터 처리 파이프라인"""
    for item in data:
        if item:  # 빈 값 필터링
            yield item.upper()

# 사용 - 메모리 효율적
lines = read_large_file("huge_file.txt")
processed = process_data(lines)
for line in processed:
    print(line)
```

### ❌ 피해야 할 예시
```python
# 메모리 비효율적인 방법
def read_entire_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()  # 전체 파일을 메모리에 로드

# 제너레이터를 리스트로 변환 (메모리 사용량 증가)
gen = (x**2 for x in range(1000000))
squares = list(gen)  # 모든 값을 메모리에 저장

# 제너레이터를 여러 번 사용 (이미 소비됨)
gen = (x for x in range(5))
print(list(gen))  # [0, 1, 2, 3, 4]
print(list(gen))  # [] - 빈 리스트!
```

## 🚨 주의사항

### 1. 제너레이터는 한 번만 소비 가능
```python
gen = (x for x in range(3))
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [] - 이미 소비됨!
```

### 2. 제너레이터 함수 내부에서 return 사용
```python
def generator_with_return():
    yield 1
    yield 2
    return "제너레이터 끝"  # StopIteration 예외와 함께 반환됨
    yield 3  # 실행되지 않음

gen = generator_with_return()
for value in gen:
    print(value)  # 1, 2

try:
    next(gen)
except StopIteration as e:
    print(f"반환값: {e.value}")  # "제너레이터 끝"
```

### 3. 제너레이터와 예외 처리
```python
def safe_generator():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError as e:
        print(f"예외 처리됨: {e}")
        yield "예외 후 값"
    finally:
        print("제너레이터 정리")

gen = safe_generator()
print(next(gen))  # 1
print(next(gen))  # 2
gen.throw(ValueError, "테스트 예외")  # 예외 전송
```

## 🔗 관련 주제

- [반복문](../../02-control-flow/loops/) - 제너레이터와 반복문
- [함수 정의와 호출](../../03-functions-modules/functions/) - 제너레이터 함수
- [데코레이터](../../06-advanced/decorators/) - 제너레이터와 데코레이터 조합

## 📖 추가 학습 자료

- [Python 공식 문서 - 제너레이터](https://docs.python.org/3/tutorial/classes.html#generators)
- [PEP 255 - 제너레이터](https://peps.python.org/pep-0255/)

---

**다음 단계**: [모범 사례](../../08-best-practices/) 학습하기
