# 조건문 🔀

> 프로그램의 흐름을 제어하는 조건문을 학습하고 다양한 상황에 맞는 로직을 구현하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] if, elif, else 문의 기본 사용법 이해
- [ ] 비교 연산자와 논리 연산자 활용
- [ ] 중첩된 조건문 작성 방법
- [ ] 삼항 연산자 사용법
- [ ] 조건문의 가독성 향상 기법
- [ ] 실무에서 자주 사용되는 조건문 패턴
- [ ] 조건문을 활용한 프로그램 흐름 제어

## 📚 핵심 개념

### 1. 기본 조건문
```python
age = 18

if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")
```

### 2. elif 사용
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### 3. 논리 연산자
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("운전 가능합니다.")
elif age >= 18 and not has_license:
    print("면허가 필요합니다.")
else:
    print("운전할 수 없습니다.")
```

### 4. 중첩 조건문
```python
weather = "sunny"
temperature = 25

if weather == "sunny":
    if temperature > 30:
        print("더운 날씨입니다.")
    elif temperature > 20:
        print("따뜻한 날씨입니다.")
    else:
        print("선선한 날씨입니다.")
else:
    print("흐린 날씨입니다.")
```

## 📁 예제 파일

- `basic_conditionals.py` - 기본 조건문 예제
- `comparison_operators.py` - 비교 연산자 활용
- `logical_operators.py` - 논리 연산자 활용
- `nested_conditionals.py` - 중첩 조건문
- `ternary_operator.py` - 삼항 연산자
- `practical_examples.py` - 실무에서 자주 사용되는 조건문 패턴

## 🏃‍♂️ 실습 과제

1. **성적 등급 계산기**: 점수에 따른 등급을 계산하는 프로그램
2. **나이별 할인 계산기**: 나이에 따른 할인율을 계산하는 프로그램
3. **날씨별 활동 추천기**: 날씨와 온도에 따른 활동을 추천하는 프로그램
4. **사용자 권한 관리**: 사용자 타입에 따른 권한을 확인하는 프로그램

## 💡 실무 팁

### ✅ 좋은 예시
```python
def calculate_discount(age, is_student=False):
    """나이와 학생 여부에 따른 할인율 계산"""
    if age < 18:
        return 0.5  # 50% 할인
    elif age >= 65:
        return 0.3  # 30% 할인
    elif is_student:
        return 0.2  # 20% 할인
    else:
        return 0.0  # 할인 없음
```

### ❌ 피해야 할 예시
```python
# 너무 깊은 중첩
if condition1:
    if condition2:
        if condition3:
            if condition4:
                # 너무 깊음
                pass

# 복잡한 조건문
if (a > b and c < d) or (e == f and g != h) or (i in j and k not in l):
    # 가독성이 떨어짐
    pass
```

## 🔗 관련 주제

- [연산자](../../01-basics/operators/) - 조건문에서 사용하는 연산자들
- [입출력](../../01-basics/input-output/) - 조건문과 함께 사용하는 입출력
- [반복문](../../02-control-flow/loops/) - 조건문과 반복문의 조합

## 📖 추가 학습 자료

- [Python 공식 문서 - 제어 흐름](https://docs.python.org/3/tutorial/controlflow.html)
- [PEP 8 - 조건문 가이드](https://pep8.org/#comparisons)

---

**다음 단계**: [반복문](../../02-control-flow/loops/) 학습하기