# -*- coding: utf-8 -*-
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage
from pageobjects.front_page import FrontPage
from testsuites.test_login import LoginAction
from pageobjects.order_inquiry_page import OrderInquiryPage
from  framework.logger import Logger

# create a logger instance
logger = Logger(logger="OrderInquiryPage").getlog()


class OrderInquiry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        # 登录系统
        LoginAction.newe_loginway(cls, '17826875820', 'bessie1234')

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    # @staticmethod
    def test_aorder_export(self):
        u"""测试订单查询--导出正常"""
        orderinquirypage = OrderInquiryPage(self.driver)
        time.sleep(2)
        orderinquirypage.open_page()
        orderinquirypage.export_data()
        orderinquirypage.get_msgtext("导出任务生成成功")
        orderinquirypage.refresh_and_close()

    def test_download_exportfile(self):
        u"""测试导出文件下载正常"""
        frontpage = FrontPage(self.driver)
        time.sleep(2)
        frontpage.click_accountname()
        frontpage.click_datacenter()
        frontpage.get_status()
        num1 = frontpage.get_downloadnumber()
        frontpage.click_downloadbtn()
        frontpage.input_verfication("M9cW")
        num2 = frontpage.get_downloadnumber()
        if len(num1) == 0:
            if int(num2) == 1:
                logger.info("导出下载成功。")
        elif len(num1) > 0:
            if int(num2) == int(num1) + 1:
                logger.info("导出下载成功。")
        else:
            logger.info("下载失败。")
        frontpage.refresh_and_close()


if __name__ == '__main__':
    unittest.main()
