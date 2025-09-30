# 프로파일링 도구

import time
import cProfile
import pstats

def slow_function():
    """느린 함수 예제"""
    total = 0
    for i in range(1000000):
        total += i
    return total

def profile_function():
    """함수 프로파일링 예제"""
    print("=== 함수 프로파일링 ===")
    
    # cProfile 사용
    cProfile.run('slow_function()')
    
    # 시간 측정
    start_time = time.time()
    result = slow_function()
    end_time = time.time()
    
    print(f"결과: {result}")
    print(f"실행 시간: {end_time - start_time:.4f}초")

if __name__ == "__main__":
    profile_function()
