# 정규표현식 🔍

> 정규표현식을 활용하여 복잡한 문자열 패턴을 매칭하고 처리하는 방법을 학습합니다.

## 🎯 학습 목표

- [ ] 정규표현식의 기본 문법 이해
- [ ] re 모듈의 주요 함수들 (search, match, findall 등) 활용
- [ ] 메타문자와 특수문자 사용법
- [ ] 그룹과 캡처 활용
- [ ] 치환과 분할 기능
- [ ] 플래그와 옵션 사용법
- [ ] 실무에서 자주 사용되는 정규표현식 패턴

## 📚 핵심 개념

### 1. 기본 정규표현식
```python
import re

# 기본 매칭
pattern = r"hello"
text = "hello world"
match = re.search(pattern, text)
```

### 2. 메타문자들
```python
# . (모든 문자)
pattern = r"h.llo"  # h + 임의 문자 + llo

# * (0개 이상)
pattern = r"ab*"    # a + b가 0개 이상

# + (1개 이상)
pattern = r"ab+"    # a + b가 1개 이상

# ? (0개 또는 1개)
pattern = r"ab?"    # a + b가 0개 또는 1개
```

### 3. 문자 클래스
```python
# [abc] - a, b, c 중 하나
pattern = r"[abc]"

# [0-9] - 숫자
pattern = r"[0-9]"

# [a-zA-Z] - 영문자
pattern = r"[a-zA-Z]"

# \d - 숫자, \w - 단어 문자, \s - 공백
pattern = r"\d+"    # 하나 이상의 숫자
```

### 4. 그룹과 캡처
```python
# 그룹화
pattern = r"(\d{3})-(\d{3})-(\d{4})"
text = "123-456-7890"
match = re.search(pattern, text)
if match:
    area_code = match.group(1)
    exchange = match.group(2)
    number = match.group(3)
```

## 📁 예제 파일

- `basic_regex.py` - 기본 정규표현식
- `metacharacters.py` - 메타문자 사용법
- `character_classes.py` - 문자 클래스
- `groups_captures.py` - 그룹과 캡처
- `substitution.py` - 치환과 분할
- `flags_options.py` - 플래그와 옵션
- `practical_examples.py` - 실무에서 자주 사용되는 패턴

## 🏃‍♂️ 실습 과제

1. **이메일 검증기**: 이메일 형식을 검증하는 프로그램
2. **전화번호 파서**: 전화번호를 파싱하는 프로그램
3. **HTML 태그 제거기**: HTML 태그를 제거하는 프로그램
4. **로그 파서**: 로그 파일에서 특정 패턴을 추출하는 프로그램

## 💡 실무 팁

### ✅ 좋은 예시
```python
import re

# 이메일 검증
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "user@example.com"
if re.match(email_pattern, email):
    print("유효한 이메일")

# 전화번호 추출
phone_pattern = r'(\d{3})-(\d{3})-(\d{4})'
text = "연락처: 123-456-7890"
match = re.search(phone_pattern, text)
```

### ❌ 피해야 할 예시
```python
# 복잡한 정규표현식
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# 너무 복잡하면 가독성이 떨어짐

# 정규표현식 남용
# 간단한 문자열 처리는 일반 메서드 사용
text = "hello world"
if "hello" in text:  # re.search보다 간단
    print("found")
```

## 🔗 관련 주제

- [문자열 처리](../../05-data-structures/string-processing/) - 정규표현식의 기초
- [파일 입출력](../../06-advanced/file-io/) - 파일에서 패턴 검색
- [예외 처리](../../02-control-flow/exception-handling/) - 정규표현식 오류 처리

## 📖 추가 학습 자료

- [Python 공식 문서 - 정규표현식](https://docs.python.org/3/library/re.html)
- [정규표현식 테스트 도구](https://regex101.com/)

---

**다음 단계**: [데코레이터](../../06-advanced/decorators/) 학습하기
