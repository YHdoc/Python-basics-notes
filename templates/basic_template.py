"""
기본 Python 파일 템플릿
새로운 Python 파일을 만들 때 사용할 수 있는 기본 구조입니다.
"""

# 표준 라이브러리 import
import os
import sys
from datetime import datetime

# 서드파티 라이브러리 import (필요시)
# import requests
# import pandas as pd

# 로컬 모듈 import (필요시)
# from utils.helpers import some_function


def main():
    """메인 함수"""
    print("프로그램을 시작합니다.")
    
    # TODO: 여기에 메인 로직을 작성하세요
    
    print("프로그램을 종료합니다.")


def helper_function(param1, param2=None):
    """
    도우미 함수
    
    Args:
        param1 (str): 첫 번째 매개변수
        param2 (int, optional): 두 번째 매개변수. Defaults to None.
    
    Returns:
        str: 처리된 결과
    """
    # TODO: 함수 로직을 구현하세요
    result = f"처리된 결과: {param1}"
    return result


class ExampleClass:
    """예제 클래스"""
    
    def __init__(self, name):
        """생성자"""
        self.name = name
        self.created_at = datetime.now()
    
    def get_info(self):
        """정보 반환"""
        return f"이름: {self.name}, 생성시간: {self.created_at}"
    
    def process_data(self, data):
        """데이터 처리"""
        # TODO: 데이터 처리 로직을 구현하세요
        return f"처리된 데이터: {data}"


if __name__ == "__main__":
    # 스크립트가 직접 실행될 때만 main() 함수 호출
    main()
