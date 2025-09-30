# 튜플 언패킹과 패킹

def demonstrate_tuple_unpacking():
    """튜플 언패킹을 보여주는 함수"""
    print("=== 튜플 언패킹 ===")
    
    # 기본 언패킹
    coordinates = (10, 20)
    x, y = coordinates
    print(f"좌표: {coordinates}")
    print(f"x: {x}, y: {y}")
    
    # 여러 값 언패킹
    rgb = (255, 128, 64)
    red, green, blue = rgb
    print(f"RGB: {rgb}")
    print(f"Red: {red}, Green: {green}, Blue: {blue}")
    
    # 함수에서 여러 값 반환
    def get_min_max(numbers):
        return min(numbers), max(numbers)
    
    data = [1, 5, 3, 9, 2, 8]
    min_val, max_val = get_min_max(data)
    print(f"데이터: {data}")
    print(f"최솟값: {min_val}, 최댓값: {max_val}")

if __name__ == "__main__":
    demonstrate_tuple_unpacking()
