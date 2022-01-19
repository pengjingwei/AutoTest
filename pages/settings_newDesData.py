from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
from pages.home_page import HomeEnter
from pages.login import Login


class FiscalYEAR(Base):
    def add_fiscal_year(self, loc, value):
        self.switch_window()
        self.switch_frame('indexSrc')
        # 预算信息+号定位
        budget_information = (By.XPATH, '//*[@id="demoTree"]/li/ul/li[1]/ul/li[3]/div/i[1]')

        # 点击展开预算信息
        self.click(budget_information)
        # 预算编制定位
        budget_making = (By.XPATH, '//*[@id="demoTree"]/li/ul/li[1]/ul/li[3]/ul/li[1]/div/cite')
        # 点击预算编制
        self.click(budget_making)

        # 编辑定位
        edit = (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/div[1]/a[1]')
        # 点击编辑
        self.click(edit)

        # 切换到新的窗口
        # handles = Base.switch_window(index=-1)

        self.switch_frame('layui-layer-iframe2')
        # 定位滚动条导致不可见的元素
        # 第十三个字段--FISCAL_YEAR字段
        select_item = (By.XPATH, '//*[@id="discernRuleId12"]/xm-select/div[2]')
        # 点击该元素
        self.scroll_click(select_item)

        #self.quit_frame()
        # self.switch_frame('layui-layer-iframe4')
        # 定位敏感规则--MASK
        fascalyear_test = (By.XPATH, '//*[@id="discernRuleId12"]/xm-select/div[3]/div/div/div[2]/div[13]/i')
        self.scroll_click(fascalyear_test)
        # self.switch_frame('indexSrc')

        # 点击脱敏条件
        choose_role_edit = (By.XPATH, '/html/body/div[1]/form/div[1]/div/div[2]/table/tbody/tr[13]/td[9]/div/i')
        self.click(choose_role_edit)

        # 进入iframe
        self.switch_frame('layui-layer-iframe1')

        # 点击选择角色框
        choose_role = (By.XPATH, '//*[@id="role"]/xm-select/div[2]')
        self.click(choose_role)
        # 选择“然”角色
        select_role = (By.XPATH, '//*[@id="role"]/xm-select/div[3]/div/div/div[3]/div[4]/div')
        self.scroll_click(select_role)

        self.parent_frame()

        # 点击确定
        click_save = (By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]')
        self.click(click_save)
        self.parent_frame()


        #self.parent_frame()
        # 定位保存
        save = (By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]')
        self.click(save)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # 登录中台
    login = Login(driver)
    login.login('admin', '123456')
    enter = HomeEnter(driver)
    enter.enter_front('id', '308', 'xpath', '//*[@title="脱敏设置"]')

    addfisalyear = FiscalYEAR(driver)
    addfisalyear.add_fiscal_year(By.XPATH, '//*[@id="discernRuleId12"]/xm-select/div[3]/div/div/div[2]/div[19]/div')

    sleep(3)
    driver.quit()
