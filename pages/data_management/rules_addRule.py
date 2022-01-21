#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author: 高莽
@Software: PyCharm
@version: 2021.2.2
@file: rules_addRule.py
@time: 2022/1/21 9:31
"""
from random import randrange
from time import sleep

from base.base import Base
'''
【数据中台】-【数据管控】-【规则管理】
1.点击左上角的“新增规则”按钮；
2.选择“字段规则”，字段名为“TEST_PAY”，字段中文名为“测试金额”；
3.启用非空配置，启用条件为“is not null”；
4.不启用“数据范围配置”、“重复值配置”、“值域配置”；
5.点击“确定”按钮；
'''

class rules_addRule(Base):
    # ------------------1. 页面元素
    # 数据管控
    dataControl = ('xpath', '//a[@id="303"]')
    # 【规则管理】
    rule = ('link text', '规则管理')

    # 1.点击左上角的“新增规则”按钮；  layui-layer-iframe1
    addNewRule = ('id', "addNewRule")
    # 2.选择“字段规则”，字段名为“TEST_PAY”，字段中文名为“测试金额”；
    word_rule = ('id', 'rulename')
    word_input=('TEST_PAY')
    # 字段中文名为
    word_cname = ('xpath', '//input[@placeholder="请输入字段中文名"]')
    cname_input=('启用非空配置')
    # 3.启用非空配置，启用条件为“is not null”；
    is_null = ('xpath', '(//i[@class="layui-icon layui-icon-ok"])[1]')
    is_start = ('xpath', '(//textarea[@placeholder="请输入条件（需自审字段、语句正确性）"])[1]')
    # 名称非空
    rulename = ('columnids is not null ')
    # 4.不启用“数据范围配置”、“重复值配置”、“值域配置”；


    # 点击“确定”按钮；确定
    sure = ('link text', '确定')

    # 保存成功断言
    # save_assert = ('xpath', '//*[text()="退出"]')

    # ------------------2. 页面业务
    # @log
    def add_rule(self):
        # login = Login(self.driver)
        # login.login('admin', '123456')
        # sleep(1)
        # 移动鼠标到【数据共享】上，点击【规则管理】，并切换到新打开的窗口
        self.mouse_over(self.dataControl)
        sleep(1)
        self.click(self.rule)
        self.switch_window()
        self.switch_frame('indexSrc')
        # 点击新增按钮
        self.click(self.addNewRule)
        # 切换弹出框
        self.switch_frame('layui-layer-iframe1')
        # 字段名
        self.input(self.word_rule,self.word_input)
        sleep(0.5)

        # 字段中文名
        self.input(self.word_cname,self.cname_input)
        sleep(0.5)
        # 启用非空配置，启用条件为“ is not null”；
        self.scroll_loc(self.is_null)
        sleep(0.5)
        self.click(self.is_null)
        sleep(1)
        self.input(self.is_start,self.rulename)
        # 确定
        self.parent_frame()
        self.click(self.sure)