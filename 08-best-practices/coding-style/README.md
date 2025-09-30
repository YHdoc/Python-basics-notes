# 코딩 스타일 가이드 📝

> Python의 코딩 스타일 가이드인 PEP 8을 학습하고 일관성 있는 코드를 작성하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] PEP 8 코딩 스타일 가이드 이해
- [ ] 변수명과 함수명 명명 규칙
- [ ] 들여쓰기와 공백 사용법
- [ ] import 문 정렬과 그룹화
- [ ] 주석과 독스트링 작성법
- [ ] 코드 포맷팅 도구 활용
- [ ] 실무에서 자주 사용되는 스타일 패턴

## 📚 핵심 개념

### 1. 명명 규칙
```python
# 변수와 함수: snake_case
user_name = "김철수"
def calculate_average():
    pass

# 클래스: PascalCase
class UserManager:
    pass

# 상수: UPPER_SNAKE_CASE
MAX_RETRY_COUNT = 3
```

### 2. 들여쓰기와 공백
```python
# 4칸 들여쓰기 사용
def function():
    if condition:
        do_something()
    else:
        do_other_thing()

# 연산자 주변 공백
result = a + b * c
```

### 3. import 문 정렬
```python
# 표준 라이브러리
import os
import sys

# 서드파티 라이브러리
import requests
import numpy as np

# 로컬 모듈
from .utils import helper_function
from .models import User
```

### 4. 독스트링 작성
```python
def calculate_discount(price, discount_rate):
    """할인가를 계산하는 함수
    
    Args:
        price (float): 원가
        discount_rate (float): 할인율 (0.0 ~ 1.0)
    
    Returns:
        float: 할인된 가격
    
    Raises:
        ValueError: 할인율이 범위를 벗어난 경우
    """
    if not 0 <= discount_rate <= 1:
        raise ValueError("할인율은 0과 1 사이여야 합니다.")
    return price * (1 - discount_rate)
```

## 📁 예제 파일

- `naming_conventions.py` - 명명 규칙
- `indentation_spacing.py` - 들여쓰기와 공백
- `import_statements.py` - import 문 정렬
- `comments_docstrings.py` - 주석과 독스트링
- `code_formatting.py` - 코드 포맷팅
- `practical_examples.py` - 실무에서 자주 사용되는 스타일 패턴

## 🏃‍♂️ 실습 과제

1. **코드 리팩토링**: 기존 코드를 PEP 8 스타일로 개선
2. **독스트링 작성**: 함수와 클래스에 독스트링 추가
3. **import 정렬**: import 문을 올바른 순서로 정렬
4. **명명 규칙 적용**: 변수와 함수명을 적절한 규칙으로 변경

## 💡 실무 팁

### ✅ 좋은 예시
```python
def calculate_user_score(user_id, quiz_results):
    """사용자의 퀴즈 점수를 계산합니다.
    
    Args:
        user_id (int): 사용자 ID
        quiz_results (list): 퀴즈 결과 리스트
    
    Returns:
        float: 평균 점수
    """
    if not quiz_results:
        return 0.0
    
    total_score = sum(quiz_results)
    average_score = total_score / len(quiz_results)
    return round(average_score, 2)
```

### ❌ 피해야 할 예시
```python
# 잘못된 명명
def calcScore(u, q):
    # 잘못된 들여쓰기
    if q:
        return sum(q)/len(q)
    return 0

# 잘못된 import 순서
from .models import User
import os
import requests
```

## 🔗 관련 주제

- [함수 정의와 호출](../../03-functions-modules/functions/) - 함수 작성 스타일
- [클래스와 객체](../../04-oop/classes-and-objects/) - 클래스 작성 스타일
- [모듈과 패키지](../../03-functions-modules/modules/) - 모듈 구조 스타일

## 📖 추가 학습 자료

- [PEP 8 - Python 코딩 스타일 가이드](https://pep8.org/)
- [Google Python 스타일 가이드](https://google.github.io/styleguide/pyguide.html)

---

**다음 단계**: [성능 최적화](../../08-best-practices/performance-optimization/) 학습하기
