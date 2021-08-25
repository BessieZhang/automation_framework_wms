# -*- coding:utf-8 -*-
import time
from framework.base_page import BasePage


class CreateOrderPage(BasePage):
    # 销售一级菜单
    saleBtn = "xpath=>//*[text()='销售']"
    # 新增订单二级菜单
    createorderBtn = "xpath=>//*[@id='menuBar']/li[3]/ul/li[1]/ul/li[8]/span[1]"
    # 店铺名称
    shopnameInput = "xpath=>//*[text()='店铺名称:']/../div/div/div/div/input"
    shopName = "xpath=>//*[@id='d_ddShop']/div/div/div/div/table/tbody/tr/td"
    # 备注
    remarkInput = "xpath=>//*[text()='备注:']/div/div/div/div/input"
    # 仓库
    warehouseInput = "xpath=>//*[text()='仓库:']/../div/div/div/div[2]/div"
    warehouseName = "xpath=>//*[text()='对接wms自动化测试仓勿动']"
    # 快递公司
    expressInput = "xpath=>//*[text()='快递公司:']/../div/div/div/div[1]/input"
    expressName = "xpath=>//*[text()='德邦快递']"
    expressSureBtn = "xpath=>//*[text()='确认']"
    # 订单号
    orderNumber = "xpath=>//*[text()='订单号:']/../div/div/div/div/input"
    # 选择客户
    customerBtn = "xpath=>//*[text()='选择客户:']/../div/div/div/div[1]/input"
    # 选择买家弹窗查询框文本框
    customerSearch = "xpath=>//*[@id='d_customdd_textCondition']/div[1]/input"
    # 查询按钮 //*[@id="d__uid_874"]/div
    # 选择买家确认按钮
    customerSureBtn = "xpath=>//*[text()='确认']"
    # 商品编码输入框
    goodsInput = "xpath=>//*[@id='d__uid_408']/div[1]/input"
    # 保存按钮
    saveBtn = "xpath=>//*[@id='d_butSave']/span[1]"
    # 保存并新增按钮 //*[@id="d_butSaveAndAdd"]/span[1]
    saveandaddBtn = "xpath=>//*[@id='d_butSaveAndAdd']/span[1]"

    # 切换到订单查询iframe中
    def switch_iframe1(self, index):
        try:
            self.switch_iframe(index)
            self.sleep(2)
        except Exception as e:
            print(e)

    # 打开订单查询页面，切换到iframe
    def open_page(self):
        self.click(self.saleBtn)
        self.click(self.createorderBtn)
        time.sleep(2)
        self.switch_iframe1(2)

    # 选择店铺名称
    def choose_Shopname(self, text):
        try:
            self.type(self.shopnameInput, text)
            time.sleep(2)
            self.click(self.shopName)
        except Exception as e:
            print(e)

    # 选择仓库
    def choose_WareHouse(self):
        try:
            self.click(self.warehouseInput)
            self.click(self.warehouseName)
        except Exception as e:
            print(e)

    # 选择快递公司
    def choose_Express(self):
        try:
            self.click(self.expressInput)
            self.click(self.expressName)
            self.click(self.expressSureBtn)
        except Exception as e:
            print(e)

    # 输入


    # 选择客户

    # 输入商品编码，选择商品

    # 保存订单
    def save_Order(self):
        self.click(self.saveBtn)

