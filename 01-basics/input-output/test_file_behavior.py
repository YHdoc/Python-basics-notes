# Python 파일 처리 동작 테스트

import os

def test_file_behavior():
    """파일 처리 동작 테스트"""
    print("=== Python 파일 처리 동작 테스트 ===")
    
    # samplefile 디렉토리 확인
    samplefile_dir = "samplefile"
    if not os.path.exists(samplefile_dir):
        os.makedirs(samplefile_dir)
        print(f"'{samplefile_dir}' 디렉토리를 생성했습니다.")
    
    test_file = os.path.join(samplefile_dir, "behavior_test.txt")
    
    # 1. 존재하지 않는 파일에 쓰기 (w 모드)
    print("\n1. 존재하지 않는 파일에 쓰기 (w 모드)")
    print(f"파일 존재 여부: {os.path.exists(test_file)}")
    
    with open(test_file, "w", encoding="utf-8") as file:
        file.write("첫 번째 내용\n")
    
    print(f"파일 생성 후 존재 여부: {os.path.exists(test_file)}")
    
    # 2. 존재하는 파일에 쓰기 (w 모드) - 덮어쓰기
    print("\n2. 존재하는 파일에 쓰기 (w 모드) - 덮어쓰기")
    with open(test_file, "w", encoding="utf-8") as file:
        file.write("두 번째 내용 (덮어쓰기)\n")
    
    # 내용 확인
    with open(test_file, "r", encoding="utf-8") as file:
        content = file.read()
        print(f"덮어쓰기 후 내용: {content.strip()}")
    
    # 3. 존재하는 파일에 추가 (a 모드)
    print("\n3. 존재하는 파일에 추가 (a 모드)")
    with open(test_file, "a", encoding="utf-8") as file:
        file.write("추가된 내용\n")
    
    # 내용 확인
    with open(test_file, "r", encoding="utf-8") as file:
        content = file.read()
        print(f"추가 후 내용:\n{content}")
    
    # 4. 존재하지 않는 파일 읽기 시도
    print("\n4. 존재하지 않는 파일 읽기 시도")
    nonexistent_file = os.path.join(samplefile_dir, "nonexistent.txt")
    try:
        with open(nonexistent_file, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"예상된 오류: {e}")
    
    # 5. 파일 삭제
    print("\n5. 파일 삭제")
    os.remove(test_file)
    print(f"파일 삭제 후 존재 여부: {os.path.exists(test_file)}")
    
    print("\n=== 테스트 완료 ===")

if __name__ == "__main__":
    test_file_behavior()
