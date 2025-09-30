# 기본값 매개변수

def greet_with_default(name, greeting="안녕하세요"):
    """기본 인사말이 있는 함수"""
    print(f"{greeting}, {name}님!")

def create_message(title, content, author="관리자", priority="보통"):
    """메시지를 생성하는 함수"""
    message = f"[{priority}] {title}\n"
    message += f"내용: {content}\n"
    message += f"작성자: {author}"
    return message

def calculate_discount(price, discount_rate=0.1, tax_rate=0.1):
    """할인가를 계산하는 함수"""
    discounted_price = price * (1 - discount_rate)
    final_price = discounted_price * (1 + tax_rate)
    return final_price

def format_phone_number(number, country_code="+82", separator="-"):
    """전화번호를 포맷하는 함수"""
    if len(number) == 10:
        formatted = f"{number[:3]}{separator}{number[3:7]}{separator}{number[7:]}"
    else:
        formatted = number
    
    return f"{country_code} {formatted}"

def log_message(message, level="INFO", timestamp=None):
    """로그 메시지를 생성하는 함수"""
    import datetime
    
    if timestamp is None:
        timestamp = datetime.datetime.now()
    
    log_entry = f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {level}: {message}"
    return log_entry

if __name__ == "__main__":
    # 기본값 사용
    greet_with_default("김철수")
    greet_with_default("이영희", "좋은 아침")
    
    # 메시지 생성
    msg1 = create_message("회의 안내", "내일 오후 2시 회의가 있습니다.")
    msg2 = create_message("긴급 공지", "시스템 점검이 있습니다.", "시스템관리자", "긴급")
    print(msg1)
    print("\n" + msg2)
    
    # 할인가 계산
    price1 = calculate_discount(10000)
    price2 = calculate_discount(10000, 0.2)
    price3 = calculate_discount(10000, 0.15, 0.05)
    print(f"할인가: {price1:.0f}원, {price2:.0f}원, {price3:.0f}원")
    
    # 전화번호 포맷
    phone1 = format_phone_number("01012345678")
    phone2 = format_phone_number("01012345678", "+1", ".")
    print(f"전화번호: {phone1}, {phone2}")
    
    # 로그 메시지
    log1 = log_message("시스템 시작")
    log2 = log_message("오류 발생", "ERROR")
    print(log1)
    print(log2)
