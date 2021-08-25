# -*- coding:utf-8 -*-
import time
from framework.base_page import BasePage

class RightMenuPage(BasePage):
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
