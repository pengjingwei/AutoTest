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
from time import sleep

from selenium import webdriver

from base.chrome_options import ChromeOptions
from pages.data_management.manage_metadata_addData import AddData
from pages.data_management.metamodel_editField import metamodel_editField
from pages.data_management.rules_addRule import rules_addRule
from pages.login import Login

'''
【数据中台】-【数据管控】-【规则管理】
1.点击左上角的“新增规则”按钮；
2.选择“字段规则”，字段名为“TEST_PAY”，字段中文名为“测试金额”；
3.启用非空配置，启用条件为“is not null”；
4.不启用“数据范围配置”、“重复值配置”、“值域配置”；
5.点击“确定”按钮；

'''


class TestAddRules(unittest.TestCase):
    def setUp(self) -> None:
        print("开始测试用例【数据中台】-【数据管控】-【元模型管理】字段创建")
        self.driver = webdriver.Chrome(options=ChromeOptions().options())
        login = Login(self.driver)
        login.login('admin', '123456')
        sleep(1)

    def tearDown(self) -> None:
        print("测试结束")
        self.driver.quit()

    def test_AddRules(self):
        action = rules_addRule(self.driver)
        action.add_rule()


if __name__ == '__main__':
    # unittest.main()

    addRule = TestAddRules()
    addRule.test_AddRules()
