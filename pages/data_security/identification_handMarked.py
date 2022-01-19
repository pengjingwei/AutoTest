from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from base.log import log
from pages.home_page import HomeEnter
from pages.login import Login


class HandMark(Base):
    dict_loc = {
        '手工标记': (By.ID, 'add'),
        '选择数据资产': (By.XPATH, '//*[@id="dataAssets"]/xm-select/div[2]'),
        '数据资产目录': (By.XPATH, '//*[@id="dataAssets"]/xm-select/div[3]/div/div[2]/div/div/div'),
        '预算管理一体化': (By.XPATH, '//*[@id="dataAssets"]/xm-select/div[3]/div/div[2]/div/div[2]/div[7]/div/div'),
        '预算信息': (By.XPATH, '//*[@id="dataAssets"]/xm-select/div[3]/div/div[2]/div/div[2]/div[7]/div[2]/div[4]/div/div'),
        '预算编制': (By.XPATH,
                 '//*[@id="dataAssets"]/xm-select/div[3]/div/div[2]/div/div[2]/div[7]/div[2]/div[4]/div[2]/div['
                 '1]/div[1]/div'),

        '单位收入预算表': (By.XPATH,
                    '//*[@id="dataAssets"]/xm-select/div[3]/div/div[2]/div/div[2]/div[7]/div[2]/div[4]/div[2]/div['
                    '1]/div[2]/div[2]/div'),
        '敏感数据标签': (By.XPATH, '//*[@id="sensitiveTab"]/xm-select/div[2]'),
        '预算年度_test': (By.XPATH, '//*[@id="sensitiveTab"]/xm-select/div[3]/div/div/div[3]/div[7]/i'),
        '保存': (By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]')
    }

    @log
    def marked(self):
        sleep(1)
        self.switch_frame('indexSrc')
        # 点击手工标记
        self.click(self.dict_loc['手工标记'])
        sleep(1)
        self.switch_frame('layui-layer-iframe2')

        # 点击选择数据资产
        self.click(self.dict_loc['选择数据资产'])
        # 选择数据资产目录
        self.click(self.dict_loc['数据资产目录'])

        # 选择预算管理一体化
        self.scroll_click(self.dict_loc['预算管理一体化'])
        # 选择预算信息
        self.scroll_click(self.dict_loc['预算信息'])
        # 选择预算编制
        self.scroll_click(self.dict_loc['预算编制'])
        # 选择单位收入预算表
        self.scroll_click(self.dict_loc['单位收入预算表'])

        # 点击敏感数据标签选择框
        self.click(self.dict_loc['敏感数据标签'])
        # 选择预算年度_test选项
        self.scroll_click(self.dict_loc['预算年度_test'])

        self.parent_frame()
        # 点击保存
        self.click(self.dict_loc['保存'])

        sleep(3)
        # 关闭当前窗口
        self.close()
        # 将窗口句柄切换回初始页
        self.switch_window(0)


if __name__ == '__main__':
    driver = webdriver.Chrome()

    login = Login(driver)
    login.login('admin', '123456')

    home = HomeEnter(driver)
    home.enter_front('id', '308', 'xpath', '//*[text()="敏感数据识别"]')

    mark = HandMark(driver)
    mark.marked()

    home.enter_front('id', '303', 'xpath', '//*[text()="元数据维护"]')
    sleep(5)
    driver.quit()
