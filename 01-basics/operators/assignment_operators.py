# 할당 연산자 예제

def basic_assignment():
    """기본 할당 연산자 사용법"""
    print("=== 기본 할당 연산자 ===")
    
    # 기본 할당
    x = 10
    print(f"x = 10: {x}")
    
    # 복합 할당 연산자
    x += 5   # x = x + 5
    print(f"x += 5: {x}")
    
    x -= 3   # x = x - 3
    print(f"x -= 3: {x}")
    
    x *= 2   # x = x * 2
    print(f"x *= 2: {x}")
    
    x /= 4   # x = x / 4
    print(f"x /= 4: {x}")
    
    x %= 3   # x = x % 3
    print(f"x %= 3: {x}")
    
    x **= 2  # x = x ** 2
    print(f"x **= 2: {x}")
    
    x //= 2  # x = x // 2
    print(f"x //= 2: {x}")

def string_assignment():
    """문자열 할당 연산자 예제"""
    print("\n=== 문자열 할당 연산자 ===")
    
    message = "Hello"
    print(f"초기 메시지: '{message}'")
    
    message += " World"  # 문자열 연결
    print(f"message += ' World': '{message}'")
    
    message *= 2  # 문자열 반복
    print(f"message *= 2: '{message}'")

def list_assignment():
    """리스트 할당 연산자 예제"""
    print("\n=== 리스트 할당 연산자 ===")
    
    numbers = [1, 2, 3]
    print(f"초기 리스트: {numbers}")
    
    numbers += [4, 5]  # 리스트 확장
    print(f"numbers += [4, 5]: {numbers}")
    
    numbers *= 2  # 리스트 반복
    print(f"numbers *= 2: {numbers}")

def practical_examples():
    """실무에서 자주 사용되는 할당 연산"""
    print("\n=== 실무 예제 ===")
    
    # 카운터 관리
    page_views = 0
    user_clicks = 0
    
    # 페이지 조회수 증가
    page_views += 1
    page_views += 1
    print(f"페이지 조회수: {page_views}")
    
    # 클릭 수 증가
    user_clicks += 5
    print(f"사용자 클릭수: {user_clicks}")
    
    # 점수 계산
    total_score = 0
    scores = [85, 92, 78, 96, 88]
    
    for score in scores:
        total_score += score
    
    average_score = total_score / len(scores)
    print(f"총점: {total_score}, 평균: {average_score}")
    
    # 문자열 빌딩
    html_content = ""
    html_content += "<html>"
    html_content += "<head><title>My Page</title></head>"
    html_content += "<body>"
    html_content += "<h1>Welcome</h1>"
    html_content += "</body>"
    html_content += "</html>"
    
    print(f"HTML 내용 길이: {len(html_content)}")

def multiple_assignment():
    """다중 할당 예제"""
    print("\n=== 다중 할당 ===")
    
    # 여러 변수에 같은 값 할당
    x = y = z = 0
    print(f"x = y = z = 0: x={x}, y={y}, z={z}")
    
    # 여러 변수에 다른 값 할당
    a, b, c = 1, 2, 3
    print(f"a, b, c = 1, 2, 3: a={a}, b={b}, c={c}")
    
    # 값 교환
    print(f"교환 전: a={a}, b={b}")
    a, b = b, a
    print(f"교환 후: a={a}, b={b}")
    
    # 리스트 언패킹
    coordinates = [10, 20, 30]
    x, y, z = coordinates
    print(f"좌표: x={x}, y={y}, z={z}")

def walrus_operator():
    """바다코끼리 연산자 (:=) 예제 (Python 3.8+)"""
    print("\n=== 바다코끼리 연산자 (:=) ===")
    
    # 조건문에서 할당과 검사 동시에
    numbers = [1, 2, 3, 4, 5]
    
    # 전통적인 방법
    total = 0
    for num in numbers:
        total += num
        if total > 6:
            break
    print(f"전통적인 방법 - 총합: {total}")
    
    # 바다코끼리 연산자 사용 (Python 3.8+)
    # 주석 처리: 이 기능은 Python 3.8 이상에서만 작동
    """
    total = 0
    for num in numbers:
        if (total := total + num) > 6:
            break
    print(f"바다코끼리 연산자 - 총합: {total}")
    """

def assignment_vs_equality():
    """할당과 비교의 차이점"""
    print("\n=== 할당 vs 비교 ===")
    
    x = 5
    print(f"x = 5 (할당): x는 {x}")
    
    # 비교 연산자
    is_equal = (x == 5)
    print(f"x == 5 (비교): {is_equal}")
    
    # 잘못된 사용 예시
    print("\n⚠️ 주의사항:")
    print("x = 5  # 할당 (값을 저장)")
    print("x == 5 # 비교 (값이 같은지 확인)")

if __name__ == "__main__":
    basic_assignment()
    string_assignment()
    list_assignment()
    practical_examples()
    multiple_assignment()
    walrus_operator()
    assignment_vs_equality()
