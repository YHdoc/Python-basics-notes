# 문자열 포맷팅 방법들

def f_string_examples():
    """f-string 예제 (Python 3.6+)"""
    print("=== f-string 예제 ===")
    
    name = "김철수"
    age = 25
    height = 175.5
    score = 95.5
    
    # 기본 사용법
    print(f"이름: {name}, 나이: {age}")
    
    # 표현식 사용
    print(f"내년 나이: {age + 1}")
    print(f"키(cm): {height}, 키(m): {height/100}")
    
    # 포맷 지정
    print(f"점수: {score:.1f}점")
    print(f"백분율: {score:.1%}")
    
    # 정렬
    print(f"이름: {name:>10}") # '        김철수'  (앞에 공백)
    print(f"나이: {age:<10}") # '25          ' (뒤에 공백)
    print(f"점수: {score:^10.1f}") # '    95.5     ' (중앙 정렬, 10칸 중 앞뒤로 균등 분배)

def format_method_examples():
    """format() 메서드 예제"""
    print("\n=== format() 메서드 예제 ===")
    
    name = "이영희"
    age = 30
    height = 165.2
    
    # 위치 기반
    print("이름: {}, 나이: {}, 키: {}cm".format(name, age, height))
    
    # 인덱스 기반
    print("이름: {0}, 나이: {1}, 키: {2}cm".format(name, age, height))
    print("키: {2}cm, 나이: {1}세, 이름: {0}".format(name, age, height))
    
    # 키워드 기반
    print("이름: {name}, 나이: {age}, 키: {height}cm".format(
        name=name, age=age, height=height))
    
    # 포맷 지정
    print("키: {height:.1f}cm".format(height=height))
    print("나이: {age:03d}세".format(age=age)) #0 : 빈 자리를 0으로 채움 / 3 : 전체 출력 폭을 3자리로 맞춤 / d : 정수를 10진수(decimal)로 출력 / 나이가 5라면 "005" 로 출력

def percent_formatting():
    """% 포맷팅 예제 (구식)"""
    print("\n=== % 포맷팅 예제 ===")
    
    name = "박민수"
    age = 28
    height = 180.5
    score = 88.7
    
    # 기본 사용법
    print("이름: %s, 나이: %d, 키: %.1fcm" % (name, age, height))
    
    # 포맷 지정자
    print("점수: %.1f점" % score)
    print("백분율: %.1f%%" % (score))
    
    # 정렬과 패딩
    print("이름: %10s" % name) #%s → 문자열(string) 출력 / 10 → 출력 폭(width)을 최소 10칸으로 맞춤
    print("나이: %05d세" % age)

def advanced_formatting():
    """고급 포맷팅 예제"""
    print("\n=== 고급 포맷팅 ===")
    
    # 숫자 포맷팅
    number = 1234567.89
    
    print(f"천 단위 구분: {number:,}")
    print(f"소수점 2자리: {number:.2f}")
    print(f"과학적 표기: {number:.2e}") # .2 → 소수점 아래 2자리까지 표시
    print(f"백분율: {number/10000:.1%}")
    
    # 날짜/시간 포맷팅
    import datetime
    now = datetime.datetime.now()
    
    print(f"현재 시간: {now:%Y-%m-%d %H:%M:%S}")
    print(f"날짜만: {now:%Y년 %m월 %d일}")
    
    # 진수 변환
    num = 255
    print(f"10진수: {num}")     # 어원 ㅇㅇ
    print(f"16진수: {num:x}")   # hexadecimal 
    print(f"8진수: {num:o}")    # octal
    print(f"2진수: {num:b}")    # binary 

def practical_formatting():
    """실무에서 자주 사용되는 포맷팅"""
    print("\n=== 실무 포맷팅 예제 ===")
    
    # 로그 메시지
    timestamp = "2024-01-15 14:30:25"
    level = "INFO"
    message = "사용자 로그인 성공"
    user_id = "user123"
    
    log_message = f"[{timestamp}] {level:5} - {message} (User: {user_id})" # {level:5} 의 :5 는 출력 폭(width)을 최소 5칸으로 맞추라는 의미
    print(log_message)
    
    # 금액 표시
    price = 1234567
    print(f"가격: {price:,}원")
    print(f"가격: {price:,.0f}원")
    
    # 진행률 표시
    current = 45
    total = 100
    percentage = (current / total) * 100
    print(f"진행률: {current}/{total} ({percentage:.1f}%)")
    
    # 테이블 형태 출력
    products = [
        ("노트북", 1500000, 5),
        ("마우스", 25000, 20),
        ("키보드", 80000, 15)
    ]
    
    print(f"{'상품명':<10} {'가격':>10} {'수량':>5}")
    print("-" * 30)
    for name, price, quantity in products:
        print(f"{name:<10} {price:>10,}원 {quantity:>5}개")

def template_strings():
    """템플릿 문자열 예제"""
    print("\n=== 템플릿 문자열 ===")
    
    # from 모듈 import 클래스/함수 : 특정 클래스나 함수를 현재 네임스페이스에 직접 가져옴
    # C#의 using 문과 비슷하게 보이지만 동작 방식은 조금 차이가 있다
    # import string 만 하는 것과 달리 이름을 좀더 짧게 쓸 수 있다 → string.Template("그냥 import") VS Template("from 모듈 import 클래스")
    # 그리고 함수 안에서 import가 가능한데, 이 경우 모듈이 최초 1번만 로딩되고 (전역 import와 동일) 
    # 단, 네임스페이스에 바인딩은 해당 함수 실행 시점에서만 이루어진다.
    # 실제로 코드가 실행될 때 네임스페이스에 객체를 바인딩한다고(파이썬이 런타임이라 그럼). C#은 컴파일할때.
    from string import Template 
    
    # Template 클래스 사용
    template = Template("안녕하세요, $name님! $age세이시군요.")
    message = template.substitute(name="김철수", age=25)
    print(message)
    
    # f-string과 비교
    name = "김철수"
    age = 25
    message = f"안녕하세요, {name}님! {age}세이시군요."
    print(message)

if __name__ == "__main__":
    f_string_examples()
    format_method_examples()
    percent_formatting()
    advanced_formatting()
    practical_formatting()
    template_strings()
