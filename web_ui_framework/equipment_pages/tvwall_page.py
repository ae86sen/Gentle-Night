
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
class TvWallPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","tvwall")
    # 视图编辑按键
    edit_btn_locator = (By.XPATH,"//i[@class='fa fa-pencil-square-o']")
    # 第一个启用走马灯复选框
    # open_light_btn_locator = (By.XPATH,"//form[@id='alarmTvForm']/div[1]//label[2]//input")
    light_btn_locator = (By.XPATH,"//form[@id='alarmTvForm']/div[1]//label[2]//input/parent::span")
    # 第一个走马灯内容输入框
    light_input_locator = (By.XPATH,"//form[@id='alarmTvForm']/div[1]//textarea")
    # 视图编辑框确认按键
    confirm_edit_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
    # 编辑成功图标
    edit_success_locator = (By.XPATH,"//i[@class='anticon anticon-check-circle']/following::span")
    # 保存配置按键
    save_conf_btn_locator = (By.XPATH,"//button[@id='save']")
    # 确定保存按键
    confirm_save_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary ant-btn-sm']")
    # 保存成功图标
    save_success_locator = (By.XPATH,"//span[text()='操作成功']")

    def open_tvwall(self):
        """打开安防设备-电视墙页面"""
        return self.driver.get(self.url)

    def edit_view(self):
        """编辑视图并保存"""
        self.wait_element_clickable(self.edit_btn_locator).click()
        # 判断第一个视图的“启用走马灯”是否勾选,
        # 通过“启用走马灯”标签的class属性值是否包含"ant-checkbox-checked"来判断
        light_elem = self.wait_element_visible(self.light_btn_locator)
        value = "ant-checkbox-checked"
        if value in light_elem.get_attribute('class'):
            # 如果包含，则证明已启用走马灯，那么直接输入走马灯内容
            self.wait_element_visible(self.light_input_locator).send_keys("autotesting")
        else:
            # 如果不包含，则证明还未启用走马灯，那么先启用，再输入
            self.wait_element_clickable(self.light_btn_locator).click()
            self.wait_element_visible(self.light_input_locator).send_keys("autotesting")
        time.sleep(0.5)
        self.wait_element_clickable(self.confirm_edit_btn_locator).click()
        return self.wait_element_text(self.edit_success_locator,"操作成功")

    def save_conf(self):
        """保存电视墙配置"""
        self.wait_element_clickable(self.save_conf_btn_locator).click()
        self.wait_element_clickable(self.confirm_save_btn_locator).click()
        return self.wait_element_text(self.save_success_locator,"操作成功")

