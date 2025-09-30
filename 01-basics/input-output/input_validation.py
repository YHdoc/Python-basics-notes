# 입력 검증과 에러 처리

def number_validation():
    """숫자 입력 검증"""
    print("=== 숫자 입력 검증 ===")
    
    # 정수 입력 검증
    while True:
        try:
            age = int(input("나이를 입력하세요: "))
            if 1 <= age <= 120:
                break
            else:
                print("나이는 1-120 사이의 숫자여야 합니다.")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")
    
    print(f"입력된 나이: {age}세")
    
    # 실수 입력 검증
    while True:
        try:
            height = float(input("키를 입력하세요 (cm): "))
            if 50 <= height <= 250:
                break
            else:
                print("키는 50-250cm 사이여야 합니다.")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")
    
    print(f"입력된 키: {height}cm")

def string_validation():
    """문자열 입력 검증"""
    print("\n=== 문자열 입력 검증 ===")
    
    # 이름 검증 (한글, 영문만)
    while True:
        name = input("이름을 입력하세요 (한글 또는 영문): ").strip()
        if name and name.replace(" ", "").isalpha():
            break
        else:
            print("이름은 한글 또는 영문만 입력해주세요.")
    
    print(f"입력된 이름: {name}")
    
    # 이메일 검증 (간단한 버전)
    while True:
        email = input("이메일을 입력하세요: ").strip()
        if "@" in email and "." in email.split("@")[1]:
            break
        else:
            print("올바른 이메일 형식을 입력해주세요.")
    
    print(f"입력된 이메일: {email}")

def choice_validation():
    """선택지 검증"""
    print("\n=== 선택지 검증 ===")
    
    # 메뉴 선택
    menu = {
        "1": "짜장면",
        "2": "짬뽕", 
        "3": "탕수육",
        "4": "볶음밥"
    }
    
    print("메뉴를 선택하세요:")
    for key, value in menu.items():
        print(f"{key}. {value}")
    
    while True:
        choice = input("선택 (1-4): ").strip()
        if choice in menu:
            break
        else:
            print("1-4 중에서 선택해주세요.")
    
    print(f"선택한 메뉴: {menu[choice]}")

def password_validation():
    """비밀번호 검증"""
    print("\n=== 비밀번호 검증 ===")
    
    while True:
        password = input("비밀번호를 입력하세요 (8자 이상, 영문+숫자): ")
        
        # 길이 확인
        if len(password) < 8:
            print("비밀번호는 8자 이상이어야 합니다.")
            continue
        
        # 영문자 포함 확인
        has_alpha = any(c.isalpha() for c in password)
        if not has_alpha:
            print("비밀번호에 영문자가 포함되어야 합니다.")
            continue
        
        # 숫자 포함 확인
        has_digit = any(c.isdigit() for c in password)
        if not has_digit:
            print("비밀번호에 숫자가 포함되어야 합니다.")
            continue
        
        # 비밀번호 확인
        confirm_password = input("비밀번호를 다시 입력하세요: ")
        if password == confirm_password:
            break
        else:
            print("비밀번호가 일치하지 않습니다.")
    
    print("비밀번호 설정이 완료되었습니다!")

def range_validation():
    """범위 검증"""
    print("\n=== 범위 검증 ===")
    
    # 점수 입력 (0-100)
    while True:
        try:
            score = int(input("점수를 입력하세요 (0-100): "))
            if 0 <= score <= 100:
                break
            else:
                print("점수는 0-100 사이여야 합니다.")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")
    
    # 등급 계산
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"점수: {score}점, 등급: {grade}")

def practical_validation():
    """실무 검증 예제"""
    print("\n=== 실무 검증 예제 ===")
    
    # 사용자 등록 폼
    print("=== 사용자 등록 ===")
    
    # 사용자명 검증
    while True:
        username = input("사용자명 (3-20자, 영문+숫자): ").strip()
        if 3 <= len(username) <= 20 and username.isalnum():
            break
        else:
            print("사용자명은 3-20자의 영문과 숫자만 사용 가능합니다.")
    
    # 전화번호 검증 (간단한 버전)
    while True:
        phone = input("전화번호 (예: 010-1234-5678): ").strip()
        # 간단한 전화번호 형식 검증
        if len(phone) == 13 and phone.count("-") == 2:
            parts = phone.split("-")
            if len(parts[0]) == 3 and len(parts[1]) == 4 and len(parts[2]) == 4:
                if all(part.isdigit() for part in parts):
                    break
        
        print("올바른 전화번호 형식을 입력해주세요 (예: 010-1234-5678)")
    
    # 생년월일 검증
    while True:
        birth = input("생년월일 (예: 1990-01-01): ").strip()
        try:
            from datetime import datetime
            datetime.strptime(birth, "%Y-%m-%d")
            break
        except ValueError:
            print("올바른 날짜 형식을 입력해주세요 (예: 1990-01-01)")
    
    print(f"\n등록 완료!")
    print(f"사용자명: {username}")
    print(f"전화번호: {phone}")
    print(f"생년월일: {birth}")

if __name__ == "__main__":
    number_validation()
    string_validation()
    choice_validation()
    password_validation()
    range_validation()
    practical_validation()
