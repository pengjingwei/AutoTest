from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class MetamodelPush(Base):
    dict_loc = {
        'ODS': (By.XPATH, '//*[@id="demoTree"]/li/ul/li[12]/div/cite'),
        '选择数据库': (By.XPATH, '//*[@id="dataSourceId"]/../div/div'),
        'ODS_DB_TEST': (By.XPATH, '//dd[text()="ODS_DB_TEST"]'),
        '预算测试表': (By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/div'),
        '推送': (By.XPATH, '//button[text()="推送"]'),
        '来源': (By.XPATH, '//*[@placeholder="请输入来源"]'),
        '确定': (By.XPATH, '//*[text()="确定"]'),
        '断言返回值': (By.XPATH, '//*[text()="推送成功！"]')
    }

    def push(self, source):
        """
        【数据管控】-【元模型管理】-【推送】
        :param source:推送数据来源，
        :return:弹出框中的文本信息
        """
        enter = HomeEnter(self.driver)
        enter.enter_front('id', '303', 'xpath', '//*[text()="元模型管理"]')
        sleep(1)
        self.switch_frame('indexSrc')
        self.click(self.dict_loc['ODS'])
        sleep(1)
        self.click(self.dict_loc['选择数据库'])
        self.scroll_click(self.dict_loc['ODS_DB_TEST'])
        sleep(1)
        self.click(self.dict_loc['预算测试表'])
        self.click(self.dict_loc['推送'])

        self.switch_frame('layui-layer-iframe2')
        self.input(self.dict_loc['来源'], source)
        sleep(1)
        self.click(self.dict_loc['确定'])
        self.parent_frame()
        result = self.get_text(self.dict_loc['断言返回值'])
        sleep(3)
        self.close()
        self.switch_window(0)
        return result


if __name__ == '__main__':
    driver = webdriver.Chrome()

    login = Login(driver)
    login.login('admin', '123456')

    push = MetamodelPush(driver)
    res = push.push('ODS层的PAY_TEST')
    driver.quit()
    print(res)
