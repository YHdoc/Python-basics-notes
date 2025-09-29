# Python 코딩 스타일 가이드 📝

> PEP 8을 기반으로 한 Python 코딩 스타일 가이드입니다.

## 📋 PEP 8 핵심 규칙

### 1. 들여쓰기 (Indentation)
```python
# ✅ 좋은 예시 - 4개의 공백 사용
def function_name():
    if condition:
        do_something()
        if another_condition:
            do_another_thing()

# ❌ 나쁜 예시 - 탭과 공백 혼용
def function_name():
	if condition:
		do_something()
```

### 2. 줄 길이 (Line Length)
```python
# ✅ 좋은 예시 - 79자 이하
def calculate_total_price(item_price, tax_rate, discount_rate):
    return item_price * (1 + tax_rate) * (1 - discount_rate)

# ❌ 나쁜 예시 - 너무 긴 줄
def calculate_total_price(item_price, tax_rate, discount_rate, shipping_cost, handling_fee, insurance_cost):
    return item_price * (1 + tax_rate) * (1 - discount_rate) + shipping_cost + handling_fee + insurance_cost
```

### 3. 빈 줄 (Blank Lines)
```python
# ✅ 좋은 예시 - 적절한 빈 줄 사용
import os
import sys

from datetime import datetime


class MyClass:
    """클래스 설명"""
    
    def __init__(self):
        self.value = 0
    
    def method1(self):
        return self.value
    
    def method2(self):
        return self.value * 2


def function1():
    return "Hello"


def function2():
    return "World"
```

### 4. 임포트 (Imports)
```python
# ✅ 좋은 예시 - 표준 라이브러리, 서드파티, 로컬 순서
import os
import sys
from datetime import datetime

import requests
import pandas as pd

from mymodule import my_function
from mypackage.utils import helper_function

# ❌ 나쁜 예시 - 순서가 뒤섞임
import requests
import os
from mymodule import my_function
import sys
```

## 🏷️ 명명 규칙 (Naming Conventions)

### 1. 변수와 함수
```python
# ✅ 좋은 예시 - snake_case 사용
user_name = "홍길동"
student_count = 25
is_valid = True

def calculate_average():
    pass

def get_user_info():
    pass

# ❌ 나쁜 예시 - camelCase 또는 PascalCase
userName = "홍길동"
StudentCount = 25
IsValid = True

def CalculateAverage():
    pass
```

### 2. 클래스
```python
# ✅ 좋은 예시 - PascalCase 사용
class UserManager:
    pass

class DatabaseConnection:
    pass

class StudentInfo:
    pass

# ❌ 나쁜 예시 - snake_case 사용
class user_manager:
    pass

class database_connection:
    pass
```

### 3. 상수
```python
# ✅ 좋은 예시 - UPPER_CASE 사용
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# ❌ 나쁜 예시 - 일반 변수와 구분 안됨
maxConnections = 100
defaultTimeout = 30
```

### 4. 특수 메서드
```python
# ✅ 좋은 예시 - 언더스코어로 시작하고 끝남
class MyClass:
    def __init__(self):
        pass
    
    def __str__(self):
        return "MyClass"
    
    def __len__(self):
        return 0
```

## 📝 주석 (Comments)

### 1. 인라인 주석
```python
# ✅ 좋은 예시 - 코드와 한 줄 띄우고 설명
x = x + 1  # 경계값 증가

# ❌ 나쁜 예시 - 너무 당연한 설명
x = x + 1  # x에 1을 더함
```

### 2. 블록 주석
```python
# ✅ 좋은 예시 - 복잡한 로직 설명
# 사용자 인증을 위해 토큰을 검증하고
# 만료 시간을 확인한 후 세션을 갱신합니다.
def authenticate_user(token):
    pass
```

### 3. 독스트링 (Docstrings)
```python
# ✅ 좋은 예시 - 함수 설명
def calculate_discount(price, discount_rate):
    """
    할인된 가격을 계산합니다.
    
    Args:
        price (float): 원래 가격
        discount_rate (float): 할인율 (0.0 ~ 1.0)
    
    Returns:
        float: 할인된 가격
    
    Raises:
        ValueError: 할인율이 범위를 벗어난 경우
    """
    if not 0 <= discount_rate <= 1:
        raise ValueError("할인율은 0과 1 사이여야 합니다")
    
    return price * (1 - discount_rate)
```

## 🔧 코드 품질 도구

### 1. Black (코드 포맷터)
```bash
# 설치
pip install black

# 사용법
black your_file.py
black your_directory/
```

### 2. Flake8 (린터)
```bash
# 설치
pip install flake8

# 사용법
flake8 your_file.py
```

### 3. MyPy (타입 체커)
```python
# 타입 힌트 사용
def greet(name: str) -> str:
    return f"Hello, {name}!"

# 사용법
mypy your_file.py
```

## 📋 체크리스트

### 코드 작성 전
- [ ] 변수명이 의미를 명확히 전달하는가?
- [ ] 함수가 하나의 책임만 가지는가?
- [ ] 클래스명이 명확한가?

### 코드 작성 중
- [ ] 들여쓰기가 일관되는가?
- [ ] 줄 길이가 79자를 넘지 않는가?
- [ ] 적절한 빈 줄을 사용하는가?
- [ ] 임포트 순서가 올바른가?

### 코드 작성 후
- [ ] 불필요한 주석을 제거했는가?
- [ ] 독스트링을 작성했는가?
- [ ] 코드가 읽기 쉬운가?
- [ ] 테스트가 가능한 구조인가?

## 🎯 실무 팁

### 1. 가독성 우선
```python
# ✅ 좋은 예시 - 명확하고 읽기 쉬움
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

# ❌ 나쁜 예시 - 복잡하고 이해하기 어려움
def check(e):
    return "@" in e and "." in e.split("@")[1]
```

### 2. 일관성 유지
```python
# ✅ 좋은 예시 - 일관된 스타일
def get_user_name():
    pass

def get_user_age():
    pass

def get_user_email():
    pass

# ❌ 나쁜 예시 - 일관성 없음
def get_user_name():
    pass

def fetch_user_age():
    pass

def retrieve_user_email():
    pass
```

### 3. 의미있는 이름 사용
```python
# ✅ 좋은 예시 - 의미가 명확함
def calculate_monthly_payment(principal, interest_rate, years):
    pass

# ❌ 나쁜 예시 - 의미가 불분명함
def calc(a, b, c):
    pass
```

---

**좋은 코드는 다른 사람이 읽기 쉬운 코드입니다! 📖✨**
