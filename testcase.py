import unittest

from ddt import data, unpack, ddt

from Calc import Calc

#加法测试
da = [
    [1, 2, 3],
    [5, 6, 11],
    [-9, 8, -1],
    [-9, -9, -18],
    [0, 0, 0],
    [50000000000000, 5, 50000000000005],
    [10, 10, 22]
]
@ddt
class TestAdd(unittest.TestCase):
    @data(*da)
    @unpack
    def testAdd(self,a,b,c):
        calc = Calc()
        sum = calc.add(a,b)

        self.assertEqual(sum,c)

#减法测试
da0 = [
        [1, 2, -1],
        [5, 6, -1],
        [-9, 8, -17],
        [-9, -9, 0],
        [0, 0, 0],
        [50000, 5, 49995],
        [10, -10, 20]
    ]
@ddt
class TestSubs(unittest.TestCase):
    @data(*da0)
    @unpack
    def testSubs(self, a, b, c):
            calc = Calc()
            sum = calc.subs(a, b)

            self.assertEqual(sum, c)


#乘法测试
da1 = [
        [1, 2, 2],
        [5, 6, 30],
        [-9, 8,-72],
        [-9, -9, 81],
        [0, 0, 0],
        [10, 10, 100],
        [50000000000000, 5, 250000000000000]
    ]
@ddt
class TestMulti(unittest.TestCase):


    @data(*da1)
    @unpack
    def testMulti(self,a,b,c):
        calc = Calc()
        sum = calc.multi(a,b)

        self.assertEqual(sum,c)

#除法测试
da3 = [
        [2, 2, 1],
        [5, 5, 1],
        [-9, 3, -3],
        [-9, -9, 1],
        [0, 1, 0],
        [50000, 5, 10000],
        [10, -10, -1]
    ]
@ddt
class TestDevision(unittest.TestCase):
    @data(*da3)
    @unpack
    def testDevision(self, a, b, c):
            calc = Calc()
            sum = calc.devision(a, b)

            self.assertEqual(sum, c)