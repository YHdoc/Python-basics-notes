# 표준 라이브러리 활용

import os
import sys
import math
import random
import datetime
import json
import csv
import urllib.request
import urllib.parse

def demonstrate_os_module():
    """os 모듈 사용 예제"""
    print("=== os 모듈 ===")
    
    # 현재 작업 디렉토리
    print(f"현재 작업 디렉토리: {os.getcwd()}")
    
    # 환경 변수
    print(f"HOME 환경 변수: {os.environ.get('HOME', 'N/A')}")
    print(f"PATH 환경 변수 (처음 50자): {os.environ.get('PATH', 'N/A')[:50]}...")
    
    # 파일/디렉토리 정보
    current_file = __file__
    print(f"현재 파일: {current_file}")
    print(f"파일 존재 여부: {os.path.exists(current_file)}")
    print(f"파일 크기: {os.path.getsize(current_file)} bytes")
    print(f"파일 확장자: {os.path.splitext(current_file)[1]}")

def demonstrate_sys_module():
    """sys 모듈 사용 예제"""
    print("\n=== sys 모듈 ===")
    
    # Python 버전 정보
    print(f"Python 버전: {sys.version}")
    print(f"Python 버전 정보: {sys.version_info}")
    
    # 실행 파일 경로
    print(f"Python 실행 파일: {sys.executable}")
    
    # 명령행 인수
    print(f"명령행 인수: {sys.argv}")
    
    # 모듈 검색 경로
    print(f"모듈 검색 경로 (처음 3개): {sys.path[:3]}")

def demonstrate_math_module():
    """math 모듈 사용 예제"""
    print("\n=== math 모듈 ===")
    
    # 상수
    print(f"π = {math.pi}")
    print(f"e = {math.e}")
    
    # 기본 함수들
    print(f"√16 = {math.sqrt(16)}")
    print(f"2^3 = {math.pow(2, 3)}")
    print(f"log(10) = {math.log(10)}")
    print(f"sin(π/2) = {math.sin(math.pi/2)}")
    print(f"cos(0) = {math.cos(0)}")
    
    # 반올림 함수들
    print(f"ceil(3.2) = {math.ceil(3.2)}")
    print(f"floor(3.8) = {math.floor(3.8)}")
    print(f"trunc(3.8) = {math.trunc(3.8)}")

def demonstrate_random_module():
    """random 모듈 사용 예제"""
    print("\n=== random 모듈 ===")
    
    # 랜덤 정수
    print(f"랜덤 정수 (1-10): {random.randint(1, 10)}")
    print(f"랜덤 정수 (1-10): {random.randint(1, 10)}")
    
    # 랜덤 실수
    print(f"랜덤 실수 (0-1): {random.random():.3f}")
    print(f"랜덤 실수 (0-1): {random.random():.3f}")
    
    # 리스트에서 랜덤 선택
    fruits = ["apple", "banana", "orange", "grape"]
    print(f"랜덤 과일: {random.choice(fruits)}")
    print(f"랜덤 과일 3개: {random.choices(fruits, k=3)}")
    
    # 리스트 섞기
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print(f"섞인 리스트: {numbers}")

def demonstrate_datetime_module():
    """datetime 모듈 사용 예제"""
    print("\n=== datetime 모듈 ===")
    
    # 현재 시간
    now = datetime.datetime.now()
    print(f"현재 시간: {now}")
    print(f"년: {now.year}")
    print(f"월: {now.month}")
    print(f"일: {now.day}")
    print(f"시간: {now.hour}")
    print(f"분: {now.minute}")
    print(f"초: {now.second}")
    
    # 날짜만
    today = datetime.date.today()
    print(f"오늘 날짜: {today}")
    
    # 시간만
    current_time = datetime.time(14, 30, 45)
    print(f"현재 시간: {current_time}")
    
    # 날짜 계산
    tomorrow = today + datetime.timedelta(days=1)
    print(f"내일: {tomorrow}")
    
    # 날짜 포맷팅
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"포맷된 시간: {formatted}")

def demonstrate_json_module():
    """json 모듈 사용 예제"""
    print("\n=== json 모듈 ===")
    
    # Python 객체를 JSON으로 변환
    data = {
        "name": "김철수",
        "age": 30,
        "city": "서울",
        "hobbies": ["독서", "영화감상", "프로그래밍"]
    }
    
    json_string = json.dumps(data, ensure_ascii=False, indent=2)
    print(f"JSON 문자열:\n{json_string}")
    
    # JSON을 Python 객체로 변환
    parsed_data = json.loads(json_string)
    print(f"파싱된 데이터: {parsed_data}")
    print(f"이름: {parsed_data['name']}")

def demonstrate_csv_module():
    """csv 모듈 사용 예제"""
    print("\n=== csv 모듈 ===")
    
    # CSV 데이터 생성
    data = [
        ["이름", "나이", "도시"],
        ["김철수", "30", "서울"],
        ["이영희", "25", "부산"],
        ["박민수", "35", "대구"]
    ]
    
    # CSV 문자열로 변환
    import io
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(data)
    csv_string = output.getvalue()
    print(f"CSV 문자열:\n{csv_string}")
    
    # CSV 문자열 파싱
    reader = csv.reader(io.StringIO(csv_string))
    parsed_data = list(reader)
    print(f"파싱된 CSV 데이터: {parsed_data}")

if __name__ == "__main__":
    demonstrate_os_module()
    demonstrate_sys_module()
    demonstrate_math_module()
    demonstrate_random_module()
    demonstrate_datetime_module()
    demonstrate_json_module()
    demonstrate_csv_module()
