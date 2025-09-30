# 변수와 데이터 타입 📊

> Python에서 변수를 선언하고 다양한 데이터 타입을 다루는 방법을 학습합니다.

## 🎯 학습 목표

- [ ] Python 변수 선언과 할당 방법 이해
- [ ] 기본 데이터 타입 (int, float, str, bool) 숙지
- [ ] 타입 변환 (Type Casting) 방법 학습
- [ ] 변수 명명 규칙과 관례 이해
- [ ] 메모리 효율적인 변수 사용법 습득

## 📚 핵심 개념

### 1. 변수 선언과 할당
```python
# 변수 선언 (타입 지정 불필요)
name = "홍길동"
age = 25
height = 175.5
is_student = True
```

### 2. 기본 데이터 타입
- **정수 (int)**: `42`, `-10`, `0`
- **실수 (float)**: `3.14`, `-2.5`, `0.0`
- **문자열 (str)**: `"Hello"`, `'World'`, `"""여러 줄"""` 
- **불린 (bool)**: `True`, `False`

### 3. 타입 확인과 변환
```python
# 타입 확인
print(type(variable))

# 타입 변환
int_value = int("123")
str_value = str(456)
float_value = float("3.14")
```

## 📦 Mutable vs Immutable

> Python에서 객체의 변경 가능성을 이해하는 것은 매우 중요.

### 핵심 개념
- **Mutable**: 생성 후 내용을 변경할 수 있는 객체
- **Immutable**: 생성 후 내용을 변경할 수 없는 객체

### 타입별 분류

| 타입 | Mutable/Immutable | 특징 | 예시 |
|------|------------------|------|------|
| `int`, `float`, `bool` | Immutable | 값 변경 시 새 객체 생성 | `x = 5; x = 6` |
| `str` | Immutable | 문자열 수정 시 새 문자열 생성 | `s = "hello"; s += " world"` |
| `tuple` | Immutable | 생성 후 수정 불가 | `t = (1, 2); t[0] = 3` (에러!) |
| `list` | Mutable | 인덱스로 요소 수정 가능 | `lst = [1, 2]; lst[0] = 3` |
| `dict` | Mutable | 키-값 쌍 추가/수정/삭제 가능 | `d = {}; d['key'] = 'value'` |
| `set` | Mutable | 요소 추가/삭제 가능 | `s = {1, 2}; s.add(3)` |

### 실험으로 이해하기

```python
# Immutable (int) - 새 객체 생성
x = 5
print(f"초기: x={x}, id={id(x)}")
x = 6  # 새로운 객체 생성
print(f"변경: x={x}, id={id(x)}")  # id가 다름!

# Mutable (list) - 같은 객체 수정
lst = [1, 2, 3]
print(f"초기: lst={lst}, id={id(lst)}")
lst[0] = 10  # 같은 객체 수정
print(f"변경: lst={lst}, id={id(lst)}")  # id가 같음!
```

### 실무에서 주의사항

#### 1. 함수 기본값으로 Mutable 객체 사용 금지
```python
# ❌ 위험한 예시
def bad_function(items=[]):  # 기본값이 mutable!
    items.append("new item")
    return items

# ✅ 안전한 예시
def good_function(items=None):
    if items is None:
        items = []
    items.append("new item")
    return items
```

#### 2. 참조 vs 복사
```python
# Mutable 객체 참조
list1 = [1, 2, 3]
list2 = list1  # 같은 객체 참조
list1.append(4)
print(list2)  # [1, 2, 3, 4] - list2도 변경됨!

# 복사가 필요한 경우
list3 = list1.copy()  # 얕은 복사
list4 = copy.deepcopy(list1)  # 깊은 복사
```

#### 3. 성능과 메모리 관점
- **Immutable 장점**: 메모리 효율적, 스레드 안전, 해시 가능
- **Mutable 장점**: in-place 수정, 유연한 데이터 구조

## 📁 예제 파일

- `basic_variables.py` - 기본 변수 선언과 할당
- `data_types.py` - 각 데이터 타입별 예제
- `type_conversion.py` - 타입 변환 예제
- `variable_naming.py` - 변수 명명 규칙과 관례
- `memory_efficiency.py` - 메모리 효율적인 변수 사용
- `mutable_immutable.py` - Mutable vs Immutable 완전 정리

## 🏃‍♂️ 실습 과제

1. **기본 변수 연습**: 개인 정보를 담는 변수들을 선언해보세요
2. **타입 변환 연습**: 사용자 입력을 받아 적절한 타입으로 변환해보세요
3. **계산기 만들기**: 두 숫자를 입력받아 사칙연산을 수행하는 프로그램을 작성해보세요

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 명확하고 의미있는 변수명
user_name = "김철수"
user_age = 30
is_premium_user = True

# 적절한 타입 변환
price = float(input("가격을 입력하세요: "))
quantity = int(input("수량을 입력하세요: "))
total = price * quantity
```

### ❌ 피해야 할 예시
```python
# 의미없는 변수명
a = "김철수"
b = 30
c = True

# 불필요한 타입 변환
age = int("25")  # 이미 정수인데 변환
```

## 🔗 관련 주제

- [연산자](../../01-basics/operators/) - 변수와 함께 사용하는 연산자들
- [입출력](../../01-basics/input-output/) - 사용자 입력을 변수에 저장하는 방법
- [자료구조 - 리스트와 튜플](../../05-data-structures/lists-tuples/) - 여러 값을 담는 자료구조

## 📖 추가 학습 자료

- [Python 공식 문서 - 내장 타입](https://docs.python.org/3/library/stdtypes.html)
- [PEP 8 - 변수 명명 규칙](https://pep8.org/#naming-conventions)

---

**다음 단계**: [연산자](../../01-basics/operators/) 학습하기
