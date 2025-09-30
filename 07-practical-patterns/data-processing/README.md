# 데이터 처리 패턴 📊

> Python에서 효율적인 데이터 처리를 위한 리스트 컴프리헨션, 제너레이터, 람다 함수 등을 학습합니다.

## 🎯 학습 목표

- [ ] 리스트 컴프리헨션의 다양한 활용법
- [ ] 딕셔너리와 집합 컴프리헨션
- [ ] 제너레이터와 제너레이터 표현식
- [ ] 람다 함수의 실무 활용
- [ ] 성능 최적화 기법
- [ ] 메모리 효율적인 데이터 처리

## 📚 핵심 개념

### 1. 리스트 컴프리헨션 (List Comprehension)

“for문을 한 줄로 줄인 문법” 이라고 생각하면 된다.
결과를 리스트(list) 로 바로 만들어 준다.
데이터 전체를 메모리에 올림.

```python
# 기본 문법: [expression for item in iterable]
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 조건부 컴프리헨션
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# 중첩 컴프리헨션
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

### 2. 딕셔너리 컴프리헨션 (Dictionary Comprehension)

```python
# 기본 문법: {key: value for item in iterable}
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 조건부 딕셔너리 컴프리헨션
even_squares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares_dict)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 문자열 처리
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(word_lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}
```

### 3. 집합 컴프리헨션 (Set Comprehension)

```python
# 기본 문법: {expression for item in iterable}
unique_lengths = {len(word) for word in ["apple", "banana", "cherry", "date"]}
print(unique_lengths)  # {4, 5, 6}

# 조건부 집합 컴프리헨션
even_squares_set = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares_set)  # {0, 4, 16, 36, 64}
```

### 4. 제너레이터 컴프리헨션(Generator Comprehension)

리스트 컴프리헨션이랑 문법은 똑같은데 대괄호 [] 대신 소괄호 () 를 쓴다
결과는 리스트처럼 메모리에 한 번에 올려놓고 쓰는 게 아니라 호출할 때마다 다음 요소를 하나씩 꺼내 쓰는 것이다.

```python
# 제너레이터 함수
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 제너레이터 사용
fib_gen = fibonacci(10)
for num in fib_gen:
    print(num, end=" ")  # 0 1 1 2 3 5 8 13 21 34

# 제너레이터 표현식
squares_gen = (x**2 for x in range(10))
print(list(squares_gen))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 5. 람다 함수 (Lambda Function)

```python
# 기본 람다 함수
square = lambda x: x**2
print(square(5))  # 25

# 내장 함수와 함께 사용
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# 필터링
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# 정렬
students = [("김철수", 85), ("이영희", 92), ("박민수", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)  # [("이영희", 92), ("김철수", 85), ("박민수", 78)]
```

## 🔄 리스트 컴프리헨션 vs 제너레이터 컴프리헨션

**1. 리스트 컴프리헨션 (List Comprehension)**

👉 실행 즉시 모든 결과를 리스트에 담아서 메모리에 저장
```python
result = [x * 2 for x in range(5)]
```

흐름
```
range(5) → [0, 1, 2, 3, 4]
    │
    ├─ x*2
    │
    └→ [0, 2, 4, 6, 8]   (완성된 리스트)
```

결과 = [0, 2, 4, 6, 8]
한 번에 다 만들어서 저장 → 빠른 접근, 하지만 메모리를 많이 씀
>
>
**2. 제너레이터 컴프리헨션 (Generator Comprehension)**
👉 필요할 때만 값을 하나씩 만들어 줌.
```python
result = (x * 2 for x in range(5))
```

흐름
```
range(5) → [0, 1, 2, 3, 4]
    │
    ├─ x*2
    │
    └→ (0) (2) (4) (6) (8) ...  ← 필요할 때 하나씩 꺼냄

```
결과 = <generator object ...> (리스트가 아님)
next(result) 를 호출할 때마다 다음 값을 꺼냄
메모리를 아껴서 대용량 데이터 처리에 유리



## 🔄 컴프리헨션 vs 전통적인 방법

### 리스트 컴프리헨션의 장점

```python
# 전통적인 방법
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

# 리스트 컴프리헨션 (더 간결하고 빠름)
squares = [x**2 for x in range(10) if x % 2 == 0]
```

### 성능 비교

```python
import time

# 큰 데이터로 성능 테스트
n = 1000000

# 전통적인 방법
start = time.time()
result1 = []
for i in range(n):
    if i % 2 == 0:
        result1.append(i**2)
traditional_time = time.time() - start

# 리스트 컴프리헨션
start = time.time()
result2 = [i**2 for i in range(n) if i % 2 == 0]
comprehension_time = time.time() - start

print(f"전통적인 방법: {traditional_time:.4f}초")
print(f"컴프리헨션: {comprehension_time:.4f}초")
```

## 💡 실무 활용 패턴

### 1. 데이터 정제

```python
# 원시 데이터 정제
raw_data = ["  apple  ", "BANANA", "  Cherry  ", "DATE"]
cleaned_data = [item.strip().lower() for item in raw_data]
print(cleaned_data)  # ['apple', 'banana', 'cherry', 'date']
```

### 2. 조건부 데이터 변환

```python
# 조건에 따른 데이터 변환
scores = [85, 92, 78, 96, 88, 72]
grades = ["A" if score >= 90 else "B" if score >= 80 else "C" for score in scores]
print(grades)  # ['B', 'A', 'C', 'A', 'B', 'C']
```

### 3. 중첩 데이터 처리

```python
# 중첩된 데이터 구조 처리
students = [
    {"name": "김철수", "scores": [85, 90, 78]},
    {"name": "이영희", "scores": [92, 88, 95]},
    {"name": "박민수", "scores": [78, 85, 82]}
]

# 각 학생의 평균 점수 계산
averages = {student["name"]: sum(student["scores"]) / len(student["scores"]) 
           for student in students}
print(averages)  # {'김철수': 84.33, '이영희': 91.67, '박민수': 81.67}
```

### 4. 메모리 효율적인 처리

```python
# 제너레이터를 사용한 메모리 효율적인 처리
def process_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip().upper()

# 큰 파일을 메모리 효율적으로 처리
processed_lines = (line for line in process_large_file("large_file.txt") 
                  if len(line) > 10)
```

## ⚡ 성능 최적화 팁

### 1. 제너레이터 사용

```python
# 메모리 사용량 비교
import sys

# 리스트 컴프리헨션 (모든 값을 메모리에 저장)
squares_list = [x**2 for x in range(1000000)]
print(f"리스트 메모리: {sys.getsizeof(squares_list)} bytes")

# 제너레이터 표현식 (필요할 때만 값 생성)
squares_gen = (x**2 for x in range(1000000))
print(f"제너레이터 메모리: {sys.getsizeof(squares_gen)} bytes")
```

### 2. 조건부 컴프리헨션 최적화

```python
# 비효율적인 방법
result = [expensive_function(x) for x in data if x > 0]

# 효율적인 방법 (조건을 먼저 확인)
result = [expensive_function(x) for x in data if x > 0]
```

### 3. 중첩 컴프리헨션 최적화

```python
# 복잡한 중첩 컴프리헨션은 가독성을 위해 분리
# 나쁜 예
result = [[i*j for j in range(10) if j % 2 == 0] for i in range(10) if i % 2 == 0]

# 좋은 예
even_numbers = [i for i in range(10) if i % 2 == 0]
result = [[i*j for j in even_numbers] for i in even_numbers]
```

## 🚨 주의사항

### 1. 가독성 vs 간결성

```python
# 너무 복잡한 컴프리헨션 (피해야 함)
result = [x**2 for x in [y for y in range(10) if y % 2 == 0] if x > 10]

# 더 읽기 쉬운 방법
even_numbers = [y for y in range(10) if y % 2 == 0]
result = [x**2 for x in even_numbers if x**2 > 10]
```

### 2. 부작용(Side Effects) 피하기

```python
# 나쁜 예 (부작용이 있는 코드)
counter = 0
result = [counter := counter + 1 for _ in range(5)]

# 좋은 예
result = list(range(1, 6))
```

### 3. 람다 함수의 적절한 사용

```python
# 간단한 람다는 괜찮음
squares = list(map(lambda x: x**2, numbers))

# 복잡한 로직은 일반 함수로
def complex_calculation(x):
    # 복잡한 계산 로직
    return result

results = list(map(complex_calculation, numbers))
```

## 📁 예제 파일

- `list_comprehension.py` - 리스트 컴프리헨션 활용
- `dictionary_comprehension.py` - 딕셔너리 컴프리헨션
- `generator_patterns.py` - 제너레이터 패턴
- `lambda_functions.py` - 람다 함수 활용

## 🏃‍♂️ 실습 과제

1. **데이터 정제 프로그램**: 원시 데이터를 정제하여 깔끔한 형태로 변환
2. **성적 관리 시스템**: 학생 성적을 처리하고 통계를 계산
3. **파일 처리 도구**: 큰 파일을 메모리 효율적으로 처리
4. **데이터 분석 도구**: 다양한 데이터 변환 및 집계 작업

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 명확하고 읽기 쉬운 컴프리헨션
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# 적절한 람다 사용
sorted_items = sorted(items, key=lambda x: x['priority'])

# 메모리 효율적인 제너레이터
large_data = (process_item(item) for item in data_source)
```

### ❌ 피해야 할 예시
```python
# 너무 복잡한 컴프리헨션
result = [f(x) for x in [g(y) for y in data if condition(y)] if h(x)]

# 부작용이 있는 람다
counter = 0
result = list(map(lambda x: counter := counter + 1, data))

# 메모리 낭비
huge_list = [x**2 for x in range(10000000)]  # 모든 값을 메모리에 저장
```

## 🔗 관련 주제

- [반복문](../../02-control-flow/loops/) - 컴프리헨션의 기초
- [함수 정의와 호출](../../03-functions-modules/functions/) - 제너레이터 함수
- [자료구조 - 리스트와 튜플](../../05-data-structures/lists-tuples/) - 기본 데이터 구조
- [자료구조 - 딕셔너리와 집합](../../05-data-structures/dictionaries-sets/) - 딕셔너리/집합 컴프리헨션

## 📖 추가 학습 자료

- [Python 공식 문서 - List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Python 공식 문서 - Generator Expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)
- [PEP 289 - Generator Expressions](https://peps.python.org/pep-0289/)

---

**다음 단계**: [에러 처리 패턴](../error-handling/) 학습하기
