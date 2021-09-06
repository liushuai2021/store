'''
unittest.TestLoader()提供了创建test suite的几种方法：
TestLoader().loadTestsFromTestCase(testCaseClass)
TestLoader().loadTestsFromModule(module, pattern=None)
TestLoader().loadTestsFromName(name, module=None)
TestLoader().loadTestsFromNames(name, module=None)
TestLoader().discover
下面一一列举其用法，并会感叹unittest的精妙之处。

l   oadTestsFromTestCase(testCaseClass)
testCaseClass必须是TestCase的子类（或孙类也行）

    loadTestsFromModule(module, pattern=None)
test case所在的module

    loadTestsFromName(name, module=None)
name是一个string，string需要是是这种格式的“module.class.method”

    loadTestsFromNames(name, module=None)
names是一个list，用法与上同

    discover(start_dir, pattern=’test*.py’, top_level_dir=None)
从python文件中获取test cases

'''
import time
import unittest,threading
from testcase import TestMulti, TestDevision, TestAdd, TestSubs
start = time.time()
# 创建2个套件，每个套件使用一个线程去执行
suite1 = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
suite2 = unittest.defaultTestLoader.loadTestsFromTestCase(TestSubs)
suite3 = unittest.defaultTestLoader.loadTestsFromTestCase(TestMulti)
suite4 = unittest.defaultTestLoader.loadTestsFromTestCase(TestDevision)

def work1():
    """执行套件1"""
    unittest.TextTestRunner().run(suite1)

def work2():
    """执行套件2"""
    unittest.TextTestRunner().run(suite2)

def work3():
    """执行套件3"""
    unittest.TextTestRunner().run(suite3)

def work4():
    """执行套件4"""
    unittest.TextTestRunner().run(suite4)



t1 = threading.Thread(target=work1)
t2 = threading.Thread(target=work2)
t3 = threading.Thread(target=work3)
t4 = threading.Thread(target=work4)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
end=time.time()
print(end-start)
