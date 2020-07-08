
import locale
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")

class ManualRotationPage(BasePage):
    """风险时段手动轮巡页面"""
    url = conf.get_str("env", "url") + conf.get_str("config_center_url", "mr")
    # 添加按键
    add_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
    # 删除按键
    del_btn_locator = (By.XPATH,"//button[@id]")
    # 名称输入框
    name_input_locator = (By.XPATH, "//input[@id='name']")
    # 发送至客户端选择框
    select_client_locator = (By.XPATH,"//input[@id='bindIpAddress']")
    # 第一个客户端
    first_client_locator = (By.XPATH,"//li[@role='option'][1]")
    # 公共视图复选框
    view_box_locator = (By.XPATH,"//ul[@role='tree-node']/li/span[2]//span")
    # 随便点一下
    text_locator = (By.XPATH,"//label[@title='规则名称']")
    # 开始时间
    start_time_locator = (By.XPATH,"//input[@class='ant-time-picker-input' and @placeholder='开始']")
    # 结束时间
    end_time_locator = (By.XPATH,"//input[@class='ant-time-picker-input' and @placeholder='结束']")
    # 确认添加按键
    confirm_add_btn_locator = (By.XPATH,"//div/button[@class='ant-btn ant-btn-primary']")
    # 第一个规则的名称
    first_rule_name_locator = (By.XPATH,"//tbody/tr[1]/td[2]//a[@title]")
    # 结果图标
    result_logo_locator = (By.XPATH, "//div[@class='ant-message-notice']//span")
    # 时间：小时
    start_hour_locator = (By.XPATH,"//div[@class='ant-time-picker-panel-combobox']/div[1]//li[contains(@class,'selected')]/following-sibling::li[1]")
    end_hour_locator = (By.XPATH,"//div[@class='ant-time-picker-panel-combobox']/div[1]//li[contains(@class,'selected')]/following-sibling::li[2]")
    # 时间：分钟
    min_locator = (By.XPATH,"//div[@class='ant-time-picker-panel-combobox']/div[2]//li[contains(@class,'selected')]/following-sibling::li[2]")
    # 第一条规则的复选框
    first_rule_box_locator = (By.XPATH,"//tbody/tr[1]/td[1]//input")
    # 删除确认按键
    confirm_del_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary ant-btn-sm']")



    def open_mr(self):
        """打开防范平台-风险时段手动轮巡页面"""
        return self.driver.get(self.url)

    def add_rule(self):
        """添加手动轮巡规则"""
        name = time.strftime('MR%H%M%S'.format(time.localtime(time.time())))
        # 点击添加
        self.wait_element_clickable(self.add_btn_locator).click()
        # 输入规则名称
        self.get_element(self.name_input_locator).send_keys(name)
        # 选择发送客户端
        self.get_element(self.select_client_locator).click()
        self.get_element(self.first_client_locator).click()
        self.get_element(self.text_locator).click()
        # 选择视图
        self.get_element(self.view_box_locator).click()
        # 输入开始时间
        time.sleep(0.5)
        self.get_element(self.start_time_locator).click()
        self.get_element(self.start_hour_locator).click()
        self.get_element(self.min_locator).click()
        self.get_element(self.text_locator).click()
        # 输入结束时间
        time.sleep(0.5)
        self.get_element(self.end_time_locator).click()
        self.get_element(self.end_hour_locator).click()
        self.get_element(self.min_locator).click()
        self.get_element(self.text_locator).click()
        time.sleep(0.5)
        # 确认
        self.get_element(self.confirm_add_btn_locator).click()
        add_result_logo = self.wait_element_text(self.result_logo_locator,"添加成功")
        add_result_data = self.wait_element_text(self.first_rule_name_locator,name)
        return add_result_logo,add_result_data

    def edit_rule(self):
        """修改手动轮巡规则"""
        name = self.wait_element_precence(self.first_rule_name_locator).text
        # 点击第一条规则进入编辑页面
        self.wait_element_clickable(self.first_rule_name_locator).click()
        # 修改名称
        time.sleep(0.5)
        self.get_element(self.name_input_locator).send_keys("test")
        # 点击确定
        self.get_element(self.confirm_add_btn_locator).click()
        new_name = name + "test"
        edit_result_logo = self.wait_element_text(self.result_logo_locator,"修改成功")
        edit_result_data = self.wait_element_text(self.first_rule_name_locator,new_name)
        return edit_result_logo,edit_result_data

    def del_rule(self):
        """删除手动轮巡规则"""
        name = self.wait_element_precence(self.first_rule_name_locator).text
        # 勾选第一条
        self.get_element(self.first_rule_box_locator).click()
        # 点击删除-确认
        self.get_element(self.del_btn_locator).click()
        self.get_element(self.confirm_del_btn_locator).click()
        del_result_logo = self.wait_element_text(self.result_logo_locator,"删除成功")
        del_result_data = self.wait_element_not_text(self.first_rule_name_locator,name)
        return del_result_logo,del_result_data