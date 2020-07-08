
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
import locale
import time
import pyautogui as ui
locale.setlocale(locale.LC_CTYPE,"chinese")

class OrganizationPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("basicdata_url", "organization")
    # 第一条组织机构的‘添加按钮’
    add_btn_locator = (By.XPATH,"//table[@id='tabletreeGrid']//tr[1]/td[contains(@class,'center-align')]/button[@title='添加']")
    # 类型
    type_locator = (By.XPATH,"//select/option[text()='省联社']")
    # 区域选择框
    dist_locator = (By.XPATH,"//button[contains(@class,'district-toggle')]")
    # 香港
    hk_locator = (By.XPATH,"//ul[@id='districtTree']//span[text()='香港特别行政区']")
    # 名称输入框
    name_input_locator = (By.XPATH,"//input[@placeholder='名称']")
    # 确定按钮
    confirm_btn_locator = (By.XPATH,"//button[@class='btn btn-primary']")
    # tr标签
    tr_locaotr =(By.XPATH,"//tr")
    # 导入组织机构按钮
    upload_org_locator = (By.XPATH, "//div[@id='excelImport']")
    # 确定导入按钮
    confirm_uoload_btn_locator = (By.XPATH, "//button[text()='确定导入']")
    # 导入成功
    upload_success_locator = (By.XPATH, "//div[@class='bootbox-body']")


    def open_organization(self):
        """打开后台组织机构页面"""
        return self.driver.get(self.url)

    def add_org(self):
        """添加3个组织机构"""
        # 1、切换iframe
        self.iframe_switch_wait()
        # 2、获取添加机构前页面中的机构数量
        n1 = len(self.get_elements(self.tr_locaotr))
        # 3、添加3个组织机构
        for i in range(3):
            # 获取时间戳
            t = time.strftime('auto%m%d%H%M%S'.format(time.localtime(time.time())))
            # 点击第一个组织的添加按钮
            self.get_element(self.add_btn_locator).click()
            time.sleep(1)
            # 点击类型
            self.get_element(self.type_locator).click()
            # 点击区域
            self.get_element(self.dist_locator).click()
            # 选择香港特别行政区
            self.get_element(self.hk_locator).click()
            # 输入名称
            self.get_element(self.name_input_locator).send_keys(t)
            time.sleep(1)
            # 点击确定
            self.get_element(self.confirm_btn_locator).click()
            time.sleep(1)
        # time.sleep(1)
        # 刷新页面
        self.driver.refresh()
        self.iframe_switch_wait()
        # 获取添加机构后页面中的机构数量
        n2 = len(self.get_elements(self.tr_locaotr))
        return n2-n1

    def upload_org(self,file_path):
        """导入组织机构"""
        self.iframe_switch_wait()
        self.get_element(self.upload_org_locator).click()
        time.sleep(1)
        # 文件导入地址
        ui.write(file_path)
        time.sleep(2)
        ui.press("enter", 2)
        time.sleep(1)
        self.wait_element_clickable(self.confirm_btn_locator).click()
        return self.wait_element_text(self.upload_success_locator,'导入成功')

    def export_org(self):
        """导出组织机构"""
        path = r"C:\Users"
        first_org_locator = (By.XPATH,"//table[@id='tabletreeGrid']//tr[1]/td")
        first_org_name_locator = (By.XPATH,"//table[@id='tabletreeGrid']//tr[1]/td//font")
        export_btn_locator = (By.XPATH,"//button[@title='导出']")
        confirm_btn_locator = (By.XPATH,"//button[@class='btn btn-primary']")
        self.iframe_switch_wait()
        self.get_element(first_org_locator).click()
        title : str = self.get_element(first_org_name_locator).text
        li = title.split("(")
        name = li[0]
        self.get_element(export_btn_locator).click()
        self.get_element(confirm_btn_locator).click()
        time.sleep(3)
        t = time.strftime('%Y%m%d'.format(time.localtime(time.time())))
        file_name = f'导出机构_{name}_{t}'
        return self.find_file(path,file_name)

    def download_moudle(self):
        """下载导入模板"""
        path = r"C:\Users"
        download_btn_locator = (By.XPATH,"//button[@title='下载导入模板']")
        self.iframe_switch_wait()
        self.get_element(download_btn_locator).click()
        time.sleep(3)
        file_name = f'机构导入模板'
        return self.find_file(path, file_name)