# 멤버십 연산자 예제
# 멤버십 연산자 : 어떤 값이 시퀀스나 컬렉션 안에 포함되어 있는지 확인할 때 쓰는 연산자
# 대표 : in / not in

def basic_membership():
    """기본 멤버십 연산자 사용법"""
    print("=== 기본 멤버십 연산자 ===")
    
    # 문자열에서 멤버십 확인
    text = "Hello World"
    print(f"문자열: '{text}'")
    print(f"'Hello' in text: {'Hello' in text}")
    print(f"'Python' in text: {'Python' in text}")
    print(f"'World' not in text: {'World' not in text}")
    
    # 리스트에서 멤버십 확인
    numbers = [1, 2, 3, 4, 5]
    print(f"\n리스트: {numbers}")
    print(f"3 in numbers: {3 in numbers}")
    print(f"6 in numbers: {6 in numbers}")
    print(f"0 not in numbers: {0 not in numbers}")
    
    # 튜플에서 멤버십 확인
    colors = ("red", "green", "blue")
    print(f"\n튜플: {colors}")
    print(f"'red' in colors: {'red' in colors}")
    print(f"'yellow' in colors: {'yellow' in colors}")

def dictionary_membership():
    """딕셔너리에서 멤버십 확인"""
    print("\n=== 딕셔너리 멤버십 ===")
    
    person = {
        "name": "김철수",
        "age": 30,
        "city": "서울"
    }
    
    print(f"딕셔너리: {person}")
    
    # 키 확인
    print(f"'name' in person: {'name' in person}")
    print(f"'email' in person: {'email' in person}")
    print(f"'age' not in person: {'age' not in person}")
    
    # 값 확인 (직접적으로는 불가능, values() 사용)
    print(f"'김철수' in person.values(): {'김철수' in person.values()}")
    print(f"'부산' in person.values(): {'부산' in person.values()}")

def set_membership():
    """집합에서 멤버십 확인"""
    print("\n=== 집합 멤버십 ===")
    
    fruits = {"apple", "banana", "orange", "grape"}
    print(f"집합: {fruits}")
    
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'mango' in fruits: {'mango' in fruits}")
    print(f"'kiwi' not in fruits: {'kiwi' not in fruits}")

def practical_examples():
    """실무에서 자주 사용되는 멤버십 연산"""
    print("\n=== 실무 예제 ===")
    
    # 사용자 권한 확인
    user_roles = ["user", "editor"]
    admin_roles = ["admin", "super_admin"]
    
    def has_admin_access(roles):
        return any(role in admin_roles for role in roles)
    
    def has_editor_access(roles):
        return "editor" in roles or "admin" in roles
    
    print(f"사용자 역할: {user_roles}")
    print(f"관리자 접근 권한: {has_admin_access(user_roles)}")
    print(f"편집자 접근 권한: {has_editor_access(user_roles)}")
    
    # 금지된 단어 필터링
    forbidden_words = ["spam", "scam", "fake", "fraud"]
    user_message = "This is not a spam message"
    
    has_forbidden = any(word in user_message.lower() for word in forbidden_words)
    print(f"\n사용자 메시지: '{user_message}'")
    print(f"금지된 단어 포함: {has_forbidden}")
    
    # 파일 확장자 확인
    allowed_extensions = [".txt", ".pdf", ".doc", ".docx"]
    filename = "document.pdf"
    
    is_allowed = any(filename.lower().endswith(ext) for ext in allowed_extensions)
    print(f"\n파일명: {filename}")
    print(f"허용된 확장자: {is_allowed}")
    
    # 이메일 도메인 확인
    trusted_domains = ["gmail.com", "yahoo.com", "company.com"]
    email = "user@gmail.com"
    domain = email.split("@")[1] if "@" in email else ""
    
    is_trusted = domain in trusted_domains
    print(f"\n이메일: {email}")
    print(f"신뢰할 수 있는 도메인: {is_trusted}")

def performance_considerations():
    """멤버십 연산의 성능 고려사항"""
    print("\n=== 성능 고려사항 ===")
    
    # 리스트 vs 집합 성능 비교
    import time
    
    # 큰 리스트 생성
    large_list = list(range(10000))
    large_set = set(range(10000))
    
    # 리스트에서 멤버십 확인
    start_time = time.time()
    result1 = 9999 in large_list
    list_time = time.time() - start_time
    
    # 집합에서 멤버십 확인
    start_time = time.time()
    result2 = 9999 in large_set
    set_time = time.time() - start_time
    
    print(f"리스트 멤버십 확인 시간: {list_time:.6f}초")
    print(f"집합 멤버십 확인 시간: {set_time:.6f}초")
    print(f"집합이 {list_time/set_time:.1f}배 빠름")
    
    # 문자열 멤버십의 효율성
    long_text = "Python is a great programming language. " * 1000
    
    start_time = time.time()
    result3 = "programming" in long_text
    string_time = time.time() - start_time
    
    print(f"긴 문자열에서 멤버십 확인 시간: {string_time:.6f}초")

def advanced_membership():
    """고급 멤버십 연산 예제"""
    print("\n=== 고급 멤버십 연산 ===")
    
    # 중첩된 구조에서 멤버십 확인
    nested_data = {
        "users": [
            {"name": "Alice", "skills": ["Python", "Java"]},
            {"name": "Bob", "skills": ["C++", "Python"]},
            {"name": "Charlie", "skills": ["JavaScript", "React"]}
        ]
    }
    
    # 특정 스킬을 가진 사용자 찾기
    target_skill = "Python"
    python_users = []
    
    for user in nested_data["users"]:
        if target_skill in user["skills"]:
            python_users.append(user["name"])
    
    print(f"Python 스킬을 가진 사용자: {python_users}")
    
    # 부분 문자열 검색
    sentences = [
        "Python is awesome",
        "I love programming",
        "Java is also good",
        "Python and Java are both great"
    ]
    
    python_sentences = [s for s in sentences if "Python" in s]
    print(f"Python을 언급한 문장: {python_sentences}")
    
    # 복합 조건 멤버십
    valid_emails = ["user@company.com", "admin@company.com", "test@company.com"]
    blocked_domains = ["spam.com", "fake.com"]
    
    def is_valid_email(email):
        if "@" not in email:
            return False
        
        domain = email.split("@")[1]
        return email in valid_emails and domain not in blocked_domains
    
    test_emails = ["user@company.com", "spam@spam.com", "new@company.com"]
    
    print(f"\n이메일 유효성 검사:")
    for email in test_emails:
        print(f"{email}: {is_valid_email(email)}")

if __name__ == "__main__":
    basic_membership()
    dictionary_membership()
    set_membership()
    practical_examples()
    performance_considerations()
    advanced_membership()
