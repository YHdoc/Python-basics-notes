# 리스트와 튜플 📋

> Python의 기본적인 시퀀스 자료구조인 리스트와 튜플을 학습하고 효율적으로 활용하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 리스트의 생성, 접근, 수정 방법 이해
- [ ] 리스트 메서드들 (append, insert, remove, pop 등) 활용
- [ ] 리스트 컴프리헨션을 통한 효율적인 리스트 생성
- [ ] 튜플의 특성과 불변성 이해
- [ ] 튜플 언패킹과 패킹 활용
- [ ] 리스트와 튜플의 차이점과 사용 시기
- [ ] 실무에서 자주 사용되는 리스트/튜플 패턴 익히기

## 📚 핵심 개념

### 1. 리스트 기본 사용법
```python
# 리스트 생성
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]

# 리스트 접근
first_item = numbers[0]
last_item = numbers[-1]

# 리스트 수정
numbers[0] = 10
numbers.append(6)
```

### 2. 리스트 메서드들
```python
# 추가/삭제
numbers.append(6)        # 끝에 추가
numbers.insert(0, 0)     # 특정 위치에 삽입
numbers.remove(3)        # 값으로 삭제
popped = numbers.pop()   # 끝에서 제거

# 정렬/검색
numbers.sort()           # 정렬
index = numbers.index(5) # 인덱스 찾기
count = numbers.count(2) # 개수 세기
```

### 3. 리스트 컴프리헨션
```python
# 기본 컴프리헨션
squares = [x**2 for x in range(10)]

# 조건부 컴프리헨션
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# 중첩 컴프리헨션
matrix = [[i+j for j in range(3)] for i in range(3)]
```

### 4. 튜플 사용법
```python
# 튜플 생성
coordinates = (10, 20)
colors = ("red", "green", "blue")

# 튜플 언패킹
x, y = coordinates
r, g, b = colors

# 튜플은 불변
# coordinates[0] = 5  # 에러 발생
```

## 📁 예제 파일

- `basic_lists.py` - 리스트 기본 사용법
- `list_methods.py` - 리스트 메서드들
- `list_comprehension.py` - 리스트 컴프리헨션
- `basic_tuples.py` - 튜플 기본 사용법
- `tuple_unpacking.py` - 튜플 언패킹과 패킹
- `lists_vs_tuples.py` - 리스트와 튜플 비교
- `practical_examples.py` - 실무에서 자주 사용되는 패턴

## 🏃‍♂️ 실습 과제

1. **학생 성적 관리**: 리스트를 활용한 성적 관리 시스템
2. **좌표계 계산**: 튜플을 활용한 좌표 계산 프로그램
3. **데이터 분석**: 리스트 컴프리헨션을 활용한 데이터 처리
4. **게임 보드**: 2차원 리스트를 활용한 게임 보드 구현

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 리스트 컴프리헨션 활용
even_numbers = [x for x in range(100) if x % 2 == 0]

# 튜플 언패킹 활용
name, age, city = ("김철수", 30, "서울")

# 적절한 자료구조 선택
coordinates = (10, 20)  # 불변 좌표
shopping_list = ["사과", "바나나"]  # 변경 가능한 목록
```

### ❌ 피해야 할 예시
```python
# 비효율적인 리스트 생성
numbers = []
for i in range(10):
    numbers.append(i**2)
# [i**2 for i in range(10)]가 더 효율적

# 불필요한 리스트 사용
constants = [3.14, 2.71]  # 튜플이 더 적합
```

## 🔗 관련 주제

- [반복문](../../02-control-flow/loops/) - 리스트와 함께 사용하는 반복문
- [함수 정의와 호출](../../03-functions-modules/functions/) - 리스트를 매개변수로 받는 함수
- [딕셔너리와 집합](../../05-data-structures/dictionaries-sets/) - 다른 자료구조와의 조합

## 📖 추가 학습 자료

- [Python 공식 문서 - 리스트](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python 공식 문서 - 튜플](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

---

**다음 단계**: [딕셔너리와 집합](../../05-data-structures/dictionaries-sets/) 학습하기
