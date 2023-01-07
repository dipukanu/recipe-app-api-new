"""
Sample test
"""
from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtact_numberrs(self):
        """Test subtract numbers"""
        res = calc.subtract(15, 10)

        self.assertEqual(res, 5)
