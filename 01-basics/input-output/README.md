# 입출력 (Input/Output) 📥📤

> Python에서 사용자 입력을 받고 결과를 출력하는 방법을 학습합니다.

## 🎯 학습 목표

- [ ] print() 함수를 활용한 다양한 출력 방법
- [ ] input() 함수로 사용자 입력 받기
- [ ] 문자열 포맷팅 (f-string, format(), %)
- [ ] 파일 입출력 기초
- [ ] 에러 처리와 입력 검증
- [ ] 실무에서 자주 사용되는 입출력 패턴

## 📚 핵심 개념

### 1. 출력 (Output)
```python
# 기본 출력
print("Hello, World!")

# 여러 값 출력
name = "김철수"
age = 25
print("이름:", name, "나이:", age)

# f-string (Python 3.6+)
print(f"이름: {name}, 나이: {age}")

# format() 메서드
print("이름: {}, 나이: {}".format(name, age))
```

### 2. 입력 (Input)
```python
# 기본 입력
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")

# 타입 변환과 함께
age = int(input("나이를 입력하세요: "))
height = float(input("키를 입력하세요: "))
```

### 3. 문자열 포맷팅
```python
# f 자체는 "formatted string"을 의미. C#의 string.Format() 또는 문자열 보간($) 을 생각해 보면 쉽다.
# f-string (권장)
name = "홍길동"
score = 95.5
print(f"{name}님의 점수는 {score:.1f}점입니다.")

# format() 메서드
print("{0}님의 점수는 {1:.1f}점입니다.".format(name, score))

# % 포맷팅 (구식)
print("%s님의 점수는 %.1f점입니다." % (name, score))
```


### 기타

1. with 문법

with 는 Context Manager(컨텍스트 관리자) 를 사용할 때 쓰는 문법.
C# 의 using 문과 매우 유사하다.
-둘 다 리소스 관리를 위한 것
-스코프를 벗어나면 자동으로 자원 해제
-예외가 발생해도 안전하게 리소스 해제

즉,
C#: using (var file = new StreamWriter("sample.txt")) { ... }
Python: with open("sample.txt", "w") as file: ...
→ 동작 의도는 동일하다.

장점: try-finally 없이도 안전하게 리소스를 정리할 수 있다.(with 문은 내부적으로 try-finally 를 자동으로 써주는 문법)




2. open 문법

open(...) 은 파일 객체를 반환하는데, 이 객체는 컨텍스트 관리자를 지원한다.

따라서 with open(...) as file: 구문을 쓰면:
파일을 열고(__enter__)
블록이 끝나면 자동으로 file.close() 를 호출해준다.




3. open 함수의 파라미터

```python
open(file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
주요 파라미터:

file : 파일 경로 (문자열 또는 Path 객체)
mode : 파일 열기 모드
"r" : 읽기 (기본값)
"w" : 쓰기 (기존 내용 삭제 후 새로 작성) 
"a" : 추가(append)
"x" : 새 파일만 생성 (이미 존재하면 오류)
"rb", "wb" : 바이너리 모드
encoding : 텍스트 인코딩 (예: "utf-8", "cp949")
newline : 줄바꿈 처리 방식




4. 파이썬의 빌트인 함수

all(), len() 같이 import 없이 바로 쓸 수 있는 전역 함수들.

Ex)
len() : 길이 반환
all() : 모든 요소가 참이면 True
any() : 하나라도 참이면 True
sum(), min(), max(), sorted(), enumerate() … 등
👉 builtins 모듈에 포함되어 있고, 기본적으로 항상 import 되어 있음.

```python
nums = [1, 2, 3, 0]
print(len(nums))       # 4
print(all(nums))       # False (0이 있어서)
print(any(nums))       # True  (0이 아닌 게 있어서)
print(sum(nums))       # 6
print(sorted(nums))    # [0, 1, 2, 3]
```


C#의 LINQ 메서드 (Count(), All(), Any(), Sum(), OrderBy()) 와 느낌이 비슷함.
* 차이
C# LINQ → 메서드 체이닝 스타일 (nums.Where(...).Select(...).ToList())
Python → 함수형 내장 함수 + 제너레이터/리스트 컴프리헨션 조합


| C# LINQ 메서드              | Python 대응 방식                                                                     | 예제 (C# → Python)                                                  |
| ------------------------ | -------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `Count()`                | `len(iterable)`                                                                  | `nums.Count()` → `len(nums)`                                      |
| `Sum()`                  | `sum(iterable)`                                                                  | `nums.Sum()` → `sum(nums)`                                        |
| `Min()`                  | `min(iterable)`                                                                  | `nums.Min()` → `min(nums)`                                        |
| `Max()`                  | `max(iterable)`                                                                  | `nums.Max()` → `max(nums)`                                        |
| `All(predicate)`         | `all(expr for x in iterable)`                                                    | `nums.All(x => x > 0)` → `all(x > 0 for x in nums)`               |
| `Any(predicate)`         | `any(expr for x in iterable)`                                                    | `nums.Any(x => x > 5)` → `any(x > 5 for x in nums)`               |
| `Where(predicate)`       | 리스트/제너레이터 컴프리헨션                                                                  | `nums.Where(x => x % 2 == 0)` → `[x for x in nums if x % 2 == 0]` |
| `Select(selector)`       | 리스트/제너레이터 컴프리헨션, `map`                                                           | `nums.Select(x => x * x)` → `[x * x for x in nums]`               |
| `OrderBy(key)`           | `sorted(iterable, key=...)`                                                      | `nums.OrderBy(x => x)` → `sorted(nums)`                           |
| `OrderByDescending(key)` | `sorted(iterable, key=..., reverse=True)`                                        | `nums.OrderByDescending(x => x)` → `sorted(nums, reverse=True)`   |
| `First()`                | `next(iter(iterable))`                                                           | `nums.First()` → `next(iter(nums))`                               |
| `FirstOrDefault()`       | `next(iter(iterable), default)`                                                  | `nums.FirstOrDefault()` → `next(iter(nums), None)`                |
| `Distinct()`             | `set(iterable)` (단, 순서 보장 X) / `dict.fromkeys(iterable)` (순서 보장)                 | `nums.Distinct()` → `list(set(nums))`                             |
| `GroupBy(key)`           | `itertools.groupby(iterable, key=...)` (정렬 필요) / `collections.defaultdict(list)` | `nums.GroupBy(x => x % 2)` → `groupby(nums, key=lambda x: x % 2)` |





## 📁 예제 파일

- `basic_output.py` - 기본 출력 방법들
- `basic_input.py` - 기본 입력 방법들
- `string_formatting.py` - 문자열 포맷팅 방법들
- `file_io_basic.py` - 파일 입출력 기초
- `input_validation.py` - 입력 검증과 에러 처리
- `practical_examples.py` - 실무에서 자주 사용되는 입출력 패턴

## 🏃‍♂️ 실습 과제

1. **개인정보 입력 프로그램**: 이름, 나이, 주소를 입력받아 출력하는 프로그램
2. **계산기 프로그램**: 두 숫자를 입력받아 사칙연산 결과를 출력하는 프로그램
3. **성적 관리 프로그램**: 학생 정보를 입력받아 성적표를 출력하는 프로그램
4. **간단한 로그인 시스템**: 아이디와 비밀번호를 입력받아 검증하는 프로그램

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 명확한 입력 안내
name = input("사용자 이름을 입력하세요: ")

# 안전한 타입 변환
try:
    age = int(input("나이를 입력하세요: "))
except ValueError:
    print("올바른 숫자를 입력해주세요.")
    age = 0

# 깔끔한 출력
print(f"안녕하세요, {name}님! ({age}세)")
```

### ❌ 피해야 할 예시
```python
# 불명확한 입력 안내
name = input("입력: ")

# 에러 처리가 없는 타입 변환
age = int(input("나이: "))  # 에러 발생 가능

# 복잡한 출력
print("안녕하세요, " + name + "님! (" + str(age) + "세)")
```

## 🔗 관련 주제

- [변수와 데이터 타입](../../01-basics/variables-and-types/) - 입력받은 데이터의 타입
- [연산자](../../01-basics/operators/) - 입력받은 데이터로 연산 수행
- [조건문](../../02-control-flow/conditionals/) - 입력 검증과 조건 처리

## 📖 추가 학습 자료

- [Python 공식 문서 - print()](https://docs.python.org/3/library/functions.html#print)
- [Python 공식 문서 - input()](https://docs.python.org/3/library/functions.html#input)
- [PEP 498 - f-string](https://peps.python.org/pep-0498/)

---

**다음 단계**: [조건문](../../02-control-flow/conditionals/README.md) 학습하기
