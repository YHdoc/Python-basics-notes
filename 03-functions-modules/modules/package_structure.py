# 패키지 구조 예제

# 이 파일은 패키지 구조를 보여주는 예제입니다.

def demonstrate_package_structure():
    """패키지 구조를 설명하는 함수"""
    print("=== 패키지 구조 예제 ===")
    print("""
    my_package/
        __init__.py          # 패키지 초기화 파일
        module1.py           # 모듈 1
        module2.py           # 모듈 2
        subpackage/          # 하위 패키지
            __init__.py      # 하위 패키지 초기화 파일
            module3.py       # 하위 패키지 모듈
    """)

def show_import_examples():
    """import 예제를 보여주는 함수"""
    print("\n=== import 예제 ===")
    print("""
    # 패키지에서 모듈 import
    from my_package import module1
    from my_package.module2 import function2
    
    # 하위 패키지에서 import
    from my_package.subpackage import module3
    from my_package.subpackage.module3 import function3
    """)

if __name__ == "__main__":
    demonstrate_package_structure()
    show_import_examples()
