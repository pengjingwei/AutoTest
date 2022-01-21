#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author: 高莽
@Software: PyCharm
@version: 2021.2.2
@file: problem_handing_solve.py
@time: 2022/1/21 11:06
"""
from time import sleep

from base.base import Base

'''
登录用户b，进入【数据中台】-【数据管控】-【问题处理】；
1.找到“预算测试”，点击右侧的“处理”按钮；
2.进入到问题单处理后，找到问题字段，点击右侧的“处理”按钮；
3.弹出的问题单处理，点击“确定”按钮；
4.保存后，勾选“预算测试”，点击左上角“提交处理结果”；
'''


class problem_handing_solve(Base):
    # ------------------1. 页面元素
    # 数据管控
    dataControl = ('xpath', '//a[@id="303"]')
    # 【问题处理】
    problem = ('link text', '问题处理')

    # 1.找到“预算测试”，点击右侧的“处理”按钮；
    check_problem = ('xpath', '(//i[@class="layui-icon layui-icon-ok"])[2]')
    problem_btn = ('xpath', '(//a[@class="caoZuoBtn caoZuoJuLiBtn"])[1]')

    # 2.进入到问题单处理后，找到问题字段，点击右侧的“处理”按钮；(//i[@class='layui-icon layui-icon-ok'])[5]
    choice_handle = ("xpath", "(//i[@class='layui-icon layui-icon-ok'])[5]")
    handle_btn = ("xpath", "(//a[@lay-event='handle'])[3]")

    # 3.切换，弹出的问题单处理，点击“确定”按钮；
    radio_method = ('xpath', '(//i[contains(@class,"layui-anim layui-icon")])[2]')

    # 4.保存后，勾选“预算测试”，点击左上角“提交处理结果”；
    # 点击“确定”按钮；确定
    sure_btn = ("xpath", "(//a[@class='layui-layer-btn0'])[2]")

    # 保存成功断言
    save_assert = ('xpath', '//*[text()="操作成功"]')
    # 弹出框关闭
    close_sure = ('xpath', "(//a[@class='layui-layer-btn0'])[2]")
    # 处理成功提交-确定
    handle_sure = ('link text', "确定")

    # 8.成功处理返回问题处理页面 提交处理结果
    handle_result = ('xpath', "//button[text()='提交处理结果']")

    # 9.信息提示弹出框   确定
    prompt_box = ('link text', "确定")

    # ------------------2. 页面业务
    # @log
    def problem_handing(self):
        # login = Login(self.driver)
        # login.login('admin', '123456')
        # sleep(1)

        # 1.移动鼠标到【数据共享】上，点击【问题处理】，并切换到新打开的窗口

        self.mouse_over(self.dataControl)
        sleep(1)
        self.click(self.problem)
        self.switch_window()
        self.switch_frame('indexSrc')

        # 2.点击右侧的“处理”按钮；
        self.click(self.check_problem)
        self.click(self.problem_btn)

        # 3.弹出的问题单处理，点击“确定”按钮；
        self.click(self.choice_handle)
        sleep(0.5)
        self.click(self.handle_btn)
        sleep(0.5)

        # 4.处理方式"忽视"；
        self.scroll_loc(self.radio_method)
        sleep(0.5)
        self.click(self.radio_method)

        sleep(1)

        # 5.确定
        # 操作成功
        self.click(self.sure_btn)
        sleep(0.5)

        # -----------断言---------
        self.assert_text(self.save_assert, "操作成功")

        # 6.关闭提示框
        self.click(self.close_sure)

        # 7.返回问题单处理页面 处理状态成功
        self.click(self.choice_handle)
        sleep(0.5)
        self.click(self.handle_sure)
        sleep(0.5)

        # 8.成功处理返回问题处理页面 提交处理结果//button[text()='提交处理结果']
        sleep(0.5)
        self.click(self.handle_result)
        sleep(0.5)

        # 9.信息弹出框关闭
        self.click(self.prompt_box)
        sleep(10)
