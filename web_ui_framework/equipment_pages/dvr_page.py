
import os
import random

import pyautogui as ui
import time
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.getconfig import conf
class DvrPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","dvr")
    dvs_tab_locator = (By.XPATH,"//div[@role='tab' and text()='录像机']")
    camera_tab_locator = (By.XPATH,"//div[@role='tab' and text()='摄像机']")
    alarm_input_tab_locator = (By.XPATH,"//div[@role='tab' and text()='报警输入']")
    alarm_output_tab_locator = (By.XPATH,"//div[@role='tab' and text()='报警输出']")
    ip_talk_tab_locator = (By.XPATH,"//div[@role='tab' and text()='语音对讲']")
    # 批量按键
    batch_btn_locator = (By.XPATH,"//button[@id='batch']")
    # 导出模板按键
    download_btn_locator = (By.XPATH,"//li[@id='exportTemplate']")
    # 导入模板下载按键
    download_imp_tem_btn_locator = (By.XPATH,"//button[@id='downloadImportTemplate']")
    # 导入按键
    import_btn_locator = (By.XPATH,"//span[@class='ant-upload']")
    # 确认导入按键
    confirm_imp_btn_locator = (By.XPATH,"//button[text()=' 确认导入']")
    # 导入成功
    import_success_locator = (By.XPATH,"//span[text()='导入成功！']")
    # 批量-》添加按键
    # add_btn_locator = (By.XPATH,"//li[@id='dvrAdd']")
    add_btn_locator = (By.XPATH, "//li[@id='dvrAdd']//a")
    # IP开始段
    ip_start_locator = (By.XPATH,"//input[@id='ipAddressStart']")
    # IP结束段
    ip_end_locator = (By.XPATH,"//input[@id='ipAddressEnd']")
    # 设备数量
    dvs_number_locator =(By.XPATH,"//li[@class='ant-pagination-total-text']")
    # 确认批量添加按键
    confirm_add_btn_locator = (By.XPATH,"//span[text()='确 认']/parent::button")
    # 批量添加成功
    bat_add_success_locator = (By.XPATH,"//i[@class='anticon anticon-check-circle']/following::span")
    # 组织机构树
    org_tree_locator = (By.XPATH,"//span[@role='combobox']")
    # 顶级机构下的第一个下级机构
    first_sub_org_locator = (By.XPATH,"//ul[@role='tree-node']/li[2]//li[1]//span[@class='ant-select-tree-title']")
    # 顶级机构下的第一个下级机构的名字
    first_sub_org_name_locator = (By.XPATH,"//ul[@role='tree-node']/li[2]//li[1]//span[@class='ant-select-tree-title']/span")
    # 箭头
    arrow_btn_locator = (By.XPATH,"//ul[@role='tree-node']/li[2]/span[1]")
    def open_dvr(self):
        """打开安防设备-视频设备页面"""
        return self.driver.get(self.url)

    def switch_to_dvs(self):
        """切换到录像机标签页"""
        self.get_element(self.dvs_tab_locator).click()
        return self.driver.current_url

    def switch_to_camera(self):
        """切换到摄像机标签页"""
        self.get_element(self.camera_tab_locator).click()
        return self.driver.current_url

    def switch_to_alarm_input(self):
        """切换到报警输入标签页"""
        self.get_element(self.alarm_input_tab_locator).click()
        return self.driver.current_url

    def switch_to_alarm_output(self):
        """切换到报警输出标签页"""
        self.get_element(self.alarm_output_tab_locator).click()
        return self.driver.current_url

    def switch_to_ip_talk(self):
        """切换到语音对讲标签页"""
        self.get_element(self.ip_talk_tab_locator).click()
        return self.driver.current_url

    def download_dvr_template(self):
        """导出模板"""
        for a, b, c in os.walk(r"C:\Users"):
            for file in c:
                if file == "视频设备模板.xls":
                    os.remove(os.path.join(a,file))
                    break
        batch_elem = self.get_element(self.batch_btn_locator)
        self.ac_hover(batch_elem)
        download_elem = self.wait_element_clickable(self.download_btn_locator)
        self.ac_click(download_elem)
        time.sleep(5)
        for a,b,c in os.walk(r"C:\Users"):
            for file in c:
                if file == "视频设备模板.xls":
                    return True

    def download_imp_tem(self):
        """导入模板下载"""
        for a, b, c in os.walk(r"C:\Users"):
            for file in c:
                if file == "视频设备导入模板.xls":
                    os.remove(os.path.join(a,file))
                    break
        self.get_element(self.download_imp_tem_btn_locator).click()
        time.sleep(5)
        for a,b,c in os.walk(r"C:\Users"):
            for file in c:
                if file == "视频设备导入模板.xls":
                    return True

    def import_file(self,file_path):
        """导入视频设备"""
        number_locator = (By.XPATH,"//div[@id='noGateway']//h1")
        time.sleep(1)
        self.get_element(self.import_btn_locator).click()
        # 文件导入地址
        time.sleep(1)
        ui.write(file_path)
        time.sleep(2)
        ui.press("enter", 2)
        time.sleep(30)
        self.wait_element_clickable(self.confirm_imp_btn_locator).click()
        time.sleep(300)
        return self.wait_element_text(number_locator,"400")

    def batch_add_dvs(self):
        """批量添加视频设备"""
        # 添加前获取当前页面中的设备数量
        # n1 = int(((self.get_element(self.dvs_number_locator).text).split(' '))[1])
        # 生成随机IP
        ip = self.random_ip()
        end_number = ip.split('.')[-1]
        end_ip = ip.replace(end_number,str(int(end_number)+3))
        batch_elem = self.get_element(self.batch_btn_locator)
        self.ac_hover(batch_elem)
        time.sleep(0.5)
        add_elem = self.wait_element_clickable(self.add_btn_locator)
        self.ac_click(add_elem)
        self.get_element(self.ip_start_locator).send_keys(ip)
        time.sleep(0.5)
        self.get_element(self.ip_end_locator).send_keys(end_ip)
        time.sleep(0.5)
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        # n2 = int(((self.get_element(self.dvs_number_locator).text).split(' '))[1])
        return self.wait_element_text(self.bat_add_success_locator,"批量添加成功")

    def switch_org(self):
        """从顶级机构切换到其第一个下级机构"""
        while True:
            try:
                self.wait_element_clickable(self.org_tree_locator).click()
                break
            except Exception:
                continue
        self.wait_element_clickable(self.first_sub_org_locator).click()
        return self.wait_element_precence(self.first_sub_org_name_locator).get_attribute("innerText")


    def search_device(self):
        """搜索设备"""
        query_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-search-btn']")
        input_locator = (By.XPATH,"//input[@class='ant-input']")
        any_locator = (By.XPATH,"//div[@class='ant-tabs-tab-active ant-tabs-tab']")
        first_name_locator = (By.XPATH,"//tbody/tr[1]//a[@class='cms-Video-editName']")
        key_word = "新建DVR"
        while True:
            try:
                self.wait_element_clickable(query_btn_locator).click()
                break
            except Exception:
                continue
        self.get_element(input_locator).send_keys(key_word)
        time.sleep(1)
        self.get_element(any_locator).click()
        time.sleep(1)
        name = self.wait_element_visible(first_name_locator).text
        return key_word in name

    def del_device(self):
        """删除设备"""
        last_box_locator = (By.XPATH,"//tbody/tr[last()]//input")
        last_name_locator = (By.XPATH,"//tbody/tr[last()]//a[@class='cms-Video-editName']")
        del_btn_locator = (By.ID,"dvrCancel")
        confirm_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary ant-btn-sm']")
        while True:
            try:
                self.get_element(last_box_locator).click()
                break
            except Exception:
                continue
        name = self.get_element(last_name_locator).text
        self.get_element(del_btn_locator).click()
        self.get_element(confirm_btn_locator).click()
        return self.wait_element_not_text(last_name_locator,name)