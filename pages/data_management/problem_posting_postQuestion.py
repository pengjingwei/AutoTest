from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class PostQuestion(Base):
    dict_loc = {
        '勾选框': (By.XPATH, '//*[@lay-id="questionaireListTable"]/div[1]/div[2]/table/tbody/tr/td/div/div'),
        '发布问题': (By.ID, 'publishQues'),
        '选择用户': (By.XPATH, '//*[@id="userId"]/../div/div'),
        'jkl1109': (By.XPATH, '//dd[text()="jkl1109"]'),
        '保存': (By.XPATH, '//*[text()="保存"]'),
        '确定': (By.XPATH, '//a[text()="确定"]'),
        '断言返回值': (By.XPATH, '//*[text()="发布成功！"]')
    }

    def post(self):
        """
        【数据管控】-【问题发布】-【发布问题】
        :return:弹出框中的文本信息
        """
        sleep(1)
        self.switch_frame('indexSrc')
        self.click(self.dict_loc['勾选框'])
        self.click(self.dict_loc['发布问题'])
        self.click(self.dict_loc['选择用户'])
        self.scroll_click(self.dict_loc['jkl1109'])
        self.click(self.dict_loc['保存'])

        result = self.get_text(self.dict_loc['断言返回值'])
        sleep(1)
        self.click(self.dict_loc['确定'])

        sleep(1)
        self.close()
        self.switch_window(0)

        return result


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login = Login(driver)
    login.login('admin', '123456')

    enter = HomeEnter(driver)
    enter.enter_front('id', '303', 'xpath', '//*[text()="问题发布"]')

    post = PostQuestion(driver)
    res = post.post()
    print(res)
    driver.quit()
