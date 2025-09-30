# import 경로 관리

import sys
import os

def show_import_paths():
    """import 경로들을 보여주는 함수"""
    print("=== Python 모듈 검색 경로 ===")
    for i, path in enumerate(sys.path):
        print(f"{i+1}. {path}")

def add_custom_path():
    """사용자 정의 경로를 추가하는 함수"""
    print("\n=== 사용자 정의 경로 추가 ===")
    
    # 현재 디렉토리의 상위 디렉토리 추가
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.append(parent_dir)
        print(f"경로 추가됨: {parent_dir}")
    else:
        print(f"경로가 이미 존재함: {parent_dir}")

def demonstrate_relative_imports():
    """상대 import 예제를 보여주는 함수"""
    print("\n=== 상대 import 예제 ===")
    print("""
    # 같은 패키지 내에서
    from .module1 import function1
    from ..parent_package import function2
    
    # 주의: 상대 import는 패키지 내에서만 사용 가능
    """)

if __name__ == "__main__":
    show_import_paths()
    add_custom_path()
    demonstrate_relative_imports()
