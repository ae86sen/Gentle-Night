
import locale
import time

import os
import pyautogui as ui
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf


class DepartmentPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("basicdata_url","department")
    # 上传
    upload_button_locator = (By.XPATH,"//div[@id='excelImport']")
    # 确认按键
    confirm_btn_locator = (By.XPATH,"//button[@class='btn btn-primary']")
    # 导入成功
    upload_success_locator = (By.XPATH,"//div[@class='bootbox-body']")
    download_button_locator = (By.XPATH,"//button[@title='导出']")
    dowload_mould_btn_locator = (By.XPATH,"//button[@title='下载导入模板']")
    # 添加按键
    add_btn_locator = (By.XPATH,"//button[@class='btn btn-primary btn-sm']")
    # 部门名称输入框
    input_name_locator = (By.XPATH,"//input[@name='txtName']")
    # 添加部门成功后，页面新增的部门
    new_dep_locator = (By.XPATH,"//table[@class='jqx-grid-table']//tr[last()]")
    def open_department(self):
        """打开后台组织机构页面"""
        return self.driver.get(self.url)

    def get_upload_elem(self):
        """获取文件上传按钮元素"""
        return self.get_element(self.upload_button_locator)

    def get_confirm_btn_elem(self):
        """获取点击文件导入\导出\添加后，弹出的确认按钮元素"""
        return self.get_element(self.confirm_btn_locator)

    def get_upload_success_elem(self):
        """获取文件上传成功后的元素"""
        return self.get_element(self.upload_success_locator)

    def get_download_elem(self):
        """获取文件导出按钮元素"""
        return self.get_element(self.download_button_locator)

    def get_download_mould_elem(self):
        """获取下载导入模板按钮元素"""
        return self.get_element(self.dowload_mould_btn_locator)

    def get_add_dep_elem(self):
        """获取添加部门按钮元素"""
        return self.get_element(self.add_btn_locator)

    def get_input_name_elem(self):
        """获取部门名称输入框元素"""
        return self.get_element(self.input_name_locator)

    def upload_file(self):
        """文件导入"""
        self.iframe_switch_wait()
        self.get_upload_elem().click()
        time.sleep(1)
        # 文件导入地址
        ui.write((r"C:\Users\zhanglinsen\Downloads\mod.xls"))
        time.sleep(2)
        ui.press("enter", 2)
        time.sleep(1)
        self.get_confirm_btn_elem().click()
        time.sleep(1)
        return self.get_upload_success_elem().text

    def download_file(self):
        """文件导出"""
        locale.setlocale(locale.LC_CTYPE, "chinese")
        t = time.strftime('%Y年%m月%d日'.format(time.localtime(time.time())))
        # Chrome浏览器默认文件下载地址
        file_path = "C:\\Users\\zhanglinsen\\Downloads\\{}_部门.xls".format(t)
        self.iframe_switch_wait()
        self.get_download_elem().click()
        time.sleep(1)
        self.get_confirm_btn_elem().click()
        time.sleep(8)
        return os.path.exists(file_path)

    def download_mould(self):
        """下载导入模板"""
        self.iframe_switch_wait()
        self.get_download_mould_elem().click()
        time.sleep(8)
        file_path = "C:\\Users\\zhanglinsen\\Downloads\\部门导入模板.xls"
        return os.path.exists(file_path)


    def add_dep(self,name):
        """添加部门"""
        # //table[@class='jqx-grid-table']//tr[last()] 新增部门
        self.iframe_switch_wait()
        self.get_add_dep_elem().click()
        time.sleep(0.5)
        self.get_input_name_elem().send_keys(name)
        time.sleep(0.2)
        self.get_confirm_btn_elem().click()
        return self.wait_element_visible(self.new_dep_locator).text
