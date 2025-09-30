# 튜플 기본 사용법

def demonstrate_tuple_creation():
    """튜플 생성 방법들을 보여주는 함수"""
    print("=== 튜플 생성 방법들 ===")
    
    # 빈 튜플 생성
    empty_tuple = ()
    empty_tuple2 = tuple()
    print(f"빈 튜플: {empty_tuple}, {empty_tuple2}")
    
    # 직접 생성
    coordinates = (10, 20)
    colors = ("red", "green", "blue")
    mixed = (1, "hello", 3.14, True)
    print(f"좌표: {coordinates}")
    print(f"색상: {colors}")
    print(f"혼합: {mixed}")
    
    # 단일 요소 튜플 (쉼표 필요)
    single_tuple = (42,)
    not_tuple = (42)
    print(f"단일 요소 튜플: {single_tuple}, 타입: {type(single_tuple)}")
    print(f"괄호만 사용: {not_tuple}, 타입: {type(not_tuple)}")
    
    # tuple() 생성자 사용
    from_list = tuple([1, 2, 3, 4, 5])
    from_string = tuple("Hello")
    print(f"리스트에서 생성: {from_list}")
    print(f"문자열에서 생성: {from_string}")

def demonstrate_tuple_access():
    """튜플 접근 방법들을 보여주는 함수"""
    print("\n=== 튜플 접근 방법들 ===")
    
    numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    print(f"원본 튜플: {numbers}")
    
    # 인덱스로 접근
    print(f"첫 번째 요소: {numbers[0]}")
    print(f"두 번째 요소: {numbers[1]}")
    print(f"마지막 요소: {numbers[-1]}")
    print(f"뒤에서 두 번째: {numbers[-2]}")
    
    # 슬라이싱
    print(f"처음 3개: {numbers[:3]}")
    print(f"마지막 3개: {numbers[-3:]}")
    print(f"중간 3개 (인덱스 2-4): {numbers[2:5]}")
    print(f"모든 요소 (2씩 건너뛰기): {numbers[::2]}")
    print(f"역순: {numbers[::-1]}")
    
    # 튜플 길이
    print(f"튜플 길이: {len(numbers)}")

def demonstrate_tuple_immutability():
    """튜플의 불변성을 보여주는 함수"""
    print("\n=== 튜플의 불변성 ===")
    
    numbers = (1, 2, 3, 4, 5)
    print(f"원본 튜플: {numbers}")
    
    # 튜플은 불변하므로 수정 불가
    try:
        numbers[0] = 10
    except TypeError as e:
        print(f"수정 시도 시 에러: {e}")
    
    # 하지만 새로운 튜플은 생성 가능
    new_numbers = numbers + (6, 7, 8)
    print(f"새로운 튜플: {new_numbers}")
    print(f"원본 튜플: {numbers}")  # 원본은 변경되지 않음
    
    # 튜플의 요소가 가변 객체인 경우
    mutable_tuple = ([1, 2, 3], [4, 5, 6])
    print(f"가변 요소를 가진 튜플: {mutable_tuple}")
    
    # 튜플 자체는 수정할 수 없지만, 내부 리스트는 수정 가능
    mutable_tuple[0].append(4)
    print(f"내부 리스트 수정 후: {mutable_tuple}")

def demonstrate_tuple_operations():
    """튜플 연산들을 보여주는 함수"""
    print("\n=== 튜플 연산들 ===")
    
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    
    # 연결
    combined = tuple1 + tuple2
    print(f"튜플 연결: {tuple1} + {tuple2} = {combined}")
    
    # 반복
    repeated = tuple1 * 3
    print(f"튜플 반복: {tuple1} * 3 = {repeated}")
    
    # 멤버십 확인
    print(f"2가 tuple1에 있는가? {2 in tuple1}")
    print(f"7이 tuple1에 있는가? {7 in tuple1}")
    
    # 튜플 비교
    tuple3 = (1, 2, 3)
    print(f"tuple1 == tuple3? {tuple1 == tuple3}")
    print(f"tuple1 is tuple3? {tuple1 is tuple3}")
    
    # 튜플의 튜플
    nested = ((1, 2), (3, 4), (5, 6))
    print(f"중첩 튜플: {nested}")
    print(f"첫 번째 요소: {nested[0]}")
    print(f"첫 번째 요소의 두 번째 값: {nested[0][1]}")

def demonstrate_tuple_methods():
    """튜플 메서드들을 보여주는 함수"""
    print("\n=== 튜플 메서드들 ===")
    
    numbers = (1, 2, 3, 2, 4, 2, 5)
    print(f"원본 튜플: {numbers}")
    
    # count() - 값의 개수 세기
    count = numbers.count(2)
    print(f"count(2): {count}")
    
    # index() - 값의 인덱스 찾기
    index = numbers.index(2)
    print(f"index(2): {index}")
    
    # index() with start parameter
    index2 = numbers.index(2, 2)
    print(f"index(2, 2): {index2}")
    
    # 튜플은 불변하므로 추가/삭제 메서드 없음
    print("튜플에는 append, insert, remove, pop 메서드가 없습니다.")

def demonstrate_tuple_iteration():
    """튜플 순회 방법들을 보여주는 함수"""
    print("\n=== 튜플 순회 방법들 ===")
    
    colors = ("red", "green", "blue", "yellow")
    
    # 기본 for문
    print("기본 for문:")
    for color in colors:
        print(f"  {color}")
    
    # enumerate 사용
    print("\nenumerate 사용:")
    for i, color in enumerate(colors):
        print(f"  {i}: {color}")
    
    # range와 인덱스 사용
    print("\nrange와 인덱스 사용:")
    for i in range(len(colors)):
        print(f"  {i}: {colors[i]}")
    
    # 역순 순회
    print("\n역순 순회:")
    for color in reversed(colors):
        print(f"  {color}")

def demonstrate_practical_examples():
    """실무에서 자주 사용되는 튜플 예제"""
    print("\n=== 실무 예제 ===")
    
    # 좌표계
    point1 = (10, 20)
    point2 = (30, 40)
    print(f"점1: {point1}")
    print(f"점2: {point2}")
    
    # 거리 계산
    import math
    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    print(f"두 점 사이의 거리: {distance:.2f}")
    
    # RGB 색상
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    print(f"RGB 색상: 빨강={red}, 초록={green}, 파랑={blue}")
    
    # 학생 정보
    student = ("김철수", 20, "컴퓨터공학", 3.5)
    name, age, major, gpa = student
    print(f"학생 정보: {name}, {age}세, {major}, GPA {gpa}")
    
    # 함수에서 여러 값 반환
    def get_stats(numbers):
        return len(numbers), sum(numbers), sum(numbers)/len(numbers)
    
    data = (1, 2, 3, 4, 5)
    count, total, average = get_stats(data)
    print(f"통계: 개수={count}, 합계={total}, 평균={average:.2f}")

if __name__ == "__main__":
    demonstrate_tuple_creation()
    demonstrate_tuple_access()
    demonstrate_tuple_immutability()
    demonstrate_tuple_operations()
    demonstrate_tuple_methods()
    demonstrate_tuple_iteration()
    demonstrate_practical_examples()
