# 예외 처리 (Exception Handling) ⚠️

> 프로그램 실행 중 발생할 수 있는 오류를 처리하고 안정적인 프로그램을 만드는 방법을 학습합니다.

## 🎯 학습 목표

- [ ] try-except 문의 기본 구조 이해
- [ ] 다양한 예외 타입과 처리 방법 학습
- [ ] finally 블록의 역할과 사용법
- [ ] else 블록의 활용
- [ ] 커스텀 예외 정의와 사용
- [ ] 실무에서 자주 사용되는 예외 처리 패턴 익히기

## 📚 핵심 개념

### 1. 기본 예외 처리
```python
try:
    # 예외가 발생할 수 있는 코드
    result = 10 / 0
except ZeroDivisionError:
    # 예외 처리 코드
    print("0으로 나눌 수 없습니다.")
```

### 2. 다양한 예외 처리
```python
try:
    # 여러 예외가 발생할 수 있는 코드
    number = int(input("숫자를 입력하세요: "))
    result = 10 / number
except ValueError:
    print("올바른 숫자를 입력해주세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print(f"예상치 못한 오류: {e}")
```

### 3. finally 블록
```python
try:
    # 파일 처리 등
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
finally:
    # 항상 실행되는 코드
    if 'file' in locals():
        file.close()
```

### 4. else 블록
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    # 예외가 발생하지 않았을 때만 실행
    print(f"결과: {result}")
```

## 📁 예제 파일

- `basic_exception_handling.py` - 기본 예외 처리
- `multiple_exceptions.py` - 여러 예외 처리
- `finally_else_blocks.py` - finally와 else 블록
- `custom_exceptions.py` - 커스텀 예외 정의
- `exception_hierarchy.py` - 예외 계층 구조
- `practical_examples.py` - 실무에서 자주 사용되는 예외 처리 패턴

## 🏃‍♂️ 실습 과제

1. **계산기 프로그램**: 나눗셈에서 0으로 나누는 오류 처리
2. **파일 처리 프로그램**: 파일이 없을 때의 오류 처리
3. **사용자 입력 검증**: 잘못된 입력에 대한 오류 처리
4. **네트워크 요청**: 연결 실패에 대한 오류 처리

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 구체적인 예외 처리
try:
    age = int(input("나이를 입력하세요: "))
except ValueError:
    print("올바른 숫자를 입력해주세요.")
    age = 0

# 리소스 정리
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
finally:
    if 'file' in locals():
        file.close()
```

### ❌ 피해야 할 예시
```python
# 너무 광범위한 예외 처리
try:
    # 모든 코드
    pass
except:
    pass  # 모든 예외를 무시

# 예외 정보를 무시
except Exception:
    print("오류 발생")  # 어떤 오류인지 모름
```

## 🔗 관련 주제

- [조건문](../../02-control-flow/conditionals/) - 예외 처리와 함께 사용하는 조건문
- [반복문](../../02-control-flow/loops/) - 예외 처리가 포함된 반복문
- [함수 정의와 호출](../../03-functions-modules/functions/) - 함수에서 예외 처리

## 📖 추가 학습 자료

- [Python 공식 문서 - 예외 처리](https://docs.python.org/3/tutorial/errors.html)
- [Python 공식 문서 - 내장 예외](https://docs.python.org/3/library/exceptions.html)

---

**다음 단계**: [함수 정의와 호출](../../03-functions-modules/functions/) 학습하기
