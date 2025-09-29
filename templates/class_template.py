"""
클래스 템플릿
새로운 클래스를 만들 때 사용할 수 있는 기본 구조입니다.
"""

from datetime import datetime
from typing import Optional, List


class TemplateClass:
    """
    클래스에 대한 설명을 여기에 작성하세요.
    
    Attributes:
        attribute1 (str): 첫 번째 속성 설명
        attribute2 (int): 두 번째 속성 설명
    """
    
    # 클래스 변수 (모든 인스턴스가 공유)
    class_variable = "공통 값"
    
    def __init__(self, param1: str, param2: int = 0):
        """
        생성자
        
        Args:
            param1 (str): 첫 번째 매개변수
            param2 (int, optional): 두 번째 매개변수. Defaults to 0.
        
        Raises:
            ValueError: 잘못된 매개변수가 전달된 경우
        """
        if not param1:
            raise ValueError("param1은 빈 문자열일 수 없습니다.")
        
        self.attribute1 = param1
        self.attribute2 = param2
        self.created_at = datetime.now()
    
    def instance_method(self) -> str:
        """
        인스턴스 메서드
        
        Returns:
            str: 처리된 결과
        """
        return f"인스턴스 메서드 결과: {self.attribute1}"
    
    @classmethod
    def class_method(cls, value: str) -> 'TemplateClass':
        """
        클래스 메서드 (팩토리 메서드)
        
        Args:
            value (str): 생성할 값
            
        Returns:
            TemplateClass: 새로운 인스턴스
        """
        return cls(value, 100)
    
    @staticmethod
    def static_method(data: List[int]) -> int:
        """
        정적 메서드 (유틸리티 함수)
        
        Args:
            data (List[int]): 처리할 데이터
            
        Returns:
            int: 처리 결과
        """
        return sum(data)
    
    def __str__(self) -> str:
        """문자열 표현"""
        return f"TemplateClass(attribute1='{self.attribute1}', attribute2={self.attribute2})"
    
    def __repr__(self) -> str:
        """개발자용 문자열 표현"""
        return f"TemplateClass('{self.attribute1}', {self.attribute2})"
    
    def __eq__(self, other) -> bool:
        """같음 비교"""
        if not isinstance(other, TemplateClass):
            return False
        return self.attribute1 == other.attribute1 and self.attribute2 == other.attribute2


# 사용 예제
if __name__ == "__main__":
    # 객체 생성
    obj1 = TemplateClass("테스트", 42)
    print(obj1)
    
    # 클래스 메서드 사용
    obj2 = TemplateClass.class_method("팩토리 생성")
    print(obj2)
    
    # 정적 메서드 사용
    result = TemplateClass.static_method([1, 2, 3, 4, 5])
    print(f"정적 메서드 결과: {result}")
