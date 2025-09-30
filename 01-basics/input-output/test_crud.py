# CRUD 테스트 파일

import os

def test_crud():
    """CRUD 테스트"""
    print("=== CRUD 테스트 시작 ===")
    
    # samplefile 디렉토리 확인 및 생성
    samplefile_dir = "samplefile"
    if not os.path.exists(samplefile_dir):
        os.makedirs(samplefile_dir)
        print(f"'{samplefile_dir}' 디렉토리를 생성했습니다.")
    
    # 파일 경로
    file_path = os.path.join(samplefile_dir, "test.txt")
    
    # CREATE - 파일 생성
    print("1. 파일 생성 (CREATE)")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("안녕하세요!\n")
        file.write("CRUD 테스트 파일입니다.\n")
    print(f"파일 생성 완료: {file_path}")
    
    # READ - 파일 읽기
    print("\n2. 파일 읽기 (READ)")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("파일 내용:")
        print(content)
    
    # UPDATE - 파일 수정
    print("3. 파일 수정 (UPDATE)")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("추가된 내용입니다.\n")
    
    # 다시 읽기
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("수정된 파일 내용:")
        print(content)
    
    # DELETE - 파일 삭제
    print("\n4. 파일 삭제 (DELETE)")
    os.remove(file_path)
    print(f"파일 삭제 완료: {file_path}")
    
    # 파일 존재 확인
    if os.path.exists(file_path):
        print("파일이 여전히 존재합니다.")
    else:
        print("파일이 성공적으로 삭제되었습니다.")
    
    print("\n=== CRUD 테스트 완료 ===")

if __name__ == "__main__":
    test_crud()
