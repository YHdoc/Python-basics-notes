# 함수 정의와 호출 🔧

> 코드의 재사용성을 높이고 모듈화된 프로그램을 만드는 함수의 정의와 호출 방법을 학습합니다.

## 🎯 학습 목표

- [ ] 함수의 기본 정의와 호출 방법 이해
- [ ] 매개변수와 인수의 개념 학습
- [ ] 기본값 매개변수와 키워드 인수 사용법
- [ ] 가변 인수 (*args, **kwargs) 활용
- [ ] 함수의 반환값과 return 문 이해
- [ ] 지역 변수와 전역 변수 개념
- [ ] 람다 함수와 고차 함수 기초

## 📚 핵심 개념

### 1. 기본 함수 정의
```python
def function_name(parameters):
    """함수에 대한 설명"""
    # 함수 본문
    return result

# 함수 호출
result = function_name(arguments)
```

### 2. 매개변수와 인수
```python
def greet(name, age):
    return f"안녕하세요, {name}님! {age}세이시군요."

# 위치 인수
message = greet("김철수", 25)

# 키워드 인수
message = greet(age=25, name="김철수")
```

### 3. 기본값 매개변수
```python
def greet(name, age=20):
    return f"안녕하세요, {name}님! {age}세이시군요."

# 기본값 사용
message = greet("김철수")  # age는 20

# 기본값 덮어쓰기
message = greet("김철수", 30)
```

### 4. 가변 인수
```python
def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="김철수", age=25, city="서울")
```

## 📁 예제 파일

- `basic_functions.py` - 기본 함수 정의와 호출
- `parameters_arguments.py` - 매개변수와 인수
- `default_parameters.py` - 기본값 매개변수
- `variable_arguments.py` - 가변 인수
- `return_values.py` - 반환값과 return 문
- `scope_variables.py` - 변수 스코프
- `lambda_functions.py` - 람다 함수
- `higher_order_functions.py` - 고차 함수
- `practical_examples.py` - 실무에서 자주 사용되는 함수 패턴

## 🏃‍♂️ 실습 과제

1. **계산기 함수**: 사칙연산을 수행하는 함수들 만들기
2. **문자열 처리 함수**: 문자열을 다양한 방법으로 처리하는 함수들
3. **리스트 처리 함수**: 리스트를 조작하고 분석하는 함수들
4. **유틸리티 함수**: 자주 사용되는 유틸리티 함수들

## 💡 실무 팁

### ✅ 좋은 예시
```python
def calculate_discount(price, discount_rate=0.1):
    """할인가를 계산하는 함수"""
    if price < 0 or discount_rate < 0:
        raise ValueError("가격과 할인율은 0 이상이어야 합니다.")
    return price * (1 - discount_rate)

# 사용
discounted_price = calculate_discount(10000, 0.15)
```

### ❌ 피해야 할 예시
```python
# 의미없는 함수명
def func(a, b):
    return a + b

# 부작용이 있는 함수
def process_data(data):
    data.append("processed")  # 원본 데이터 변경
    return data
```

## 🔗 관련 주제

- [조건문](../../02-control-flow/conditionals/) - 함수 내에서 사용하는 조건문
- [반복문](../../02-control-flow/loops/) - 함수 내에서 사용하는 반복문
- [예외 처리](../../02-control-flow/exception-handling/) - 함수에서 예외 처리
- [모듈과 패키지](../../03-functions-modules/modules/) - 함수를 모듈로 구성하는 방법

## 📖 추가 학습 자료

- [Python 공식 문서 - 함수 정의](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [PEP 8 - 함수 정의 가이드](https://pep8.org/#function-definitions)

---

**다음 단계**: [모듈과 패키지](../../03-functions-modules/modules/) 학습하기
