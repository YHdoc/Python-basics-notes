# 기본 import 사용법

# 표준 라이브러리 import
import math
import random
import datetime

# 특정 함수만 import
from math import sqrt, pi, sin, cos
from random import randint, choice
from datetime import date, time, datetime

# 별칭 사용
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 로컬 모듈 import (예시)
# from my_module import my_function
# from my_package import my_module

if __name__ == "__main__":
    print("=== 기본 import 사용법 ===")
    
    # math 모듈 사용
    print(f"√16 = {math.sqrt(16)}")
    print(f"π = {math.pi}")
    print(f"sin(π/2) = {math.sin(math.pi/2)}")
    
    # 직접 import한 함수 사용
    print(f"√25 = {sqrt(25)}")
    print(f"π = {pi}")
    
    # random 모듈 사용
    print(f"랜덤 정수: {random.randint(1, 10)}")
    print(f"랜덤 선택: {random.choice(['사과', '바나나', '오렌지'])}")
    
    # datetime 모듈 사용
    now = datetime.datetime.now()
    print(f"현재 시간: {now}")
    
    today = date.today()
    print(f"오늘 날짜: {today}")
    
    # 별칭 사용 예시 (실제로는 설치된 라이브러리 필요)
    # arr = np.array([1, 2, 3, 4, 5])
    # print(f"NumPy 배열: {arr}")
    
    print("\n=== import 순서 예제 ===")
    print("1. 표준 라이브러리")
    print("2. 서드파티 라이브러리")
    print("3. 로컬 모듈")
    print("4. 각 그룹 내에서는 알파벳 순")
