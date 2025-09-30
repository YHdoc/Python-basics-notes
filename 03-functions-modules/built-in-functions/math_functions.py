# 수학 관련 함수들

def demonstrate_math_functions():
    """수학 관련 함수들을 보여주는 함수"""
    print("=== 수학 관련 함수들 ===")
    
    # abs 함수
    print(f"abs(-5): {abs(-5)}")
    print(f"abs(3.14): {abs(3.14)}")
    print(f"abs(-2.5): {abs(-2.5)}")
    
    # round 함수
    print(f"round(3.14159): {round(3.14159)}")
    print(f"round(3.14159, 2): {round(3.14159, 2)}")
    print(f"round(3.14159, 3): {round(3.14159, 3)}")
    
    # min 함수
    print(f"min(1, 5, 3, 9, 2): {min(1, 5, 3, 9, 2)}")
    print(f"min([10, 5, 8, 3, 7]): {min([10, 5, 8, 3, 7])}")
    print(f"min('hello'): {min('hello')}")
    
    # max 함수
    print(f"max(1, 5, 3, 9, 2): {max(1, 5, 3, 9, 2)}")
    print(f"max([10, 5, 8, 3, 7]): {max([10, 5, 8, 3, 7])}")
    print(f"max('hello'): {max('hello')}")
    
    # sum 함수
    print(f"sum([1, 2, 3, 4, 5]): {sum([1, 2, 3, 4, 5])}")
    print(f"sum(range(10)): {sum(range(10))}")
    
    # pow 함수
    print(f"pow(2, 3): {pow(2, 3)}")
    print(f"pow(2, 3, 5): {pow(2, 3, 5)}")  # 2^3 mod 5
    print(f"2 ** 3: {2 ** 3}")  # 동일한 결과

def demonstrate_advanced_math():
    """고급 수학 함수들을 보여주는 함수"""
    print("\n=== 고급 수학 함수들 ===")
    
    # divmod 함수
    quotient, remainder = divmod(17, 5)
    print(f"divmod(17, 5): quotient={quotient}, remainder={remainder}")
    
    # bin, oct, hex 함수
    number = 255
    print(f"bin(255): {bin(number)}")
    print(f"oct(255): {oct(number)}")
    print(f"hex(255): {hex(number)}")
    
    # ord, chr 함수
    print(f"ord('A'): {ord('A')}")
    print(f"chr(65): {chr(65)}")
    print(f"ord('가'): {ord('가')}")
    print(f"chr(44032): {chr(44032)}")

def demonstrate_math_with_collections():
    """컬렉션과 함께 사용하는 수학 함수들"""
    print("\n=== 컬렉션과 함께 사용하는 수학 함수들 ===")
    
    # 리스트의 통계
    numbers = [85, 92, 78, 96, 88, 91, 75, 83, 90, 87]
    print(f"점수들: {numbers}")
    print(f"총점: {sum(numbers)}")
    print(f"평균: {sum(numbers) / len(numbers):.1f}")
    print(f"최고점: {max(numbers)}")
    print(f"최저점: {min(numbers)}")
    
    # 딕셔너리의 값들로 계산
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}
    print(f"학생 점수: {scores}")
    print(f"평균 점수: {sum(scores.values()) / len(scores):.1f}")
    print(f"최고 점수: {max(scores.values())}")
    print(f"최저 점수: {min(scores.values())}")
    
    # 최고/최저 점수를 받은 학생
    max_score = max(scores.values())
    min_score = min(scores.values())
    max_student = [name for name, score in scores.items() if score == max_score]
    min_student = [name for name, score in scores.items() if score == min_score]
    print(f"최고 점수 학생: {max_student}")
    print(f"최저 점수 학생: {min_student}")

if __name__ == "__main__":
    demonstrate_math_functions()
    demonstrate_advanced_math()
    demonstrate_math_with_collections()
