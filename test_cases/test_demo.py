import unittest
from unittest import TestCase

from pages.Demo import demo


class TestDemo(TestCase):

    def setUp(self) -> None:
        print('前置')

    def tearDown(self) -> None:
        print('后置')

    def test_demo(self):
        result = demo('admin', '123456')

        expect = '退出系统'

        self.assertEqual(expect, result)

    def test_demo1(self):
        result = demo('a', '123456')
        expect = '用户不存在'

        self.assertEqual(expect, result)

    def test_demo2(self):
        result = demo('admin', '1')
        expect = '密码错误'

        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
