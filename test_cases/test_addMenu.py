from unittest import TestCase

from ddt import ddt, unpack, data
from selenium import webdriver

from pages.home_page import HomeEnter
from pages.metadata import MetaData
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
        enter = HomeEnter(self.driver)
        enter.enter_front(username, password, manner_over, path_over, manner, path)
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
