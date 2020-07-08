
import locale
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")




class ResGroupPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","resgroup")
    # 动态分组
    dyna_group_locator = (By.XPATH,"//ul[@role='menu']/li[@class='ant-dropdown-menu-item'][1]/a")
    # 静态分组
    sta_group_locator = (By.XPATH,"//ul[@role='menu']/li[@class='ant-dropdown-menu-item'][2]/a")
    # 分组名称输入框
    name_input_locator = (By.XPATH,"//input[@id='name']")
    # 保存按键
    save_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary' and @style]")
    # 响应图标
    response_logo_locator = (By.XPATH,"//div[@class='ant-message-notice']//span")
    # 第一个分组的名称
    first_group_name_locator = (By.XPATH,"//tbody/tr[1]//div[@class]/parent::div")
    # 第一个分组的复选框
    first_group_box_locator = (By.XPATH,"//tbody/tr[1]//input")
    # 添加分组到左侧列表的按键
    add_to_right_btn_locator = (By.XPATH,"//button[@id='SelectDeviceAdd']")
    # 第一个编辑按键
    first_edit_btn_locator = (By.XPATH,"//tbody/tr[1]//a[@id='2']")
    # 第一个删除按键
    first_del_btn_locator = (By.XPATH,"//tbody/tr[1]//a[@title='删除']")
    # 确定删除按键
    confirm_del_btn_locator = (By.XPATH,"//span[text()='确 定']/parent::button")


    def open_resgroup(self):
        """打开安防设备-资源分组页面"""
        return self.driver.get(self.url)

    def add_dynamic_group(self,tab_xpath,add_xpath):
        """添加动态分组"""
        name = time.strftime('动态CG%H%M%S'.format(time.localtime(time.time())))
        tab_locator = (By.XPATH,"{}".format(tab_xpath))
        add_locator = (By.XPATH,"{}".format(add_xpath))
        # 点击分组标签页
        self.get_element(tab_locator).click()
        # 点击添加
        self.get_element(add_locator).click()
        # 点击动态分组
        self.get_element(self.dyna_group_locator).click()
        # 输入分组名称
        self.get_element(self.name_input_locator).send_keys(name)
        # 点击保存
        self.get_element(self.save_btn_locator).click()
        add_result_logo = self.wait_element_text(self.response_logo_locator,"添加成功")
        add_result_data = self.wait_element_text(self.first_group_name_locator,name)
        return add_result_logo,add_result_data

    def add_static_group(self,tab_xpath,add_xpath):
        """添加静态分组"""
        name = time.strftime('静态CG%H%M%S'.format(time.localtime(time.time())))
        tab_locator = (By.XPATH, "{}".format(tab_xpath))
        add_locator = (By.XPATH, "{}".format(add_xpath))
        # 点击分组标签页
        self.get_element(tab_locator).click()
        # 点击添加
        self.get_element(add_locator).click()
        # 点击静态分组
        self.get_element(self.sta_group_locator).click()
        # 输入分组名称
        self.get_element(self.name_input_locator).send_keys(name)
        # 勾选需要添加的分组
        self.get_element(self.first_group_box_locator).click()
        # 点击添加
        self.wait_element_clickable(self.add_to_right_btn_locator).click()
        # 点击保存
        self.get_element(self.save_btn_locator).click()
        add_result_logo = self.wait_element_text(self.response_logo_locator,"添加成功")
        add_result_data = self.wait_element_text(self.first_group_name_locator,name)
        return add_result_logo,add_result_data,name

    def edit_static_group(self,tab_xpath,name):
        """编辑静态分组"""
        tab_locator = (By.XPATH, "{}".format(tab_xpath))
        # 点击分组标签页
        self.get_element(tab_locator).click()
        # 点击第一条数据编辑
        self.get_element(self.first_edit_btn_locator).click()
        # 输入分组名称
        self.get_element(self.name_input_locator).send_keys("test")
        # 点击保存
        self.get_element(self.save_btn_locator).click()
        new_name = name + "test"
        edit_result_logo = self.wait_element_text(self.response_logo_locator, "修改成功")
        edit_result_data = self.wait_element_text(self.first_group_name_locator, new_name)
        return edit_result_logo, edit_result_data, new_name


    def del_static_group(self,tab_xpath,new_name):
        """删除静态分组"""
        tab_locator = (By.XPATH, "{}".format(tab_xpath))
        # 点击分组标签页
        self.get_element(tab_locator).click()
        # 第一个静态分组
        locator = (By.XPATH,"//tbody/tr[1]//div[@class]/parent::div[text='{}']".format(new_name))
        # 点击删除
        self.get_element(self.first_del_btn_locator).click()
        # 点击确定删除
        self.wait_element_clickable(self.confirm_del_btn_locator).click()
        del_result_logo = self.wait_element_text(self.response_logo_locator, "删除成功")
        del_result_data = self.isElementExist(locator)
        return del_result_logo,del_result_data

