from unittest import TestCase

from selenium import webdriver

from pages.login import Login


class TestLogin(TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def testLogin(self):
        login = Login(self.driver)
        res = login.login('admin', '123456')
        expect = '退出系统'
        self.assertEqual(expect, res)


if __name__ == '__main__':
    test = TestLogin()
    test.testLogin()
