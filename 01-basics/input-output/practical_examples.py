# 실무에서 자주 사용되는 입출력 패턴

def personal_info_program():
    """개인정보 입력 프로그램"""
    print("=== 개인정보 입력 프로그램 ===")

    values = input("이름과 나이를 입력하세요 (예: 김철수 25): ").split()
    if(len(values) == 2):
        name, age = values
        age = int(age)
        print(f"이름 : {name} 나이 : {age}")
        

    # TODO: 이름, 나이, 주소를 입력받아 출력하는 프로그램을 구현해보세요
    pass

def calculator_program():
    """계산기 프로그램"""
    print("=== 계산기 프로그램 ===")
    # TODO: 두 숫자를 입력받아 사칙연산 결과를 출력하는 프로그램을 구현해보세요
    pass

def grade_management_program():
    """성적 관리 프로그램"""
    print("=== 성적 관리 프로그램 ===")
    # TODO: 학생 정보를 입력받아 성적표를 출력하는 프로그램을 구현해보세요
    pass

def login_system():
    """간단한 로그인 시스템"""
    print("=== 로그인 시스템 ===")
    # TODO: 아이디와 비밀번호를 입력받아 검증하는 프로그램을 구현해보세요
    pass

def file_processor():
    """파일 처리 프로그램"""
    print("=== 파일 처리 프로그램 ===")
    # TODO: 텍스트 파일을 읽어서 처리하고 결과를 출력하는 프로그램을 구현해보세요
    pass

def data_export():
    """데이터 내보내기 프로그램"""
    print("=== 데이터 내보내기 프로그램 ===")
    # TODO: 사용자 데이터를 CSV나 JSON 파일로 내보내는 프로그램을 구현해보세요
    pass

if __name__ == "__main__":
    personal_info_program()
    calculator_program()
    grade_management_program()
    login_system()
    file_processor()
    data_export()
