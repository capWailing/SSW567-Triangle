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
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertNotEqual(classifyTriangle(2, 2, 3), 'Equilateral', '2,2,3 is not a equilateral triangle')

    def testEquilateralTrianglesC(self):
        self.assertNotEqual(classifyTriangle(3, 2, 2), 'Equilateral', '3,2,2 is not a equilateral triangle')

    def testEquilateralTrianglesD(self):
        self.assertNotEqual(classifyTriangle(2, 3, 2), 'Equilateral', '2,3,2 is not a equilateral triangle')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(4, 6, 6), 'Scalene', '4,6,6 should be scalene')

    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(6, 4, 6), 'Scalene', '6,4,6 should be scalene')

    def testScaleneTrianglesC(self):
        self.assertEqual(classifyTriangle(6, 6, 4), 'Scalene', '6,6,4 should be scalene')

    def testScaleneTrianglesD(self):
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'Scalene', '3,4,5 is not a scalene triangle')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Isosceles', '3,4,6 should be isosceles')

    def testNotTriangleA(self):
        self.assertEqual(classifyTriangle(2, 3, 5), 'NotATriangle', '2,3,5 is not a triangle')

    def testNotTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 2), 'NotATriangle', '5,3,2 is not a triangle')

    def testNotTriangleC(self):
        self.assertEqual(classifyTriangle(2, 5, 3), 'NotATriangle', '2,5,3 is not a triangle')

    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(201, 2, 2), 'InvalidInput', '201,2,2 is invalid input')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(2, 201, 2), 'InvalidInput', '2,201,2 is invalid input')

    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle(2, 2, 201), 'InvalidInput', '2,2,201 is invalid input')

    def testInvalidInput4(self):
        self.assertEqual(classifyTriangle(-2, 2, 2), 'InvalidInput', '-2,2,2 is invalid input')

    def testInvalidInput5(self):
        self.assertEqual(classifyTriangle(2, -2, 2), 'InvalidInput', '2,-2,2 is invalid input')

    def testInvalidInput6(self):
        self.assertEqual(classifyTriangle(2, 2, -2), 'InvalidInput', '2,2,-2 is invalid input')

    def testInvalidInput7(self):
        self.assertEqual(classifyTriangle('2', 2, 2), 'InvalidInput', "'2',2,2 is invalid input")

    def testInvalidInput8(self):
        self.assertEqual(classifyTriangle(2, '2', 2), 'InvalidInput', "2,'2',2 is invalid input")

    def testInvalidInput9(self):
        self.assertEqual(classifyTriangle(2, 2, '2'), 'InvalidInput', "2,2,'2' is invalid input")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
