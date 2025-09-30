# 람다 함수

# 기본 람다 함수
add = lambda x, y: x + y
multiply = lambda x, y: x * y
square = lambda x: x ** 2

# 조건부 람다 함수
is_even = lambda x: x % 2 == 0
is_positive = lambda x: x > 0
get_grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"

# 문자열 처리 람다 함수
upper_case = lambda s: s.upper()
lower_case = lambda s: s.lower()
reverse_string = lambda s: s[::-1]

# 리스트 처리 람다 함수
double_list = lambda lst: [x * 2 for x in lst]
filter_positive = lambda lst: list(filter(lambda x: x > 0, lst))
sort_by_length = lambda lst: sorted(lst, key=lambda x: len(x))

# 딕셔너리 처리 람다 함수
get_values = lambda d: list(d.values())
get_keys = lambda d: list(d.keys())
sort_dict_by_value = lambda d: sorted(d.items(), key=lambda x: x[1])

if __name__ == "__main__":
    print("=== 기본 람다 함수 ===")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"4 * 7 = {multiply(4, 7)}")
    print(f"6의 제곱 = {square(6)}")
    
    print("\n=== 조건부 람다 함수 ===")
    print(f"8은 짝수인가? {is_even(8)}")
    print(f"7은 짝수인가? {is_even(7)}")
    print(f"5는 양수인가? {is_positive(5)}")
    print(f"-3은 양수인가? {is_positive(-3)}")
    print(f"85점의 등급: {get_grade(85)}")
    print(f"95점의 등급: {get_grade(95)}")
    
    print("\n=== 문자열 처리 람다 함수 ===")
    text = "Hello World"
    print(f"원본: {text}")
    print(f"대문자: {upper_case(text)}")
    print(f"소문자: {lower_case(text)}")
    print(f"역순: {reverse_string(text)}")
    
    print("\n=== 리스트 처리 람다 함수 ===")
    numbers = [1, 2, 3, 4, 5]
    print(f"원본: {numbers}")
    print(f"2배: {double_list(numbers)}")
    print(f"양수만: {filter_positive([1, -2, 3, -4, 5])}")
    
    words = ["apple", "banana", "cherry", "date"]
    print(f"원본: {words}")
    print(f"길이순 정렬: {sort_by_length(words)}")
    
    print("\n=== 딕셔너리 처리 람다 함수 ===")
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
    print(f"원본: {scores}")
    print(f"키들: {get_keys(scores)}")
    print(f"값들: {get_values(scores)}")
    print(f"값순 정렬: {sort_dict_by_value(scores)}")
