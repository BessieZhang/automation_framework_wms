# -*- coding:utf-8 -*-
from framework.base_page import BasePage

from framework.base_page import BasePage


class FrontPage(BasePage):
    # 版本更新弹窗按钮
    # submitButton = "xpath=>//*[@id='d_tipUpdate']/div/div[2]/span[2]/div/button/span"
    submitButton = "xpath=>//*[text()='我知道啦！']"
    # 修改密码弹窗关闭按钮
    closeBtn = "xpath=>//*[@id='d__uid_20_close']"
    # 切换仓库下拉按钮 //*[@id="showStorage"]
    showWarehouse = "xpath=>//*[@id='showStorage']"
    # 切换到自动化测试仓 //*[@id="24488001"]
    warehouseBtn = "xpath=>//*[text()='自动化测试仓勿动']"
    # 右上角账号名bessie
    accountnameList = "xpath=>//*[text()='bessie']"
    # 右上角下拉列表数据中心
    dataCenter = "xpath=>//*[text()='数据中心']"
    # 数据中心下载按钮
    downloadBtn = "xpath=>//*[text()='下载']"
    # 第一条下载数据的状态
    firstData = "xpath=>//tbody/tr/td/div/table/tbody/tr[1]/td[5]/div/span/font"
    # 第一条下载数据的下载次数
    firstdatadownloadNumber = "xpath=>//tbody/tr/td/div/table/tbody/tr[1]/td[7]/div"
    # 第一条下载数据的下载按钮
    firstdataDownload = "xpath=>//tbody/tr/td/div/table/tbody/tr[1]/td[8]/div/div/a[1]"
    # 下载二次验证输入框 //*[@id="d__uid_314"]/div/input //*[@id="d_exportPassword"]
    verificationInput = "xpath=>//*[@id='d_exportPassword']/div[2]/div/div/div/input"
    # 二次验证弹窗继续下载按钮
    verificationBtn = "xpath=>//*[@id='d_btnCheckPassword']"

    # 点击我知道了按钮
    def click_btn(self):
        if self.find_element(self.submitButton):
            self.click(self.submitButton)
        else:
            pass

    # 点击修改密码弹窗关闭按钮
    def click_colsebtn(self):
        if self.find_element(self.closeBtn):
            self.click(self.closeBtn)
        else:
            pass

    # 刷新页面后，关闭修改密码弹窗
    def refresh_and_close(self):
        self.refresh_window()
        self.click_colsebtn()

    # 切换到自动化测试仓勿动
    def switch_warehouse(self):
        self.click(self.showWarehouse)
        self.click(self.warehouseBtn)
        self.sleep(2)

    # 点击右上角账号名bessie
    def click_accountname(self):
        self.click(self.accountnameList)

    # 点击右上角数据中心
    def click_datacenter(self):
        self.click(self.dataCenter)

    # 获取第一条数据的状态并判断状态，成功则点击下载导出
    def get_status(self):
        status = self.find_element(self.firstData)
        if status.text == "成功":
            print("导出成功。")
        elif status.text == "等待中":
            self.sleep(2)
            self.get_status()

    # 获取第一条数据的下载次数
    def get_downloadnumber(self):
        num = self.find_element(self.firstdatadownloadNumber).text
        print("下载次数：%s" %num)
        return num

    # 点击第一条数据的下载按钮
    def click_downloadbtn(self):
        self.click(self.firstdataDownload)

    # 输入二次验证码，确认下载
    def input_verfication(self, text):
        self.type(self.verificationInput, text)
        self.click(self.verificationBtn)
        self.sleep(1)

