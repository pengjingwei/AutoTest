#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author: 高莽
@Software: PyCharm
@version: 2021.2.2
@file: subscription_viewData.py
@time: 2022/1/18 11:31
"""
from time import sleep

from selenium import webdriver

from base.base import Base
from base.log import log
from pages.login import Login


class subscription_viewData(Base):
    # 数据共享
    dataShare = ('xpath', '//a[@id="306"]')
    # 数据订阅
    databook = ('xpath', "//a[@title='数据订阅']")
    # addStrategy = ('xpath', '//*[@id="addStrategy"]')
    # 预算信息
    layerSelect1 = ('xpath', "(//i[@data-id='9595C93AA08043B1917EE755E74D6DDA'])[1]")
    # 【预算编制】
    layerSelect2 = ('xpath', '//cite[@data-title="预算编制"]')

    # layerSelect3 = ('xpath', '//*[text()="ODS"]')
    @log
    def share_viewData(self):
        login = Login(self.driver)
        login.login('admin', '123456')
        sleep(1)
        # 移动鼠标到【数据共享】上，点击【数据订阅】，并切换到新打开的窗口
        self.mouse_over(self.dataShare)
        self.click(self.databook)
        self.switch_window()
        '''
        【数据资产目录】-【预算管理一体化】-【预算信息】-【预算编制】，
        找到脱敏的表“单位收入预算表
        '''
        self.switch_frame('indexSrc')
        # 点击展开 预算信息
        self.click(self.layerSelect1)
        sleep(0.5)
        # 【预算编制】，
        self.click(self.layerSelect2)
