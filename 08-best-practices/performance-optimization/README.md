# 성능 최적화 ⚡

> Python 코드의 성능을 최적화하고 효율적인 프로그램을 작성하는 방법을 학습합니다.

## 🎯 학습 목표

- [ ] Python 성능 특성 이해
- [ ] 프로파일링 도구 활용
- [ ] 알고리즘 복잡도 분석
- [ ] 메모리 사용량 최적화
- [ ] I/O 성능 최적화
- [ ] 캐싱과 메모이제이션 활용
- [ ] 실무에서 자주 사용되는 최적화 기법

## 📚 핵심 개념

### 1. 프로파일링
```python
import cProfile
import pstats

def slow_function():
    # 느린 함수
    pass

# 프로파일링 실행
cProfile.run('slow_function()')
```

### 2. 메모이제이션
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 3. 리스트 컴프리헨션
```python
# 비효율적
result = []
for i in range(1000):
    if i % 2 == 0:
        result.append(i**2)

# 효율적
result = [i**2 for i in range(1000) if i % 2 == 0]
```

### 4. 제너레이터 활용
```python
def read_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()
```

## 📁 예제 파일

- `profiling_tools.py` - 프로파일링 도구
- `algorithm_complexity.py` - 알고리즘 복잡도
- `memory_optimization.py` - 메모리 최적화
- `io_optimization.py` - I/O 최적화
- `caching_memoization.py` - 캐싱과 메모이제이션
- `practical_examples.py` - 실무에서 자주 사용되는 최적화 기법

## 🏃‍♂️ 실습 과제

1. **성능 측정기**: 함수의 실행 시간을 측정하는 도구
2. **메모리 사용량 분석기**: 메모리 사용량을 분석하는 도구
3. **캐싱 시스템**: 결과를 캐싱하는 시스템
4. **배치 처리기**: 대용량 데이터를 배치로 처리하는 시스템

## 💡 실무 팁

### ✅ 좋은 예시
```python
# 효율적인 데이터 처리
def process_data_efficiently(data):
    # 제너레이터 사용
    filtered = (item for item in data if item > 0)
    processed = (item * 2 for item in filtered)
    return list(processed)

# 메모이제이션 활용
@lru_cache(maxsize=1000)
def expensive_calculation(n):
    # 비용이 큰 계산
    return sum(i**2 for i in range(n))
```

### ❌ 피해야 할 예시
```python
# 비효율적인 반복문
result = []
for i in range(len(data)):
    if data[i] > 0:
        result.append(data[i] * 2)

# 불필요한 객체 생성
def bad_function():
    return [i**2 for i in range(1000000)]  # 메모리 낭비
```

## 🔗 관련 주제

- [제너레이터](../06-advanced/generators/) - 메모리 효율적인 데이터 처리
- [리스트 컴프리헨션](../05-data-structures/lists-tuples/) - 효율적인 리스트 생성
- [데코레이터](../06-advanced/decorators/) - 성능 측정 데코레이터

## 📖 추가 학습 자료

- [Python 공식 문서 - 성능 최적화](https://docs.python.org/3/library/profile.html)
- [Python 성능 최적화 가이드](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)

---

**다음 단계**: [테스트와 디버깅](./testing-debugging/) 학습하기
