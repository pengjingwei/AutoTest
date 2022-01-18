from unittest import TestCase

from ddt import ddt, unpack, data
from selenium import webdriver

from pages.home_page import HomeEnter
from pages.data_management.metadata import MetaData
from pages.login import Login
from util.readExcel import ReadExcel


@ddt
class TestAddMenu(TestCase):
    da = ReadExcel().read_execl(path=r'E:\PycharmProjects\workTest\report\testDate.xlsx')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    @data(*da)
    @unpack
    def test_addMenu(self, username, password, manner_over, path_over, manner, path, name_text, expect, text_flag=0,
                     instruction_text='', flag=1):
        # 登录
        login = Login(self.driver)
        login.login(username, password)

        # 从首页进入其他界面
        enter = HomeEnter(self.driver)
        enter.enter_front(manner_over, path_over, manner, path)

        # 元数据维护【+】功能
        metadata = MetaData(self.driver)
        if text_flag == '':
            text_flag = 0
        if flag == '':
            flag = 1
        res = metadata.add_menu(name_text, text_flag, instruction_text, flag)

        self.assertEqual(expect, res)


if __name__ == '__main__':
    test = TestAddMenu()
    test.test_addMenu()
