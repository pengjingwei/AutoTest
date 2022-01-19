from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class Label(Base):
    dict_loc = {
        '新增': (By.ID, 'addTag'),
        '标签编码': (By.ID, 'code'),
        '标签名称': (By.ID, 'name'),
        '敏感级别': (By.XPATH, '//*[@id="levelId"]/../div[1]'),
        '一般': (By.XPATH, '//*[@id="levelId"]/../div/dl/dd[4]'),
        '敏感规则': (By.XPATH, '//*[@id="xmSelect"]/xm-select/div[2]'),
        '预算年度_测试': (By.XPATH, '//*[@id="xmSelect"]/xm-select/div[3]/div/div/div[2]/div[27]/div'),
        '加密方式': (By.XPATH, '//*[@id="encryptionModel"]/../div[1]'),
        'AES-128': (By.XPATH, '//*[@id="encryptionModel"]/../div[1]/dl/dd[2]'),
        '保存': (By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]')
    }

    def add_label(self, code, name):
        sleep(1)
        self.switch_frame('indexSrc')
        # 点击新增按钮
        self.click(self.dict_loc['新增'])
        sleep(1)
        self.switch_frame('layui-layer-iframe1')
        # 向标签编码输入框输入内容
        self.input(self.dict_loc['标签编码'], code)
        # 向标签名称输入框输入内容
        self.input(self.dict_loc['标签名称'], name)

        # 点击敏感级别选择框
        self.click(self.dict_loc['敏感级别'])
        # 选择‘一般’选项
        self.scroll_click(self.dict_loc['一般'])

        # 点击敏感规则选择框
        self.click(self.dict_loc['敏感规则'])
        # 选择‘预算年度_测试’选项
        self.scroll_click(self.dict_loc['预算年度_测试'])
        sleep(1)

        # 点击加密方式选择框
        self.scroll_click(self.dict_loc['加密方式'])
        # 选择‘AES-128’选项
        self.scroll_click(self.dict_loc['AES-128'])

        self.parent_frame()
        # 点击保存按钮
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
    home.enter_front('id', '308', 'xpath', '//*[text()="敏感标签设置"]')

    label = Label(driver)
    label.add_label(1024, '测试')
    driver.quit()
