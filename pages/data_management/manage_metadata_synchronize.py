from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class Synchronize(Base):
    dict_loc = {
        '展开预算信息': (By.XPATH, '//*[@id="ODSmenuTree"]/li/ul/li[1]/ul/li[3]/div/i[1]'),
        '预算编制': (By.XPATH, '//*[text()="预算编制"]'),
        '同步': (By.ID, 'synchronization'),
        '请选择类型': (By.XPATH, '//input[@placeholder="请选择类型"]/..'),
        '基础数据': (By.XPATH, '//dd[text()="基础数据"]'),
        '表名': (),  # 目前系统有bug，表名选项没有输入框，无法定位
        '确定': (By.XPATH, '//a[text()="确定"]')
    }

    def synchronize(self):
        """
        【数据管控】-【元数据维护】-【同步】
        :return:无
        """
        enter = HomeEnter(self.driver)
        enter.enter_front('id', '303', 'xpath', '//*[text()="元数据维护"]')
        sleep(1)
        self.switch_frame('indexSrc')
        self.click(self.dict_loc['展开预算信息'])
        self.click(self.dict_loc['预算编制'])
        sleep(1)
        self.click(self.dict_loc['同步'])
        self.switch_frame('layui-layer-iframe2')
        self.click(self.dict_loc['请选择类型'])
        self.scroll_click(self.dict_loc['基础数据'])
        # self.input(self.dict_loc['表名'], '预算测试表')
        self.parent_frame()
        self.click(self.dict_loc['确定'])

        sleep(2)
        self.close()
        self.switch_window(0)


if __name__ == '__main__':
    driver = webdriver.Chrome()

    login = Login(driver)
    login.login('admin', '123456')

    sync = Synchronize(driver)
    sync.synchronize()
    sleep(3)
    driver.quit()
