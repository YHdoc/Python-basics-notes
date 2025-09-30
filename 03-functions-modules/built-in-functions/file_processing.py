# 파일 처리 관련 모듈들

import json
import csv
import os
from pathlib import Path

def demonstrate_file_processing():
    """파일 처리 관련 모듈들을 보여주는 함수"""
    print("=== 파일 처리 관련 모듈들 ===")
    
    # pathlib 사용
    current_file = Path(__file__)
    print(f"현재 파일: {current_file}")
    print(f"파일명: {current_file.name}")
    print(f"확장자: {current_file.suffix}")
    print(f"부모 디렉토리: {current_file.parent}")
    
    # 파일 존재 여부 확인
    print(f"파일 존재: {current_file.exists()}")
    print(f"파일 크기: {current_file.stat().st_size} bytes")

if __name__ == "__main__":
    demonstrate_file_processing()
