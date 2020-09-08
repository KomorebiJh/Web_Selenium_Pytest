# -*- coding:utf-8 -*-
import re
import pytest

from common.readconfig import ini
from page_object.enterprise_loginpage import Login_Page


class TestLogin:

    @pytest.fixture(scope='function', autouse=True)
    def open_login(self, drivers):
        """ 打开登录页 """
        login = Login_Page(drivers)
        login.get_url(ini.url)

    def test_enterprise_login(self, drivers):

        loginpage = Login_Page(drivers)
        loginpage.switch_iframe()
        loginpage.input_number('13250292262')  # 调用页面对象中的方法
        loginpage.input_password('1234qwer')
        loginpage.Login_btn()  # 调用页面对象类中的点击登录按钮方法
        loginpage.wait(3)
        loginpage.ingone_password()
        loginpage.wait(3)

        try:
            assert 'MAXHUB会议管理后台' in drivers.title
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.',format(e))


if __name__ == '__main__':
    pytest.main(['TestCase/test_enterprise_login.py'])