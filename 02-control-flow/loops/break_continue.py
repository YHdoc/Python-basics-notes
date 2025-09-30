# break와 continue 사용법

def basic_break():
    """기본 break 사용법"""
    print("=== 기본 break 사용법 ===")
    
    # for문에서 break
    print("for문에서 break:")
    for i in range(10):
        if i == 5:
            print(f"  {i}에서 break!")
            break
        print(f"  {i}")
    
    # while문에서 break
    print("\nwhile문에서 break:")
    count = 0
    while count < 10:
        if count == 3:
            print(f"  {count}에서 break!")
            break
        print(f"  {count}")
        count += 1

def basic_continue():
    """기본 continue 사용법"""
    print("\n=== 기본 continue 사용법 ===")
    
    # for문에서 continue
    print("for문에서 continue (짝수 건너뛰기):")
    for i in range(10):
        if i % 2 == 0:
            continue  # 짝수는 건너뛰기
        print(f"  {i}")  # 홀수만 출력
    
    # while문에서 continue
    print("\nwhile문에서 continue (3의 배수 건너뛰기):")
    num = 0
    while num < 10:
        num += 1
        if num % 3 == 0:
            continue  # 3의 배수는 건너뛰기
        print(f"  {num}")

def break_in_nested_loops():
    """중첩 반복문에서 break"""
    print("\n=== 중첩 반복문에서 break ===")
    
    # 내부 반복문에서만 break
    print("내부 반복문에서 break:")
    for i in range(3):
        print(f"  외부 반복 {i}:")
        for j in range(5):
            if j == 2:
                print(f"    j={j}에서 break!")
                break  # 내부 반복문만 종료
            print(f"    j={j}")
    
    # 외부 반복문까지 종료하려면 플래그 사용
    print("\n외부 반복문까지 종료 (플래그 사용):")
    should_break = False
    for i in range(3):
        if should_break:
            break
        print(f"  외부 반복 {i}:")
        for j in range(5):
            if j == 2:
                print(f"    j={j}에서 전체 종료!")
                should_break = True
                break
            print(f"    j={j}")

def continue_in_nested_loops():
    """중첩 반복문에서 continue"""
    print("\n=== 중첩 반복문에서 continue ===")
    
    # 내부 반복문에서 continue
    print("내부 반복문에서 continue:")
    for i in range(3):
        print(f"  외부 반복 {i}:")
        for j in range(5):
            if j == 2:
                print(f"    j={j} 건너뛰기")
                continue  # 내부 반복문의 다음 반복으로
            print(f"    j={j}")

def practical_break_examples():
    """실무에서 자주 사용되는 break 예제"""
    print("\n=== 실무 break 예제 ===")
    
    # 리스트에서 특정 값 찾기
    numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    target = 7
    
    print(f"리스트에서 {target} 찾기:")
    found = False
    for i, num in enumerate(numbers):
        if num == target:
            print(f"  {target}을 인덱스 {i}에서 찾았습니다!")
            found = True
            break
    
    if not found:
        print(f"  {target}을 찾을 수 없습니다.")
    
    # 사용자 입력 처리
    print("\n사용자 입력 처리 (quit 입력시 종료):")
    while True:
        user_input = input("  메시지를 입력하세요 (quit로 종료): ")
        if user_input.lower() == "quit":
            print("  프로그램을 종료합니다.")
            break
        print(f"  입력된 메시지: {user_input}")

def practical_continue_examples():
    """실무에서 자주 사용되는 continue 예제"""
    print("\n=== 실무 continue 예제 ===")
    
    # 데이터 필터링
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("5보다 작은 수만 출력:")
    
    for num in numbers:
        if num >= 5:
            continue  # 5 이상은 건너뛰기
        print(f"  {num}")
    
    # 파일 처리 (가상의 예제)
    print("\n파일 처리 (빈 줄 건너뛰기):")
    lines = ["첫 번째 줄", "", "세 번째 줄", "", "다섯 번째 줄"]
    
    for line in lines:
        if not line.strip():  # 빈 줄이면 건너뛰기
            continue
        print(f"  처리된 줄: {line}")

def break_continue_with_else():
    """break/continue와 else 절"""
    print("\n=== break/continue와 else 절 ===")
    
    # for문의 else 절
    print("for문의 else 절:")
    for i in range(5):
        if i == 3:
            print(f"  {i}에서 break!")
            break
    else:
        print("  반복문이 정상적으로 완료되었습니다.")
    
    # break 없이 완료된 경우
    print("\nbreak 없이 완료:")
    for i in range(3):
        print(f"  {i}")
    else:
        print("  반복문이 정상적으로 완료되었습니다.")

def optimization_tips():
    """break/continue 최적화 팁"""
    print("\n=== break/continue 최적화 팁 ===")
    
    # 비효율적인 방법
    print("비효율적인 방법:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    
    print(f"  짝수들: {even_numbers}")
    
    # 효율적인 방법 (continue 사용)
    print("\n효율적인 방법 (continue 사용):")
    even_numbers = []
    
    for num in numbers:
        if num % 2 != 0:
            continue  # 홀수는 건너뛰기
        even_numbers.append(num)
    
    print(f"  짝수들: {even_numbers}")
    
    # 더 효율적인 방법 (리스트 컴프리헨션)
    print("\n더 효율적인 방법 (리스트 컴프리헨션):")
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"  짝수들: {even_numbers}")

def common_mistakes():
    """자주 하는 실수들"""
    print("\n=== 자주 하는 실수들 ===")
    
    # continue를 잘못 사용한 예
    print("continue를 잘못 사용한 예:")
    print("잘못된 코드:")
    print("  for i in range(5):")
    print("      if i == 2:")
    print("          continue")
    print("      print(i)")
    print("      i += 1  # 이 줄은 실행되지 않음!")
    
    print("\n올바른 코드:")
    for i in range(5):
        if i == 2:
            continue
        print(f"  {i}")
    
    # break를 잘못 사용한 예
    print("\nbreak를 잘못 사용한 예:")
    print("중첩 반복문에서 외부 반복문까지 종료하려면:")
    print("  플래그 변수나 함수를 사용해야 함")

if __name__ == "__main__":
    basic_break()
    basic_continue()
    break_in_nested_loops()
    continue_in_nested_loops()
    practical_break_examples()
    practical_continue_examples()
    break_continue_with_else()
    optimization_tips()
    common_mistakes()
