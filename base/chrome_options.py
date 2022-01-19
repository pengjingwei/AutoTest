'''
    Chrome浏览器的配置:
        通过webdriver启动的浏览器默认是零缓存（不读取本地缓存数据）的浏览器。相当于隐身浏览器，包括各类设置都是已经有的。
        options没有任何技术含量，所有的内容都是已经写死的内容
        一般就是一次编写，以后固定使用。
'''
from time import sleep

from selenium import webdriver


class ChromeOptions:
    def options(self):
        # chrome浏览器的配置项，可以通过修改默认参数，改变默认启动的浏览器的形态
        options = webdriver.ChromeOptions()
        # 将浏览器默认设置为最大窗体
        options.add_argument('start-maximized')
        # 设置默认窗体的启动大小

        # 去掉默认的提示自动化信息：没啥用，一般没有什么影响。警告条可能会导致页面内容的遮挡或者挤压，影响自动化测试
        options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        # 去掉控制台多余信息
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # 去掉账号密码弹窗
        prefs = {
            "credentials_enable_service": False,
            'profile.password_manager_enable': False
        }
        options.add_experimental_option("prefs", prefs)

        return options
