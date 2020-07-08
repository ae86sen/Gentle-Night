
import locale

import os
import pyautogui as ui
import time

from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")

class EmployeePage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("basicdata_url","employee")
    steps_path = os.path.join(os.path.dirname(__file__), "employee_page_steps.yaml")
    # 导入人员列表按钮
    upload_emp_locator = (By.XPATH,"//div[@id='excelImport']")
    # 确定导入按钮
    confirm_uoload_btn_locator = (By.XPATH,"//button[text()='确定导入']")
    # 导入成功
    upload_success_locator = (By.XPATH, "//div[@class='bootbox-body']")
    # 添加人员按钮
    add_emp_locator = (By.XPATH,"//a[@class='btn btn-primary btn-sm']")
    # 姓名输入框
    input_name_locator = (By.XPATH,"//input[@name='txtEmpName']")
    # 保存按钮
    save_btn_locator = (By.XPATH,"//button[@class='btn btn-primary' and text()='保存']")
    # 人员已存在弹窗的关闭按钮
    close_btn_locator = (By.XPATH,"//button[@class='btn btn-primary' and text()='确认']")
    # 导出按钮
    download_btn_locator = (By.XPATH,"//a[@class='btn btn-default btn-sm']")
    # 导出确认按钮
    confirm_btn_locator = (By.XPATH,"//button[@class='btn btn-primary' and text()='确认']")
    # 下载导入模板
    download_moudl_locator = (By.XPATH,"//button[@title='下载导入模板']")
    # 人员编码
    td_locator = (By.XPATH,"//tbody/tr[1]/td[2]")
    def open_employee(self):
        """打开后台人员列表页面"""
        return self.driver.get(self.url)

    def get_upload_emp_elem(self):
        """获取人员列表导入按钮元素"""
        return self.get_element(self.upload_emp_locator)

    def get_confirm_upload_elem(self):
        """获取确认导入人员列表按钮元素"""
        return self.get_element(self.confirm_uoload_btn_locator)

    def get_upload_success_elem(self):
        """获取上传成功元素"""
        return self.get_element(self.upload_success_locator)

    def get_add_emp_elem(self):
        """获取添加人员按钮元素"""
        return self.get_element(self.add_emp_locator)

    def get_input_name_elem(self):
        """获取人员姓名输入框元素"""
        return self.get_element(self.input_name_locator)

    def get_save_btn_elem(self):
        """获取保存按钮元素"""
        return self.get_element(self.save_btn_locator)

    def get_close_btn_elem(self):
        """获取人员名称存在时的弹窗的关闭按钮元素"""
        return self.get_element(self.close_btn_locator)

    def get_download_btn_elem(self):
        """获取导出按钮元素"""
        return self.get_element(self.download_btn_locator)

    def get_confirm_btn_elem(self):
        """获取导出确认按钮元素"""
        return self.get_element(self.confirm_btn_locator)

    def get_download_moudl_elem(self):
        """获取下载导入模板元素"""
        return self.get_element(self.download_moudl_locator)

    def upload_emp_file(self,file_path):
        """导入人员列表"""
        self.iframe_switch_wait()
        self.get_upload_emp_elem().click()
        time.sleep(1)
        # 文件导入地址
        ui.write(file_path)
        time.sleep(2)
        ui.press("enter", 2)
        time.sleep(1)
        self.get_confirm_upload_elem().click()
        time.sleep(1)
        return self.get_upload_success_elem().text

    def add_emp(self):
        """添加人员"""
        self.iframe_switch_wait()
        # 获取添加人员之前第一行人员的编码
        n1 = int(self.get_element(self.td_locator).text)
        # 点击添加人员
        self.get_add_emp_elem().click()
        t = time.strftime('t%H%M%S'.format(time.localtime(time.time())))
        # 输入名称
        self.get_input_name_elem().send_keys(t)
        # 点击保存
        self.get_save_btn_elem().click()
        time.sleep(1)
        self.driver.refresh()
        self.iframe_switch_wait()
        # while True:
        #     # 判断人员已存在的弹框元素是否存在，若存在，则重新输入；反之，则退出循环
        #     if self.isElementExist(self.close_btn_locator) == True:
        #         self.get_close_btn_locator().click()
        #         time.sleep(1)
        #         self.get_input_name_elem().clear()
        #         time.sleep(0.5)
        #         name += '1'
        #         self.get_input_name_elem().send_keys(name)
        #         time.sleep(0.5)
        #         self.get_save_btn_elem().click()
        #         continue
        #     else:
        #         break
        # 获取添加人员后第一行人员的编码
        n2 = int(self.get_element(self.td_locator).text)
        return n2-n1

    def download_file(self):
        """导出人员信息"""
        # Chrome浏览器默认文件下载地址
        path = r"C:\Users"
        self.iframe_switch_wait()
        self.wait_element_clickable(self.download_btn_locator).click()
        self.wait_element_clickable(self.confirm_btn_locator).click()
        time.sleep(3)
        t = time.strftime('%Y%m%d'.format(time.localtime(time.time())))
        file_name = f'人员信息_{t}'
        return self.find_file(path,file_name)


    def download_moudle(self):
        """下载人员信息模板"""
        path = r"C:\Users"
        self.iframe_switch_wait()
        self.get_download_moudl_elem().click()
        time.sleep(3)
        t = time.strftime('%Y%m%d'.format(time.localtime(time.time())))
        file_name = f'人员信息_{t}'
        return self.find_file(path,file_name)

    def switch_org(self):
        """切换组织机构"""
        first_org_locator = (By.XPATH,"//ul[@id='orgTree']//ul/li[1]/a")
        first_org_name_locator = (By.XPATH,"//ul[@id='orgTree']//ul/li[1]/a/span[2]")
        title_name = (By.XPATH,"//div[@id='orgTitleContainer']")
        self.iframe_switch_wait()
        name = self.get_element(first_org_name_locator).text
        self.get_element(first_org_locator).click()
        title = self.get_element(title_name).text
        return name == title

    def edit_employee(self):
        """编辑人员信息"""
        first_emp_locator = (By.XPATH,"//table[@id='personListTable']/tbody/tr[1]")
        edit_btn_locator = (By.XPATH,"//a[@class='btn btn-primary btn-xs edit']")
        name_input_locator = (By.XPATH,"//input[@name='txtEmpName']")
        save_btn_locator = (By.XPATH,"//div[@class='modal-footer']//button")
        first_emp_name_locator = (By.XPATH,"//table[@id='personListTable']/tbody/tr[1]/td[3]")
        self.iframe_switch_wait()
        while True:
            try:
                self.get_element(first_emp_locator).click()
                break
            except Exception:
                continue
        name = "autotest"
        self.get_element(edit_btn_locator).click()
        time.sleep(1)
        self.get_element(name_input_locator).clear()
        time.sleep(1)
        self.get_element(name_input_locator).send_keys(name)
        self.get_element(save_btn_locator).click()
        time.sleep(1)
        first_name = self.get_element(first_emp_name_locator).text
        print(first_name)
        return first_name == name

    def del_employee(self):
        """删除人员"""
        first_emp_locator = (By.XPATH, "//table[@id='personListTable']/tbody/tr[1]")
        first_emp_name_locator = (By.XPATH,"//table[@id='personListTable']/tbody/tr[1]/td[3]")
        arrow_btn_locator = (By.XPATH,"//button[@class='btn btn-default dropdown-toggle btn-xs']")
        del_btn_locator = (By.XPATH,"//ul[@id='handleMenu']/li[1]/button")
        confirm_del_locator = (By.XPATH,"//button[@data-bb-handler='confirm']")
        self.iframe_switch_wait()
        while True:
            try:
                self.get_element(first_emp_locator).click()
                break
            except Exception:
                continue
        name = self.get_element(first_emp_name_locator).text
        self.get_element(arrow_btn_locator).click()
        self.get_element(del_btn_locator).click()
        self.get_element(confirm_del_locator).click()
        time.sleep(1)
        return self.wait_element_not_text(first_emp_name_locator,name)