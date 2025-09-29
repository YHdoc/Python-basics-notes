"""
리스트 컴프리헨션 패턴
간결하고 효율적인 리스트 생성 방법을 학습합니다.
"""

# TODO: 기본 리스트 컴프리헨션
# numbers = [1, 2, 3, 4, 5]
# squares = [x**2 for x in numbers]
# print("제곱수:", squares)

# TODO: 조건이 있는 리스트 컴프리헨션
# even_squares = [x**2 for x in numbers if x % 2 == 0]
# print("짝수의 제곱:", even_squares)

# TODO: 문자열 리스트 처리
# words = ["hello", "world", "python", "programming"]
# upper_words = [word.upper() for word in words]
# print("대문자 변환:", upper_words)

# TODO: 길이가 5 이상인 단어만 필터링
# long_words = [word for word in words if len(word) >= 5]
# print("긴 단어들:", long_words)

# TODO: 중첩된 리스트 컴프리헨션
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [num for row in matrix for num in row]
# print("평면화된 리스트:", flattened)

# TODO: 딕셔너리에서 리스트 생성
# student_scores = {"김철수": 85, "이영희": 92, "박민수": 78}
# high_scores = [name for name, score in student_scores.items() if score >= 80]
# print("80점 이상 학생:", high_scores)

# TODO: 파일명에서 확장자 추출
# filenames = ["document.pdf", "image.jpg", "script.py", "data.csv"]
# extensions = [filename.split('.')[-1] for filename in filenames]
# print("확장자들:", extensions)

# TODO: 숫자 범위에서 조건부 리스트 생성
# multiples_of_3 = [x for x in range(1, 21) if x % 3 == 0]
# print("3의 배수:", multiples_of_3)

# TODO: 복잡한 조건
# numbers = range(1, 11)
# result = [x**2 if x % 2 == 0 else x**3 for x in numbers]
# print("짝수는 제곱, 홀수는 세제곱:", result)

# TODO: 문자열 처리 - 단어 길이별 분류
# text = "Python is a great programming language"
# words = text.split()
# word_lengths = {len(word): [w for w in words if len(w) == len(word)] for word in words}
# print("길이별 단어 분류:", word_lengths)

# TODO: 실무 예제 - 데이터 정제
# raw_data = ["  apple  ", "banana", "  cherry  ", "date", "  elderberry  "]
# cleaned_data = [item.strip().title() for item in raw_data if len(item.strip()) > 3]
# print("정제된 데이터:", cleaned_data)

# TODO: 성능 비교 (일반적인 방법 vs 컴프리헨션)
# # 일반적인 방법
# squares_normal = []
# for x in range(1000):
#     squares_normal.append(x**2)

# # 컴프리헨션 방법
# squares_comprehension = [x**2 for x in range(1000)]

# print("일반 방법 결과 개수:", len(squares_normal))
# print("컴프리헨션 결과 개수:", len(squares_comprehension))

if __name__ == "__main__":
    print("리스트 컴프리헨션 패턴 예제를 실행합니다.")
    print("TODO 부분을 완성한 후 실행해보세요!")
