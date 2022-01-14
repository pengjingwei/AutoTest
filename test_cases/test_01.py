from unittest import TestCase

from pages.test import test


class TestDemo(TestCase):

    def test_01(self):
        res = test()
        expect = "新增成功！"

        self.assertEqual(expect, res)
