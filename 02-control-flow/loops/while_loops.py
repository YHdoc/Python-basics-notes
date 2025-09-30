# while문 기본 사용법

def basic_while_loop():
    """기본 while문 사용법"""
    print("=== 기본 while문 ===")
    
    # 카운터를 사용한 while문
    count = 0
    while count < 5:
        print(f"카운트: {count}")
        count += 1
    
    print("while문 종료!")

def while_with_condition():
    """조건을 사용한 while문"""
    print("\n=== 조건을 사용한 while문 ===")
    
    # 사용자 입력을 받는 while문
    print("숫자를 입력하세요 (0을 입력하면 종료):")
    total = 0
    count = 0
    
    while True:
        try:
            num = int(input("숫자 입력: "))
            if num == 0:
                break
            total += num
            count += 1
            print(f"현재 합계: {total}")
        except ValueError:
            print("올바른 숫자를 입력해주세요.")
    
    if count > 0:
        average = total / count
        print(f"입력된 숫자 개수: {count}")
        print(f"총합: {total}")
        print(f"평균: {average:.2f}")

def while_with_list():
    """리스트와 함께 사용하는 while문"""
    print("\n=== 리스트와 while문 ===")
    
    # 리스트에서 요소 제거
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"원본 리스트: {numbers}")
    
    # 5보다 큰 수 제거
    while numbers and numbers[0] <= 5:
        removed = numbers.pop(0)
        print(f"제거된 수: {removed}, 남은 리스트: {numbers}")
    
    print(f"최종 리스트: {numbers}")

def while_with_string():
    """문자열과 함께 사용하는 while문"""
    print("\n=== 문자열과 while문 ===")
    
    # 문자열에서 특정 문자 제거
    text = "Hello, World! This is a test."
    print(f"원본 문자열: {text}")
    
    # 공백 제거
    while " " in text:
        text = text.replace(" ", "", 1)  # 첫 번째 공백만 제거
        print(f"공백 제거 후: '{text}'")
    
    print(f"최종 문자열: '{text}'")

def while_with_file():
    """파일과 함께 사용하는 while문"""
    print("\n=== 파일과 while문 ===")
    
    # 가상의 파일 읽기 시뮬레이션
    lines = [
        "첫 번째 줄",
        "두 번째 줄",
        "세 번째 줄",
        "END"  # 종료 조건
    ]
    
    index = 0
    print("파일 내용 읽기:")
    while index < len(lines) and lines[index] != "END":
        print(f"라인 {index + 1}: {lines[index]}")
        index += 1
    
    print("파일 읽기 완료!")

def while_with_nested():
    """중첩된 while문"""
    print("\n=== 중첩된 while문 ===")
    
    # 구구단 출력
    i = 2
    while i <= 3:  # 2단, 3단만 출력
        print(f"\n{i}단:")
        j = 1
        while j <= 9:
            result = i * j
            print(f"{i} × {j} = {result}")
            j += 1
        i += 1

def while_with_break_continue():
    """while문에서 break와 continue 사용"""
    print("\n=== while문에서 break와 continue ===")
    
    # 1부터 10까지 출력하되, 5는 건너뛰기
    num = 1
    while num <= 10:
        if num == 5:
            num += 1
            continue  # 5는 건너뛰고 다음 반복으로
        
        if num == 8:
            break  # 8에서 반복문 종료
        
        print(f"숫자: {num}")
        num += 1
    
    print("while문 종료!")

def practical_while_examples():
    """실무에서 자주 사용되는 while문 예제"""
    print("\n=== 실무 while문 예제 ===")
    
    # 숫자 맞추기 게임
    import random
    
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("1부터 100 사이의 숫자를 맞춰보세요!")
    print(f"최대 {max_attempts}번의 기회가 있습니다.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"시도 {attempts + 1}: 숫자를 입력하세요: "))
            attempts += 1
            
            if guess == target:
                print(f"축하합니다! {attempts}번 만에 맞췄습니다!")
                break
            elif guess < target:
                print("더 큰 수입니다.")
            else:
                print("더 작은 수입니다.")
            
            if attempts < max_attempts:
                print(f"남은 기회: {max_attempts - attempts}번")
        
        except ValueError:
            print("올바른 숫자를 입력해주세요.")
            attempts -= 1  # 잘못된 입력은 시도 횟수에서 제외
    
    else:
        print(f"게임 종료! 정답은 {target}이었습니다.")

def while_loop_patterns():
    """while문 패턴들"""
    print("\n=== while문 패턴들 ===")
    
    # 메뉴 시스템 패턴
    print("=== 메뉴 시스템 ===")
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 옵션 1")
        print("2. 옵션 2")
        print("3. 옵션 3")
        print("0. 종료")
        
        choice = input("선택: ")
        
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            print("옵션 1을 선택했습니다.")
        elif choice == "2":
            print("옵션 2를 선택했습니다.")
        elif choice == "3":
            print("옵션 3을 선택했습니다.")
        else:
            print("올바른 메뉴를 선택해주세요.")
    
    # 데이터 처리 패턴
    print("\n=== 데이터 처리 패턴 ===")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    processed_data = []
    
    while data:
        item = data.pop(0)
        if item % 2 == 0:
            processed_data.append(item * 2)
        else:
            processed_data.append(item)
        
        print(f"처리된 항목: {item}, 처리된 데이터: {processed_data}")
    
    print(f"최종 처리된 데이터: {processed_data}")

if __name__ == "__main__":
    basic_while_loop()
    while_with_condition()
    while_with_list()
    while_with_string()
    while_with_file()
    while_with_nested()
    while_with_break_continue()
    practical_while_examples()
    while_loop_patterns()
