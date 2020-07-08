
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
import locale
locale.setlocale(locale.LC_CTYPE,"chinese")

class TimetempPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("basicdata_url", "timetemp")
    add_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-dashed']")
    input_name_locator = (By.XPATH,"//input[@id='name']")
    # 时间段1 开始时间
    t1_begin_locator = (By.XPATH,"//tr[1]/td[2]//input")
    # 时间段1 结束时间
    t1_end_locator = (By.XPATH,"//tr[1]/td[3]//input")
    sp1_begin_locator = (By.XPATH,"//tr[1]/td[2]/span/span")
    sp1_end_locator = (By.XPATH,"//tr[1]/td[3]/span/span")
    confirm_btn_locator = (By.XPATH,"//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']")
    add_success_locator = (By.XPATH,"//span[text()='添加成功']")
    # 模板数量
    li_locator = (By.XPATH,"//ul[@class='cms-TimeTemplate-siderList']/li")
    def open_timetemp(self):
        """打开时间管理页面"""
        return self.driver.get(self.url)

    def get_add_btn_elem(self):
        """获取添加按钮元素"""
        return self.get_element(self.add_btn_locator)

    def get_input_name_elem(self):
        """获取名称输入框元素"""
        return self.get_element(self.input_name_locator)

    def add_time_temp(self):
        """添加时间模板"""
        # 获取添加前的模板数量
        time.sleep(1)
        n1 = len(self.get_elements(self.li_locator))
        # 点击添加按钮
        self.get_add_btn_elem().click()
        t = time.strftime('time%m%d%H%M%S'.format(time.localtime(time.time())))
        # 输入模板名称
        self.get_input_name_elem().send_keys(t)
        time.sleep(1)
        begin_elem = self.get_element(self.t1_begin_locator)
        end_elem = self.get_element(self.t1_end_locator)
        # 修改input标签只读属性
        js_code = "arguments[0].readOnly = false;"
        self.driver.execute_script(js_code,begin_elem)
        self.driver.execute_script(js_code,end_elem)
        # 修改时间
        js_code_begin = "arguments[0].value ='09:00';"
        js_code_end = "arguments[0].value ='10:00';"
        self.driver.execute_script(js_code_begin,begin_elem)
        self.driver.execute_script(js_code_end,end_elem)
        time.sleep(1)
        # 模板信息填写完毕，点击确定
        self.get_element(self.confirm_btn_locator).click()
        time.sleep(1)
        n2 = len(self.get_elements(self.li_locator))
        return n2-n1