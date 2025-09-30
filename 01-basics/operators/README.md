# 연산자 🔢

> Python에서 사용할 수 있는 다양한 연산자들을 학습하고 실무에서 활용하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 산술 연산자 (+, -, *, /, %, **, //) 이해
- [ ] 비교 연산자 (==, !=, <, >, <=, >=) 활용
- [ ] 논리 연산자 (and, or, not) 조합
- [ ] 할당 연산자 (=, +=, -=, *=, /=) 사용법
- [ ] 비트 연산자 (&, |, ^, ~, <<, >>) 기초
- [ ] 멤버십 연산자 (in, not in) 활용
- [ ] 연산자 우선순위 이해

## 📚 핵심 개념

### 1. 산술 연산자
```python
# 기본 산술 연산
a = 10
b = 3

print(a + b)    # 덧셈: 13
print(a - b)    # 뺄셈: 7
print(a * b)    # 곱셈: 30
print(a / b)    # 나눗셈: 3.333...
print(a % b)    # 나머지: 1
print(a ** b)   # 거듭제곱: 1000
print(a // b)   # 몫: 3
```

### 2. 비교 연산자
```python
x = 5
y = 10

print(x == y)   # 같다: False
print(x != y)   # 다르다: True
print(x < y)    # 작다: True
print(x > y)    # 크다: False
print(x <= y)   # 작거나 같다: True
print(x >= y)   # 크거나 같다: False
```

### 3. 논리 연산자
```python
age = 25
has_license = True

# and: 모든 조건이 True여야 True
can_drive = age >= 18 and has_license

# or: 하나라도 True면 True
is_young_or_old = age < 20 or age > 60

# not: 조건을 반대로
is_not_adult = not (age >= 18)
```

### 4. 할당 연산자
```python
count = 10

count += 5      # count = count + 5
count -= 3      # count = count - 3
count *= 2      # count = count * 2
count /= 4      # count = count / 4
count %= 3      # count = count % 3
```

## 📁 예제 파일

- `arithmetic_operators.py` - 산술 연산자 예제
- `comparison_operators.py` - 비교 연산자 예제
- `logical_operators.py` - 논리 연산자 예제
- `assignment_operators.py` - 할당 연산자 예제
- `bitwise_operators.py` - 비트 연산자 예제
- `membership_operators.py` - 멤버십 연산자 예제
- `operator_precedence.py` - 연산자 우선순위 예제
- `practical_examples.py` - 실무에서 자주 사용되는 연산자 패턴

## 🏃‍♂️ 실습 과제

1. **계산기 만들기**: 두 숫자를 입력받아 모든 산술 연산을 수행하는 프로그램
2. **성적 판정**: 점수를 입력받아 합격/불합격을 판정하는 프로그램
3. **나이대 분류**: 나이를 입력받아 어린이/청소년/성인/노인으로 분류하는 프로그램
4. **비밀번호 검증**: 비밀번호의 길이와 특수문자 포함 여부를 확인하는 프로그램

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 명확한 조건문
if user_age >= 18 and has_valid_id:
    print("서비스 이용 가능")

# 효율적인 할당
total_score += current_score
user_count += 1

# 안전한 나눗셈
result = dividend / divisor if divisor != 0 else 0
```

### ❌ 피해야 할 예시
```python
# 복잡한 연산자 조합
if a == b and c != d or e > f and g < h:  # 괄호로 명확히 구분

# 불필요한 연산
result = x + 0  # 그냥 x 사용
```

## 🔗 관련 주제

- [변수와 데이터 타입](../../01-basics/variables-and-types/) - 연산자와 함께 사용하는 변수들
- [조건문](../../02-control-flow/conditionals/) - 연산자를 활용한 조건문
- [입출력](../../01-basics/input-output/) - 연산 결과를 출력하는 방법

## 📖 추가 학습 자료

- [Python 공식 문서 - 연산자](https://docs.python.org/3/reference/expressions.html#operator-precedence)
- [PEP 8 - 연산자 사용 가이드](https://pep8.org/#other-recommendations)

---

**다음 단계**: [입출력](../../01-basics/input-output/) 학습하기
