# 반복문 (for/while) 🔄

> 프로그램에서 반복적인 작업을 수행하는 반복문을 학습하고 다양한 상황에 맞는 반복문을 작성하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] for문의 기본 구조와 사용법 이해
- [ ] while문의 기본 구조와 사용법 이해
- [ ] range() 함수를 활용한 반복문 작성
- [ ] 중첩된 반복문 작성 방법 학습
- [ ] break와 continue 문의 활용
- [ ] enumerate()와 zip() 함수 활용
- [ ] 실무에서 자주 사용되는 반복문 패턴 익히기

## 📚 핵심 개념

### 1. for문
```python
# 기본 for문
for item in sequence:
    # 반복할 코드
    print(item)

# range() 함수와 함께
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# 리스트와 함께
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

### 2. while문
```python
# 기본 while문
count = 0
while count < 5:
    print(count)
    count += 1

# 조건이 True인 동안 반복
while True:
    user_input = input("종료하려면 'quit' 입력: ")
    if user_input == "quit":
        break
```

### 3. break와 continue
```python
# break: 반복문 종료
for i in range(10):
    if i == 5:
        break  # 5에서 반복문 종료
    print(i)

# continue: 다음 반복으로 건너뛰기
for i in range(10):
    if i % 2 == 0:
        continue  # 짝수는 건너뛰기
    print(i)  # 홀수만 출력
```

### 4. enumerate()와 zip()
```python
# enumerate(): 인덱스와 값 함께 사용
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# zip(): 여러 시퀀스 동시 반복
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

## 📁 예제 파일

- `for_loops.py` - for문 기본 사용법
- `while_loops.py` - while문 기본 사용법
- `range_function.py` - range() 함수 활용
- `nested_loops.py` - 중첩된 반복문
- `break_continue.py` - break와 continue 사용법
- `enumerate_zip.py` - enumerate()와 zip() 활용
- `practical_examples.py` - 실무에서 자주 사용되는 반복문 패턴

## 🏃‍♂️ 실습 과제

1. **구구단 출력**: 2단부터 9단까지 구구단을 출력하는 프로그램
2. **숫자 맞추기 게임**: 1-100 사이의 숫자를 맞추는 게임
3. **별 찍기**: 다양한 모양의 별 패턴을 출력하는 프로그램
4. **리스트 처리**: 리스트의 요소들을 다양한 방법으로 처리하는 프로그램

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 명확한 반복문
for i in range(len(items)):
    if items[i] > 0:
        print(f"양수: {items[i]}")

# 더 파이썬다운 방법
for item in items:
    if item > 0:
        print(f"양수: {item}")

# enumerate 사용
for i, item in enumerate(items):
    if item > 0:
        print(f"인덱스 {i}: 양수 {item}")
```

### ❌ 피해야 할 예시
```python
# 무한 루프 위험
while True:
    # break 조건이 없음

# 불필요한 복잡성
for i in range(len(items)):
    item = items[i]  # 직접 접근이 더 간단
```

## 🔗 관련 주제

- [조건문](../../02-control-flow/conditionals/) - 반복문과 함께 사용하는 조건문
- [예외 처리](../../02-control-flow/exception-handling/) - 반복문에서 발생하는 예외 처리
- [자료구조 - 리스트와 튜플](../../05-data-structures/lists-tuples/) - 반복문에서 사용하는 자료구조

## 📖 추가 학습 자료

- [Python 공식 문서 - for문](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python 공식 문서 - while문](https://docs.python.org/3/tutorial/controlflow.html#while-statements)

---

**다음 단계**: [예외 처리](../../02-control-flow/exception-handling/) 학습하기
