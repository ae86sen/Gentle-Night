

import locale
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")

class AutoRotationPage(BasePage):
    """定时轮巡页面"""
    url = conf.get_str("env", "url") + conf.get_str("config_center_url", "ar")
    # 添加按键
    add_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-dropdown-trigger ant-btn-primary']")
    # 删除按键
    del_btn_locator = (By.XPATH,"//button[@id='autoRotationMainDel']")
    # 名称输入框
    name_input_locator = (By.XPATH, "//input[@id='name']")
    # 添加分组轮巡
    add_group_locator = (By.XPATH,"//ul[@id='menu']/li[1]//span")
    # 添加视图轮巡
    add_view_locator = (By.XPATH,"//ul[@id='menu']/li[2]//span")
    # 定时轮巡添加按键
    add_auto_btn_locator = (By.XPATH,"//a/button[@class='ant-btn ant-btn-primary']")
    # 开始时间输入框
    start_time_input_locator = (By.XPATH,"//span[@class='ant-time-picker ']/input[@placeholder]")
    # 时间：小时
    hour_locator = (By.XPATH,"//div[@class='ant-time-picker-panel-combobox']/div[1]//li[contains(@class,'selected')]/following-sibling::li[1]")
    # 时间：分钟
    min_locator = (By.XPATH,"//div[@class='ant-time-picker-panel-combobox']/div[2]//li[contains(@class,'selected')]/following-sibling::li[2]")
    # 窗格选择按键-4窗格
    four_windows_locator = (By.XPATH,"//div[@class='cms-text-right']/a[2]")
    # 第一个窗口
    win_1st_locator = (By.XPATH,"//ul[contains(@class,'canvasFour')]/li[1]//input")
    # 第二个窗口
    win_2nd_locator = (By.XPATH,"//ul[contains(@class,'canvasFour')]/li[2]//input")
    # 第三个窗口
    win_3rd_locator = (By.XPATH,"//ul[contains(@class,'canvasFour')]/li[3]//input")
    # 第四个窗口
    win_4th_locator = (By.XPATH,"//ul[contains(@class,'canvasFour')]/li[4]//input")
    # 分组轮巡选择框
    select_group_locator = (By.XPATH,"//div[@id='timingGroupEditorSelect']//input")
    # 第一个分组
    first_group_locator = (By.XPATH,"//li[@role='option'][1]")
    # 随便点一下
    text_locator = (By.XPATH,"//label[@for='startTime']")
    # 轮巡规则配置页面的确认按键
    confirm_rule_btn_locator = (By.XPATH,"//form[@id='timingGroupEditorForm']/ancestor::div[@class='ant-modal-content']//button[@class='ant-btn ant-btn-primary']")
    # 确认添加按键
    confirm_add_btn_locator = (By.XPATH,"//span[text()='确 认']/parent::button")
    # 结果图标
    result_logo_locator = (By.XPATH, "//div[@class='ant-message-notice']//span")
    # 第一个规则的名称
    first_rule_name_locator = (By.XPATH,"//tbody/tr[1]/td[2]//span/a")
    # 第一条规则的复选框
    first_rule_box_locator = (By.XPATH,"//tbody/tr[1]/td[1]//input")
    # 删除确认按键
    confirm_del_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary ant-btn-sm']")


    def open_ar(self):
        """打开防范平台-定时轮巡页面"""
        return self.driver.get(self.url)

    # def add_rule(self):
    #     """添加定时轮巡规则"""
    #     self.steps(r"E:\MyGit\config_center_pages\auto_rotation_page.yaml")
    #     add_result_logo = self.wait_element_text(self.result_logo_locator, "操作成功")
    #     add_result_data = self.wait_element_text(self.first_rule_name_locator, "testinggggg")
    #     return add_result_logo, add_result_data
    def add_rule(self):
        """添加定时轮巡规则"""
        name = time.strftime('MR%H%M%S'.format(time.localtime(time.time())))
        # 点击添加
        self.get_element(self.add_btn_locator).click()
        # 点击分组定时轮巡
        self.get_element(self.add_group_locator).click()
        # 输入名称
        self.get_element(self.name_input_locator).send_keys(name)
        # 点击添加进入规则配置界面
        self.get_element(self.add_auto_btn_locator).click()
        # 输入开始时间
        self.wait_element_clickable(self.start_time_input_locator).click()
        self.wait_element_clickable(self.hour_locator).click()
        self.wait_element_clickable(self.min_locator).click()
        self.get_element(self.text_locator).click()
        # 选择四窗格
        self.get_element(self.four_windows_locator).click()
        # 勾选窗格
        self.get_element(self.win_1st_locator).click()
        self.get_element(self.win_2nd_locator).click()
        self.get_element(self.win_3rd_locator).click()
        self.get_element(self.win_4th_locator).click()
        # 选择分组
        self.get_element(self.select_group_locator).click()
        self.get_element(self.first_group_locator).click()
        self.get_element(self.text_locator).click()
        # 点击确认回到添加页面
        self.get_element(self.confirm_rule_btn_locator).click()
        # 点击确认
        self.get_element(self.confirm_add_btn_locator).click()
        add_result_logo = self.wait_element_text(self.result_logo_locator,"操作成功")
        add_result_data = self.wait_element_text(self.first_rule_name_locator,name)
        return add_result_logo,add_result_data

    def edit_rule(self):
        """编辑定时轮巡规则"""
        name = self.wait_element_precence(self.first_rule_name_locator).text
        self.wait_element_clickable(self.first_rule_name_locator).click()
        time.sleep(0.5)
        self.get_element(self.name_input_locator).send_keys('test')
        self.get_element(self.confirm_add_btn_locator).click()
        new_name = name + "test"
        edit_result_logo = self.wait_element_text(self.result_logo_locator,"操作成功")
        edit_result_data = self.wait_element_text(self.first_rule_name_locator,new_name)
        return edit_result_logo,edit_result_data

    def del_rule(self):
        """删除定时轮巡规则"""
        name =self.wait_element_precence(self.first_rule_name_locator).text
        # 勾选第一条
        self.get_element(self.first_rule_box_locator).click()
        # 点击删除-确认
        self.get_element(self.del_btn_locator).click()
        self.get_element(self.confirm_del_btn_locator).click()
        del_result_logo = self.wait_element_text(self.result_logo_locator,"删除成功")
        del_result_data = self.wait_element_not_text(self.first_rule_name_locator,name)
        return del_result_logo,del_result_data