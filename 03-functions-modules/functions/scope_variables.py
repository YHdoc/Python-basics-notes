# 변수 스코프

# 전역 변수
global_var = "전역 변수"

def demonstrate_scope():
    """변수 스코프를 보여주는 함수"""
    # 지역 변수
    local_var = "지역 변수"
    
    print(f"함수 내부 - 전역 변수: {global_var}")
    print(f"함수 내부 - 지역 변수: {local_var}")
    
    def inner_function():
        """내부 함수"""
        inner_var = "내부 함수 변수"
        print(f"내부 함수 - 전역 변수: {global_var}")
        print(f"내부 함수 - 지역 변수: {local_var}")
        print(f"내부 함수 - 내부 변수: {inner_var}")
    
    inner_function()

def modify_global_variable():
    """전역 변수를 수정하는 함수"""
    global global_var
    global_var = "수정된 전역 변수"
    print(f"전역 변수 수정: {global_var}")

def variable_shadowing():
    """변수 섀도잉을 보여주는 함수"""
    shadow_var = "지역 변수"
    print(f"지역 변수: {shadow_var}")
    
    def inner():
        shadow_var = "내부 함수 변수"
        print(f"내부 함수 변수: {shadow_var}")
    
    inner()
    print(f"지역 변수 (변경되지 않음): {shadow_var}")

def nonlocal_example():
    """nonlocal 키워드 사용 예제"""
    outer_var = "외부 함수 변수"
    
    def inner():
        nonlocal outer_var
        outer_var = "내부 함수에서 수정"
        print(f"내부 함수에서 수정: {outer_var}")
    
    print(f"수정 전: {outer_var}")
    inner()
    print(f"수정 후: {outer_var}")

def closure_example():
    """클로저 예제"""
    def create_multiplier(factor):
        def multiplier(number):
            return number * factor
        return multiplier
    
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"2 * 5 = {double(5)}")
    print(f"3 * 5 = {triple(5)}")

def scope_chain_example():
    """스코프 체인 예제"""
    level1 = "레벨 1"
    
    def level2_function():
        level2 = "레벨 2"
        
        def level3_function():
            level3 = "레벨 3"
            print(f"레벨 3에서 접근 가능한 변수들:")
            print(f"  level1: {level1}")
            print(f"  level2: {level2}")
            print(f"  level3: {level3}")
        
        level3_function()
    
    level2_function()

if __name__ == "__main__":
    print("=== 변수 스코프 예제 ===")
    
    print(f"전역에서 - 전역 변수: {global_var}")
    
    demonstrate_scope()
    
    print("\n=== 전역 변수 수정 ===")
    modify_global_variable()
    print(f"전역에서 - 수정된 전역 변수: {global_var}")
    
    print("\n=== 변수 섀도잉 ===")
    variable_shadowing()
    
    print("\n=== nonlocal 키워드 ===")
    nonlocal_example()
    
    print("\n=== 클로저 ===")
    closure_example()
    
    print("\n=== 스코프 체인 ===")
    scope_chain_example()
