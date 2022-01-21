from unittest import TestCase
from selenium import webdriver

from pages.data_management.policy_addPolicy import AddPolicy


class TestAddPolicy(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_addPolicy(self):
        policy_manage = AddPolicy(self.driver)
        res = policy_manage.add_policy('名称', '自动化新增策略', '自动化新增策略')
        expect = '新增策略'
        self.assertEqual(expect, res)


if __name__ == '__main__':
    add_policy = TestAddPolicy()
    add_policy.test_addPolicy()
