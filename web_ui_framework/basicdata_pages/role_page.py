
import locale

import time
import pyautogui as ui
import os
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")

class RolePage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("basicdata_url", "role")
    add_btn_locator = (By.XPATH,"//button[@title='添加']")
    input_name_locator = (By.XPATH,"//input[@name='Role.Name']")
    confirm_btn_locator = (By.XPATH,"//button[text()='确定']")
    confirm_download_btn_locator = (By.XPATH,"//button[text()='确认']")
    download_btn_locator = (By.XPATH,"//button[@title='导出']")
    confirm_upload_btn_locator = (By.XPATH,"//button[text()='确定导入']")
    upload_btn_locator = (By.XPATH,"//div[@id='excelImport']")
    upload_success_locator = (By.XPATH,"//div[@class='bootbox-body']")
    download_moudl_locator = (By.XPATH, "//button[@title='下载导入模板']")
    # 备注输入框
    remark_locator = (By.XPATH,"//textarea")
    # 主页中的备注信息
    info_locator = (By.XPATH,"//tr[@class='info']/td[2]")
    def open_role(self):
        """打开后台角色权限页面"""
        return self.driver.get(self.url)

    def get_add_btn_elem(self):
        """获取添加按钮元素"""
        return self.get_element(self.add_btn_locator)

    def get_input_name_elem(self):
        """获取名称输入框元素"""
        return self.get_element(self.input_name_locator)

    def get_confirm_btn_elem(self):
        """获取添加->确定按钮元素"""
        return self.get_element(self.confirm_btn_locator)

    def get_confirm_download_btn_elem(self):
        """获取导出->确定按钮元素"""
        return self.get_element(self.confirm_download_btn_locator)

    def get_confirm_upload_btn_elem(self):
        """获取导入->确定按钮元素"""
        return self.get_element(self.confirm_upload_btn_locator)

    def get_download_btn_elem(self):
        """获取导出按钮元素"""
        return self.get_element(self.download_btn_locator)

    def get_upload_btn_elem(self):
        """获取导入按钮元素"""
        return self.get_element(self.upload_btn_locator)

    def get_download_moudl_elem(self):
        """获取下载导入模板元素"""
        return self.get_element(self.download_moudl_locator)

    def add_role(self):
        """添加角色"""
        self.iframe_switch_wait()
        self.get_add_btn_elem().click()
        t = time.strftime('auto%m%d%H%M%S'.format(time.localtime(time.time())))
        self.wait_element_visible(self.input_name_locator).send_keys(t)
        time.sleep(1)
        self.get_element(self.remark_locator).send_keys("auto_test")
        time.sleep(1)
        self.get_confirm_btn_elem().click()
        time.sleep(1)
        self.driver.refresh()
        self.iframe_switch_wait()
        return self.get_element(self.info_locator).text

    def download_file(self):
        """导出角色信息"""
        # Chrome浏览器默认文件下载地址
        path = r"C:\Users"
        self.iframe_switch_wait()
        self.get_download_btn_elem().click()
        self.wait_element_clickable(self.confirm_download_btn_locator).click()
        time.sleep(3)
        t = time.strftime('%Y%m%d'.format(time.localtime(time.time())))
        file_name = f'角色导出数据_{t}'
        return self.find_file(path, file_name)


    def upload_file(self,file_path):
        """导入角色信息"""
        self.iframe_switch_wait()
        self.get_upload_btn_elem().click()
        time.sleep(1)
        ui.write(file_path)
        time.sleep(1)
        ui.press("enter",2)
        time.sleep(1)
        self.wait_element_clickable(self.confirm_upload_btn_locator).click()
        time.sleep(1)
        return self.wait_element_visible(self.upload_success_locator).text

    def download_moudle(self):
        """下载导入模板"""
        self.iframe_switch_wait()
        self.get_download_moudl_elem().click()
        path = r"C:\Users"
        file_name = "角色导入模板"
        time.sleep(3)
        return self.find_file(path,file_name)

    def edit_role(self):
        """编辑角色信息"""
        first_role_locator = (By.XPATH,"//table[@id='RoleListTable']/tbody/tr[1]")
        edit_btn_locator = (By.XPATH,"//p[@class='margin-top-sm']/a[3]")
        name_input_locator = (By.XPATH,"//input[@name='Role.Name']")
        confirm_btn_locator = (By.XPATH,"//div[@class='modal-footer']//button[@class='btn btn-primary']")
        first_role_name_locator = (By.XPATH,"//table[@id='RoleListTable']/tbody/tr[1]/td[1]")
        self.iframe_switch_wait()
        while True:
            try:
                self.get_element(first_role_locator).click()
                break
            except Exception:
                continue
        name = 'autotest'
        self.get_element(edit_btn_locator).click()
        time.sleep(1)
        self.get_element(name_input_locator).clear()
        time.sleep(1)
        self.get_element(name_input_locator).send_keys(name)
        self.get_element(confirm_btn_locator).click()
        return self.wait_element_text(first_role_name_locator,name)

    def del_role(self):
        """删除角色"""
        first_role_locator = (By.XPATH, "//table[@id='RoleListTable']/tbody/tr[1]")
        del_btn_locator = (By.XPATH, "//p[@class='margin-top-sm']/a[4]")
        confirm_btn_locator = (By.XPATH, "//div[@class='modal-footer']//button[@class='btn btn-primary']")
        first_role_name_locator = (By.XPATH, "//table[@id='RoleListTable']/tbody/tr[1]/td[1]")
        self.iframe_switch_wait()
        while True:
            try:
                self.get_element(first_role_locator).click()
                break
            except Exception:
                continue
        name = self.get_element(first_role_name_locator).text
        self.get_element(del_btn_locator).click()
        self.get_element(confirm_btn_locator).click()
        time.sleep(1)
        return self.wait_element_not_text(first_role_name_locator,name)

