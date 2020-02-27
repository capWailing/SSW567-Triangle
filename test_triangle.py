# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    """
        unit test class for testing triangles
    """
    # define multiple sets of tests as functions with names that begin

    def test_right_triangle(self):
        """
            test case when triangle is a right triangle
        :return:
        """
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')

    def test_equilateral_triangles(self):
        """
            test case when triangle is an equilateral triangle
        :return:
        """
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

        self.assertNotEqual(classifyTriangle(2, 2, 3), 'Equilateral',
                            '2,2,3 is not a equilateral triangle')

        self.assertNotEqual(classifyTriangle(3, 2, 2), 'Equilateral',
                            '3,2,2 is not a equilateral triangle')

        self.assertNotEqual(classifyTriangle(2, 3, 2), 'Equilateral',
                            '2,3,2 is not a equilateral triangle')

    def test_scalene_triangles(self):
        """
            test case when triangle is a scalene
        :return:
        """
        self.assertEqual(classifyTriangle(4, 6, 6), 'Scalene', '4,6,6 should be scalene')

        self.assertEqual(classifyTriangle(6, 4, 6), 'Scalene', '6,4,6 should be scalene')

        self.assertEqual(classifyTriangle(6, 6, 4), 'Scalene', '6,6,4 should be scalene')

        self.assertNotEqual(classifyTriangle(3, 4, 5), 'Scalene', '3,4,5 is not a scalene triangle')

    def test_isosceles_triangles(self):
        """
            test case when triangle is an isosceles triangle
        :return:
        """
        self.assertEqual(classifyTriangle(3, 4, 6), 'Isosceles', '3,4,6 should be isosceles')

    def test_not_triangle(self):
        """
            test case when triangel is not a triangle
        :return:
        """
        self.assertEqual(classifyTriangle(2, 3, 5), 'NotATriangle', '2,3,5 is not a triangle')

        self.assertEqual(classifyTriangle(5, 3, 2), 'NotATriangle', '5,3,2 is not a triangle')

        self.assertEqual(classifyTriangle(2, 5, 3), 'NotATriangle', '2,5,3 is not a triangle')

    def test_invalid_input(self):
        """
            test case when the input is invalid
        :return:
        """
        self.assertEqual(classifyTriangle(201, 2, 2), 'InvalidInput', '201,2,2 is invalid input')

        self.assertEqual(classifyTriangle(2, 201, 2), 'InvalidInput', '2,201,2 is invalid input')

        self.assertEqual(classifyTriangle(2, 2, 201), 'InvalidInput', '2,2,201 is invalid input')

        self.assertEqual(classifyTriangle(-2, 2, 2), 'InvalidInput', '-2,2,2 is invalid input')

        self.assertEqual(classifyTriangle(2, -2, 2), 'InvalidInput', '2,-2,2 is invalid input')

        self.assertEqual(classifyTriangle(2, 2, -2), 'InvalidInput', '2,2,-2 is invalid input')

        self.assertEqual(classifyTriangle('2', 2, 2), 'InvalidInput', "'2',2,2 is invalid input")

        self.assertEqual(classifyTriangle(2, '2', 2), 'InvalidInput', "2,'2',2 is invalid input")
        self.assertEqual(classifyTriangle(2, 2, '2'), 'InvalidInput', "2,2,'2' is invalid input")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
