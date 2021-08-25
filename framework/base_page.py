# -*- coding: utf-8 -*-
import time

from selenium.common.exceptions import NoSuchElementException
import os.path
from framework.logger import Logger
import random


# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器并停止测试
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def bace(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s." % e)

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        :return:
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # 定位单个元素方法
    def find_element(self, selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpath=> //*[@id='u1']/a[7]"
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == "id":
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == "name":
            try:
                element = self.driver.find_element_by_name(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == "c" or selector_by == "class_name":
            try:
                element = self.driver.find_element_by_class_name(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == "l" or selector_by == "link_text":
            try:
                element = self.driver.find_element_by_link_text(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == "p" or selector_by == "partial_link_text":
            try:
                element = self.driver.find_element_by_partial_link_text(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == "t" or selector_by == "tag_name":
            try:
                element = self.driver.find_element_by_tag_name(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == "x" or selector_by == "xpath":
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

        # 定位多个元素方法

    def find_elements(self, selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpath=> //*[@id='u1']/a[7]"
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        elements = ''
        if '=>' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == "id":
            try:
                elements = self.driver.find_elements_by_id(selector_value)
                logger.info("Had find the elements \' %s \' successful "
                            "by %s via value: %s " % (elements.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == "name":
            try:
                elements = self.driver.find_elements_by_name(selector_value)
                logger.info("Had find the elements \' %s \' successful "
                            "by %s via value: %s " % (elements.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == "c" or selector_by == "class_name":
            try:
                elements = self.driver.find_elements_by_class_name(selector_value)
                logger.info("Had find the elements \' %s \' successful "
                            "by %s via value: %s " % (elements.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == "l" or selector_by == "link_text":
            try:
                elements = self.driver.find_elements_by_link_text(selector_value)
                logger.info("Had find the elements \' %s \' successful "
                            "by %s via value: %s " % (elements.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == "p" or selector_by == "partial_link_text":
            try:
                elements = self.driver.find_elements_by_partial_link_text(selector_value)
                logger.info("Had find the elements \' %s \' successful "
                            "by %s via value: %s " % (elements.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == "t" or selector_by == "tag_name":
            try:
                elements = self.driver.find_elements_by_tag_name(selector_value)
                logger.info("Had find the elements \' %s \' successful "
                            "by %s via value: %s " % (elements.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == "x" or selector_by == "xpath":
            try:
                elements = self.driver.find_elements_by_xpath(selector_value)
                logger.info("Had find the elements successful "
                            "by %s via value: %s " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            try:
                elements = self.driver.find_elements_by_css_selector(selector_value)
                logger.info("Had find the elements \' %s \' successful "
                            "by %s via value: %s " % (elements.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return elements

    # 输入
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \'  in input box." % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s." % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s. " % e)
            self.get_windows_img()

    # 点击元素--单个
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \'s was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s." % e)
            self.get_windows_img()

    #
    # # 点击元素--多个
    # def click_s(self, selector):
    #     els = self.find_elements(selector)
    #     try:
    #         els.click()
    #         logger.info("The element \' %s \' was clicked." % el.text)
    #     except NameError as e:
    #         logger.error("Failed to click the element with %s." % e)
    #         self.get_windows_img()

    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s." % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds." % seconds)

    # 通过index切换iframe框架
    def switch_iframe(self, index):
        try:
            self.driver.switch_to.frame(index)
            logger.info("Had switch to the iframe.")
        except NameError as e:
            logger.error("Failed to switch the iframe.")
            self.get_windows_img()

    # 获取弹窗提示信息
    def get_alert_text(self):
        try:
            alert_switch = self.driver.switch_to.alert
            message = alert_switch.text
            print(message)
            logger.info("Had switch to the alert, alert message: %s." % message)
        except NameError as e:
            logger.error("Failed to get the alert message.")
            self.get_windows_img()

    # 获取报错提示信息：客户名称重复
    # def get_alert(self, text):
    #     try:
    #         if unicode(text) in self.driver.page_source:
    #             print(u"验证通过，系统提示与期望提示'%s'一致。" % text)
    #         else:
    #             print(u"验证失败，系统提示与期望提示'%s'不一致。" % text)
    #     except Exception as e:
    #         print(u"捕捉到异常信息: %s 。" % e)

    # 随机生成手机号
    def RandomPhone(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        randomPre = random.choice(prelist)
        Number = "".join(random.choice("0123456789") for i in range(8))
        phoneNum = randomPre + Number
        return phoneNum

    # 按照英文名搜索目标操作员:展开下拉、选择目标
    def search_objoperator(self, btn1, options, text):
        try:
            self.find_element(btn1).click()
            self.sleep(1)
            all_options = self.find_elements(options)
            self.sleep(1)
            print(len(all_options))
            for a in range(len(all_options)):
                if all_options[a].text == text:
                    obj_option = all_options[a]
                    print(obj_option.text)
                    obj_option.click()
                    break
                else:
                    pass
            self.sleep(1)
            # self.click(btn2)
            # self.sleep(2)
        except Exception as e:
            print(e)

    # 关闭版本更新弹窗
    def close_tipmessage(self, btn1):
        try:
            self.find_element(btn1).click()
            logger.info("Have finded the tipmessage and closed!")
        except:
            logger.info("No tipmessage finded!")
            pass

    # 刷新窗口
    def refresh_window(self):
        self.driver.refresh()
        self.sleep(2)
