from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


def test():
    # 实例化浏览器对象，获取到浏览器对象后就能对浏览器进行一系列操作
    driver = webdriver.Chrome()

    # 打开目标网址
    driver.get("http://172.16.101.71:19002/dataCenter/login.html")

    # 最大化窗口
    driver.maximize_window()

    # 设置隐式等待时间，等待10秒
    driver.implicitly_wait(10)

    # 定位用户名输入框
    ele = driver.find_element('id', 'username')
    # 向用户名输入框输入admin
    ele.send_keys('admin')

    # 定位密码输入框，并输入123456
    driver.find_element('name', 'password').send_keys('123456')

    # 定位登录按钮并点击
    driver.find_element('xpath', '//*[@id="loginBtn"]').click()

    # 强制等待1秒
    sleep(1)

    # 实例化鼠标事件
    ac = ActionChains(driver)

    # 定位【数据管控】元素
    element = driver.find_element('id', '303')

    # 执行将鼠标移动到【数据管控】上事件
    ac.move_to_element(element).perform()

    # 强制等待1秒
    sleep(1)

    # 定位【元数据维护】并点击
    driver.find_element('xpath', '//*[text()="元数据维护"]').click()

    # 获取所有浏览器的窗口句柄
    handles = driver.window_handles

    # 切换到最新打开的浏览器窗口
    driver.switch_to.window(handles[-1])

    # 进入名为indexSrc的frame框内
    driver.switch_to.frame('indexSrc')

    # 定位【+】并点击
    driver.find_element('id', 'addMenu').click()

    # 进入名为layui-layer-iframe2的frame框内
    driver.switch_to.frame('layui-layer-iframe2')

    # 定位名称输入框并输入123
    driver.find_element('id', 'name').send_keys('123')

    # 直接跳出frame框，返回到html
    # driver.switch_to.default_content()

    # 从名为layui-layer-iframe2的frame框返回到上级frame，即indexSrc
    driver.switch_to.parent_frame()

    # 定位【保存】按钮，并点击
    driver.find_element('xpath', '//*[@id="layui-layer2"]/div[3]/a[1]').click()

    # 获取弹窗中的文本信息
    result = driver.find_element('xpath', '//*[@id="layui-layer3"]/div[2]').text

    # 定位弹窗中的【确定】按钮并点击
    driver.find_element('xpath', '//*[@id="layui-layer3"]/div[3]/a').click()

    # 强制等待3秒
    sleep(3)

    # 关闭浏览器，释放资源
    driver.quit()

    # 函数返回值为获取的弹窗中的文本信息
    return result
