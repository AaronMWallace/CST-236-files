"""
Test for source.source1
"""
from source.source1 import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

  
    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_isosceles(self):
        ret = get_triangle_type(1,2,2)
        self.assertEqual(ret, 'isosceles')
        
    def test_invalid_triangle(self):
        ret = get_triangle_type('a',2,2)
        self.assertEqual(ret, 'invalid')

    def test_invalid_triangle2(self):
        ret = get_triangle_type(3,0,2)
        self.assertEqual(ret, 'invalid')

    def test_list_input(self):
        a  = [1,2,3]
        ret = get_triangle_type(a,2,2)
   
    def test_dict_input(self):
        a  = {'tri':1, 'an':2, 'gle':3}
        ret = get_triangle_type(a,2,2)
