
import locale
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")

class IVVPage(BasePage):
    """智能视图页面"""
    url = conf.get_str("env","url") + conf.get_str("config_center_url","ivv")
    # 添加按键
    add_btn_locator = (By.XPATH,"//button[@id='add']")
    # 删除按键
    del_btn_locator = (By.XPATH,"//button[@id='del']")
    # 名称输入框
    name_input_locator = (By.XPATH,"//input[@id='name']")
    # 报警源添加按键
    add_as_btn_locator = (By.XPATH,"//i[@class='anticon anticon-plus']/parent::button")
    # 第一个报警源复选框
    first_as_box_locator= (By.XPATH,"//div[@class='ant-col-24'][1]//input")
    # 随便点一下
    text_locator = (By.XPATH,"//label[@title='报警源分组']")
    # 添加确认按键
    confirm_add_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
    # 结果图标
    result_logo_locator = (By.XPATH, "//div[@class='ant-message-notice']//span")
    # 第一个智能视图的名称
    first_ivv_name_locator = (By.XPATH,"//tbody/tr[1]//a")
    # 第一个智能视图的复选框
    first_ivv_box_locator = (By.XPATH,"//tbody/tr[1]//input")
    # 确认删除按键
    confirm_del_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary ant-btn-sm']")

    def open_ivv(self):
        """打开防范平台-智能视图轮巡页面"""
        return self.driver.get(self.url)

    def add_ivv(self):
        """添加智能视图"""
        name = time.strftime('IVV%H%M%S'.format(time.localtime(time.time())))
        # 点击添加
        self.get_element(self.add_btn_locator).click()
        # 输入名称
        self.get_element(self.name_input_locator).send_keys(name)
        # 点击添加报警源
        self.wait_element_clickable(self.add_as_btn_locator).click()
        # 勾选第一个报警源
        self.get_element(self.first_as_box_locator).click()
        self.get_element(self.text_locator).click()
        # 点击确认
        self.get_element(self.confirm_add_btn_locator).click()
        add_result_logo = self.wait_element_text(self.result_logo_locator,"添加成功")
        add_result_data = self.wait_element_text(self.first_ivv_name_locator,name)
        return add_result_logo,add_result_data

    def edit_ivv(self):
        """编辑智能视图"""
        name = self.get_element(self.first_ivv_name_locator).text
        # 点击第一个智能视图进入编辑页面
        self.wait_element_clickable(self.first_ivv_name_locator).click()
        # 修改名称
        self.get_element(self.name_input_locator).send_keys("a")
        # 点击确认
        time.sleep(0.5)
        self.get_element(self.confirm_add_btn_locator).click()
        new_name = name + "a"
        edit_result_logo = self.wait_element_text(self.result_logo_locator,"修改成功")
        edit_result_data = self.wait_element_text(self.first_ivv_name_locator,new_name)
        return edit_result_logo ,edit_result_data

    def del_ivv(self):
        """删除智能视图"""
        del_ivv_name = self.get_element(self.first_ivv_name_locator).text
        # del_ivv_locator = (By.XPATH,"//tbody/tr[1]//a[text()='{}']".format(del_ivv_name))
        # 勾选第一个智能视图
        self.get_element(self.first_ivv_box_locator).click()
        # 点击删除
        self.get_element(self.del_btn_locator).click()
        # 确认删除
        self.wait_element_clickable(self.confirm_del_btn_locator).click()
        del_result_logo = self.wait_element_text(self.result_logo_locator,"删除成功")
        del_result_data = self.wait_element_not_text(self.first_ivv_box_locator,del_ivv_name)
        return del_result_logo,del_result_data
