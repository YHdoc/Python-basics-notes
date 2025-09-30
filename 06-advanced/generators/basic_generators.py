# 기본 제너레이터

def count_up_to(max_count):
    """기본 제너레이터 예제"""
    count = 1
    while count <= max_count:
        yield count
        count += 1

if __name__ == "__main__":
    counter = count_up_to(5)
    for num in counter:
        print(num)
