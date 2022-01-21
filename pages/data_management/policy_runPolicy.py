from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class RunPolicy(Base):
    dict_loc = {
        '运行按钮': (By.XPATH, '/html/body/div/form/div/div[1]/div[2]/table/tbody/tr[1]/td[7]/div/a[1]'),
        '确定': (By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]'),
        '确定启动成功': (By.XPATH, '//*[@id="layui-layer2"]/div[3]/a'),
        '文本内容': (By.XPATH, '//*[text()="策略启动成功！"]')
    }

    def run_policy(self):
        # sleep(1)
        self.switch_window()
        self.switch_frame('indexSrc')
        sleep(0.5)
        self.click(self.dict_loc['运行按钮'])
        sleep(0.5)
        self.click(self.dict_loc['确定'])
        sleep(0.5)
        result = self.get_text(self.dict_loc['文本内容'])
        # result = driver.find_element(self.dict_loc['文本内容']).text
        print(result)
        self.click(self.dict_loc['确定启动成功'])
        # self.assertEqual(exp, result)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login = Login(driver)
    login.login('admin', '123456')
    enter = HomeEnter(driver)
    enter.enter_front('id', '303', 'xpath', '//*[text()="策略管理"]')
    # exp = "策略启动成功！"
    policy = RunPolicy(driver)
    policy.run_policy()
    sleep(3)
    driver.quit()
