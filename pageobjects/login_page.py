# -*- coding: utf-8 -*-
from framework.base_page import BasePage


class LoginPage(BasePage):
    # 旧版登录页面
    # 公司名称输入框
    companyName = "xpath=>//*[@id='comName']"
    # 账号输入框
    accountName = "xpath=>//*[@id='userId']"
    # 密码输入框
    passWord = "xpath=>//*[@id='password']"
    # 登录按钮
    submitButton = "xpath=>//button/span"

    # 新版账号密码登录页面
    # 账号输入框
    newAccount = "xpath=>//*[@id='d_mobile']/div/input"
    # 密码输入框
    newPassword = "xpath=>//*[@id='d_mPwd']/div/input"
    # 登录按钮
    newSubmit = "xpath=>//*[@id='login']/span"

    # 输入公司名称
    def type_companyName(self, text):
        self.type(self.companyName, text)

    # 输入账号
    def type_accountName(self, text):
        self.type(self.accountName, text)

    # 输入密码
    def type_passWord(self, text):
        self.type(self.passWord, text)

    # 点击登录按钮
    def click_submit(self):
        self.click(self.submitButton)

    # 输入账号
    def type_Newaccount(self, text):
        self.type(self.newAccount, text)

    # 输入密码
    def type_Newpassword(self, text):
        self.type(self.newPassword, text)

    # 点击登录按钮
    def click_submit1(self):
        self.click(self.newSubmit)


