# 파일 입출력 💾

> Python에서 파일을 읽고 쓰는 방법을 학습하고 다양한 파일 형식을 처리하는 방법을 익힙니다.

## 🎯 학습 목표

- [ ] 기본 파일 읽기/쓰기 방법 이해
- [ ] 다양한 파일 모드 (r, w, a, x) 활용
- [ ] with 문을 사용한 안전한 파일 처리
- [ ] 텍스트 파일과 바이너리 파일 처리
- [ ] CSV, JSON 파일 처리 방법
- [ ] 파일 경로 처리 (pathlib 모듈)
- [ ] 실무에서 자주 사용되는 파일 처리 패턴

## 📚 핵심 개념

### 1. 기본 파일 처리
```python
# 파일 쓰기
with open("file.txt", "w") as file:
    file.write("Hello, World!")

# 파일 읽기
with open("file.txt", "r") as file:
    content = file.read()
```

### 2. 파일 모드들
```python
# 읽기 모드
with open("file.txt", "r") as file:
    content = file.read()

# 쓰기 모드
with open("file.txt", "w") as file:
    file.write("New content")

# 추가 모드
with open("file.txt", "a") as file:
    file.write("Appended content")
```

### 3. CSV 파일 처리
```python
import csv

# CSV 읽기
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# CSV 쓰기
with open("output.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
```

### 4. JSON 파일 처리
```python
import json

# JSON 읽기
with open("data.json", "r") as file:
    data = json.load(file)

# JSON 쓰기
with open("output.json", "w") as file:
    json.dump(data, file, indent=2)
```

## 📁 예제 파일

- `basic_file_operations.py` - 기본 파일 입출력
- `file_modes.py` - 다양한 파일 모드
- `csv_processing.py` - CSV 파일 처리
- `json_processing.py` - JSON 파일 처리
- `pathlib_usage.py` - pathlib 모듈 활용
- `practical_examples.py` - 실무에서 자주 사용되는 패턴

## 🏃‍♂️ 실습 과제

1. **로그 파일 분석기**: 로그 파일을 읽고 분석하는 프로그램
2. **데이터 변환기**: CSV를 JSON으로 변환하는 프로그램
3. **백업 도구**: 파일을 백업하는 간단한 도구
4. **설정 파일 관리자**: 설정 파일을 읽고 쓰는 프로그램

## 💡 실무 팁

### ✅ 좋은 예시
```python
# with 문 사용
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()

# pathlib 사용
from pathlib import Path
file_path = Path("data") / "file.txt"
if file_path.exists():
    content = file_path.read_text()
```

### ❌ 피해야 할 예시
```python
# 파일을 닫지 않음
file = open("file.txt", "r")
content = file.read()
# file.close() 누락

# 인코딩 지정 없이 파일 읽기
with open("file.txt", "r") as file:  # 인코딩 문제 가능
    content = file.read()
```

## 🔗 관련 주제

- [문자열 처리](../../05-data-structures/string-processing/) - 파일 내용 처리
- [예외 처리](../../02-control-flow/exception-handling/) - 파일 처리 중 오류 처리
- [정규표현식](../../06-advanced/regex/) - 파일 내용 패턴 매칭

## 📖 추가 학습 자료

- [Python 공식 문서 - 파일 입출력](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python 공식 문서 - pathlib](https://docs.python.org/3/library/pathlib.html)

---

**다음 단계**: [정규표현식](../../06-advanced/regex/) 학습하기
