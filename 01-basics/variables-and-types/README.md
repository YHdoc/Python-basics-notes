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

## 📁 예제 파일

- `basic_variables.py` - 기본 변수 선언과 할당
- `data_types.py` - 각 데이터 타입별 예제
- `type_conversion.py` - 타입 변환 예제
- `variable_naming.py` - 변수 명명 규칙과 관례
- `memory_efficiency.py` - 메모리 효율적인 변수 사용

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
