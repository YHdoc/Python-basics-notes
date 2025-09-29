"""
딕셔너리 컴프리헨션 패턴
효율적인 딕셔너리 생성과 변환 방법을 학습합니다.
"""

# TODO: 기본 딕셔너리 컴프리헨션
# numbers = [1, 2, 3, 4, 5]
# squares_dict = {x: x**2 for x in numbers}
# print("제곱 딕셔너리:", squares_dict)

# TODO: 조건이 있는 딕셔너리 컴프리헨션
# even_squares = {x: x**2 for x in numbers if x % 2 == 0}
# print("짝수의 제곱:", even_squares)

# TODO: 문자열 처리
# words = ["apple", "banana", "cherry", "date"]
# word_lengths = {word: len(word) for word in words}
# print("단어 길이:", word_lengths)

# TODO: 기존 딕셔너리 변환
# student_scores = {"김철수": 85, "이영희": 92, "박민수": 78, "최지영": 95}
# passed_students = {name: score for name, score in student_scores.items() if score >= 80}
# print("80점 이상 학생:", passed_students)

# TODO: 키와 값 교체
# original = {"a": 1, "b": 2, "c": 3}
# swapped = {value: key for key, value in original.items()}
# print("키-값 교체:", swapped)

# TODO: 중첩된 딕셔너리 처리
# data = {
#     "students": ["김철수", "이영희", "박민수"],
#     "scores": [85, 92, 78],
#     "grades": ["B", "A", "C"]
# }
# student_info = {name: {"score": score, "grade": grade} 
#                for name, score, grade in zip(data["students"], data["scores"], data["grades"])}
# print("학생 정보:", student_info)

# TODO: 파일 확장자별 그룹화
# files = ["document.pdf", "image.jpg", "script.py", "data.csv", "photo.png", "code.py"]
# file_groups = {}
# for file in files:
#     ext = file.split('.')[-1]
#     if ext not in file_groups:
#         file_groups[ext] = []
#     file_groups[ext].append(file)
# print("확장자별 파일:", file_groups)

# TODO: 컴프리헨션으로 파일 그룹화
# from collections import defaultdict
# file_groups = defaultdict(list)
# for file in files:
#     ext = file.split('.')[-1]
#     file_groups[ext].append(file)
# print("컴프리헨션 파일 그룹:", dict(file_groups))

# TODO: 카운팅 딕셔너리
# text = "hello world python programming"
# words = text.split()
# word_count = {word: words.count(word) for word in set(words)}
# print("단어 카운트:", word_count)

# TODO: 더 효율적인 카운팅 (Counter 사용)
# from collections import Counter
# word_count_counter = Counter(words)
# print("Counter 사용:", dict(word_count_counter))

# TODO: 데이터 정제와 변환
# raw_data = {
#     "  apple  ": 5,
#     "banana": 3,
#     "  cherry  ": 8,
#     "date": 2
# }
# cleaned_data = {key.strip().title(): value for key, value in raw_data.items()}
# print("정제된 데이터:", cleaned_data)

# TODO: 조건부 값 변환
# temperatures = {"서울": 25, "부산": 28, "대구": 30, "인천": 22}
# weather_status = {city: "더움" if temp > 27 else "시원함" for city, temp in temperatures.items()}
# print("날씨 상태:", weather_status)

# TODO: 복잡한 변환
# products = {
#     "laptop": {"price": 1000, "stock": 5},
#     "mouse": {"price": 20, "stock": 50},
#     "keyboard": {"price": 80, "stock": 10}
# }
# 
# # 재고가 10개 이상인 제품만 선택하고 가격에 세금 추가
# high_stock_products = {
#     name: {"price": info["price"] * 1.1, "stock": info["stock"]}
#     for name, info in products.items()
#     if info["stock"] >= 10
# }
# print("고재고 제품 (세금 포함):", high_stock_products)

if __name__ == "__main__":
    print("딕셔너리 컴프리헨션 패턴 예제를 실행합니다.")
    print("TODO 부분을 완성한 후 실행해보세요!")
