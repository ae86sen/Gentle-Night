
import locale
import random

import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")

class AlarmHostPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","alarm")
    alarm_host_tab_locator = (By.XPATH,"//div[@role='tab' and text()='报警主机']")
    alarm_system_tab_locator = (By.XPATH,"//div[@role='tab' and text()='报警子系统']")
    alarm_zone_tab_locator = (By.XPATH,"//div[@role='tab' and text()='防区']")
    alarm_output_tab_locator = (By.XPATH,"//div[@role='tab' and text()='报警输出']")
    # 组织机构树
    org_tree_locator = (By.XPATH, "//span[@role='combobox']")
    # 顶级机构下的第一个下级机构
    first_sub_org_locator = (By.XPATH, "//ul[@role='tree-node']/li[2]//li[1]//span[@class='ant-select-tree-title']")
    # 顶级机构下的第一个下级机构的名字
    first_sub_org_name_locator = (
    By.XPATH, "//ul[@role='tree-node']/li[2]//li[1]//span[@class='ant-select-tree-title']/span")
    # 箭头
    arrow_btn_locator = (By.XPATH, "//ul[@role='tree-node']/li[2]/span[1]")
    # 添加报警服务按键
    add_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
    # 名称输入框
    name_input_locator = (By.XPATH,"//input[@id='name']")
    # ip输入框
    ip_input_locator = (By.XPATH,"//input[@id='ipAddress']")
    # 确认添加按键
    confirm_add_btn_locator = (By.XPATH,"//span[text()='确 认']/parent::button")
    # 添加成功图标
    add_success_locator = (By.XPATH,"//div[@class='ant-message-notice']//span")
    # 第一个报警服务的菜单按键
    first_menu_locator = (By.XPATH,"//div[@id='alarmServiceTable']//tbody/tr[1]//a")
    # 第一个报警服务的同步按键
    first_sync_locator = (By.XPATH,"//div[contains(@style,'absolute')][1]//a[text()='同步']")
    # 第一个报警服务的编辑按键
    first_edit_locator = (By.XPATH,"//div[contains(@style,'absolute')][1]//a[text()='编辑']")
    # 第一个报警服务的删除按键
    first_del_locator = (By.XPATH,"//ul[@id='alarmHostMenu']//a[@title='删除']/span")
    # 删除确认按键
    confirm_del_btn_locator = (By.XPATH,"//div[@class='ant-confirm-btns']/button[@class='ant-btn ant-btn-primary']")

    def open_alarm(self):
        """打开报警主机页面"""
        return self.driver.get(self.url)

    def switch_to_alarm_host(self):
        """切换到报警主机标签页"""
        self.wait_element_clickable(self.alarm_host_tab_locator).click()
        return self.driver.current_url

    def switch_to_alarm_system(self):
        """切换到报警系统标签页"""
        self.wait_element_clickable(self.alarm_system_tab_locator).click()
        return self.driver.current_url

    def switch_to_alarm_zone(self):
        """切换到报警防区标签页"""
        self.wait_element_clickable(self.alarm_zone_tab_locator).click()
        return self.driver.current_url

    def switch_to_alarm_output(self):
        """切换到报警输出标签页"""
        self.wait_element_clickable(self.alarm_output_tab_locator).click()
        return self.driver.current_url

    def switch_org(self):
        """从顶级机构切换到其第一个下级机构"""
        self.get_element(self.org_tree_locator).click()
        self.get_element(self.arrow_btn_locator).click()
        # time.sleep(2)
        self.wait_element_clickable(self.first_sub_org_locator).click()
        return self.wait_element_precence(self.first_sub_org_name_locator).get_attribute("innerText")

    def add_alarm_service(self):
        """添加报警服务"""
        name = time.strftime('%H%M%S'.format(time.localtime(time.time())))
        ip = self.random_ip()
        self.wait_element_clickable(self.add_btn_locator).click()
        self.wait_element_visible(self.name_input_locator).send_keys(name)
        self.wait_element_visible(self.ip_input_locator).send_keys(ip)
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        return self.wait_element_text(self.add_success_locator,'添加成功')

    def sync_alarm_service(self):
        """同步报警服务"""
        self.wait_element_clickable(self.first_menu_locator).click()
        self.wait_element_clickable(self.first_sync_locator).click()
        return self.wait_element_text(self.add_success_locator,'同步请求成功')

    def edit_alarm_service(self):
        """编辑报警服务信息"""
        # 点击菜单
        self.wait_element_clickable(self.first_menu_locator).click()
        # 点击编辑
        self.wait_element_clickable(self.first_edit_locator).click()
        # 修改名称
        self.wait_element_visible(self.name_input_locator).send_keys("test")
        # 点击确定
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        return self.wait_element_text(self.add_success_locator,'修改成功')

    def del_alarm_service(self):
        """删除报警服务"""
        self.wait_element_clickable(self.first_menu_locator).click()
        self.wait_element_clickable(self.first_del_locator).click()
        self.wait_element_clickable(self.confirm_del_btn_locator).click()
        return self.wait_element_text(self.add_success_locator,"删除成功")