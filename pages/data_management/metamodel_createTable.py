from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class CreateTable(Base):
    pass
    dict_loc = {
        'ODS': (By.XPATH, '//*[text()="ODS"]'),
        '选择数据库': (By.XPATH, '//*[@id="dataSourceId"]/../div/div'),
        'ODS_DB_TEST': (By.XPATH, '//dd[text()="ODS_DB_TEST"]'),
        '确定': (By.XPATH, '//a[text()="确定"]'),
        '断言返回值': (By.XPATH, '//*[text()="创建成功！"]')
    }

    def create_table(self, name):
        """
        【数据管控】-【元模型管理】-【创建表】
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
        sleep(0.5)
        str = '//*[text()="{}"]/../../td[11]/div/a[3]'.format(name)
        self.dict_loc['创建表'] = (By.XPATH, str)
        self.click(self.dict_loc['创建表'])
        self.click(self.dict_loc['确定'])
        result = self.get_text(self.dict_loc['断言返回值'])
        sleep(2)
        self.close()
        self.switch_window(0)
        return result


if __name__ == '__main__':
    driver = webdriver.Chrome()

    login = Login(driver)
    login.login('admin', '123456')

    table = CreateTable(driver)
    table.create_table()

    sleep(3)
    driver.quit()
