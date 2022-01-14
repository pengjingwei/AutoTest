from time import sleep

from selenium import webdriver

from base.base import Base
from base.log import log
from pages.login import Login


class PolicyManage(Base):

    dataGovernance = ('id', '303')
    policyManage = ('xpath', "//*[@title='策略管理']")
    addStrategy = ('xpath', '//*[@id="addStrategy"]')

    layerSelect1 = ('xpath', "//*[@id='zeshu']/xm-select/div[2]")
    layerSelect2 = ('xpath', '//*[text()="数据分层"]')
    layerSelect3 = ('xpath', '//*[text()="ODS"]')

    sourceSelect1 = ('xpath', '//*[@id="zeshus"]/xm-select/div[2]')
    sourceSelect2 = ('xpath', '//*[text()="SJZT_DATA_SHARE"]')

    tableSelect1 = ('xpath', '//*[@id="zeshuss"]/xm-select/div[2]')
    tableSelect2 = ('xpath', '//*[text()="API_CONFIG"]')

    tableName = ('xpath', '//*[text()="API_APPLY_NAME"]')
    addPolicy = ('id', 'tjgz')
    name = ('id', 'rulenames')

    btn1 = ('xpath', '//*[@id="layui-layer2"]/div[3]/a[1]')
    btn2 = ('xpath', '//*[text()="保存并继续"]')

    policyName = ('id', 'mingc')
    policyDes = ('id', 'clms')

    btn3 = ('xpath', '//*[@id="layui-layer2"]/div[3]/a[1]')

    @log
    def enter_policy(self):
        login = Login(self.driver)
        login.login('admin', '123456')
        sleep(1)
        # 移动鼠标到【数据管控】上，点击【策略管理】，并切换到新打开的窗口
        self.mouse_over(self.dataGovernance)
        self.click(self.policyManage)
        self.switch_window()

    # text:添加规则的规则中文名
    # policyName：策略的策略名
    # policyDes:策略的描述
    @log
    def add_policy(self, text, policy_name, policy_des):
        """
        新增策略
        :param text: 规则字段名称
        :param policy_name: 策略名称
        :param policy_des: 策略详细描述
        :return: 新增策略元素
        """
        self.enter_policy()

        # 点击【新增策略】
        self.switch_frame('indexSrc')
        self.click(self.addStrategy)

        # 选择数据分层
        self.switch_frame('layui-layer-iframe1')
        self.click(self.layerSelect1)
        self.click(self.layerSelect2)
        self.click(self.layerSelect3)

        # 选择数据源
        self.click(self.sourceSelect1)
        self.click(self.sourceSelect2)

        # 选择数据表
        self.click(self.tableSelect1)
        self.click(self.tableSelect2)
        sleep(1)

        # 选择字段，并添加规则
        self.click(self.tableName)
        self.click(self.addPolicy)

        self.switch_frame('layui-layer-iframe2')
        self.clear(self.name)
        self.input(self.name, text)
        self.parent_frame()

        self.click(self.btn1)
        sleep(2)
        self.parent_frame()
        self.click(self.btn2)

        # 输入新增基本信息
        sleep(1)
        self.switch_frame('layui-layer-iframe2')

        self.input(self.policyName, policy_name)
        self.input(self.policyDes, policy_des)
        self.parent_frame()

        # 保存策略
        self.click(self.btn3)

        # 获取断言信息
        res = self.get_text(self.addStrategy)
        return res


if __name__ == '__main__':
    driver = webdriver.Chrome()
    policy = PolicyManage(driver)
    policy.add_policy('名称', '新增策略', '新增策略')
