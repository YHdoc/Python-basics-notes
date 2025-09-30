# super() 함수 사용법

class Person:
    """사람 기본 클래스"""
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(f"Person.__init__ 호출됨: {name}")
    
    def introduce(self):
        return f"안녕하세요, 저는 {self.name}입니다."
    
    def get_info(self):
        return f"이름: {self.name}, 나이: {self.age}, 성별: {self.gender}"

class Student(Person):
    """학생 클래스"""
    
    def __init__(self, name, age, gender, student_id, major):
        # super()를 사용하여 부모 클래스의 __init__ 호출
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major
        print(f"Student.__init__ 호출됨: {name}")
    
    def introduce(self):
        # 부모 클래스의 메서드 호출 후 추가 정보
        base_intro = super().introduce()
        return f"{base_intro} {self.major} 전공 학생입니다."
    
    def get_info(self):
        # 부모 클래스의 메서드 호출 후 추가 정보
        base_info = super().get_info()
        return f"{base_info}, 학번: {self.student_id}, 전공: {self.major}"

class Teacher(Person):
    """교사 클래스"""
    
    def __init__(self, name, age, gender, teacher_id, subject):
        # super()를 사용하여 부모 클래스의 __init__ 호출
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.subject = subject
        print(f"Teacher.__init__ 호출됨: {name}")
    
    def introduce(self):
        # 부모 클래스의 메서드 호출 후 추가 정보
        base_intro = super().introduce()
        return f"{base_intro} {self.subject} 교사입니다."
    
    def get_info(self):
        # 부모 클래스의 메서드 호출 후 추가 정보
        base_info = super().get_info()
        return f"{base_info}, 교사번호: {self.teacher_id}, 담당과목: {self.subject}"

class GraduateStudent(Student):
    """대학원생 클래스 - Student를 상속"""
    
    def __init__(self, name, age, gender, student_id, major, advisor, research_area):
        # super()를 사용하여 부모 클래스의 __init__ 호출
        super().__init__(name, age, gender, student_id, major)
        self.advisor = advisor
        self.research_area = research_area
        print(f"GraduateStudent.__init__ 호출됨: {name}")
    
    def introduce(self):
        # 부모 클래스의 메서드 호출 후 추가 정보
        base_intro = super().introduce()
        return f"{base_intro} {self.research_area} 분야를 연구하고 있습니다."
    
    def get_info(self):
        # 부모 클래스의 메서드 호출 후 추가 정보
        base_info = super().get_info()
        return f"{base_info}, 지도교수: {self.advisor}, 연구분야: {self.research_area}"

if __name__ == "__main__":
    print("=== super() 함수 사용 예제 ===")
    
    # 객체 생성 (초기화 순서 확인)
    print("1. Student 객체 생성:")
    student = Student("김철수", 20, "남", "2023001", "컴퓨터공학")
    
    print("\n2. Teacher 객체 생성:")
    teacher = Teacher("이영희", 35, "여", "T001", "수학")
    
    print("\n3. GraduateStudent 객체 생성:")
    grad_student = GraduateStudent("박민수", 25, "남", "2023002", "컴퓨터공학", "이영희", "인공지능")
    
    # 각 객체의 정보 출력
    print(f"\n=== 객체 정보 ===")
    print(f"학생: {student.get_info()}")
    print(f"교사: {teacher.get_info()}")
    print(f"대학원생: {grad_student.get_info()}")
    
    # 각 객체의 자기소개
    print(f"\n=== 자기소개 ===")
    print(f"학생: {student.introduce()}")
    print(f"교사: {teacher.introduce()}")
    print(f"대학원생: {grad_student.introduce()}")
    
    # MRO (Method Resolution Order) 확인
    print(f"\n=== MRO 확인 ===")
    print(f"Student MRO: {Student.__mro__}")
    print(f"Teacher MRO: {Teacher.__mro__}")
    print(f"GraduateStudent MRO: {GraduateStudent.__mro__}")
