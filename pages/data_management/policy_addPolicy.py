from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from base.log import log
from pages.home_page import HomeEnter
from pages.login import Login


class AddPolicy(Base):
    dict_loc = {
        '新增策略': (By.XPATH, '//*[@id="addStrategy"]'),
        '请选择数据分层': (By.XPATH, "//*[@id='zeshu']/xm-select/div[2]"),
        '数据分层': (By.XPATH, '//*[text()="数据分层"]'),
        'ODS': (By.XPATH, '//*[text()="ODS"]'),
        '请选择数据源': (By.XPATH, '//*[@id="zeshus"]/xm-select/div[2]'),
        'ODS_DB_TEST': (By.XPATH, '//*[text()="ODS_DB_TEST"]'),
        '请选择数据表': (By.XPATH, '//*[@id="zeshuss"]/xm-select/div[2]'),
        'PAY_TEST': (By.XPATH, '//*[text()="PAY_TEST"]'),
        'TEST_PAY': (By.XPATH, '//*[text()="TEST_PAY"]'),
        '添加规则': (By.ID, 'tjgz'),
        '类型': (By.XPATH, '//*[@id="zhonglei"]/../div/div'),
        '测试金额': (By.XPATH, '//*[@id="zhonglei"]/../div/dl/dd[3]'),  # 可能会发生变化
        '字段名': (By.ID, 'rulename'),
        '字段中文名': (By.ID, 'rulenames'),
        '确定添加': (By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]'),
        '保存并继续': (By.XPATH, '//*[text()="保存并继续"]'),
        '项目名称': (By.XPATH, '//*[@id="compareType"]/../div/div'),
        '新增测试项目': (By.XPATH, '//*[@id="compareType"]/../div/dl/dd'),
        '策略名称': (By.ID, 'mingc'),
        '策略描述': (By.ID, 'clms'),
        '确定保存': (By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]'),
        '断言返回值': (By.XPATH, '//*[text()="新增成功!"]')
    }

    @log
    def add_policy(self, name, chinese_name, policy_name, policy_des):
        """
        新增策略
        :param name: 字段名
        :param chinese_name: 字段中文名
        :param policy_name: 策略名称
        :param policy_des: 策略详细描述
        :return: 弹出框中的文本信息
        """
        sleep(1)
        # 点击【新增策略】
        self.switch_frame('indexSrc')
        self.click(self.dict_loc['新增策略'])

        # 选择数据分层
        self.switch_frame('layui-layer-iframe1')
        self.click(self.dict_loc['请选择数据分层'])
        self.click(self.dict_loc['数据分层'])
        self.scroll_click(self.dict_loc['ODS'])

        # 选择数据源
        self.click(self.dict_loc['请选择数据源'])
        self.scroll_click(self.dict_loc['ODS_DB_TEST'])

        # 选择数据表
        self.click(self.dict_loc['请选择数据表'])
        self.scroll_click(self.dict_loc['PAY_TEST'])
        sleep(1)

        # 选择字段，并添加规则
        self.scroll_click(self.dict_loc['TEST_PAY'])
        sleep(1)
        self.click(self.dict_loc['添加规则'])

        self.switch_frame('layui-layer-iframe2')
        self.click(self.dict_loc['类型'])
        self.scroll_click(self.dict_loc['测试金额'])
        self.clear(self.dict_loc['字段名'])
        self.input(self.dict_loc['字段名'], name)
        self.clear(self.dict_loc['字段中文名'])
        self.input(self.dict_loc['字段中文名'], chinese_name)

        self.parent_frame()
        self.click(self.dict_loc['确定添加'])
        sleep(1)

        self.parent_frame()
        self.click(self.dict_loc['保存并继续'])

        # 输入新增基本信息
        sleep(1)
        self.switch_frame('layui-layer-iframe2')
        self.click(self.dict_loc['项目名称'])
        self.scroll_click(self.dict_loc['新增测试项目'])
        self.input(self.dict_loc['策略名称'], policy_name)
        self.input(self.dict_loc['策略描述'], policy_des)
        self.parent_frame()

        # 保存策略
        self.click(self.dict_loc['确定保存'])

        # 获取断言信息
        result = self.get_text(self.dict_loc['断言返回值'])
        sleep(3)
        self.close()
        self.switch_window(0)
        return result


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login = Login(driver)
    login.login('admin', '123456')
    enter = HomeEnter(driver)
    enter.enter_front('id', '303', 'xpath', '//*[text()="策略管理"]')
    policy = AddPolicy(driver)
    res = policy.add_policy('名称', '中文名', '新增策略', '新增策略')
    print(res)
    driver.quit()
