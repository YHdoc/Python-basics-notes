# 실무에서 자주 사용되는 예외 처리 패턴

import json
import os
import time
from typing import Optional, Dict, Any

def demonstrate_file_operations():
    """파일 작업 예외 처리 패턴"""
    print("=== 파일 작업 예외 처리 ===")
    
    def safe_read_file(file_path: str) -> Optional[str]:
        """안전한 파일 읽기"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file_path}")
            return None
        except PermissionError:
            print(f"파일 읽기 권한이 없습니다: {file_path}")
            return None
        except UnicodeDecodeError as e:
            print(f"파일 인코딩 오류: {e}")
            return None
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return None
    
    def safe_write_file(file_path: str, content: str) -> bool:
        """안전한 파일 쓰기"""
        try:
            # 디렉토리가 없으면 생성
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
        except PermissionError:
            print(f"파일 쓰기 권한이 없습니다: {file_path}")
            return False
        except OSError as e:
            print(f"파일 시스템 오류: {e}")
            return False
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return False
    
    # 테스트
    test_files = [
        "existing_file.txt",
        "nonexistent_file.txt",
        "/root/restricted_file.txt",  # 권한 오류 시뮬레이션
    ]
    
    for file_path in test_files:
        content = safe_read_file(file_path)
        if content:
            print(f"파일 읽기 성공: {file_path}")
        else:
            print(f"파일 읽기 실패: {file_path}")
    
    # 파일 쓰기 테스트
    success = safe_write_file("test_output.txt", "테스트 내용")
    print(f"파일 쓰기 결과: {'성공' if success else '실패'}")

def demonstrate_json_handling():
    """JSON 처리 예외 처리 패턴"""
    print("\n=== JSON 처리 예외 처리 ===")
    
    def safe_load_json(json_string: str) -> Optional[Dict[str, Any]]:
        """안전한 JSON 로딩"""
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            print(f"JSON 파싱 오류: {e}")
            print(f"오류 위치: 라인 {e.lineno}, 컬럼 {e.colno}")
            return None
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return None
    
    def safe_dump_json(data: Any, file_path: str) -> bool:
        """안전한 JSON 저장"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            return True
        except TypeError as e:
            print(f"JSON 직렬화 불가능한 타입: {e}")
            return False
        except OSError as e:
            print(f"파일 저장 오류: {e}")
            return False
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return False
    
    # 테스트
    test_json_strings = [
        '{"name": "김철수", "age": 30}',  # 유효한 JSON
        '{"name": "이영희", "age": 25,}',  # 잘못된 JSON (trailing comma)
        '{"name": "박민수", "age": 35',    # 잘못된 JSON (닫는 괄호 없음)
        'not json at all',                 # JSON이 아님
    ]
    
    for json_str in test_json_strings:
        data = safe_load_json(json_str)
        if data:
            print(f"JSON 로딩 성공: {data}")
        else:
            print(f"JSON 로딩 실패: {json_str[:30]}...")
    
    # JSON 저장 테스트
    test_data = {"users": [{"name": "김철수", "age": 30}]}
    success = safe_dump_json(test_data, "test_data.json")
    print(f"JSON 저장 결과: {'성공' if success else '실패'}")

def demonstrate_network_operations():
    """네트워크 작업 예외 처리 패턴"""
    print("\n=== 네트워크 작업 예외 처리 ===")
    
    def safe_http_request(url: str, timeout: int = 10) -> Optional[Dict[str, Any]]:
        """안전한 HTTP 요청"""
        try:
            import urllib.request
            import urllib.error
            
            with urllib.request.urlopen(url, timeout=timeout) as response:
                if response.status == 200:
                    data = response.read().decode('utf-8')
                    return {"status": response.status, "data": data}
                else:
                    print(f"HTTP 오류: {response.status}")
                    return None
                    
        except urllib.error.URLError as e:
            print(f"URL 오류: {e}")
            return None
        except urllib.error.HTTPError as e:
            print(f"HTTP 오류: {e.code} - {e.reason}")
            return None
        except TimeoutError:
            print(f"요청 시간 초과: {timeout}초")
            return None
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return None
    
    def safe_download_file(url: str, file_path: str) -> bool:
        """안전한 파일 다운로드"""
        try:
            import urllib.request
            
            with urllib.request.urlopen(url) as response:
                with open(file_path, 'wb') as file:
                    file.write(response.read())
            return True
            
        except urllib.error.URLError as e:
            print(f"다운로드 URL 오류: {e}")
            return False
        except OSError as e:
            print(f"파일 저장 오류: {e}")
            return False
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return False
    
    # 테스트 (실제로는 작동하지 않을 수 있음)
    test_urls = [
        "https://httpbin.org/json",  # 유효한 URL
        "https://nonexistent-domain.com",  # 존재하지 않는 도메인
        "https://httpbin.org/status/404",  # 404 오류
    ]
    
    for url in test_urls:
        result = safe_http_request(url)
        if result:
            print(f"HTTP 요청 성공: {url}")
        else:
            print(f"HTTP 요청 실패: {url}")

def demonstrate_database_operations():
    """데이터베이스 작업 예외 처리 패턴"""
    print("\n=== 데이터베이스 작업 예외 처리 ===")
    
    class DatabaseConnection:
        def __init__(self):
            self.connected = False
        
        def connect(self):
            # 연결 시뮬레이션
            if not self.connected:
                self.connected = True
                print("데이터베이스 연결 성공")
        
        def disconnect(self):
            if self.connected:
                self.connected = False
                print("데이터베이스 연결 해제")
        
        def execute_query(self, query: str) -> Optional[list]:
            if not self.connected:
                raise ConnectionError("데이터베이스에 연결되지 않았습니다")
            
            # 쿼리 실행 시뮬레이션
            if "SELECT" in query.upper():
                return [{"id": 1, "name": "김철수"}, {"id": 2, "name": "이영희"}]
            elif "INSERT" in query.upper():
                return [{"affected_rows": 1}]
            else:
                raise ValueError(f"지원하지 않는 쿼리: {query}")
    
    def safe_database_operation(db: DatabaseConnection, query: str) -> Optional[list]:
        """안전한 데이터베이스 작업"""
        try:
            return db.execute_query(query)
        except ConnectionError as e:
            print(f"연결 오류: {e}")
            return None
        except ValueError as e:
            print(f"쿼리 오류: {e}")
            return None
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return None
    
    # 테스트
    db = DatabaseConnection()
    db.connect()
    
    test_queries = [
        "SELECT * FROM users",
        "INSERT INTO users (name) VALUES ('박민수')",
        "DELETE FROM users WHERE id = 1",  # 지원하지 않는 쿼리
    ]
    
    for query in test_queries:
        result = safe_database_operation(db, query)
        if result:
            print(f"쿼리 실행 성공: {query}")
            print(f"결과: {result}")
        else:
            print(f"쿼리 실행 실패: {query}")
    
    db.disconnect()

def demonstrate_retry_pattern():
    """재시도 패턴"""
    print("\n=== 재시도 패턴 ===")
    
    def retry_operation(func, max_retries: int = 3, delay: float = 1.0):
        """재시도 데코레이터"""
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_retries:
                        print(f"시도 {attempt + 1} 실패: {e}. {delay}초 후 재시도...")
                        time.sleep(delay)
                    else:
                        print(f"최대 재시도 횟수({max_retries}) 초과. 최종 실패: {e}")
            
            raise last_exception
        return wrapper
    
    @retry_operation
    def unreliable_operation():
        """불안정한 작업 시뮬레이션"""
        import random
        if random.random() < 0.7:  # 70% 확률로 실패
            raise ConnectionError("연결 실패")
        return "작업 성공"
    
    # 테스트
    try:
        result = unreliable_operation()
        print(f"최종 결과: {result}")
    except Exception as e:
        print(f"모든 재시도 실패: {e}")

def demonstrate_validation_patterns():
    """검증 패턴"""
    print("\n=== 검증 패턴 ===")
    
    class ValidationError(Exception):
        """검증 오류"""
        def __init__(self, message: str, field: str = None):
            super().__init__(message)
            self.field = field
    
    def validate_email(email: str) -> str:
        """이메일 검증"""
        if not email:
            raise ValidationError("이메일은 필수입니다", "email")
        
        if "@" not in email:
            raise ValidationError("올바른 이메일 형식이 아닙니다", "email")
        
        if "." not in email.split("@")[1]:
            raise ValidationError("올바른 이메일 형식이 아닙니다", "email")
        
        return email
    
    def validate_age(age: Any) -> int:
        """나이 검증"""
        if not isinstance(age, (int, str)):
            raise ValidationError("나이는 숫자여야 합니다", "age")
        
        try:
            age_int = int(age)
        except ValueError:
            raise ValidationError("나이는 숫자여야 합니다", "age")
        
        if age_int < 0 or age_int > 150:
            raise ValidationError("나이는 0-150 사이여야 합니다", "age")
        
        return age_int
    
    def validate_user_data(data: Dict[str, Any]) -> Dict[str, Any]:
        """사용자 데이터 검증"""
        errors = []
        validated_data = {}
        
        # 이메일 검증
        try:
            validated_data["email"] = validate_email(data.get("email"))
        except ValidationError as e:
            errors.append(f"이메일 오류: {e}")
        
        # 나이 검증
        try:
            validated_data["age"] = validate_age(data.get("age"))
        except ValidationError as e:
            errors.append(f"나이 오류: {e}")
        
        if errors:
            raise ValidationError("; ".join(errors))
        
        return validated_data
    
    # 테스트
    test_data = [
        {"email": "user@example.com", "age": 25},
        {"email": "invalid-email", "age": 30},
        {"email": "user@domain.com", "age": -5},
        {"email": "", "age": "not-a-number"},
    ]
    
    for data in test_data:
        try:
            validated = validate_user_data(data)
            print(f"검증 성공: {validated}")
        except ValidationError as e:
            print(f"검증 실패: {e}")

def demonstrate_resource_management():
    """리소스 관리 패턴"""
    print("\n=== 리소스 관리 패턴 ===")
    
    class ResourceManager:
        """리소스 관리자"""
        def __init__(self, resource_name: str):
            self.resource_name = resource_name
            self.allocated = False
        
        def allocate(self):
            if self.allocated:
                raise RuntimeError(f"{self.resource_name}이 이미 할당되었습니다")
            self.allocated = True
            print(f"{self.resource_name} 할당됨")
        
        def deallocate(self):
            if not self.allocated:
                raise RuntimeError(f"{self.resource_name}이 할당되지 않았습니다")
            self.allocated = False
            print(f"{self.resource_name} 해제됨")
        
        def __enter__(self):
            self.allocate()
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.deallocate()
            if exc_type:
                print(f"예외 발생: {exc_type.__name__}: {exc_val}")
            return False  # 예외를 다시 발생시킴
    
    def safe_resource_usage():
        """안전한 리소스 사용"""
        try:
            with ResourceManager("데이터베이스 연결") as db:
                print("데이터베이스 작업 수행 중...")
                # 작업 중 예외 발생 시뮬레이션
                raise ValueError("작업 중 오류 발생")
        except Exception as e:
            print(f"작업 실패: {e}")
    
    def unsafe_resource_usage():
        """안전하지 않은 리소스 사용"""
        resource = ResourceManager("파일 핸들")
        try:
            resource.allocate()
            print("파일 작업 수행 중...")
            raise IOError("파일 작업 중 오류 발생")
        except Exception as e:
            print(f"작업 실패: {e}")
        finally:
            # finally 블록에서도 예외가 발생할 수 있음
            try:
                resource.deallocate()
            except Exception as e:
                print(f"리소스 해제 중 오류: {e}")
    
    print("안전한 리소스 사용 (with 문):")
    safe_resource_usage()
    
    print("\n안전하지 않은 리소스 사용:")
    unsafe_resource_usage()

if __name__ == "__main__":
    demonstrate_file_operations()
    demonstrate_json_handling()
    demonstrate_network_operations()
    demonstrate_database_operations()
    demonstrate_retry_pattern()
    demonstrate_validation_patterns()
    demonstrate_resource_management()
