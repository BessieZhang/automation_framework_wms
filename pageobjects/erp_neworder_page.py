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
    warehouseSearch = "xpath=>//*[@id='d_querySingleEditor']/div[1]/input"
    warehouseName = "xpath=>//*[text()='对接wms自动化测试仓勿动']"
    # 快递公司
    expressInput = "xpath=>//*[text()='快递公司:']/../div/div/div/div[1]/input"
    expressName = "xpath=>//*[text()='德邦自动化测试勿动']"
    # 订单号
    orderNumber = "xpath=>//*[text()='订单号:']/../div/div/div/div/input"
    # 选择客户
    customerBtn = "xpath=>//*[@id='d_show_buyer']/div[2]/div/div/div[2]/div"
    # 选择买家弹窗查询框文本框
    customerSearch = "xpath=>//*[@id='d_customdd_textCondition']/div[1]/input"
    # 查询按钮
    customerEnter = "xpath=>//*[@id='d_customdd_textCondition']/div[2]/div"
    # 选择买家确认按钮
    customerSureBtn = "xpath=>//*[text()='确 认']"
    # 快速选择商品输入框
    goodsInput = "xpath=>//*[@id='d_container']/div/div/span/div/input"
    # 快速选择商品查询按钮
    goodsSearch = "xpath=>//*[@id='g_search_button']/div"
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
    def choose_WareHouse(self, text):
        try:
            self.click(self.warehouseInput)
            self.type(self.warehouseSearch, text)
            self.click(self.warehouseName)
        except Exception as e:
            print(e)

    # 选择快递公司
    def choose_Express(self, text):
        try:
            self.type(self.expressInput, text)
            self.click(self.expressName)
        except Exception as e:
            print(e)

    # 填写订单号
    def input_orderno(self, text):
        try:
            self.type(self.orderNumber, text)
            time.sleep(1)
        except Exception as e:
            print(e)

    # 选择客户
    def choose_customer(self, text):
        try:
            self.click(self.customerBtn)
            self.type(self.customerSearch, text)
            time.sleep(1)
            self.click(self.customerEnter)
            time.sleep(1)
            self.click(self.customerSureBtn)
        except Exception as e:
            print(e)

    # 输入商品编码，选择商品
    def input_goods(self, text):
        try:
            self.type(self.goodsInput, text)
            self.click(self.goodsSearch)
        except Exception as e:
            print(e)

    # 保存订单
    def save_Order(self):
        try:
            self.click(self.saveBtn)
        except Exception as e:
            print(e)

