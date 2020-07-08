
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
class EquipLinkPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("alarm_url","equiplink")
    # 摄像机标签页
    camera_tab_locator = (By.XPATH,"//a[text()='摄像机']")
    # DVS输出标签页
    DVS_tab_locator = (By.XPATH,"//a[text()='DVS输出']")
    # 报警输出标签页
    alarm_output_locator = (By.XPATH,"//a[text()='报警输出']")
    # 显示复选框
    display_box_locator = (By.XPATH,"//tbody/tr[2]/td[2]//input")
    # DVS和报警输出控制输出复选框
    output_box_locator = (By.XPATH,"//tbody/tr[2]/td[2]//input")
    # 数量
    link_number_locator = (By.XPATH,"//ul[@id='listMenu']/li[1]//strong")


    def open_equiplink(self):
        """打开报警管理-设备关联关系页面"""
        return self.driver.get(self.url)

    def add_equip_link(self):
        """添加设备关联关系：视频网关关联-摄像机、DVS输出、报警输出"""
        # 点击报警输出标签页
        self.get_element(self.alarm_output_locator).click()
        time.sleep(0.5)
        self.get_element(self.output_box_locator).click()
        # 点击DVS输出标签页
        self.get_element(self.DVS_tab_locator).click()
        time.sleep(0.5)
        # 勾选控制输出复选框
        self.get_element(self.output_box_locator).click()
        # 点击摄像机标签页
        self.get_element(self.camera_tab_locator).click()
        time.sleep(0.5)
        # 勾选显示复选框
        self.get_element(self.display_box_locator).click()
        return self.wait_element_visible(self.link_number_locator).text

    def clear(self):
        """清理【添加设备关联关系】的测试环境"""
        # 点击报警输出标签页
        self.get_element(self.alarm_output_locator).click()
        time.sleep(0.5)
        self.get_element(self.output_box_locator).click()
        # 点击DVS输出标签页
        self.get_element(self.DVS_tab_locator).click()
        time.sleep(0.5)
        # 勾选控制输出复选框
        self.get_element(self.output_box_locator).click()
        # 点击摄像机标签页
        self.get_element(self.camera_tab_locator).click()
        time.sleep(0.5)
        # 勾选显示复选框
        self.get_element(self.display_box_locator).click()