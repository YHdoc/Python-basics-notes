# 매개변수와 인수

def greet_with_title(name, title):
    """이름과 직책을 받아 인사하는 함수"""
    print(f"안녕하세요, {title} {name}님!")

def calculate_rectangle_area(length, width):
    """사각형의 넓이를 계산하는 함수"""
    return length * width

def create_user_profile(name, age, email, city="서울"):
    """사용자 프로필을 생성하는 함수"""
    profile = {
        "name": name,
        "age": age,
        "email": email,
        "city": city
    }
    return profile

def process_scores(*scores):
    """여러 점수를 처리하는 함수"""
    if not scores:
        return 0, 0
    
    total = sum(scores)
    average = total / len(scores)
    return total, average

def print_user_info(**user_info):
    """사용자 정보를 출력하는 함수"""
    print("사용자 정보:")
    for key, value in user_info.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    # 위치 인수 사용
    greet_with_title("김철수", "부장")
    
    # 키워드 인수 사용
    greet_with_title(title="과장", name="이영희")
    
    # 사각형 넓이 계산
    area1 = calculate_rectangle_area(10, 5)
    area2 = calculate_rectangle_area(width=8, length=12)
    print(f"사각형 넓이: {area1}, {area2}")
    
    # 사용자 프로필 생성
    profile1 = create_user_profile("박민수", 30, "park@email.com")
    profile2 = create_user_profile("최지영", 25, "choi@email.com", "부산")
    print(f"프로필1: {profile1}")
    print(f"프로필2: {profile2}")
    
    # 가변 인수 사용
    total1, avg1 = process_scores(85, 92, 78, 96)
    total2, avg2 = process_scores(90, 88)
    print(f"점수 합계: {total1}, 평균: {avg1:.1f}")
    print(f"점수 합계: {total2}, 평균: {avg2:.1f}")
    
    # 키워드 인수 사용
    print_user_info(name="김철수", age=30, city="서울", job="개발자")
