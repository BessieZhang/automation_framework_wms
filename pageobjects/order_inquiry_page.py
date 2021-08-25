# -*- coding:utf-8 -*-
import time
from framework.base_page import BasePage


class OrderInquiryPage(BasePage):
    # 出库一级菜单
    deliveryBtn = "xpath=>//*[text()='出库']"
    # 订单查询二级菜单
    orderInquiryBtn = "xpath=>//*[text()='订单查询']"
    timeBtn = "xpath=>//*[text()='近30天']"
    # 查询按钮
    searchBtn = "xpath=>//*[@id='d_btnSearch']"
    # 导出按钮
    exportBtn = "xpath=>//*[@id='d_btnExport']"
    # 确认导出按钮
    submitexportBtn = "xpath=>//*[@id='d_btnSubmitExport']"
    # 修改密码弹窗关闭按钮
    closeBtn = "xpath=>//*[@id='d__uid_20_close']"

    # 切换到订单查询iframe中
    def switch_iframe1(self, index):
        try:
            self.switch_iframe(index)
            # self.sleep(2)
        except Exception as e:
            print(e)

    # 打开订单查询页面，切换到iframe
    def open_page(self):
        self.click(self.deliveryBtn)
        self.click(self.orderInquiryBtn)
        time.sleep(2)
        self.switch_iframe1(1)

    # 查询近30天数据并导出
    def export_data(self):
        self.click(self.timeBtn)
        self.click(self.searchBtn)
        time.sleep(2)
        self.click(self.exportBtn)
        time.sleep(1)
        self.click(self.submitexportBtn)
        time.sleep(1)
        self.get_msgtext("导出任务生成成功")

    # 判断是否导出成功
    def get_msgtext(self, text):
        try:
            if text in self.driver.page_source:
                print("订单查询导出成功。")
            else:
                print("订单查询导出失败。")
        except Exception as e:
            print(e)

    # # 点击修改密码弹窗关闭按钮
    def click_colsebtn(self):
        if self.find_element(self.closeBtn):
            self.click(self.closeBtn)
        else:
            pass

    # 刷新页面后，关闭修改密码弹窗
    def refresh_and_close(self):
        self.refresh_window()
        self.click_colsebtn()
