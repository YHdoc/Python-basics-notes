# 프로젝트 구조 📁

> Python 프로젝트를 체계적으로 구성하고 관리하는 방법을 학습합니다.

## 🎯 학습 목표

- [ ] Python 프로젝트의 표준 구조 이해
- [ ] 패키지와 모듈의 적절한 구성
- [ ] 설정 파일 관리 방법
- [ ] 의존성 관리 (requirements.txt, pipenv)
- [ ] 가상환경 설정과 관리
- [ ] 프로젝트 문서화 방법
- [ ] 실무에서 자주 사용되는 프로젝트 구조

## 📚 핵심 개념

### 1. 표준 프로젝트 구조
```
my_project/
├── README.md
├── requirements.txt
├── setup.py
├── my_project/
│   ├── __init__.py
│   ├── main.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── models/
│       ├── __init__.py
│       └── user.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
└── docs/
    └── api.md
```

### 2. requirements.txt
```
requests==2.28.1
numpy>=1.21.0
pandas<2.0.0
```

### 3. setup.py
```python
from setuptools import setup, find_packages

setup(
    name="my_project",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "numpy>=1.21.0",
    ],
)
```

### 4. 가상환경 설정
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt
```

## 📁 예제 파일

- `standard_structure.py` - 표준 프로젝트 구조
- `package_organization.py` - 패키지 구성
- `dependency_management.py` - 의존성 관리
- `virtual_environment.py` - 가상환경 설정
- `documentation.py` - 프로젝트 문서화
- `practical_examples.py` - 실무에서 자주 사용되는 프로젝트 구조

## 🏃‍♂️ 실습 과제

1. **새 프로젝트 생성**: 표준 구조로 새 프로젝트 생성
2. **패키지 구성**: 모듈을 적절한 패키지로 구성
3. **의존성 관리**: requirements.txt 작성 및 관리
4. **문서화**: README.md와 API 문서 작성

## 💡 실무 팁

### ✅ 좋은 예시
```python
# __init__.py에서 적절한 import
from .main import main_function
from .utils.helpers import helper_function

__version__ = "1.0.0"
__all__ = ["main_function", "helper_function"]
```

### ❌ 피해야 할 예시
```python
# 잘못된 프로젝트 구조
project/
├── file1.py
├── file2.py
├── file3.py
└── utils.py  # 모든 유틸리티가 하나의 파일에

# requirements.txt 없이 프로젝트 관리
# 의존성 추적 불가능
```

## 🔗 관련 주제

- [모듈과 패키지](../../03-functions-modules/modules/) - 프로젝트 구조의 기초
- [코딩 스타일](../../08-best-practices/coding-style/) - 일관성 있는 코드 작성
- [테스트와 디버깅](../../08-best-practices/testing-debugging/) - 프로젝트 테스트 구조

## 📖 추가 학습 자료

- [Python 공식 문서 - 패키지](https://docs.python.org/3/tutorial/modules.html#packages)
- [Python 프로젝트 구조 가이드](https://docs.python-guide.org/writing/structure/)

---

**완료**: Python 기초 학습 과정 완료! 🎉
