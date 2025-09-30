# 리스트 메서드들

def demonstrate_list_methods():
    """리스트 메서드들을 보여주는 함수"""
    print("=== 리스트 메서드들 ===")
    
    # 추가 메서드들
    numbers = [1, 2, 3]
    print(f"원본: {numbers}")
    
    # append() - 끝에 추가
    numbers.append(4)
    print(f"append(4): {numbers}")
    
    # insert() - 특정 위치에 삽입
    numbers.insert(1, 1.5)
    print(f"insert(1, 1.5): {numbers}")
    
    # extend() - 여러 요소 추가
    numbers.extend([5, 6, 7])
    print(f"extend([5, 6, 7]): {numbers}")
    
    # 삭제 메서드들
    print(f"\n삭제 메서드들:")
    print(f"현재 리스트: {numbers}")
    
    # remove() - 값으로 삭제
    numbers.remove(1.5)
    print(f"remove(1.5): {numbers}")
    
    # pop() - 인덱스로 삭제 (기본값: 마지막)
    popped = numbers.pop()
    print(f"pop(): {numbers}, 삭제된 값: {popped}")
    
    popped2 = numbers.pop(0)
    print(f"pop(0): {numbers}, 삭제된 값: {popped2}")
    
    # del 문
    del numbers[1]
    print(f"del numbers[1]: {numbers}")
    
    # clear() - 모든 요소 삭제
    numbers.clear()
    print(f"clear(): {numbers}")

def demonstrate_search_methods():
    """검색 관련 메서드들을 보여주는 함수"""
    print("\n=== 검색 관련 메서드들 ===")
    
    numbers = [1, 2, 3, 2, 4, 2, 5]
    print(f"원본: {numbers}")
    
    # index() - 값의 인덱스 찾기
    index = numbers.index(2)
    print(f"index(2): {index}")
    
    # count() - 값의 개수 세기
    count = numbers.count(2)
    print(f"count(2): {count}")
    
    # in 연산자
    print(f"3 in numbers: {3 in numbers}")
    print(f"6 in numbers: {6 in numbers}")

def demonstrate_sort_methods():
    """정렬 관련 메서드들을 보여주는 함수"""
    print("\n=== 정렬 관련 메서드들 ===")
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"원본: {numbers}")
    
    # sort() - 원본 리스트 정렬
    numbers.sort()
    print(f"sort(): {numbers}")
    
    # sort(reverse=True) - 역순 정렬
    numbers.sort(reverse=True)
    print(f"sort(reverse=True): {numbers}")
    
    # sorted() - 새로운 정렬된 리스트 반환
    original = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_list = sorted(original)
    print(f"원본: {original}")
    print(f"sorted(original): {sorted_list}")
    
    # 문자열 정렬
    words = ["banana", "apple", "cherry", "date"]
    print(f"문자열 원본: {words}")
    words.sort()
    print(f"문자열 정렬: {words}")
    
    # 길이로 정렬
    words.sort(key=len)
    print(f"길이로 정렬: {words}")

def demonstrate_reverse_methods():
    """역순 관련 메서드들을 보여주는 함수"""
    print("\n=== 역순 관련 메서드들 ===")
    
    numbers = [1, 2, 3, 4, 5]
    print(f"원본: {numbers}")
    
    # reverse() - 원본 리스트 역순
    numbers.reverse()
    print(f"reverse(): {numbers}")
    
    # reversed() - 역순 이터레이터 반환
    original = [1, 2, 3, 4, 5]
    reversed_list = list(reversed(original))
    print(f"원본: {original}")
    print(f"reversed(): {reversed_list}")

def demonstrate_copy_methods():
    """복사 관련 메서드들을 보여주는 함수"""
    print("\n=== 복사 관련 메서드들 ===")
    
    original = [1, 2, [3, 4]]
    print(f"원본: {original}")
    
    # copy() - 얕은 복사
    shallow_copy = original.copy()
    print(f"copy(): {shallow_copy}")
    
    # 슬라이싱으로 복사
    slice_copy = original[:]
    print(f"슬라이싱 복사: {slice_copy}")
    
    # list() 생성자로 복사
    constructor_copy = list(original)
    print(f"list() 복사: {constructor_copy}")
    
    # 얕은 복사의 문제점
    original[2][0] = 999
    print(f"원본 수정 후:")
    print(f"원본: {original}")
    print(f"얕은 복사: {shallow_copy}")  # 중첩 리스트도 변경됨

def demonstrate_practical_examples():
    """실무에서 자주 사용되는 리스트 메서드 예제"""
    print("\n=== 실무 예제 ===")
    
    # 학생 점수 관리
    scores = [85, 92, 78, 96, 88]
    print(f"원본 점수: {scores}")
    
    # 최고점과 최저점 제거
    scores.remove(max(scores))
    scores.remove(min(scores))
    print(f"최고점/최저점 제거 후: {scores}")
    
    # 평균 계산
    average = sum(scores) / len(scores)
    print(f"평균: {average:.2f}")
    
    # 점수 등급 분류
    grade_a = [score for score in scores if score >= 90]
    grade_b = [score for score in scores if 80 <= score < 90]
    grade_c = [score for score in scores if score < 80]
    
    print(f"A등급 (90점 이상): {grade_a}")
    print(f"B등급 (80-89점): {grade_b}")
    print(f"C등급 (80점 미만): {grade_c}")
    
    # 중복 제거 (순서 유지)
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    print(f"원본: {numbers}")
    print(f"중복 제거: {unique_numbers}")

if __name__ == "__main__":
    demonstrate_list_methods()
    demonstrate_search_methods()
    demonstrate_sort_methods()
    demonstrate_reverse_methods()
    demonstrate_copy_methods()
    demonstrate_practical_examples()
