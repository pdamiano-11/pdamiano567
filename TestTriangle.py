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
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    
    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(7,6,4),'Scalene','7,6,4 is a Scalene triangle')
    
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(5,3,5),'Isoceles','5,3,5 is an Isoceles triangle')
    
    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(8,8,3),'Isoceles','8,8,3 is an Isoceles triangle')
    
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testNoTriangleA(self): 
        self.assertEqual(classifyTriangle(6,0,2),'InvalidInput','6,0,2 is not a triangle')

    def testNoTriangleB(self): 
        self.assertEqual(classifyTriangle(-2,7,4),'InvalidInput','-2,7,4 is not a triangle')
    
    def testNoTriangleC(self): 
        self.assertEqual(classifyTriangle(15,3,1),'NotATriangle','15,3,1 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

