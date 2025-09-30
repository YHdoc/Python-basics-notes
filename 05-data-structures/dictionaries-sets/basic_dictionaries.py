# 딕셔너리 기본 사용법

def demonstrate_dictionary_creation():
    """딕셔너리 생성 방법들을 보여주는 함수"""
    print("=== 딕셔너리 생성 방법들 ===")
    
    # 빈 딕셔너리 생성
    empty_dict = {}
    empty_dict2 = dict()
    print(f"빈 딕셔너리: {empty_dict}, {empty_dict2}")
    
    # 직접 생성
    person = {"name": "김철수", "age": 30, "city": "서울"}
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
    print(f"사람 정보: {person}")
    print(f"점수: {scores}")
    
    # dict() 생성자 사용
    from_list = dict([("a", 1), ("b", 2), ("c", 3)])
    from_kwargs = dict(name="이영희", age=25, city="부산")
    print(f"리스트에서 생성: {from_list}")
    print(f"키워드 인수로 생성: {from_kwargs}")
    
    # zip()을 사용한 생성
    keys = ["x", "y", "z"]
    values = [1, 2, 3]
    from_zip = dict(zip(keys, values))
    print(f"zip으로 생성: {from_zip}")

def demonstrate_dictionary_access():
    """딕셔너리 접근 방법들을 보여주는 함수"""
    print("\n=== 딕셔너리 접근 방법들 ===")
    
    person = {"name": "김철수", "age": 30, "city": "서울", "job": "개발자"}
    print(f"원본 딕셔너리: {person}")
    
    # 키로 접근
    name = person["name"]
    age = person["age"]
    print(f"이름: {name}, 나이: {age}")
    
    # get() 메서드로 안전한 접근
    salary = person.get("salary", 0)
    department = person.get("department", "미지정")
    print(f"급여: {salary}, 부서: {department}")
    
    # 키 존재 확인
    print(f"'name' 키가 있는가? {'name' in person}")
    print(f"'salary' 키가 있는가? {'salary' in person}")
    
    # 모든 키, 값, 항목 접근
    print(f"모든 키: {list(person.keys())}")
    print(f"모든 값: {list(person.values())}")
    print(f"모든 항목: {list(person.items())}")

def demonstrate_dictionary_modification():
    """딕셔너리 수정 방법들을 보여주는 함수"""
    print("\n=== 딕셔너리 수정 방법들 ===")
    
    person = {"name": "김철수", "age": 30}
    print(f"원본: {person}")
    
    # 값 수정
    person["age"] = 31
    print(f"나이 수정: {person}")
    
    # 새 키-값 추가
    person["city"] = "서울"
    person["job"] = "개발자"
    print(f"새 항목 추가: {person}")
    
    # update() 메서드로 여러 항목 추가/수정
    person.update({"age": 32, "salary": 5000, "department": "IT"})
    print(f"update() 사용: {person}")
    
    # 항목 삭제
    del person["department"]
    print(f"del로 삭제: {person}")
    
    # pop() 메서드로 삭제
    salary = person.pop("salary", 0)
    print(f"pop()으로 삭제: {person}, 삭제된 값: {salary}")
    
    # popitem() 메서드로 마지막 항목 삭제
    last_item = person.popitem()
    print(f"popitem()으로 삭제: {person}, 삭제된 항목: {last_item}")

def demonstrate_dictionary_iteration():
    """딕셔너리 순회 방법들을 보여주는 함수"""
    print("\n=== 딕셔너리 순회 방법들 ===")
    
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}
    print(f"원본: {scores}")
    
    # 키만 순회
    print("키만 순회:")
    for name in scores:
        print(f"  {name}")
    
    # 키만 순회 (명시적)
    print("\nkeys()로 순회:")
    for name in scores.keys():
        print(f"  {name}")
    
    # 값만 순회
    print("\n값만 순회:")
    for score in scores.values():
        print(f"  {score}")
    
    # 키-값 쌍 순회
    print("\n키-값 쌍 순회:")
    for name, score in scores.items():
        print(f"  {name}: {score}")
    
    # enumerate와 함께 사용
    print("\nenumerate와 함께:")
    for i, (name, score) in enumerate(scores.items()):
        print(f"  {i+1}. {name}: {score}")

def demonstrate_nested_dictionaries():
    """중첩 딕셔너리를 보여주는 함수"""
    print("\n=== 중첩 딕셔너리 ===")
    
    # 중첩 딕셔너리 생성
    students = {
        "Alice": {
            "age": 20,
            "major": "컴퓨터공학",
            "grades": [85, 92, 78, 96]
        },
        "Bob": {
            "age": 21,
            "major": "수학",
            "grades": [90, 88, 95, 87]
        },
        "Charlie": {
            "age": 19,
            "major": "물리학",
            "grades": [75, 82, 88, 91]
        }
    }
    
    print(f"학생 정보: {students}")
    
    # 중첩 접근
    alice_age = students["Alice"]["age"]
    alice_avg = sum(students["Alice"]["grades"]) / len(students["Alice"]["grades"])
    print(f"Alice의 나이: {alice_age}")
    print(f"Alice의 평균 점수: {alice_avg:.1f}")
    
    # 중첩 순회
    print("\n학생별 정보:")
    for name, info in students.items():
        avg_grade = sum(info["grades"]) / len(info["grades"])
        print(f"  {name}: {info['age']}세, {info['major']}, 평균 {avg_grade:.1f}점")

def demonstrate_dictionary_operations():
    """딕셔너리 연산들을 보여주는 함수"""
    print("\n=== 딕셔너리 연산들 ===")
    
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"c": 4, "d": 5, "e": 6}
    
    print(f"dict1: {dict1}")
    print(f"dict2: {dict2}")
    
    # 딕셔너리 복사
    dict1_copy = dict1.copy()
    print(f"dict1 복사: {dict1_copy}")
    
    # 딕셔너리 병합 (Python 3.9+)
    # merged = dict1 | dict2
    # print(f"병합: {merged}")
    
    # update()로 병합
    dict1.update(dict2)
    print(f"update()로 병합: {dict1}")
    
    # 딕셔너리 비교
    dict3 = {"a": 1, "b": 2, "c": 3}
    print(f"dict1 == dict3? {dict1_copy == dict3}")
    print(f"dict1 is dict3? {dict1_copy is dict3}")

if __name__ == "__main__":
    demonstrate_dictionary_creation()
    demonstrate_dictionary_access()
    demonstrate_dictionary_modification()
    demonstrate_dictionary_iteration()
    demonstrate_nested_dictionaries()
    demonstrate_dictionary_operations()
