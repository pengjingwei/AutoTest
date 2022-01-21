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
from pages.login import Login

'''
【数据中台】-【数据管控】-【元模型管理】界面
1.点击左侧树选择数据分层为“ODS”层；
2.右上角资源库选择ODS_DB_TEST；
3.选择表中文名为“预算测试表”的选项，点击右侧“编辑字段”按钮；
4.进入后点击左上角“新增”按钮；
5.名称设置为“测试ID”，字段设置为“TEST_ID”，类型为“NUMBER”，长度设为15，不可为空，是主键；
6.点击“确定”按钮；

'''


class TestEditField(unittest.TestCase):
    def setUp(self) -> None:
        print("开始测试用例【数据中台】-【数据管控】-【元模型管理】字段创建")
        self.driver = webdriver.Chrome(options=ChromeOptions().options())
        login = Login(self.driver)
        login.login('admin', '123456')
        sleep(1)

    def tearDown(self) -> None:
        print("测试结束")
        self.driver.quit()

    def test_EditField(self):
        action = metamodel_editField(self.driver)
        action.editfield()


if __name__ == '__main__':
    # unittest.main()

    addData = TestEditField()
    addData.test_EditField()
