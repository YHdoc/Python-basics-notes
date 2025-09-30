# 리스트와 튜플 비교

def demonstrate_differences():
    """리스트와 튜플의 차이점을 보여주는 함수"""
    print("=== 리스트 vs 튜플 ===")
    
    # 생성
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)
    print(f"리스트: {my_list}")
    print(f"튜플: {my_tuple}")
    
    # 수정 가능성
    my_list[0] = 10  # 가능
    print(f"리스트 수정 후: {my_list}")
    
    # my_tuple[0] = 10  # 불가능 (에러 발생)
    print("튜플은 수정할 수 없습니다.")

if __name__ == "__main__":
    demonstrate_differences()
