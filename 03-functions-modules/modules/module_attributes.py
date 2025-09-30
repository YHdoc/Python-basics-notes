# 모듈 속성과 메타데이터

# 모듈 레벨 변수들
__version__ = "1.0.0"
__author__ = "Python 학습자"
__email__ = "learner@example.com"

# 모듈 설명
__doc__ = """
이 모듈은 모듈 속성과 메타데이터를 보여주는 예제입니다.
"""

# 공개할 함수들 정의
__all__ = ["get_module_info", "show_attributes"]

def get_module_info():
    """모듈 정보를 반환하는 함수"""
    return {
        "name": __name__,
        "version": __version__,
        "author": __author__,
        "email": __email__,
        "doc": __doc__
    }

def show_attributes():
    """모듈 속성들을 보여주는 함수"""
    print("=== 모듈 속성들 ===")
    print(f"__name__: {__name__}")
    print(f"__version__: {__version__}")
    print(f"__author__: {__author__}")
    print(f"__email__: {__email__}")
    print(f"__doc__: {__doc__}")
    print(f"__all__: {__all__}")

if __name__ == "__main__":
    show_attributes()
    print(f"\n모듈 정보: {get_module_info()}")
