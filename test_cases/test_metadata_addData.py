#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author: 高莽
@Software: PyCharm
@version: 2021.2.2
@file: test_metadata_addData.py.py
@time: 2022/1/18 16:21
"""
import unittest

from selenium import webdriver

from pages.data_management.manage_metadata_addData import AddData


class TestAddData(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        print("测试结束")
        # self.driver.quit()

    def test_addData(self):
        action = AddData(self.driver)
        action.metadata()


if __name__ == '__main__':
    # unittest.main()

    addData = TestAddData()
    addData.test_addData()
