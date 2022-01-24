"""
数据中台首页
从数据中台首页进入各模块
"""
from time import sleep

from base.base import Base


class HomeEnter(Base):

    def enter_front(self, manner_over, path_over, manner, path):
        """
        首页进入各模块的前置操作,将鼠标移动到大模块之上，点击大模块下的各子模块
        :param manner_over:定位元素的方式
        :param path_over:定位元素方式的具体值
        :param manner: 定位元素的方式
        :param path: 定位元素方式的具体值
        :return: 无
        """
        module = (manner_over, path_over)
        submodules = (manner, path)
        self.switch_window(0)
        sleep(1)
        # 将鼠标移动到大模块之上
        self.mouse_over(module)
        # 点击大模块下的各子模块
        self.click(submodules)
        self.switch_window()
