# 기본 파일 입출력

def demonstrate_basic_file_operations():
    """기본 파일 입출력 방법들을 보여주는 함수"""
    print("=== 기본 파일 입출력 ===")
    
    # 파일 쓰기
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write("Hello, World!\n")
        file.write("This is a sample file.\n")
        file.write("Python file I/O example.\n")
    
    print("파일 쓰기 완료!")
    
    # 파일 읽기
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(f"파일 내용:\n{content}")
    
    # 줄 단위로 읽기
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(f"줄 단위 읽기: {lines}")
    
    # 파일 삭제
    import os
    os.remove("sample.txt")
    print("파일 삭제 완료!")

if __name__ == "__main__":
    demonstrate_basic_file_operations()
