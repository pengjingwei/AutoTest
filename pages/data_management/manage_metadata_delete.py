from selenium.webdriver.common.by import By

from base.base import Base


class Delete(Base):
    """
    元数据维护
    删除表功能
    """
    dict_loc = {
        '左侧树目录': (By.XPATH, '//*[@id="ODSmenuTree"]/li/ul/li[3]'),
        '删除': (By.XPATH, '//*[@id="index"]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[8]/div/a[2]'),
        '弹窗文本': (By.XPATH, '//*[@id="layui-layer2"]/div[2]'),
        '弹窗确定': (By.XPATH, '//*[@id="layui-layer2"]/div[3]/a[1]')
    }

    def delete_table(self):
        self.switch_frame("indexSrc")

        self.click(self.dict_loc['左侧树目录'])
        self.click(self.dict_loc['删除'])

        result = self.get_text(self.dict_loc['弹窗文本'])
        self.click(self.dict_loc['弹窗确定'])

        return result
