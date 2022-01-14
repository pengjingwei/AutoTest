from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def demo(username, password):
    driver = webdriver.Chrome()  # 实例化一个浏览器驱动

    url = 'http://172.16.101.71:19002/dataCenter/login.html'
    driver.get(url)  # 打开指定url网址

    driver.implicitly_wait(10)  # 设置隐式等待
    driver.maximize_window()  # 最大化窗口

    # 用户名输入框元素定位
    el = driver.find_element_by_id('username')  # 通过id属性定位
    # el = driver.find_element(By.ID, 'username')
    # el = driver.find_element_by_css_selector('input#username')  # 通过css选择器定位
    el.send_keys(username)  # 向用户名输入框输入
    # driver.find_element(By.ID, 'username').send_keys('admin')

    # 密码输入框元素定位
    ele = driver.find_element_by_name('password')  # 通过name属性定位
    ele.send_keys(password)  # 向密码输入框输入

    # 登录按钮元素定位
    element = driver.find_element_by_class_name('loginBtn')  # 通过class名称定位
    element.click()  # 点击按钮
    sleep(3)

    try:
        # 登录成功后的返回值
        res = driver.find_element(By.XPATH, "//a[@onclick='layuiBack()']").text  # 获取元素的文本信息

    except:
        res = driver.find_element(By.XPATH, "//*[@id='layui-layer100001']/div[2]").text
        driver.find_element(By.XPATH, '//*[@id="layui-layer100001"]/div[3]/a').click()
    finally:
        driver.quit()
    return res
