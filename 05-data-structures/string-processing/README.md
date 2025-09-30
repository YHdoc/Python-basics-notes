# 문자열 처리 📝

> Python에서 문자열을 효율적으로 처리하고 조작하는 방법을 학습합니다.

## 🎯 학습 목표

- [ ] 문자열의 기본 특성과 불변성 이해
- [ ] 문자열 메서드들 (split, join, replace, strip 등) 활용
- [ ] 문자열 포맷팅 방법들 (f-string, format, %)
- [ ] 정규표현식을 활용한 문자열 패턴 매칭
- [ ] 문자열 인코딩과 유니코드 처리
- [ ] 문자열 검색과 치환 기법
- [ ] 실무에서 자주 사용되는 문자열 처리 패턴

## 📚 핵심 개념

### 1. 문자열 기본 특성
```python
# 문자열은 불변
text = "Hello"
# text[0] = "h"  # 에러 발생

# 문자열 연결
result = "Hello" + " " + "World"
```

### 2. 문자열 메서드들
```python
text = "  Hello, World!  "

# 공백 제거
cleaned = text.strip()

# 분할과 결합
words = text.split(",")
joined = "-".join(words)

# 대소문자 변환
upper_text = text.upper()
lower_text = text.lower()
```

### 3. 문자열 포맷팅
```python
name = "김철수"
age = 30

# f-string (권장)
message = f"안녕하세요, {name}님! {age}세이시군요."

# format() 메서드
message = "안녕하세요, {}님! {}세이시군요.".format(name, age)

# % 포맷팅
message = "안녕하세요, %s님! %d세이시군요." % (name, age)
```

### 4. 정규표현식
```python
import re

# 패턴 매칭
pattern = r"\d+"
text = "I have 123 apples and 456 oranges"
numbers = re.findall(pattern, text)
```

## 📁 예제 파일

- `basic_string_methods.py` - 기본 문자열 메서드들
- `string_formatting.py` - 문자열 포맷팅 방법들
- `string_search_replace.py` - 문자열 검색과 치환
- `regular_expressions.py` - 정규표현식 활용
- `string_encoding.py` - 문자열 인코딩 처리
- `practical_examples.py` - 실무에서 자주 사용되는 패턴

## 🏃‍♂️ 실습 과제

1. **텍스트 분석기**: 텍스트의 통계를 분석하는 프로그램
2. **CSV 파서**: CSV 파일을 파싱하는 프로그램
3. **이메일 검증기**: 이메일 형식을 검증하는 프로그램
4. **로그 파서**: 로그 파일을 분석하는 프로그램

## 💡 실무 팁

### ✅ 좋은 예시
```python
# f-string 사용
name = "김철수"
age = 30
message = f"안녕하세요, {name}님! {age}세이시군요."

# 안전한 문자열 처리
text = "  Hello, World!  "
cleaned = text.strip().lower()

# 정규표현식 활용
import re
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

### ❌ 피해야 할 예시
```python
# 비효율적인 문자열 연결
result = ""
for word in words:
    result += word + " "
# " ".join(words)가 더 효율적

# 하드코딩된 포맷팅
message = "Hello, " + name + "! You are " + str(age) + " years old."
```

## 🔗 관련 주제

- [리스트와 튜플](./lists-tuples/) - 문자열을 리스트로 변환
- [딕셔너리와 집합](./dictionaries-sets/) - 문자열 데이터 구조화
- [정규표현식](../../06-advanced/regex/) - 고급 문자열 패턴 매칭

## 📖 추가 학습 자료

- [Python 공식 문서 - 문자열](https://docs.python.org/3/tutorial/introduction.html#strings)
- [Python 공식 문서 - 정규표현식](https://docs.python.org/3/library/re.html)

---

**다음 단계**: [파일 입출력](../../06-advanced/file-io/) 학습하기
