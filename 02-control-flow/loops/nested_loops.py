# 중첩된 반복문

def basic_nested_loops():
    """기본 중첩 반복문"""
    print("=== 기본 중첩 반복문 ===")
    
    # 2차원 배열 시뮬레이션
    print("2차원 배열 (3x3):")
    for i in range(3):
        for j in range(3):
            print(f"({i}, {j})", end=" ")
        print()  # 줄바꿈

def multiplication_table():
    """구구단 표"""
    print("\n=== 구구단 표 ===")
    
    # 전체 구구단 (2단~9단)
    for i in range(2, 10):
        print(f"\n{i}단:")
        for j in range(1, 10):
            result = i * j
            print(f"  {i} × {j} = {result}")

def star_patterns():
    """별 찍기 패턴들"""
    print("\n=== 별 찍기 패턴들 ===")
    
    # 직각 삼각형
    print("직각 삼각형:")
    for i in range(1, 6):
        for j in range(i):
            print("*", end="")
        print()
    
    # 역직각 삼각형
    print("\n역직각 삼각형:")
    for i in range(5, 0, -1):
        for j in range(i):
            print("*", end="")
        print()
    
    # 피라미드
    print("\n피라미드:")
    for i in range(1, 6):
        # 공백 출력
        for j in range(5 - i):
            print(" ", end="")
        # 별 출력
        for j in range(2 * i - 1):
            print("*", end="")
        print()
    
    # 다이아몬드
    print("\n다이아몬드:")
    # 상단 부분
    for i in range(1, 4):
        for j in range(3 - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()
    # 하단 부분
    for i in range(2, 0, -1):
        for j in range(3 - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()

def matrix_operations():
    """행렬 연산"""
    print("\n=== 행렬 연산 ===")
    
    # 행렬 생성
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    print("행렬 1:")
    for row in matrix1:
        print(row)
    
    print("\n행렬 2:")
    for row in matrix2:
        print(row)
    
    # 행렬 덧셈
    print("\n행렬 덧셈 결과:")
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
        print(row)

def nested_with_conditions():
    """조건문이 있는 중첩 반복문"""
    print("\n=== 조건문이 있는 중첩 반복문 ===")
    
    # 2차원 배열에서 특정 값 찾기
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    target = 7
    found = False
    
    print(f"행렬에서 {target} 찾기:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                print(f"  {target}을 ({i}, {j}) 위치에서 찾았습니다!")
                found = True
                break
        if found:
            break
    
    if not found:
        print(f"  {target}을 찾을 수 없습니다.")

def nested_with_break_continue():
    """break와 continue가 있는 중첩 반복문"""
    print("\n=== break와 continue가 있는 중첩 반복문 ===")
    
    # 소수 찾기 (2부터 20까지)
    print("소수 찾기 (2-20):")
    for num in range(2, 21):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break  # 내부 반복문 종료
        if is_prime:
            print(f"  {num}은 소수입니다.")

def practical_nested_examples():
    """실무에서 자주 사용되는 중첩 반복문 예제"""
    print("\n=== 실무 중첩 반복문 예제 ===")
    
    # 학생 성적 처리
    students = [
        ["Alice", [85, 92, 78]],
        ["Bob", [90, 88, 95]],
        ["Charlie", [75, 82, 88]]
    ]
    
    print("학생 성적 처리:")
    for student in students:
        name = student[0]
        scores = student[1]
        
        total = 0
        for score in scores:
            total += score
        
        average = total / len(scores)
        print(f"  {name}: 평균 {average:.1f}점")
    
    # 2차원 데이터 분석
    print("\n2차원 데이터 분석:")
    data = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    
    # 각 행의 합계
    for i, row in enumerate(data):
        row_sum = sum(row)
        print(f"  행 {i+1}의 합계: {row_sum}")
    
    # 각 열의 합계
    for j in range(len(data[0])):
        col_sum = 0
        for i in range(len(data)):
            col_sum += data[i][j]
        print(f"  열 {j+1}의 합계: {col_sum}")

def nested_loop_optimization():
    """중첩 반복문 최적화 팁"""
    print("\n=== 중첩 반복문 최적화 팁 ===")
    
    # 비효율적인 방법
    print("비효율적인 방법:")
    numbers = [1, 2, 3, 4, 5]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                print(f"  {numbers[i]} + {numbers[j]} = {numbers[i] + numbers[j]}")
    
    # 효율적인 방법
    print("\n효율적인 방법:")
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            print(f"  {numbers[i]} + {numbers[j]} = {numbers[i] + numbers[j]}")

if __name__ == "__main__":
    basic_nested_loops()
    multiplication_table()
    star_patterns()
    matrix_operations()
    nested_with_conditions()
    nested_with_break_continue()
    practical_nested_examples()
    nested_loop_optimization()
