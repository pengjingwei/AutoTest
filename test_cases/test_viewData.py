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
from time import sleep
from unittest import TestCase

from selenium import webdriver

from base.chrome_options import ChromeOptions
from pages.data_security.subscription_viewData import subscription_viewData
from pages.login import Login


class TestviewData(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(options=ChromeOptions().options())
        login = Login(self.driver)
        login.login('admin', '123456')
        sleep(1)

    def tearDown(self) -> None:
        print("测试结束")
        self.driver.quit()
    # 查看加密规则
    def test_viewData(self):
        action = subscription_viewData(self.driver)
        action.share_viewData()


if __name__ == '__main__':
    # unittest.main()

    viewData = TestviewData()
    viewData.test_viewData()
