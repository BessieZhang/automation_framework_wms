# -*- coding:utf-8 -*-
import time
from framework.base_page import BasePage


class ReviewOrderPage(BasePage):
    # 销售一级菜单
    saleBtn = "xpath=>//*[text()='销售']"
    # 订单审核二级菜单
    orderreviewBtn = "xpath=>//*[@id='menuBar']/li[3]/ul/li[1]/ul/li[1]/span[1]"

    # 订单号查询框
    ordernoInput = "xpath=>//*[@id='d_approveForm']/div/table/tbody/tr[2]/td[2]/div/div/div/div/div/input"
    # 查询按钮
    searchBtn = "xpath=>//*[@id='d_btnAPQuery']/span/span"
    # 订单勾选框
    checkBox = "xpath=>//*[@id='d_gridTrade']/div[2]/table/tbody/tr/td/div/table/tbody/tr/td[2]/div/span/span"
    # 确认审核按钮
    reviewSureBtn = "xpath=>//*[@id='d_btnCommit']/span/span[2]"


    # 切换到订单审核iframe中
    def switch_iframe1(self, index):
        try:
            self.switch_iframe(index)
            self.sleep(2)
        except Exception as e:
            print(e)

    # 打开订单审核页面，切换到iframe
    def open_page(self):
        self.click(self.saleBtn)
        self.click(self.orderreviewBtn)
        time.sleep(2)
        self.switch_iframe1(2)

    # 填写订单号
    def input_orderno(self, text):
        try:
            self.type(self.ordernoInput, text)
            time.sleep(1)
        except Exception as e:
            print(e)

    # 点击查询按钮
    def search_Order(self):
        try:
            self.click(self.searchBtn)
        except Exception as e:
            print(e)

    # 勾选订单
    def check_Order(self):
        try:
            self.click(self.checkBox)
        except Exception as e:
            print(e)

    # 点击确认审核
    def click_ReviewBtn(self):
        try:
            self.click(self.reviewSureBtn)
        except Exception as e:
            print(e)
            