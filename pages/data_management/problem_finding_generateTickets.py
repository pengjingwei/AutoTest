from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class GenerateTicket(Base):
    dict_loc = {
        # 场景测试123可以换成要定位的问题单名称
        '勾选框': (By.XPATH, '//div[text()="场景测试123"]/../../td[1]/div/div'),
        '生成问题单': (By.ID, 'geneQuestionSheet'),
        '标题': (By.ID, 'title'),
        '保存': (By.XPATH, '//a[text()="保存"]'),
        '确定': (By.XPATH, '//a[text()="确定"]'),
        '断言返回值': (By.XPATH, '//*[text()="新增成功！"]')
    }

    def ticket(self, title):
        """
        【数据管控】-【问题发现】-【生成问题单】
        :param title:问题单的标题
        :return: 弹出框中的文本信息
        """
        sleep(1)
        self.switch_frame('indexSrc')

        self.click(self.dict_loc['勾选框'])
        self.click(self.dict_loc['生成问题单'])
        self.input(self.dict_loc['标题'], title)
        sleep(1)
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
    enter.enter_front('id', '303', 'xpath', '//*[text()="问题发现"]')

    tickets = GenerateTicket(driver)
    res = tickets.ticket('预算测试')
    print(res)

    sleep(3)
    driver.quit()
