# 파일 입출력 기초

import os

def ensure_samplefile_directory():
    """samplefile 디렉토리 존재 확인 및 생성"""
    samplefile_dir = "samplefile"
    if not os.path.exists(samplefile_dir):
        os.makedirs(samplefile_dir)
        print(f"'{samplefile_dir}' 디렉토리를 생성했습니다.")
    return samplefile_dir

def basic_file_operations():
    """기본 파일 입출력"""
    print("=== 기본 파일 입출력 ===")
    
    # samplefile 디렉토리 확인
    samplefile_dir = ensure_samplefile_directory()
    file_path = os.path.join(samplefile_dir, "sample.txt")
    
    # 파일 쓰기
    with open(file_path, "w", encoding="utf-8") as file:  # 모드가 'w' 일 경우, 파일이 없으면 새로 생성하고 있으면 기존 내용을 모두 지우고 덮어씌운다
        file.write("안녕하세요!\n")
        file.write("Python 파일 입출력 예제입니다.\n")
        file.write("한글도 잘 저장됩니다.\n")
    
    print(f"파일 쓰기 완료: {file_path}")
    
    # 파일 읽기
    with open(file_path, "r", encoding="utf-8") as file: # 'r' 일 경우, 파일이 없으면 에러 발생
        content = file.read()
        print("파일 내용:")
        print(content)
    
    # 파일 삭제
    os.remove(file_path)
    print(f"파일 삭제 완료: {file_path}")

def line_by_line_operations():
    """줄 단위 파일 처리"""
    print("\n=== 줄 단위 파일 처리 ===")
    
    # samplefile 디렉토리 확인
    samplefile_dir = ensure_samplefile_directory()
    file_path = os.path.join(samplefile_dir, "lines.txt")
    
    # 여러 줄 쓰기
    lines = [
        "첫 번째 줄",
        "두 번째 줄", 
        "세 번째 줄",
        "마지막 줄"
    ]
    
    with open(file_path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")
    
    print(f"여러 줄 파일 쓰기 완료: {file_path}")
    
    # 줄 단위로 읽기
    with open(file_path, "r", encoding="utf-8") as file:
        print("파일 내용 (줄 단위):")
        for i, line in enumerate(file, 1):
            print(f"{i}: {line.strip()}")
    
    # 모든 줄을 리스트로 읽기
    with open(file_path, "r", encoding="utf-8") as file:
        all_lines = file.readlines()
        print(f"\n총 {len(all_lines)}줄 읽음")
    
    # 파일 삭제
    os.remove(file_path)
    print(f"파일 삭제 완료: {file_path}")

def csv_file_example():
    """CSV 파일 예제"""
    print("\n=== CSV 파일 예제 ===")
    
    # samplefile 디렉토리 확인
    samplefile_dir = ensure_samplefile_directory()
    file_path = os.path.join(samplefile_dir, "users.csv")
    
    # CSV 파일 쓰기
    import csv
    
    data = [
        ["이름", "나이", "직업"],
        ["김철수", "25", "개발자"],
        ["이영희", "30", "디자이너"],
        ["박민수", "28", "기획자"]
    ]
    
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    print(f"CSV 파일 쓰기 완료: {file_path}")
    
    # CSV 파일 읽기
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        print("CSV 파일 내용:")
        for row in reader:
            print(f"{row[0]:<8} {row[1]:<5} {row[2]}")
    
    # 파일 삭제
    os.remove(file_path)
    print(f"파일 삭제 완료: {file_path}")

def json_file_example():
    """JSON 파일 예제"""
    print("\n=== JSON 파일 예제 ===")
    
    # samplefile 디렉토리 확인
    samplefile_dir = ensure_samplefile_directory()
    file_path = os.path.join(samplefile_dir, "user.json")
    
    import json
    
    # JSON 데이터
    user_data = {
        "name": "김철수",
        "age": 25,
        "hobbies": ["독서", "영화감상", "프로그래밍"],
        "address": {
            "city": "서울",
            "district": "강남구"
        }
    }
    
    # JSON 파일 쓰기
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(user_data, file, ensure_ascii=False, indent=2)
    
    print(f"JSON 파일 쓰기 완료: {file_path}")
    
    # JSON 파일 읽기
    with open(file_path, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        print("JSON 파일 내용:")
        print(f"이름: {loaded_data['name']}")
        print(f"나이: {loaded_data['age']}")
        print(f"취미: {', '.join(loaded_data['hobbies'])}")
        print(f"주소: {loaded_data['address']['city']} {loaded_data['address']['district']}")
    
    # 파일 삭제
    os.remove(file_path)
    print(f"파일 삭제 완료: {file_path}")

def file_modes():
    """파일 모드 예제"""
    print("\n=== 파일 모드 ===")
    
    # samplefile 디렉토리 확인
    samplefile_dir = ensure_samplefile_directory()
    file_path = os.path.join(samplefile_dir, "modes_test.txt")
    
    # 쓰기 모드 (w) - 파일이 있으면 덮어쓰기
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("첫 번째 내용\n")
    
    # 추가 모드 (a) - 파일 끝에 추가
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("추가된 내용\n")
    
    # 읽기 모드 (r) - 파일 읽기
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("파일 내용:")
        print(content)
    
    # 읽기+쓰기 모드 (r+) - 읽기와 쓰기 모두 가능
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.read()
        file.write("읽기+쓰기 모드로 추가\n")
    
    # 파일 삭제
    os.remove(file_path)
    print(f"파일 삭제 완료: {file_path}")

def error_handling():
    """파일 입출력 에러 처리"""
    print("\n=== 에러 처리 ===")
    
    # samplefile 디렉토리 확인
    samplefile_dir = ensure_samplefile_directory()
    nonexistent_file = os.path.join(samplefile_dir, "nonexistent.txt")
    test_file = os.path.join(samplefile_dir, "test_file.txt")
    
    # 존재하지 않는 파일 읽기
    try:
        with open(nonexistent_file, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {nonexistent_file}")
    except PermissionError:
        print("파일 접근 권한이 없습니다.")
    except Exception as e:
        print(f"예상치 못한 오류: {e}")
    
    # 파일 존재 여부 확인
    if os.path.exists(test_file):
        print(f"{test_file} 파일이 존재합니다.")
    else:
        print(f"{test_file} 파일이 존재하지 않습니다.")
    
    # 테스트 파일 생성 및 확인
    with open(test_file, "w", encoding="utf-8") as file:
        file.write("테스트 파일입니다.")
    
    if os.path.exists(test_file):
        print(f"{test_file} 파일이 생성되었습니다.")
        os.remove(test_file)
        print(f"{test_file} 파일이 삭제되었습니다.")

if __name__ == "__main__":
    basic_file_operations()
    line_by_line_operations()
    csv_file_example()
    json_file_example()
    file_modes()
    error_handling()
