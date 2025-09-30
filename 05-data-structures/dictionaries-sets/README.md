# 딕셔너리와 집합 📚

> Python의 고급 자료구조인 딕셔너리와 집합을 학습하고 효율적으로 활용하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 딕셔너리의 생성, 접근, 수정 방법 이해
- [ ] 딕셔너리 메서드들 (keys, values, items 등) 활용
- [ ] 딕셔너리 컴프리헨션을 통한 효율적인 딕셔너리 생성
- [ ] 집합의 특성과 집합 연산 이해
- [ ] 집합 메서드들 (add, remove, union, intersection 등) 활용
- [ ] 딕셔너리와 집합의 실무 활용 사례
- [ ] 성능 최적화를 위한 자료구조 선택

## 📚 핵심 개념

### 1. 딕셔너리 기본 사용법
```python
# 딕셔너리 생성
person = {"name": "김철수", "age": 30, "city": "서울"}
scores = dict(Alice=85, Bob=92, Charlie=78)

# 접근과 수정
name = person["name"]
person["age"] = 31
person["job"] = "개발자"
```

### 2. 딕셔너리 메서드들
```python
# 키, 값, 항목 접근
keys = person.keys()
values = person.values()
items = person.items()

# 안전한 접근
age = person.get("age", 0)
name = person.pop("name", "Unknown")
```

### 3. 딕셔너리 컴프리헨션
```python
# 기본 컴프리헨션
squares = {x: x**2 for x in range(5)}

# 조건부 컴프리헨션
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

### 4. 집합 사용법
```python
# 집합 생성
fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 4, 5])

# 집합 연산
union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
```

## 📁 예제 파일

- `basic_dictionaries.py` - 딕셔너리 기본 사용법
- `dictionary_methods.py` - 딕셔너리 메서드들
- `dictionary_comprehension.py` - 딕셔너리 컴프리헨션
- `basic_sets.py` - 집합 기본 사용법
- `set_operations.py` - 집합 연산들
- `practical_examples.py` - 실무에서 자주 사용되는 패턴

## 🏃‍♂️ 실습 과제

1. **사용자 관리 시스템**: 딕셔너리를 활용한 사용자 정보 관리
2. **단어 빈도 분석**: 텍스트에서 단어 빈도를 계산하는 프로그램
3. **데이터 중복 제거**: 집합을 활용한 중복 데이터 제거
4. **관계 분석**: 집합 연산을 활용한 데이터 관계 분석

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 딕셔너리 컴프리헨션 활용
word_count = {word: text.count(word) for word in set(text.split())}

# 안전한 딕셔너리 접근
age = person.get("age", 0)

# 집합으로 중복 제거
unique_items = set(duplicate_list)
```

### ❌ 피해야 할 예시
```python
# 키 존재 확인 없이 접근
age = person["age"]  # KeyError 가능

# 비효율적인 중복 제거
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
# set(items)가 더 효율적
```

## 🔗 관련 주제

- [리스트와 튜플](../../05-data-structures/lists-tuples/) - 다른 자료구조와의 조합
- [함수 정의와 호출](../../03-functions-modules/functions/) - 딕셔너리를 매개변수로 받는 함수
- [반복문](../../02-control-flow/loops/) - 딕셔너리와 집합 순회

## 📖 추가 학습 자료

- [Python 공식 문서 - 딕셔너리](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python 공식 문서 - 집합](https://docs.python.org/3/tutorial/datastructures.html#sets)

---

**다음 단계**: [문자열 처리](../../05-data-structures/string-processing/) 학습하기
