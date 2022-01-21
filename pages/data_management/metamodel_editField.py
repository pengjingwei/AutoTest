#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author: 高莽
@Software: PyCharm
@version: 2021.2.2
@file: metamodel_editField.py
@time: 2022/1/20 10:56
"""
from random import random, randrange
from time import sleep

from base.base import Base
from base.log import log
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


# 字段创建完成
class metamodel_editField(Base):
    # ------------------1. 页面元素
    # 数据管控
    dataControl = ('xpath', '//a[@id="303"]')
    # 元模型管理 //a[@title='元数据维护']
    model = ('link text', '元模型管理')

    # 1.点击左侧树选择数据分层为“ODS”层
    ODS = ('xpath', "//cite[@data-title='ODS']")
    # 2.返回frame 右上角资源库选择ODS_DB_TEST
    select_db = ('xpath', '//input[@placeholder="请选择"][1]')
    # 资源库选择ODS_DB_TEST
    ODS_DB_TEST = ('xpath', '//dd[text()="ODS_DB_TEST"]')
    # 3.选择表中文名为“预算测试表”的选项，点击右侧“编辑字段”按钮
    EditWord = ('xpath', '//a[@class="caoZuoBtn"][1]')
    # 4.切换frame进入后点击左上角“新增”按钮；
    AddFrame = "layui-layer-iframe4"
    AddWord = ('xpath', '//button[text()="新增"]')

    # 5.切换frame,名称设置为“测试ID”，字段设置为“TEST_ID”，类型为“NUMBER”，长度设为15，不可为空，是主键；
    # 名称
    num = str(randrange(100))
    print(num)
    AddModelFrame = "layui-layer-iframe1"
    name = ('xpath', '//input[@placeholder="请输入名称"]')
    wordtext = "测试ID_" + num

    # 字段名称
    CodeName = ('xpath', '//input[@lay-reqtext="字段名称不能为空"]')
    CodeText = "TEST_ID_" + num
    # 类型 - 下拉框
    type = ('xpath', '//input[@placeholder="请选择类型"]')
    selecttype = ('xpath', '//dd[@lay-value="2"]')
    # 长度设为15
    length = ('id', 'columnLength')
    # 是否为空 - 单选框
    is_null = ('xpath', '//div[@class="layui-unselect layui-form-radio"]//i[1]')

    # 是主键 - 单选框
    is_id = ('xpath', '(//i[@class="layui-anim layui-icon"])[3]')

    # 确定  返回 frame  self.parent_frame()
    save = ('xpath', '//button[text()="确定"]')
    # save = ('xpath', '//div[@class="layui-layer-btn layui-layer-btn-"]//a[1]')
    # 保存成功断言
    save_assert = ('xpath', '//*[text()="退出"]')

    # ------------------2. 页面业务
    @log
    def editfield(self):
        # login = Login(self.driver)
        # login.login('admin', '123456')
        # sleep(1)
        # 移动鼠标到【数据共享】上，点击【数据订阅】，并切换到新打开的窗口
        self.mouse_over(self.dataControl)
        sleep(1)
        self.click(self.model)
        self.switch_window()
        self.switch_frame('indexSrc')
        # 点击展开 ods
        self.click(self.ODS)
        sleep(0.5)
        # 切回主框架
        # self.parent_frame()
        # 【下拉框】ODS_DB_TEST，
        self.click(self.select_db)
        sleep(0.5)
        self.click(self.ODS_DB_TEST)
        sleep(0.5)

        #  3.选择表中文名为“预算测试表”的选项，点击右侧“编辑字段”按钮
        self.click(self.EditWord)

        sleep(0.5)
        # 切换弹出框
        self.switch_frame('layui-layer-iframe2')
        sleep(1)
        # 点击新增
        self.click(self.AddWord)
        sleep(1)
        # 新增数据模型弹出框  layui-layer-iframe1
        self.switch_frame(self.AddModelFrame)
        # 名称
        self.input(self.name, self.wordtext)
        sleep(1)
        # 字段名称
        self.input(self.CodeName, self.CodeText)
        sleep(1)

        # 类型
        self.click(self.type)
        if self.click(self.selecttype) != "DATE":
            # 长度
            self.input(self.length, '8')
            self.scroll_loc(self.save)
        sleep(1)
        # 是否为空
        self.click(self.is_null)
        sleep(1)
        # 是否主键
        self.click(self.is_id)
        sleep(1)
        # 确定
        self.click(self.save)
