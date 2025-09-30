# 표준 프로젝트 구조

"""
표준 Python 프로젝트 구조 예제

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
"""

def demonstrate_project_structure():
    """프로젝트 구조를 보여주는 함수"""
    print("=== 표준 Python 프로젝트 구조 ===")
    print("""
    my_project/
    ├── README.md              # 프로젝트 설명
    ├── requirements.txt       # 의존성 목록
    ├── setup.py              # 패키지 설정
    ├── my_project/           # 메인 패키지
    │   ├── __init__.py       # 패키지 초기화
    │   ├── main.py           # 메인 모듈
    │   ├── utils/            # 유틸리티 패키지
    │   │   ├── __init__.py
    │   │   └── helpers.py
    │   └── models/           # 모델 패키지
    │       ├── __init__.py
    │       └── user.py
    ├── tests/                # 테스트 패키지
    │   ├── __init__.py
    │   └── test_main.py
    └── docs/                 # 문서
        └── api.md
    """)

if __name__ == "__main__":
    demonstrate_project_structure()
