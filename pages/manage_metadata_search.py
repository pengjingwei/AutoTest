from selenium import webdriver
from selenium.webdriver.common.by import By


from time import sleep

from base.base import Base
from pages.home_page import HomeEnter


class Search(Base):
    def search_item(self, query_text):
        sleep(1)
        # 搜索框定位
        self.switch_frame('indexSrc')
        # 搜索框定位
        search_box = (By.XPATH, '//*[@id="keywords"]')
        # 输入查询内容
        self.input(search_box,query_text)
        # 查询图标定位
        search_icon = (By.XPATH, '//*[@id="index"]/div[1]/div[1]/div/i')
        # 点击查询图标
        self.click(search_icon)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    #登录中台
    enter = HomeEnter(driver)
    enter.enter_front('admin', '123456', 'id', '303', 'xpath', '//*[@title="元数据维护"]')
    search = Search(driver)
    search.search_item("PAY_VOUCHER")
    sleep(3)
    driver.quit()
