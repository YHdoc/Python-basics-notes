# 조건문 (if/elif/else) 🔀

> 프로그램의 흐름을 제어하는 조건문을 학습하고 다양한 상황에 맞는 조건을 작성하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] if/elif/else 문의 기본 구조 이해
- [ ] 비교 연산자와 논리 연산자 활용
- [ ] 중첩된 조건문 작성 방법 학습
- [ ] 삼항 연산자 (Ternary Operator) 사용법 숙지
- [ ] 실무에서 자주 사용되는 조건문 패턴 익히기

## 📚 핵심 개념

### 1. 기본 조건문 구조
```python
if condition:
    # 조건이 True일 때 실행
    statement1
    statement2
elif another_condition:
    # 다른 조건이 True일 때 실행
    statement3
else:
    # 모든 조건이 False일 때 실행
    statement4
```

### 2. 비교 연산자
- `==` : 같다
- `!=` : 다르다
- `>` : 크다
- `<` : 작다
- `>=` : 크거나 같다
- `<=` : 작거나 같다

### 3. 논리 연산자
- `and` : 그리고 (모든 조건이 True)
- `or` : 또는 (하나라도 True)
- `not` : 아니다 (조건을 반대로)

### 4. 삼항 연산자
```python
# 기본 형태
result = value_if_true if condition else value_if_false

# 예시
grade = "합격" if score >= 60 else "불합격"
```

## 📁 예제 파일

- `basic_conditionals.py` - 기본 if/elif/else 구조
- `comparison_operators.py` - 비교 연산자 활용
- `logical_operators.py` - 논리 연산자 조합
- `nested_conditionals.py` - 중첩된 조건문
- `ternary_operator.py` - 삼항 연산자 사용법
- `practical_examples.py` - 실무에서 자주 사용되는 패턴

## 🏃‍♂️ 실습 과제

1. **성적 등급 판정**: 점수를 입력받아 A/B/C/D/F 등급을 출력하는 프로그램
2. **계절 판정**: 월을 입력받아 해당하는 계절을 출력하는 프로그램
3. **로그인 시스템**: 아이디와 비밀번호를 확인하는 간단한 로그인 프로그램
4. **할인 계산기**: 구매 금액에 따라 할인율을 적용하는 프로그램

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 명확한 조건과 적절한 들여쓰기
if user_age >= 18:
    if has_license:
        print("운전 가능합니다.")
    else:
        print("면허가 필요합니다.")
else:
    print("미성년자는 운전할 수 없습니다.")

# 가독성 좋은 삼항 연산자
status = "활성" if user.is_active else "비활성"
```

### ❌ 피해야 할 예시
```python
# 복잡한 중첩 (3단계 이상)
if condition1:
    if condition2:
        if condition3:
            if condition4:
                # 너무 깊은 중첩

# 의미없는 변수명
if a > b:
    c = True
else:
    c = False
```

## 🔗 관련 주제

- [연산자](../01-basics/operators/) - 조건문에서 사용하는 연산자들
- [반복문](./loops/) - 조건문과 함께 사용하는 반복문
- [예외 처리](./exception-handling/) - 오류 상황을 처리하는 방법

## 📖 추가 학습 자료

- [Python 공식 문서 - if 문](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [PEP 8 - 들여쓰기 규칙](https://pep8.org/#indentation)

---

**다음 단계**: [반복문](./loops/) 학습하기
