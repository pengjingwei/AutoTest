
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

tests = unittest.defaultTestLoader.discover(r'../test_cases', pattern="test*.py")

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
filename = r"../report/reportReport{}.html".format(now)
file = open(file=filename, mode='w+', encoding='utf-8')

runner = HTMLTestRunner.HTMLTestRunner(
    title='数据管控模块测试报告',
    description='元数据维护新增目录测试',
    stream=file,
    verbosity=1
)

runner.run(tests)
file.close()
