# 단위 테스트

import unittest

def add_numbers(a, b):
    """두 숫자를 더하는 함수"""
    return a + b

def divide_numbers(a, b):
    """두 숫자를 나누는 함수"""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

class TestMathFunctions(unittest.TestCase):
    """수학 함수들의 테스트 클래스"""
    
    def test_add_numbers(self):
        """덧셈 함수 테스트"""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_divide_numbers(self):
        """나눗셈 함수 테스트"""
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertEqual(divide_numbers(7, 3), 7/3)
    
    def test_divide_by_zero(self):
        """0으로 나누기 테스트"""
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == '__main__':
    unittest.main()
