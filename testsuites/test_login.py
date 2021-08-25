# -*- coding: utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage
from pageobjects.front_page import FrontPage


class LoginAction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    @staticmethod
    def old_loginway(self, companyname, accountname, password):
        loginpage = LoginPage(self.driver)
        time.sleep(2)
        loginpage.type_companyName(companyname)
        loginpage.type_accountName(accountname)
        loginpage.type_passWord(password)
        time.sleep(2)
        loginpage.click_submit()
        time.sleep(2)
        loginpage.get_windows_img()

        frontpage = FrontPage(self.driver)
        time.sleep(2)
        frontpage.click_btn()
        frontpage.click_colsebtn()

    @staticmethod
    def newe_loginway(self,newaccount, newpassword):
        loginpage = LoginPage(self.driver)
        time.sleep(2)
        loginpage.type_Newaccount(newaccount)
        loginpage.type_Newpassword(newpassword)
        time.sleep(2)
        loginpage.click_submit1()
        time.sleep(2)
        loginpage.get_windows_img()

        frontpage = FrontPage(self.driver)
        time.sleep(2)
        frontpage.click_btn()
        frontpage.click_colsebtn()
        frontpage.switch_warehouse()


if __name__ == '__main__':
    unittest.main()
