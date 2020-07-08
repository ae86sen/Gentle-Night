
import locale
import random
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
import pyautogui as ui
locale.setlocale(locale.LC_CTYPE, "chinese")


class IPVoicePage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","ipvoice")
    # 添加语音对讲服务按键
    add_btn_locator = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    # 名称输入框
    name_input_locator = (By.XPATH, "//input[@id='name']")
    # ip输入框
    ip_input_locator = (By.XPATH, "//input[@id='ipAddress']")
    # 确认添加按键
    confirm_add_btn_locator = (By.XPATH, "//span[text()='确 认']/parent::button")
    # 添加成功图标
    add_success_locator = (By.XPATH, "//div[@class='ant-message-notice']//span")
    # 第一个对讲服务的菜单按键
    first_menu_locator = (By.XPATH, "//div[@id='voiceServerTable']//tbody/tr[1]//a")
    # 第一个对讲服务的编辑按键
    first_edit_locator = (By.XPATH, "//div[contains(@style,'absolute')][1]//a[@class]/span")
    # 第一个对讲服务的删除按键
    first_del_locator = (By.XPATH, "//ul[@id='voiceServerMenu']//a[@title='删除']/span")
    # 第一个对讲服务的导入按键
    first_import_locator = (By.XPATH, "//input[@type='file']")
    # 确认导入按键
    confirm_imp_btn_locator = (By.XPATH,"//button[text()=' 确认导入']")
    # 删除确认按键
    confirm_del_btn_locator = (By.XPATH, "//div[@class='ant-confirm-btns']/button[@class='ant-btn ant-btn-primary']")
    # 组织机构树
    org_tree_locator = (By.XPATH, "//span[@role='combobox']")
    # 顶级机构下的第一个下级机构
    first_sub_org_locator = (By.XPATH, "//ul[@role='tree-node']/li[2]//li[1]//span[@class='ant-select-tree-title']")
    # 顶级机构下的第一个下级机构的名字
    first_sub_org_name_locator = (
    By.XPATH, "//ul[@role='tree-node']/li[2]//li[1]//span[@class='ant-select-tree-title']/span")
    # 箭头
    arrow_btn_locator = (By.XPATH, "//ul[@role='tree-node']/li[2]/span[1]")
    # 中心主机数量
    host_number_locator = (By.XPATH,"//div[@id='IptalkHostTable']//li[1]")
    # 前端面板数量
    panel_number_locator = (By.XPATH,"//div[@id='IptalkPanelTable']//li[1]")
    # 报警输入数量
    alarm_number_locator = (By.XPATH,"//div[@id='VoiceAlarmInputTable']//li[1]")

    def open_ipvoice(self):
        """打开安防设备-语音对讲页面"""
        return self.driver.get(self.url)

    def add_voice_service(self,ip):
        """添加对讲服务"""
        type_locator = (By.XPATH,"//form//div[@class='ant-select-selection__rendered']/following-sibling::span")
        first_service_name =(By.XPATH,"//div[@id='voiceServerTable']//tbody/tr[1]/td[3]")
        name = time.strftime('%H%M%S'.format(time.localtime(time.time())))
        self.wait_element_clickable(self.add_btn_locator).click()
        self.wait_element_visible(self.name_input_locator).send_keys(name)
        self.wait_element_visible(self.ip_input_locator).send_keys(ip)
        self.get_element(type_locator).click()
        i = 2
        while i <=10:
            self.wait_element_clickable(self.confirm_add_btn_locator).click()
            try:
                result = self.wait_element_text(first_service_name, name)
            except Exception:
                self.get_element(type_locator).click()
                service_locator = (By.XPATH, f"//ul[contains(@class,'dropdown-menu-vertical')]//li[{i}]")
                self.get_element(service_locator).click()
                i += 1
                continue
            else:
                return result

    def edit_voice_service(self):
        """编辑对讲服务信息"""
        # 点击菜单
        self.wait_element_clickable(self.first_menu_locator).click()
        # 点击编辑
        self.wait_element_clickable(self.first_edit_locator).click()
        # 修改名称
        self.wait_element_visible(self.name_input_locator).send_keys("test")
        # 点击确定
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        return self.wait_element_text(self.add_success_locator,'修改成功')

    def del_voice_service(self):
        """删除对讲服务"""
        self.wait_element_clickable(self.first_menu_locator).click()
        self.wait_element_clickable(self.first_del_locator).click()
        self.wait_element_clickable(self.confirm_del_btn_locator).click()
        return self.wait_element_text(self.add_success_locator,"删除成功")

    def switch_org(self):
        """从顶级机构切换到其第一个下级机构"""
        self.wait_element_clickable(self.org_tree_locator).click()
        self.wait_element_clickable(self.arrow_btn_locator).click()
        self.wait_element_clickable(self.first_sub_org_locator).click()
        return self.wait_element_precence(self.first_sub_org_name_locator).get_attribute("innerText")

    def import_device(self,file_path):
        """导入设备"""
        self.wait_element_clickable(self.first_menu_locator).click()
        self.wait_element_clickable(self.first_import_locator).click()
        # 文件导入地址
        time.sleep(1)
        ui.write(file_path)
        time.sleep(2)
        ui.press("enter", 2)
        time.sleep(15)
        self.get_element(self.confirm_imp_btn_locator).click()
        time.sleep(70)
        self.driver.refresh()
        # 获取中心对讲主机数量
        n1:str = self.wait_element_visible(self.host_number_locator).text
        center_host_number = n1.split(' ')[1]
        # 获取前端面板数量
        n2:str = self.wait_element_visible(self.panel_number_locator).text
        panel_number = n2.split(' ')[1]
        # 获取报警输入数量
        n3:str = self.wait_element_visible(self.alarm_number_locator).text
        alarm_number = n3.split(' ')[1]
        return center_host_number,panel_number,alarm_number