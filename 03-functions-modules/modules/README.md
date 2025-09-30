# 모듈과 패키지 📦

> 코드를 재사용 가능한 모듈과 패키지로 구성하여 체계적인 프로그램을 만드는 방법을 학습합니다.

## 🎯 학습 목표

- [ ] 모듈의 개념과 import 문 사용법 이해
- [ ] 다양한 import 방식 (import, from import, as) 학습
- [ ] 패키지의 구조와 __init__.py 파일 이해
- [ ] 내장 모듈과 표준 라이브러리 활용
- [ ] 모듈 검색 경로와 sys.path 이해
- [ ] 모듈의 __name__과 __main__ 사용법
- [ ] 패키지 설치와 관리 (pip) 기초

## 📚 핵심 개념

### 1. 모듈 import
```python
# 전체 모듈 import
import math
result = math.sqrt(16)

# 특정 함수만 import
from math import sqrt, pi
result = sqrt(16)

# 별칭 사용
import numpy as np
import pandas as pd
```

### 2. 모듈 생성
```python
# my_module.py
def greet(name):
    return f"안녕하세요, {name}님!"

PI = 3.14159

if __name__ == "__main__":
    print("모듈이 직접 실행되었습니다.")
```

### 3. 패키지 구조
```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

### 4. __init__.py 파일
```python
# __init__.py
from .module1 import function1
from .module2 import function2

__version__ = "1.0.0"
__all__ = ["function1", "function2"]
```

## 📁 예제 파일

- `basic_imports.py` - 기본 import 사용법
- `module_creation.py` - 모듈 생성 예제
- `package_structure.py` - 패키지 구조 예제
- `builtin_modules.py` - 내장 모듈 사용법
- `module_attributes.py` - 모듈 속성과 메타데이터
- `import_paths.py` - import 경로 관리
- `practical_examples.py` - 실무에서 자주 사용되는 모듈 패턴

## 🏃‍♂️ 실습 과제

1. **유틸리티 모듈**: 자주 사용되는 함수들을 모듈로 만들기
2. **데이터 처리 패키지**: 데이터를 처리하는 여러 모듈로 구성된 패키지
3. **설정 관리 모듈**: 애플리케이션 설정을 관리하는 모듈
4. **로깅 모듈**: 로그를 관리하는 모듈

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 명확한 import
from datetime import datetime, timedelta
from pathlib import Path

# 모듈별로 그룹화
import os
import sys
from typing import List, Dict

# 로컬 모듈
from .utils import helper_function
from .models import User
```

### ❌ 피해야 할 예시
```python
# 너무 많은 import
from module import *

# 모호한 import
import module1, module2, module3

# 순환 import
# module1.py에서 module2 import
# module2.py에서 module1 import
```

## 🔗 관련 주제

- [함수 정의와 호출](../../03-functions-modules/functions/) - 모듈에 포함될 함수들
- [클래스와 객체](../../04-oop/classes-and-objects/) - 모듈에 포함될 클래스들
- [내장 함수와 라이브러리](../../03-functions-modules/built-in-functions/) - 표준 라이브러리 활용

## 📖 추가 학습 자료

- [Python 공식 문서 - 모듈](https://docs.python.org/3/tutorial/modules.html)
- [Python 공식 문서 - 패키지](https://docs.python.org/3/tutorial/modules.html#packages)
- [PEP 8 - import 순서](https://pep8.org/#imports)

---

**다음 단계**: [내장 함수와 라이브러리](../../03-functions-modules/built-in-functions/) 학습하기
