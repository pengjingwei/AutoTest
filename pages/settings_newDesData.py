from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class FiscalYEAR(Base):
    dict_loc = {
        '左侧目录加号展开预算信息': (By.XPATH, '//*[@id="demoTree"]/li/ul/li[1]/ul/li[3]/div/i[1]'),
        '进入预算编制': (By.XPATH, '//*[@id="demoTree"]/li/ul/li[1]/ul/li[3]/ul/li[1]/div/cite'),
        '编辑': (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/div[1]/a[1]'),
        '要脱敏的字段': (By.XPATH, '//*[@id="discernRuleId12"]/xm-select/div[2]'),
        '敏感规则': (By.XPATH, '//*[@id="discernRuleId12"]/xm-select/div[3]/div/div/div[2]/div[13]/i'),
        '脱敏条件': (By.XPATH, '/html/body/div[1]/form/div[1]/div/div[2]/table/tbody/tr[13]/td[9]/div/i'),
        '选择角色': (By.XPATH, '//*[@id="role"]/xm-select/div[2]'),
        '选中角色': (By.XPATH, '//*[@id="role"]/xm-select/div[3]/div/div/div[3]/div[4]/div'),
        '点击确定': (By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]'),
        '点击保存': (By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]')
    }

    def add_fiscal_year(self):
        self.switch_window()
        self.switch_frame('indexSrc')
        # 点击展开预算信息
        self.click(self.dict_loc['左侧目录加号展开预算信息'])
        # 点击预算编制
        self.click(self.dict_loc['进入预算编制'])
        # 点击“单位收入预算表”的编辑按钮
        self.click(self.dict_loc['编辑'])
        self.switch_frame('layui-layer-iframe2')
        # 定位滚动条导致不可见的元素
        # 第十三个字段
        self.scroll_click(self.dict_loc['要脱敏的字段'])
        # 定位敏感规则--MASK
        self.scroll_click(self.dict_loc['敏感规则'])
        # 点击脱敏条件
        self.click(self.dict_loc['脱敏条件'])
        # 进入iframe
        self.switch_frame('layui-layer-iframe1')
        # 点击选择角色框
        self.click(self.dict_loc['选择角色'])
        # 选择“然”角色
        self.scroll_click(self.dict_loc['选中角色'])
        self.parent_frame()
        # 点击确定
        self.click(self.dict_loc['点击确定'])
        self.parent_frame()
        # 点击保存
        self.click(self.dict_loc['点击保存'])


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # 登录中台
    login = Login(driver)
    login.login('admin', '123456')
    enter = HomeEnter(driver)
    enter.enter_front('id', '308', 'xpath', '//*[@title="脱敏设置"]')
    # 实例化
    addfisalyear = FiscalYEAR(driver)
    addfisalyear.add_fiscal_year()
    sleep(3)
    driver.quit()
