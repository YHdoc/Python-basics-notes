# 내장 모듈 사용법

import os
import sys
import math
import random
import datetime
import json
import csv

def demonstrate_builtin_modules():
    """내장 모듈 사용 예제"""
    print("=== 내장 모듈 사용 예제 ===")
    
    # os 모듈
    print(f"현재 작업 디렉토리: {os.getcwd()}")
    print(f"환경 변수 PATH: {os.environ.get('PATH', 'N/A')[:50]}...")
    
    # sys 모듈
    print(f"Python 버전: {sys.version}")
    print(f"실행 파일 경로: {sys.executable}")
    
    # math 모듈
    print(f"π = {math.pi}")
    print(f"√16 = {math.sqrt(16)}")
    print(f"sin(π/2) = {math.sin(math.pi/2)}")
    
    # random 모듈
    print(f"랜덤 정수 (1-10): {random.randint(1, 10)}")
    print(f"랜덤 실수 (0-1): {random.random():.3f}")
    
    # datetime 모듈
    now = datetime.datetime.now()
    print(f"현재 시간: {now}")
    print(f"오늘 날짜: {now.date()}")
    
    # json 모듈
    data = {"name": "김철수", "age": 30, "city": "서울"}
    json_str = json.dumps(data, ensure_ascii=False)
    print(f"JSON 문자열: {json_str}")
    
    # csv 모듈 (예제)
    print("CSV 모듈은 파일 처리를 위해 사용됩니다.")

if __name__ == "__main__":
    demonstrate_builtin_modules()
