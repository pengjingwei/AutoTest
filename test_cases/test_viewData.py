#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author: 高莽
@Software: PyCharm
@version: 2021.2.2
@file: test_viewData.py
@time: 2022/1/18 11:41
"""
import unittest
from unittest import TestCase

from selenium import webdriver

from pages.data_security.subscription_viewData import subscription_viewData


class TestviewData(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        print("测试结束")
        # self.driver.quit()

    def test_viewData(self):
        action=subscription_viewData(self.driver)
        action.share_viewData()
        # policy_manage = PolicyManage(self.driver)
        # res = policy_manage.add_policy('名称', '自动化新增策略', '自动化新增策略')
        # expect = '新增策略'
        # self.assertEqual(expect, res)


if __name__ == '__main__':
    # unittest.main()

    viewData = TestviewData()
    viewData.test_viewData()