# -*- coding:utf-8 -*-
from common.readelement import Element
from page.webpage import WebPage

login = Element('login')

class Login_Page(WebPage):
    """ 登录类 """

    def switch_iframe(self):
        self.Switch_iframe(login['窗口切换'])

    def input_number(self, text):
        self.input_text(login['手机号'], text)

    def input_password(self, text):
        self.input_text(login['密码'], text)

    def Login_btn(self):
        self.is_click(login['登录'])

    def ingone_password(self):
        self.is_click(login['继续登录'])


if __name__ == '__main__':
    pass