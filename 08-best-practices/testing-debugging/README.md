# 테스트와 디버깅 🐛

> Python에서 테스트를 작성하고 디버깅하는 방법을 학습하여 안정적인 코드를 만드는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 단위 테스트 작성 방법 이해
- [ ] unittest 모듈 활용
- [ ] pytest 프레임워크 사용법
- [ ] 테스트 주도 개발(TDD) 기초
- [ ] 디버깅 도구와 기법
- [ ] 로깅을 활용한 디버깅
- [ ] 실무에서 자주 사용되는 테스트 패턴

## 📚 핵심 개념

### 1. 단위 테스트
```python
import unittest

def add_numbers(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```

### 2. pytest 사용
```python
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_add_numbers_with_fixtures():
    # pytest fixture 사용
    pass
```

### 3. 디버깅 기법
```python
import pdb

def debug_function():
    x = 10
    y = 20
    pdb.set_trace()  # 디버거 시작
    result = x + y
    return result
```

### 4. 로깅 활용
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug(f"처리할 데이터: {data}")
    try:
        result = data * 2
        logger.info(f"처리 완료: {result}")
        return result
    except Exception as e:
        logger.error(f"처리 중 오류 발생: {e}")
        raise
```

## 📁 예제 파일

- `unit_testing.py` - 단위 테스트
- `pytest_usage.py` - pytest 사용법
- `debugging_techniques.py` - 디버깅 기법
- `logging_debugging.py` - 로깅을 활용한 디버깅
- `test_driven_development.py` - 테스트 주도 개발
- `practical_examples.py` - 실무에서 자주 사용되는 테스트 패턴

## 🏃‍♂️ 실습 과제

1. **계산기 테스트**: 간단한 계산기 함수들의 테스트 작성
2. **데이터 검증기**: 데이터 검증 함수들의 테스트 작성
3. **API 테스트**: API 함수들의 테스트 작성
4. **통합 테스트**: 여러 모듈을 함께 테스트하는 통합 테스트

## 💡 실무 팁

### ✅ 좋은 예시
```python
def test_user_creation():
    """사용자 생성 테스트"""
    user = create_user("김철수", "kim@example.com")
    assert user.name == "김철수"
    assert user.email == "kim@example.com"
    assert user.is_active is True

def test_invalid_email():
    """잘못된 이메일 테스트"""
    with pytest.raises(ValueError):
        create_user("김철수", "invalid-email")
```

### ❌ 피해야 할 예시
```python
# 테스트가 명확하지 않음
def test_something():
    result = some_function()
    assert result  # 무엇을 테스트하는지 불분명

# 예외 처리가 없는 테스트
def test_division():
    result = divide(10, 0)  # ZeroDivisionError 발생 가능
    assert result == 0
```

## 🔗 관련 주제

- [예외 처리](../02-control-flow/exception-handling/) - 테스트에서 예외 처리
- [함수 정의와 호출](../03-functions-modules/functions/) - 테스트할 함수들
- [클래스와 객체](../04-oop/classes-and-objects/) - 클래스 테스트

## 📖 추가 학습 자료

- [Python 공식 문서 - unittest](https://docs.python.org/3/library/unittest.html)
- [pytest 공식 문서](https://docs.pytest.org/)

---

**다음 단계**: [프로젝트 구조](./project-structure/) 학습하기
