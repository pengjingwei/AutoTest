from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class EditMenu(Base):
    """
    元数据维护模块
    【移动目录】
    """

    def move_menu(self):
        sleep(1)
        self.switch_frame('indexSrc')
        # 勾选框定位
        check_box = (By.XPATH, '//*[@id="index"]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/div')
        # el = self.location(check_box)
        # print(el)
        self.click(check_box)
        # 移动目录按钮
        editMenu = (By.ID, 'editMenu')
        self.click(editMenu)

        self.switch_frame('layui-layer-iframe2')
        # 数据分层选择框
        data_select = (By.XPATH, '//*[@id="modelIdCopy"]/xm-select')
        self.click(data_select)

        # 展开选项
        expand = (By.XPATH, '//*[@id="modelIdCopy"]/xm-select/div[3]/div/div[2]/div/div/i[1]')
        self.click(expand)

        # 要选择的目录
        menu = (By.XPATH, '//*[@id="modelIdCopy"]/xm-select/div[3]/div/div[2]/div/div[2]/div[4]')
        self.click(menu)

        # 返回上一级frame
        self.parent_frame()

        # 点击保存
        save = (By.XPATH, '//*[text()="保存"]')
        self.click(save)

        sleep(3)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login = Login(driver)
    login.login('admin', '123456')
    enter = HomeEnter(driver)
    enter.enter_front('id', '303', 'xpath', '//*[@title="元数据维护"]')
    eidt = EditMenu(driver)
    eidt.move_menu()
    driver.quit()
