from random import randrange

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class AddMetaData(Base):
    dict_loc = {
        # '左侧ODS节点': (By.XPATH, '//*[@id="demoTree"]/li/ul/li[12]/div/cite'),
        '右上方资源库': (By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[1]/div/div/input'),
        '选中ODS_DB_TEST': (By.XPATH, '/html/body/div[1]/div/div[1]/form/div[1]/div[1]/div/dl/dd[5]'),
        '新增': (By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/button[1]'),
        '选择方式': (By.XPATH, '//*[@id="addWarp"]/div[1]/div/div/div/input'),
        '选择“新增”方式': (By.XPATH, '//*[@id="addWarp"]/div[1]/div/div/dl/dd[2]'),
        '选择数据分层': (By.XPATH, '//*[@id="logic"]/xm-select/div[2]'),
        '点击数据资产目录': (By.XPATH, '//*[@id="logic"]/xm-select/div[3]/div/div[2]/div/div/div'),
        '点击预算管理一体化': (By.XPATH, '//*[@id="logic"]/xm-select/div[3]/div/div[2]/div/div[2]/div[1]/div/div'),
        '展开预算信息': (By.XPATH, '//*[@id="logic"]/xm-select/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div/div'),
        '选中预算编制': (By.XPATH, '//*[@id="logic"]/xm-select/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[3]/div['
                             '2]/div[1]/div'),
        '输入编码': (By.XPATH, '//*[@id="newAdd"]/div[1]/div/input'),
        '编码内容': str(randrange(100)),
        '点击输入中文表名': (By.XPATH, '//*[@id="newAdd"]/div[2]/div/input'),
        '表中文名': '预算测试表'+str(randrange(100)),
        '点击输入英文表名': (By.XPATH, '//*[@id="newAdd"]/div[3]/div/input'),
        '表名': 'PAY_TEST'+str(randrange(100)),
        '输入版本': (By.XPATH, '//*[@id="newAdd"]/div[4]/div/input'),
        '版本': '0.0.1',
        '保存': (By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]')
    }

    def add(self):
        self.switch_window()
        self.switch_frame('indexSrc')
        # 点击左侧ODS节点
        # self.click(self.dict_loc['左侧ODS节点'])
        # 点击右上方选择资源库
        sleep(0.5)
        self.click(self.dict_loc['右上方资源库'])
        sleep(0.5)
        self.click(self.dict_loc['选中ODS_DB_TEST'])
        # 点击新增
        self.click(self.dict_loc['新增'])
        sleep(0.5)
        self.click(self.dict_loc['选择方式'])
        self.click(self.dict_loc['选择“新增”方式'])
        self.click(self.dict_loc['选择数据分层'])
        self.click(self.dict_loc['点击数据资产目录'])
        self.click(self.dict_loc['点击预算管理一体化'])
        self.click(self.dict_loc['展开预算信息'])
        self.click(self.dict_loc['选中预算编制'])
        self.input(self.dict_loc['输入编码'], self.dict_loc['编码内容'])
        self.input(self.dict_loc['点击输入中文表名'], self.dict_loc['表中文名'])
        self.input(self.dict_loc['点击输入英文表名'], self.dict_loc['表名'])
        self.input(self.dict_loc['输入版本'], self.dict_loc['版本'])
        self.click(self.dict_loc['保存'])


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # 登录中台
    login = Login(driver)
    login.login('admin', '123456')
    enter = HomeEnter(driver)
    enter.enter_front('id', '303', 'xpath', '//*[@title="元模型管理"]')
    # 实例化
    add_meta_data = AddMetaData(driver)
    add_meta_data.add()
    sleep(3)
    driver.quit()
