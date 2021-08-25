# -*- coding: utf-8 -*-
import time
import unittest
import os.path
import random
from selenium import webdriver
from framework.browser_engine import BrowserEngine
from pageobjects.erp_login_page import LoginPage
from pageobjects.erp_neworder_page import CreateOrderPage
# from pageobjects.front_page import FrontPage


class LoginAction(unittest.TestCase):

    chrome_driver_path = os.path.dirname(os.path.abspath('.')) + '/tools/chromedriver'

    def setUp(self):
        options = webdriver.ChromeOptions()

        prefs = {
            'profile.default_content_setting_values':
                {
                    'notifications': 2
                }
        }

        options.add_experimental_option('prefs', prefs)

        self.driver = webdriver.Chrome(self.chrome_driver_path,options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://erp.hupun.com/login")
        time.sleep(2)

        self.loginpage = LoginPage(self.driver)
        self.loginpage.login_action('17826875820', 'bessie1234')
        time.sleep(2)

    # @classmethod
    # def setUpClass(cls):
    #     # browse = BrowserEngine(cls)
    #     driver = webdriver.Chrome(cls.chrome_driver_path)
    #     driver.get('https://erp.hupun.com/login')
    #     # cls.driver = browse.open_browser(cls)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    # @staticmethod
    def test_createorder(self):
        self.neworderpage = CreateOrderPage(self.driver)
        self.neworderpage.open_page()
        self.neworderpage.choose_Shopname('自动化测试店铺勿动')
        time.sleep(1)
        self.neworderpage.choose_WareHouse('对接wms自动化测试仓勿动')
        self.neworderpage.choose_Express('德邦自动化测试勿动')
        time.sleep(1)
        orderno = ''.join(random.sample(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 9))
        # print(orderno)
        self.neworderpage.input_orderno(orderno)
        time.sleep(1)
        self.neworderpage.choose_customer('自动化测试客户勿动')
        time.sleep(1)
        self.neworderpage.input_goods('au010')
        self.neworderpage.save_Order()
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
