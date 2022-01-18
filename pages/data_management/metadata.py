
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base import Base
from base.log import log, consoleLog
from pages.home_page import HomeEnter


class MetaData(Base):
    """
    元数据维护模块
    【+】功能
    """

    @log
    def add_menu(self, name_text, text_flag=0, instruction_text='', flag=1):
        """
        【+】功能测试
        :param name_text:向名称输入框输入的内容
        :param instruction_text:向说明输入框输入的内容
        :param text_flag: 对说明输入框的输入控制，默认为0，可不输入，需要输入时，传入非0值
        :param flag: 保存或关闭按钮的点击，默认点击保存按钮，flag=0时，点击关闭按钮
        :return:获取到的弹窗的文本信息
        """

        sleep(1)
        self.switch_frame('indexSrc')

        button = (By.ID, 'addMenu')  # 【+】元素定位
        self.click(button)
        consoleLog('新增目录')

        self.switch_frame('layui-layer-iframe2')
        name = (By.ID, 'name')  # 弹出窗口中名称输入框定位
        self.input(name, name_text)

        js = 'document.querySelectorAll("select")[0].style.display="block";'  # js代码使下拉框样式变为可见
        self.execute_script(js)  # 执行上面的js代码
        sleep(1)
        select = (By.ID, 'datasourceId')  # 选择框的定位
        self.selector_text(select, 'SJZT_DATA_SHARE')

        if text_flag:
            instruction = (By.ID, 'remark')  # 说明输入框的定位
            self.input(instruction, instruction_text)

        if flag:
            self.parent_frame()
            save = (By.XPATH, '//*[text()="保存"]')  # 保存按钮的定位
            self.click(save)
            sleep(1)

            confirm_text = (By.XPATH, '//*[@id="layui-layer3"]/div[2]')  # 对确定弹窗文本信息的定位
            result = self.get_text(confirm_text)

            confirm = (By.XPATH, '//*[@id="layui-layer3"]/div[3]/a')  # 确定按钮的定位
            self.click(confirm)
            consoleLog(result)

            return result

        else:
            self.parent_frame()
            close = (By.XPATH, '//*[text()="关闭"]')  # 关闭按钮的定位
            self.click(close)
            consoleLog("取消新增")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    enter = HomeEnter(driver)
    enter.enter_front('admin', '123456', 'id', '303', 'xpath', '//*[@title="元数据维护"]')
    metadata = MetaData(driver)
    res = metadata.add_menu('自动化测试')
    print(res)
    driver.quit()
