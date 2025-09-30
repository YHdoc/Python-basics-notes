# range() 함수 활용

def basic_range():
    """기본 range() 함수 사용법"""
    print("=== 기본 range() 함수 ===")
    
    # range(stop)
    print("range(5):")
    for i in range(5):
        print(f"  {i}")
    
    # range(start, stop)
    print("\nrange(2, 8):")
    for i in range(2, 8):
        print(f"  {i}")
    
    # range(start, stop, step)
    print("\nrange(0, 10, 2):")
    for i in range(0, 10, 2):
        print(f"  {i}")
    
    # 역순 range
    print("\nrange(10, 0, -1):")
    for i in range(10, 0, -1):
        print(f"  {i}")

def range_with_list():
    """range()와 리스트 생성"""
    print("\n=== range()로 리스트 생성 ===")
    
    # range를 리스트로 변환
    numbers = list(range(10))
    print(f"list(range(10)): {numbers}")
    
    # 짝수 리스트
    even_numbers = list(range(0, 20, 2))
    print(f"짝수 리스트: {even_numbers}")
    
    # 홀수 리스트
    odd_numbers = list(range(1, 20, 2))
    print(f"홀수 리스트: {odd_numbers}")
    
    # 역순 리스트
    reverse_numbers = list(range(10, 0, -1))
    print(f"역순 리스트: {reverse_numbers}")

def range_with_indexing():
    """range()를 인덱싱에 사용"""
    print("\n=== range()를 인덱싱에 사용 ===")
    
    fruits = ["apple", "banana", "orange", "grape", "kiwi"]
    print(f"과일 목록: {fruits}")
    
    # 인덱스와 함께 출력
    print("인덱스와 함께:")
    for i in range(len(fruits)):
        print(f"  {i}: {fruits[i]}")
    
    # 특정 범위의 요소만 출력
    print("\n인덱스 1부터 3까지:")
    for i in range(1, 4):
        print(f"  {i}: {fruits[i]}")

def range_with_conditions():
    """range()와 조건문 조합"""
    print("\n=== range()와 조건문 조합 ===")
    
    # 1부터 20까지의 수 중에서 3의 배수만 출력
    print("3의 배수:")
    for i in range(1, 21):
        if i % 3 == 0:
            print(f"  {i}")
    
    # 1부터 20까지의 수 중에서 소수 찾기 (간단한 버전)
    print("\n소수:")
    for num in range(2, 21):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"  {num}")

def range_with_math():
    """range()와 수학 연산"""
    print("\n=== range()와 수학 연산 ===")
    
    # 제곱수 계산
    print("제곱수:")
    for i in range(1, 11):
        square = i ** 2
        print(f"  {i}² = {square}")
    
    # 팩토리얼 계산
    print("\n팩토리얼:")
    for n in range(1, 6):
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"  {n}! = {factorial}")
    
    # 피보나치 수열
    print("\n피보나치 수열:")
    a, b = 0, 1
    for i in range(10):
        print(f"  F({i}) = {a}")
        a, b = b, a + b

def range_with_nested():
    """중첩된 range() 사용"""
    print("\n=== 중첩된 range() 사용 ===")
    
    # 구구단 표
    print("구구단 (2단~5단):")
    for i in range(2, 6):
        print(f"\n{i}단:")
        for j in range(1, 10):
            result = i * j
            print(f"  {i} × {j} = {result}")
    
    # 별 찍기 (삼각형)
    print("\n별 찍기 (삼각형):")
    for i in range(1, 6):
        for j in range(i):
            print("*", end="")
        print()  # 줄바꿈

def range_with_advanced():
    """고급 range() 사용법"""
    print("\n=== 고급 range() 사용법 ===")
    
    # range 객체의 속성
    r = range(5, 15, 2)
    print(f"range(5, 15, 2):")
    print(f"  시작: {r.start}")
    print(f"  끝: {r.stop}")
    print(f"  간격: {r.step}")
    print(f"  길이: {len(r)}")
    print(f"  요소들: {list(r)}")
    
    # range 슬라이싱
    r = range(20)
    print(f"\nrange(20) 슬라이싱:")
    print(f"  처음 5개: {list(r[:5])}")
    print(f"  마지막 5개: {list(r[-5:])}")
    print(f"  중간 5개: {list(r[5:10])}")
    
    # range 포함 여부 확인
    r = range(10, 20, 2)
    print(f"\nrange(10, 20, 2) 포함 여부:")
    print(f"  12 in range: {12 in r}")
    print(f"  13 in range: {13 in r}")
    print(f"  18 in range: {18 in r}")

def practical_range_examples():
    """실무에서 자주 사용되는 range() 예제"""
    print("\n=== 실무 range() 예제 ===")
    
    # 데이터 처리 (배치 처리)
    data = list(range(1, 101))  # 1부터 100까지의 데이터
    batch_size = 10
    
    print(f"총 {len(data)}개의 데이터를 {batch_size}개씩 처리:")
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        print(f"  배치 {i//batch_size + 1}: {batch}")
    
    # 시간 시뮬레이션
    print("\n시간 시뮬레이션 (24시간):")
    for hour in range(24):
        if 6 <= hour < 12:
            period = "오전"
        elif 12 <= hour < 18:
            period = "오후"
        elif 18 <= hour < 22:
            period = "저녁"
        else:
            period = "밤"
        
        print(f"  {hour:02d}:00 - {period}")
    
    # 점수 등급 분류
    print("\n점수 등급 분류:")
    scores = [85, 92, 78, 96, 88, 91, 75, 83, 90, 87]
    
    grade_ranges = [
        (90, 100, "A"),
        (80, 89, "B"),
        (70, 79, "C"),
        (60, 69, "D"),
        (0, 59, "F")
    ]
    
    for score in scores:
        for min_score, max_score, grade in grade_ranges:
            if min_score <= score <= max_score:
                print(f"  {score}점: {grade}등급")
                break

if __name__ == "__main__":
    basic_range()
    range_with_list()
    range_with_indexing()
    range_with_conditions()
    range_with_math()
    range_with_nested()
    range_with_advanced()
    practical_range_examples()
