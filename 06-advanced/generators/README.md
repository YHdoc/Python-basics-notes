# 제너레이터 ⚡

> Python의 제너레이터를 학습하고 메모리 효율적인 데이터 처리를 구현하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 제너레이터의 개념과 yield 키워드 이해
- [ ] 제너레이터 함수와 제너레이터 표현식 작성
- [ ] 제너레이터의 메모리 효율성 이해
- [ ] 제너레이터 메서드들 (send, throw, close) 활용
- [ ] 제너레이터와 이터레이터의 차이점
- [ ] 제너레이터를 활용한 데이터 파이프라인 구축
- [ ] 실무에서 자주 사용되는 제너레이터 패턴

## 📚 핵심 개념

### 1. 기본 제너레이터
```python
def count_up_to(max_count):
    count = 1
    while count <= max_count:
        yield count
        count += 1

# 사용
counter = count_up_to(5)
for num in counter:
    print(num)
```

### 2. 제너레이터 표현식
```python
# 리스트 컴프리헨션
squares_list = [x**2 for x in range(10)]

# 제너레이터 표현식
squares_gen = (x**2 for x in range(10))
```

### 3. 제너레이터 메서드들
```python
def number_generator():
    num = 0
    while True:
        received = yield num
        if received is not None:
            num = received
        else:
            num += 1

gen = number_generator()
print(next(gen))  # 0
print(gen.send(10))  # 10
print(next(gen))  # 11
```

### 4. 제너레이터 체이닝
```python
def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

def process_lines(lines):
    for line in lines:
        yield line.upper()

# 체이닝
lines = read_file("data.txt")
filtered = filter_lines(lines, "error")
processed = process_lines(filtered)
```

## 📁 예제 파일

- `basic_generators.py` - 기본 제너레이터
- `generator_expressions.py` - 제너레이터 표현식
- `generator_methods.py` - 제너레이터 메서드들
- `generator_chaining.py` - 제너레이터 체이닝
- `memory_efficiency.py` - 메모리 효율성
- `practical_examples.py` - 실무에서 자주 사용되는 패턴

## 🏃‍♂️ 실습 과제

1. **파일 처리기**: 대용량 파일을 효율적으로 처리하는 제너레이터
2. **데이터 파이프라인**: 여러 단계의 데이터 처리를 연결하는 파이프라인
3. **무한 시퀀스**: 무한한 데이터 시퀀스를 생성하는 제너레이터
4. **배치 처리기**: 데이터를 배치 단위로 처리하는 제너레이터

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

# 사용
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

# 제너레이터를 리스트로 변환
gen = (x**2 for x in range(1000000))
squares = list(gen)  # 메모리 사용량 증가
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
