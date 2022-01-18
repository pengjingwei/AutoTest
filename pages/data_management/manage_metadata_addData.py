#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author: 高莽
@Software: PyCharm
@version: 2021.2.2
@file: manage_metadata_addData.py
@time: 2022/1/18 16:02
"""
from time import sleep

from base.base import Base
from pages.login import Login


class AddData(Base):
    """
    元数据维护模块
    【移动目录】
    """
    # 页面元素
    # 数据管控
    dataControl = ('xpath', '//a[@id="303"]')
    # 数据维护 //a[@title='元数据维护']
    datarestore = ('xpath', '//a[@title="元数据维护"]')

    # 预算信息
    layerSelect1 = ('xpath', "(//i[@data-id='9595C93AA08043B1917EE755E74D6DDA'])[1]")
    # 【预算编制】
    layerSelect2 = ('xpath', '//cite[@data-title="预算编制"]')
    # 新增数据
    layerSelect3 = ('id', 'addData')
    # 类型 - 业务数据  //input[@placeholder='请选择类型']

    TypeSelect = ('xpath', '//input[@placeholder="请选择类型"]')
    Select01 = ('xpath', '//dd[text()="业务数据"]')

    # 表名 - 下拉框
    tablename = ('xpath', '//input[@placeholder="请输入编码"]')
    text="BGT_TABLE_01"

    # 表中文名
    tableCName = ('xpath', '//input[@placeholder="请输入名称"]')
    textCN="预算编制表01"
    # 来源 - 下拉框
    source = ('xpath', '//input[@placeholder="请输入来源"]')
    sourceText = "一体化部标"
    # 版本 - 下拉框
    vision = ('xpath', '//input[@placeholder="请输入版本"]')
    visionText = "V 4.2"
    # 保存 -
    save = ('link text', '保存')
    # 保存成功断言
    save_assert = ('xpath', '//*[text()="退出"]')

    # 页面业务
    def metadata(self):
        login = Login(self.driver)
        login.login('admin', '123456')
        sleep(1)
        # 移动鼠标到【数据共享】上，点击【数据订阅】，并切换到新打开的窗口
        self.mouse_over(self.dataControl)
        sleep(1)
        self.click(self.datarestore)
        self.switch_window()
        self.switch_frame('indexSrc')
        # 点击展开 预算信息
        self.click(self.layerSelect1)
        sleep(0.5)
        # 【预算编制】，
        self.click(self.layerSelect2)
        sleep(0.5)
        # 新增数据
        self.click(self.layerSelect3)
        sleep(0.5)
        # 切换弹出框  layui-layer-iframe2
        self.switch_frame('layui-layer-iframe2')
        # 类型
        self.click(self.TypeSelect)
        sleep(1)
        self.click(self.Select01)
        sleep(1)
        # 表名
        self.input(self.tablename,self.text)
        sleep(1)

        # 表中文名
        self.input(self.tableCName,self.textCN)
        sleep(1)

        # 来源
        self.input(self.source,self.sourceText)
        sleep(1)
        # 版本
        self.input(self.vision,self.visionText)
        sleep(1)
        # 保存

        self.click(self.save)
        # result = self.get_text(self.dict_loc['弹窗文本'])