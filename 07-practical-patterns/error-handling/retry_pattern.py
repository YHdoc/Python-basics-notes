"""
재시도 패턴
실패할 수 있는 작업을 자동으로 재시도하는 패턴을 학습합니다.
"""

import time
import random
from functools import wraps
from typing import Callable, Any, Optional


def simple_retry(max_attempts: int = 3, delay: float = 1.0):
    """
    간단한 재시도 데코레이터
    
    Args:
        max_attempts (int): 최대 시도 횟수
        delay (float): 재시도 간격 (초)
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"시도 {attempt + 1} 실패: {e}. {delay}초 후 재시도...")
                        time.sleep(delay)
                    else:
                        print(f"최종 실패: {max_attempts}번 시도 후 포기")
            
            raise last_exception
        return wrapper
    return decorator


def exponential_backoff_retry(max_attempts: int = 3, base_delay: float = 1.0):
    """
    지수 백오프 재시도 데코레이터
    
    Args:
        max_attempts (int): 최대 시도 횟수
        base_delay (float): 기본 지연 시간
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        delay = base_delay * (2 ** attempt)  # 지수적으로 증가
                        print(f"시도 {attempt + 1} 실패: {e}. {delay}초 후 재시도...")
                        time.sleep(delay)
                    else:
                        print(f"최종 실패: {max_attempts}번 시도 후 포기")
            
            raise last_exception
        return wrapper
    return decorator


class RetryableOperation:
    """재시도 가능한 작업을 관리하는 클래스"""
    
    def __init__(self, max_attempts: int = 3, delay: float = 1.0):
        self.max_attempts = max_attempts
        self.delay = delay
    
    def execute(self, func: Callable, *args, **kwargs) -> Any:
        """함수를 재시도 로직과 함께 실행"""
        last_exception = None
        
        for attempt in range(self.max_attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                if attempt < self.max_attempts - 1:
                    print(f"시도 {attempt + 1} 실패: {e}. {self.delay}초 후 재시도...")
                    time.sleep(self.delay)
                else:
                    print(f"최종 실패: {self.max_attempts}번 시도 후 포기")
        
        raise last_exception


# TODO: 실패할 수 있는 함수들 (테스트용)
def unreliable_function():
    """50% 확률로 실패하는 함수"""
    if random.random() < 0.5:
        raise ConnectionError("네트워크 연결 실패")
    return "성공!"

def api_call_simulation():
    """API 호출 시뮬레이션"""
    if random.random() < 0.7:
        raise TimeoutError("API 타임아웃")
    return {"status": "success", "data": "API 응답"}

def file_operation():
    """파일 작업 시뮬레이션"""
    if random.random() < 0.3:
        raise FileNotFoundError("파일을 찾을 수 없습니다")
    return "파일 처리 완료"

# TODO: 데코레이터 사용 예제
@simple_retry(max_attempts=3, delay=1.0)
def decorated_function():
    """데코레이터가 적용된 함수"""
    return unreliable_function()

@exponential_backoff_retry(max_attempts=4, base_delay=0.5)
def api_with_backoff():
    """지수 백오프가 적용된 API 호출"""
    return api_call_simulation()

# TODO: 클래스 사용 예제
def test_retry_patterns():
    """재시도 패턴 테스트"""
    print("=== 재시도 패턴 테스트 ===")
    
    # 1. 데코레이터 사용
    print("\n1. 데코레이터 사용:")
    try:
        result = decorated_function()
        print(f"결과: {result}")
    except Exception as e:
        print(f"최종 실패: {e}")
    
    # 2. 지수 백오프 데코레이터
    print("\n2. 지수 백오프 데코레이터:")
    try:
        result = api_with_backoff()
        print(f"결과: {result}")
    except Exception as e:
        print(f"최종 실패: {e}")
    
    # 3. 클래스 사용
    print("\n3. 클래스 사용:")
    retry_op = RetryableOperation(max_attempts=3, delay=1.0)
    try:
        result = retry_op.execute(file_operation)
        print(f"결과: {result}")
    except Exception as e:
        print(f"최종 실패: {e}")

# TODO: 실무 예제 - API 호출
def make_api_request(url: str, timeout: int = 5) -> dict:
    """API 요청 함수 (실제로는 requests 라이브러리 사용)"""
    # 시뮬레이션: 30% 확률로 실패
    if random.random() < 0.3:
        raise ConnectionError(f"API 요청 실패: {url}")
    
    return {"url": url, "status": 200, "data": "응답 데이터"}

@simple_retry(max_attempts=3, delay=2.0)
def reliable_api_call(url: str) -> dict:
    """재시도 로직이 포함된 안정적인 API 호출"""
    return make_api_request(url)

# TODO: 실무 예제 - 파일 처리
def process_large_file(filename: str) -> str:
    """대용량 파일 처리 (시뮬레이션)"""
    if random.random() < 0.4:
        raise MemoryError("메모리 부족")
    
    return f"파일 {filename} 처리 완료"

@exponential_backoff_retry(max_attempts=5, base_delay=1.0)
def robust_file_processing(filename: str) -> str:
    """견고한 파일 처리"""
    return process_large_file(filename)

if __name__ == "__main__":
    print("재시도 패턴 예제를 실행합니다.")
    
    # TODO: 테스트 실행
    # test_retry_patterns()
    
    # TODO: 실무 예제 테스트
    # print("\n=== 실무 예제 테스트 ===")
    # 
    # # API 호출 테스트
    # try:
    #     result = reliable_api_call("https://api.example.com/data")
    #     print(f"API 호출 성공: {result}")
    # except Exception as e:
    #     print(f"API 호출 최종 실패: {e}")
    # 
    # # 파일 처리 테스트
    # try:
    #     result = robust_file_processing("large_data.csv")
    #     print(f"파일 처리 성공: {result}")
    # except Exception as e:
    #     print(f"파일 처리 최종 실패: {e}")
    
    print("TODO 부분을 완성한 후 실행해보세요!")
