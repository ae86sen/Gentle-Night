
import time
from selenium.webdriver.common.by import By
import pyautogui as ui
from common.base_page import BasePage
from common.getconfig import conf


class SdaPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","videogate")
    url_master = conf.get_str("env","url_master") + conf.get_str("equipment_url","videogate")
    # 上传SDE文件按键
    upload_sde_btn_locator = (By.XPATH,"//button[@class='ant-btn']")
    # 成功图标
    success_logo_locator = (By.XPATH, "//div[@class='ant-message-notice']//span")
    # 第一个文件的删除按键
    first_file_del_locator = (By.XPATH,"//tbody/tr[1]//button[1]")
    # 删除确定按键
    confirm_btn_locator = (By.XPATH,"//span[text()='确 定']/parent::button")

    def open_master_sda(self):
        """打开分中心安防设备-虚拟主机类型页面"""
        sda_locator =(By.XPATH,"//a[@href='/equipment/home/sda']")
        locator = (By.XPATH,"//div[@class='ant-menu-submenu-title']")
        self.driver.get(self.url_master)
        time.sleep(1)
        self.get_element(locator).click()
        return self.get_element(sda_locator).click()

    def open_sda(self):
        """打开安防设备-虚拟主机类型页面"""
        sda_locator =(By.XPATH,"//a[@href='/equipment/home/sda']")
        locator = (By.XPATH,"//div[@class='ant-menu-submenu-title']")
        self.driver.get(self.url)
        time.sleep(1)
        self.get_element(locator).click()
        return self.get_element(sda_locator).click()

    def upload_sde_file(self,file_path):
        """上传SDE文件"""
        self.get_element(self.upload_sde_btn_locator).click()
        time.sleep(0.5)
        ui.write(file_path)
        time.sleep(1.5)
        ui.press("enter",2)
        time.sleep(1)
        # return self.wait_element_text(self.success_logo_locator,"上传成功")

    def del_sde_file(self):
        """删除SDE文件"""
        self.get_element(self.first_file_del_locator).click()
        self.wait_element_clickable(self.confirm_btn_locator).click()


    def get_info(self):
        locator = (By.XPATH,"//tbody/tr[1]//a")
        return self.wait_element_text(locator,"纵目安防监测主机")
