
import locale

import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")



class AlarmLinkPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("alarm_url","alarmlink")
    add_btn_locator = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    # 启用按键
    start_btn_locator = (By.XPATH,"//div[@id='allDeviceContent']//input")
    # 名称输入框
    input_name_locator = (By.XPATH,"//input[@id='txtName']")
    # 网络异常复选框
    net_err_box_locator = (By.XPATH, "//input[@value='Server,NetError']")
    # 联动动作添加按键
    add_action_btn_locator = (By.XPATH, "//a[@id='addActions']")
    # 联动动作-接警中心人工处理
    manual_locator = (By.XPATH, "//li/a[text()='接警中心人工处理']")
    # 联动动作-朗读信息
    read_msg_locator = (By.XPATH, "//li/a[text()='朗读信息']")
    # 联动动作确认按键
    confirm_btn_locator = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    # 朗读内容输入框
    read_msg_input_locator = (By.XPATH,"//div[@class='DraftEditor-editorContainer']//div[@data-offset-key]")
    # 保存按键
    save_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary ant-btn-lg']")
    # 结果图标
    result_logo_locator = (By.XPATH, "//div[@class='ant-message-notice']//span")
    # 第一个联动规则名称
    first_rule_name_locator = (By.XPATH,"//tbody/tr[1]//a")
    # 第一个联动规则的复选框
    first_rule_box_locator = (By.XPATH,"//tbody/tr[1]//label//input")
    # 删除按键
    del_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-danger']")
    # 确认删除按键
    confirm_del_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary ant-btn-sm']")

    def open_alarmlink(self):
        """打开报警管理-联动规则页面"""
        return self.driver.get(self.url)

    def add_alarm_link(self):
        """添加联动规则-服务器-网络异常：接警中心人工处理+朗读信息"""
        name = time.strftime('AL%H%M%S'.format(time.localtime(time.time())))
        # 点击添加
        self.get_element(self.add_btn_locator).click()
        # 勾选启用
        self.get_element(self.start_btn_locator).click()
        # 输入规则名称
        self.get_element(self.input_name_locator).send_keys(name)
        # 勾选联动事件
        self.get_element(self.net_err_box_locator).click()
        # 点击添加联动动作
        self.wait_element_clickable(self.add_action_btn_locator).click()
        # 点击接警中心人工处理-确定
        self.wait_element_clickable(self.manual_locator).click()
        self.wait_element_clickable(self.confirm_btn_locator).click()
        # 点击添加联动动作
        self.wait_element_clickable(self.add_action_btn_locator).click()
        # 点击朗读信息
        self.wait_element_clickable(self.read_msg_locator).click()
        # 输入朗读内容-确定
        self.get_element(self.read_msg_input_locator).send_keys("autotesting")
        self.get_element(self.confirm_btn_locator).click()
        # 点击保存
        self.get_element(self.save_btn_locator).click()
        add_result_logo = self.wait_element_text(self.result_logo_locator,"保存成功")
        add_result_data = self.wait_element_text(self.first_rule_name_locator,name)
        return add_result_logo,add_result_data

    def edit_alarm_link(self):
        """编辑联动规则"""
        first_rule_name = self.get_element(self.first_rule_name_locator).text
        # 点击第一条规则进入编辑页面
        self.wait_element_clickable(self.first_rule_name_locator).click()
        # 修改名称
        self.get_element(self.input_name_locator).send_keys("test")
        # 保存
        self.get_element(self.save_btn_locator).click()
        new_name = first_rule_name + "test"
        edit_result_logo = self.wait_element_text(self.result_logo_locator,"保存成功")
        edit_result_data = self.wait_element_text(self.first_rule_name_locator,new_name)
        return edit_result_logo,edit_result_data

    def del_alarm_link(self):
        """删除联动规则"""
        del_rule_name = self.get_element(self.first_rule_name_locator).text
        # del_rule_locator = (By.XPATH,"//tbody//a[text()='{}']".format(del_rule_name))
        # 勾选第一条规则
        self.get_element(self.first_rule_box_locator).click()
        # 点击删除
        self.get_element(self.del_btn_locator).click()
        # 点击确认
        self.wait_element_clickable(self.confirm_del_btn_locator).click()
        self.driver.refresh()
        del_result_data = self.wait_element_not_text(self.first_rule_name_locator,del_rule_name)
        return del_result_data