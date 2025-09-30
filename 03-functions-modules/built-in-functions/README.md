# 내장 함수와 라이브러리 🛠️

> Python에 내장된 유용한 함수들과 표준 라이브러리를 활용하여 효율적인 프로그램을 만드는 방법을 학습합니다.

## 🎯 학습 목표

- [ ] 주요 내장 함수들 (print, input, len, type 등) 활용
- [ ] 수학 관련 내장 함수들 (abs, round, min, max 등) 사용법
- [ ] 문자열 처리 내장 함수들 (str, int, float 등) 활용
- [ ] 컬렉션 관련 내장 함수들 (list, dict, set 등) 사용법
- [ ] 표준 라이브러리 주요 모듈들 (os, sys, datetime 등) 활용
- [ ] 파일 처리 관련 모듈들 (json, csv, pathlib 등) 사용법
- [ ] 네트워크와 웹 관련 모듈들 (urllib, requests 등) 기초

## 📚 핵심 개념

### 1. 주요 내장 함수들
```python
# 입출력
print("Hello, World!")
name = input("이름을 입력하세요: ")

# 타입 변환
number = int("123")
text = str(456)
decimal = float("3.14")

# 길이와 타입 확인
length = len("Hello")
data_type = type(42)
```

### 2. 수학 관련 함수들
```python
# 절댓값과 반올림
abs_value = abs(-5)
rounded = round(3.14159, 2)

# 최대/최소값
maximum = max(1, 5, 3, 9, 2)
minimum = min([10, 5, 8, 3, 7])

# 합계
total = sum([1, 2, 3, 4, 5])
```

### 3. 컬렉션 관련 함수들
```python
# 리스트 생성
numbers = list(range(5))
squares = [x**2 for x in range(5)]

# 딕셔너리 생성
person = dict(name="김철수", age=30)
scores = dict(zip(["A", "B", "C"], [85, 92, 78]))

# 집합 생성
unique_numbers = set([1, 2, 2, 3, 3, 4])
```

### 4. 표준 라이브러리 활용
```python
import os
import sys
import datetime
import json

# 시스템 정보
current_dir = os.getcwd()
python_version = sys.version

# 날짜/시간
now = datetime.datetime.now()
today = datetime.date.today()

# JSON 처리
data = {"name": "김철수", "age": 30}
json_string = json.dumps(data)
```

## 📁 예제 파일

- `basic_builtin_functions.py` - 기본 내장 함수들
- `math_functions.py` - 수학 관련 함수들
- `string_functions.py` - 문자열 처리 함수들
- `collection_functions.py` - 컬렉션 관련 함수들
- `standard_library.py` - 표준 라이브러리 활용
- `file_processing.py` - 파일 처리 관련 모듈들
- `practical_examples.py` - 실무에서 자주 사용되는 내장 함수 패턴

## 🏃‍♂️ 실습 과제

1. **데이터 변환기**: 다양한 타입의 데이터를 변환하는 프로그램
2. **통계 계산기**: 리스트의 통계를 계산하는 프로그램
3. **파일 관리자**: 파일과 디렉토리를 관리하는 프로그램
4. **JSON 데이터 처리**: JSON 데이터를 읽고 쓰는 프로그램

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 적절한 내장 함수 사용
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)

# 타입 안전성
user_input = input("숫자를 입력하세요: ")
try:
    number = int(user_input)
except ValueError:
    print("올바른 숫자를 입력해주세요.")
```

### ❌ 피해야 할 예시
```python
# 불필요한 반복문
total = 0
for num in numbers:
    total += num
# sum(numbers)가 더 간단

# 타입 확인 없이 변환
number = int(input("숫자: "))  # 에러 가능성
```

## 🔗 관련 주제

- [함수 정의와 호출](./functions/) - 내장 함수를 활용한 함수 정의
- [모듈과 패키지](./modules/) - 표준 라이브러리 모듈 사용
- [자료구조](../../05-data-structures/) - 내장 함수로 자료구조 조작

## 📖 추가 학습 자료

- [Python 공식 문서 - 내장 함수](https://docs.python.org/3/library/functions.html)
- [Python 공식 문서 - 표준 라이브러리](https://docs.python.org/3/library/)

---

**다음 단계**: [클래스와 객체](../../04-oop/classes-and-objects/) 학습하기
