# 실무에서 자주 사용되는 클래스 패턴

import json
import os
from datetime import datetime
from typing import List, Dict, Optional, Any

class User:
    """사용자 클래스 - 실무 패턴 예제"""
    
    def __init__(self, user_id: str, username: str, email: str, role: str = "user"):
        """생성자"""
        self._user_id = user_id
        self._username = username
        self._email = email
        self._role = role
        self._created_at = datetime.now()
        self._last_login = None
        self._is_active = True
    
    @property
    def user_id(self):
        """사용자 ID (읽기 전용)"""
        return self._user_id
    
    @property
    def username(self):
        """사용자명"""
        return self._username
    
    @username.setter
    def username(self, value):
        """사용자명 설정"""
        if not value or len(value) < 3:
            raise ValueError("사용자명은 3자 이상이어야 합니다.")
        self._username = value
    
    @property
    def email(self):
        """이메일"""
        return self._email
    
    @email.setter
    def email(self, value):
        """이메일 설정"""
        if "@" not in value or "." not in value:
            raise ValueError("올바른 이메일 형식이 아닙니다.")
        self._email = value
    
    @property
    def role(self):
        """역할"""
        return self._role
    
    @role.setter
    def role(self, value):
        """역할 설정"""
        if value not in ["user", "admin", "moderator"]:
            raise ValueError("유효하지 않은 역할입니다.")
        self._role = value
    
    @property
    def is_active(self):
        """활성 상태"""
        return self._is_active
    
    def activate(self):
        """계정 활성화"""
        self._is_active = True
    
    def deactivate(self):
        """계정 비활성화"""
        self._is_active = False
    
    def login(self):
        """로그인"""
        if not self._is_active:
            raise ValueError("비활성화된 계정입니다.")
        self._last_login = datetime.now()
    
    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            "user_id": self._user_id,
            "username": self._username,
            "email": self._email,
            "role": self._role,
            "created_at": self._created_at.isoformat(),
            "last_login": self._last_login.isoformat() if self._last_login else None,
            "is_active": self._is_active
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """딕셔너리로부터 생성"""
        user = cls(
            user_id=data["user_id"],
            username=data["username"],
            email=data["email"],
            role=data.get("role", "user")
        )
        user._created_at = datetime.fromisoformat(data["created_at"])
        if data.get("last_login"):
            user._last_login = datetime.fromisoformat(data["last_login"])
        user._is_active = data.get("is_active", True)
        return user
    
    def __str__(self):
        """문자열 표현"""
        return f"User({self._username}, {self._email}, {self._role})"

def demonstrate_user_management():
    """사용자 관리 예제"""
    print("=== 사용자 관리 예제 ===")
    
    # 사용자 생성
    user1 = User("user001", "김철수", "kim@example.com", "user")
    user2 = User("user002", "이영희", "lee@example.com", "admin")
    
    print(f"사용자1: {user1}")
    print(f"사용자2: {user2}")
    
    # 로그인
    user1.login()
    user2.login()
    
    # 사용자 정보 수정
    user1.username = "김철수2"
    user1.email = "kim2@example.com"
    
    # 딕셔너리로 변환
    user_dict = user1.to_dict()
    print(f"사용자1 딕셔너리: {user_dict}")
    
    # 딕셔너리로부터 사용자 생성
    user3 = User.from_dict(user_dict)
    print(f"딕셔너리로부터 생성된 사용자: {user3}")

class Product:
    """상품 클래스 - 상품 관리 예제"""
    
    def __init__(self, product_id: str, name: str, price: float, category: str):
        """생성자"""
        self._product_id = product_id
        self._name = name
        self._price = price
        self._category = category
        self._stock = 0
        self._is_available = True
        self._created_at = datetime.now()
    
    @property
    def product_id(self):
        """상품 ID (읽기 전용)"""
        return self._product_id
    
    @property
    def name(self):
        """상품명"""
        return self._name
    
    @name.setter
    def name(self, value):
        """상품명 설정"""
        if not value or len(value) < 2:
            raise ValueError("상품명은 2자 이상이어야 합니다.")
        self._name = value
    
    @property
    def price(self):
        """가격"""
        return self._price
    
    @price.setter
    def price(self, value):
        """가격 설정"""
        if value < 0:
            raise ValueError("가격은 0 이상이어야 합니다.")
        self._price = value
    
    @property
    def category(self):
        """카테고리"""
        return self._category
    
    @property
    def stock(self):
        """재고"""
        return self._stock
    
    @property
    def is_available(self):
        """판매 가능 여부"""
        return self._is_available and self._stock > 0
    
    def add_stock(self, quantity: int):
        """재고 추가"""
        if quantity <= 0:
            raise ValueError("추가할 재고는 0보다 커야 합니다.")
        self._stock += quantity
    
    def remove_stock(self, quantity: int):
        """재고 차감"""
        if quantity <= 0:
            raise ValueError("차감할 재고는 0보다 커야 합니다.")
        if quantity > self._stock:
            raise ValueError("재고가 부족합니다.")
        self._stock -= quantity
    
    def set_availability(self, available: bool):
        """판매 가능 여부 설정"""
        self._is_available = available
    
    def get_discounted_price(self, discount_rate: float):
        """할인된 가격 계산"""
        if not 0 <= discount_rate <= 1:
            raise ValueError("할인율은 0-1 사이여야 합니다.")
        return self._price * (1 - discount_rate)
    
    def __str__(self):
        """문자열 표현"""
        status = "판매 가능" if self.is_available else "판매 불가"
        return f"Product({self._name}, {self._price}원, 재고: {self._stock}, {status})"

def demonstrate_product_management():
    """상품 관리 예제"""
    print("\n=== 상품 관리 예제 ===")
    
    # 상품 생성
    product1 = Product("P001", "노트북", 1000000, "전자제품")
    product2 = Product("P002", "마우스", 50000, "전자제품")
    
    print(f"상품1: {product1}")
    print(f"상품2: {product2}")
    
    # 재고 추가
    product1.add_stock(10)
    product2.add_stock(50)
    
    print(f"재고 추가 후:")
    print(f"상품1: {product1}")
    print(f"상품2: {product2}")
    
    # 재고 차감
    product1.remove_stock(3)
    product2.remove_stock(10)
    
    print(f"재고 차감 후:")
    print(f"상품1: {product1}")
    print(f"상품2: {product2}")
    
    # 할인된 가격 계산
    discounted_price = product1.get_discounted_price(0.1)  # 10% 할인
    print(f"상품1 10% 할인 가격: {discounted_price:.0f}원")

class Order:
    """주문 클래스 - 주문 관리 예제"""
    
    def __init__(self, order_id: str, customer_id: str):
        """생성자"""
        self._order_id = order_id
        self._customer_id = customer_id
        self._items = []
        self._status = "pending"
        self._created_at = datetime.now()
        self._total_amount = 0
    
    @property
    def order_id(self):
        """주문 ID (읽기 전용)"""
        return self._order_id
    
    @property
    def customer_id(self):
        """고객 ID (읽기 전용)"""
        return self._customer_id
    
    @property
    def items(self):
        """주문 항목 (읽기 전용)"""
        return self._items.copy()
    
    @property
    def status(self):
        """주문 상태"""
        return self._status
    
    @property
    def total_amount(self):
        """총 금액 (읽기 전용)"""
        return self._total_amount
    
    def add_item(self, product: Product, quantity: int):
        """주문 항목 추가"""
        if quantity <= 0:
            raise ValueError("수량은 0보다 커야 합니다.")
        if not product.is_available:
            raise ValueError("판매 불가능한 상품입니다.")
        if quantity > product.stock:
            raise ValueError("재고가 부족합니다.")
        
        # 기존 항목이 있는지 확인
        for item in self._items:
            if item["product"].product_id == product.product_id:
                item["quantity"] += quantity
                break
        else:
            self._items.append({
                "product": product,
                "quantity": quantity
            })
        
        self._calculate_total()
    
    def remove_item(self, product_id: str):
        """주문 항목 제거"""
        self._items = [item for item in self._items if item["product"].product_id != product_id]
        self._calculate_total()
    
    def update_quantity(self, product_id: str, quantity: int):
        """수량 업데이트"""
        if quantity <= 0:
            self.remove_item(product_id)
            return
        
        for item in self._items:
            if item["product"].product_id == product_id:
                if quantity > item["product"].stock:
                    raise ValueError("재고가 부족합니다.")
                item["quantity"] = quantity
                break
        
        self._calculate_total()
    
    def _calculate_total(self):
        """총 금액 계산"""
        self._total_amount = sum(
            item["product"].price * item["quantity"]
            for item in self._items
        )
    
    def confirm(self):
        """주문 확인"""
        if self._status != "pending":
            raise ValueError("확인할 수 없는 주문 상태입니다.")
        self._status = "confirmed"
    
    def cancel(self):
        """주문 취소"""
        if self._status == "completed":
            raise ValueError("완료된 주문은 취소할 수 없습니다.")
        self._status = "cancelled"
    
    def complete(self):
        """주문 완료"""
        if self._status != "confirmed":
            raise ValueError("확인된 주문만 완료할 수 있습니다.")
        
        # 재고 차감
        for item in self._items:
            item["product"].remove_stock(item["quantity"])
        
        self._status = "completed"
    
    def __str__(self):
        """문자열 표현"""
        return f"Order({self._order_id}, {self._customer_id}, {self._status}, {self._total_amount}원)"

def demonstrate_order_management():
    """주문 관리 예제"""
    print("\n=== 주문 관리 예제 ===")
    
    # 상품 생성
    product1 = Product("P001", "노트북", 1000000, "전자제품")
    product2 = Product("P002", "마우스", 50000, "전자제품")
    
    # 재고 추가
    product1.add_stock(10)
    product2.add_stock(50)
    
    # 주문 생성
    order = Order("O001", "C001")
    print(f"주문 생성: {order}")
    
    # 주문 항목 추가
    order.add_item(product1, 2)
    order.add_item(product2, 5)
    
    print(f"항목 추가 후: {order}")
    print(f"주문 항목: {order.items}")
    
    # 주문 확인
    order.confirm()
    print(f"주문 확인 후: {order}")
    
    # 주문 완료
    order.complete()
    print(f"주문 완료 후: {order}")
    
    # 재고 확인
    print(f"상품1 재고: {product1.stock}")
    print(f"상품2 재고: {product2.stock}")

class FileManager:
    """파일 관리 클래스 - 파일 작업 예제"""
    
    def __init__(self, base_path: str):
        """생성자"""
        self._base_path = base_path
        self._files = {}
        self._ensure_directory()
    
    def _ensure_directory(self):
        """디렉토리 존재 확인 및 생성"""
        if not os.path.exists(self._base_path):
            os.makedirs(self._base_path)
    
    @property
    def base_path(self):
        """기본 경로 (읽기 전용)"""
        return self._base_path
    
    def create_file(self, filename: str, content: str = ""):
        """파일 생성"""
        file_path = os.path.join(self._base_path, filename)
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self._files[filename] = {
                "path": file_path,
                "size": len(content),
                "created_at": datetime.now(),
                "modified_at": datetime.now()
            }
            
            print(f"파일 생성 완료: {filename}")
            return True
            
        except Exception as e:
            print(f"파일 생성 실패: {e}")
            return False
    
    def read_file(self, filename: str):
        """파일 읽기"""
        if filename not in self._files:
            print(f"파일이 존재하지 않습니다: {filename}")
            return None
        
        file_path = self._files[filename]["path"]
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print(f"파일 읽기 완료: {filename}")
            return content
            
        except Exception as e:
            print(f"파일 읽기 실패: {e}")
            return None
    
    def update_file(self, filename: str, content: str):
        """파일 업데이트"""
        if filename not in self._files:
            print(f"파일이 존재하지 않습니다: {filename}")
            return False
        
        file_path = self._files[filename]["path"]
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self._files[filename]["size"] = len(content)
            self._files[filename]["modified_at"] = datetime.now()
            
            print(f"파일 업데이트 완료: {filename}")
            return True
            
        except Exception as e:
            print(f"파일 업데이트 실패: {e}")
            return False
    
    def delete_file(self, filename: str):
        """파일 삭제"""
        if filename not in self._files:
            print(f"파일이 존재하지 않습니다: {filename}")
            return False
        
        file_path = self._files[filename]["path"]
        
        try:
            os.remove(file_path)
            del self._files[filename]
            
            print(f"파일 삭제 완료: {filename}")
            return True
            
        except Exception as e:
            print(f"파일 삭제 실패: {e}")
            return False
    
    def list_files(self):
        """파일 목록 조회"""
        return list(self._files.keys())
    
    def get_file_info(self, filename: str):
        """파일 정보 조회"""
        if filename not in self._files:
            return None
        return self._files[filename].copy()
    
    def __str__(self):
        """문자열 표현"""
        return f"FileManager({self._base_path}, {len(self._files)} files)"

def demonstrate_file_management():
    """파일 관리 예제"""
    print("\n=== 파일 관리 예제 ===")
    
    # 파일 관리자 생성
    file_manager = FileManager("test_files")
    print(f"파일 관리자: {file_manager}")
    
    # 파일 생성
    file_manager.create_file("test1.txt", "첫 번째 파일 내용")
    file_manager.create_file("test2.txt", "두 번째 파일 내용")
    
    # 파일 목록 조회
    files = file_manager.list_files()
    print(f"파일 목록: {files}")
    
    # 파일 읽기
    content = file_manager.read_file("test1.txt")
    print(f"파일 내용: {content}")
    
    # 파일 업데이트
    file_manager.update_file("test1.txt", "업데이트된 내용")
    
    # 파일 정보 조회
    info = file_manager.get_file_info("test1.txt")
    print(f"파일 정보: {info}")
    
    # 파일 삭제
    file_manager.delete_file("test2.txt")
    
    # 최종 파일 목록
    files = file_manager.list_files()
    print(f"최종 파일 목록: {files}")

class Configuration:
    """설정 클래스 - 설정 관리 예제"""
    
    def __init__(self, config_file: str = "config.json"):
        """생성자"""
        self._config_file = config_file
        self._config = {}
        self._load_config()
    
    def _load_config(self):
        """설정 로드"""
        try:
            if os.path.exists(self._config_file):
                with open(self._config_file, 'r', encoding='utf-8') as f:
                    self._config = json.load(f)
                print(f"설정 로드 완료: {self._config_file}")
            else:
                print(f"설정 파일이 존재하지 않습니다: {self._config_file}")
        except Exception as e:
            print(f"설정 로드 실패: {e}")
    
    def _save_config(self):
        """설정 저장"""
        try:
            with open(self._config_file, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, ensure_ascii=False, indent=2)
            print(f"설정 저장 완료: {self._config_file}")
        except Exception as e:
            print(f"설정 저장 실패: {e}")
    
    def get(self, key: str, default=None):
        """설정 값 조회"""
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any):
        """설정 값 설정"""
        self._config[key] = value
        self._save_config()
    
    def delete(self, key: str):
        """설정 값 삭제"""
        if key in self._config:
            del self._config[key]
            self._save_config()
    
    def get_all(self):
        """모든 설정 조회"""
        return self._config.copy()
    
    def update(self, config_dict: Dict[str, Any]):
        """설정 업데이트"""
        self._config.update(config_dict)
        self._save_config()
    
    def __str__(self):
        """문자열 표현"""
        return f"Configuration({self._config_file}, {len(self._config)} settings)"

def demonstrate_configuration_management():
    """설정 관리 예제"""
    print("\n=== 설정 관리 예제 ===")
    
    # 설정 생성
    config = Configuration("test_config.json")
    print(f"설정: {config}")
    
    # 설정 값 설정
    config.set("database.host", "localhost")
    config.set("database.port", 5432)
    config.set("database.name", "mydb")
    config.set("app.debug", True)
    config.set("app.version", "1.0.0")
    
    # 설정 값 조회
    host = config.get("database.host")
    port = config.get("database.port")
    debug = config.get("app.debug")
    
    print(f"데이터베이스 호스트: {host}")
    print(f"데이터베이스 포트: {port}")
    print(f"디버그 모드: {debug}")
    
    # 모든 설정 조회
    all_config = config.get_all()
    print(f"모든 설정: {all_config}")
    
    # 설정 업데이트
    config.update({
        "app.name": "MyApp",
        "app.author": "Developer"
    })
    
    # 설정 삭제
    config.delete("app.debug")
    
    # 최종 설정
    final_config = config.get_all()
    print(f"최종 설정: {final_config}")

if __name__ == "__main__":
    demonstrate_user_management()
    demonstrate_product_management()
    demonstrate_order_management()
    demonstrate_file_management()
    demonstrate_configuration_management()
