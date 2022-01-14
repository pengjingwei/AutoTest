
from base.base import Base
from base.log import log, consoleLog


class Login(Base):
    url = "http://172.16.101.71:19002/dataCenter/login.html"
    username = ('id', 'username')
    password = ('id', 'password')
    button = ('id', 'loginBtn')
    result = ('xpath', "//a[@onclick='layuiBack()']")

    @log
    def login(self, username, password):
        self.open(self.url)
        self.max_window()
        self.wait(10)

        self.input(self.username, username)
        self.input(self.password, password)
        self.click(self.button)
        consoleLog('登录成功')

        result = self.get_text(self.result)
        return result
