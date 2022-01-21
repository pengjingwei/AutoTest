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
from pages.data_management.problem_handing_solve import problem_handing_solve
from pages.data_management.rules_addRule import rules_addRule
from pages.login import Login

'''
登录用户b，进入【数据中台】-【数据管控】-【问题处理】；
1.找到“预算测试”，点击右侧的“处理”按钮；
2.进入到问题单处理后，找到问题字段，点击右侧的“处理”按钮；
3.弹出的问题单处理，点击“确定”按钮；
4.保存后，勾选“预算测试”，点击左上角“提交处理结果”；

'''


class TestProblemSolve(unittest.TestCase):
    def setUp(self) -> None:
        print("登录用户b，进入【数据中台】-【数据管控】-【问题处理】")
        self.driver = webdriver.Chrome(options=ChromeOptions().options())
        self.driver.implicitly_wait(20)
        login = Login(self.driver)
        login.login('jkl1109', '123456')
        sleep(1)

    def tearDown(self) -> None:
        print("测试结束")
        self.driver.quit()

    def test_Problem_solve(self):
        action = problem_handing_solve(self.driver)
        action.problem_handing()



if __name__ == '__main__':
    # unittest.main()

    addRule = TestProblemSolve()
    addRule.test_Problem_solve()
