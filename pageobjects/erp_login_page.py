# -*- coding: utf-8 -*-
from framework.base_page import BasePage


class LoginPage(BasePage):
    # 账号输入框
    accountName = "xpath=>//*[@id='app']/div[2]/div[2]/div[3]/div[1]/input"
    # 密码输入框
    passWord = "xpath=>//*[@id='app']/div[2]/div[2]/div[3]/div[2]/input"
    # 登录按钮
    submitButton = "xpath=>//*[@id='app']/div[2]/div[2]/div[3]/div[5]/button"
    # 选择公司
    companyBtn = "xpath=>//*[text()='qa-bs注册']"

    # 输入账号
    def type_accountName(self, text):
        self.type(self.accountName, text)

    # 输入密码
    def type_passWord(self, text):
        self.type(self.passWord, text)

    # 点击登录按钮
    def click_submit(self):
        self.click(self.submitButton)

    # 选择公司
    def choose_company(self):
        if self.find_element(self.companyBtn):
            self.click(self.companyBtn)
            print("选择目标公司成功")
        else:
            print("无需选择目标公司")
            pass

    def login_action(self, accountName, passWord):
        self.type_accountName(accountName)
        self.type_passWord(passWord)
        self.click_submit()
        self.choose_company()

