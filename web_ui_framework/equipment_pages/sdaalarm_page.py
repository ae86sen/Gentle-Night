
import locale
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")

class SdaAlarmPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","videogate")
    # 组织机构树
    org_tree_locator = (By.XPATH, "//span[@role='combobox']")
    # 顶级机构下的第一个下级机构
    first_sub_org_locator = (By.XPATH, "//ul[@role='tree-node']/li[2]//li[1]//span[@class='ant-select-tree-title']")
    # 顶级机构下的第一个下级机构的名字
    first_sub_org_name_locator = (
    By.XPATH, "//ul[@role='tree-node']/li[2]//li[1]//span[@class='ant-select-tree-title']/span")
    # 箭头
    arrow_btn_locator = (By.XPATH, "//ul[@role='tree-node']/li[2]/span[1]")
    # 添加主机按键
    add_host_btn_locator = (By.XPATH,"//a/button[@class='ant-btn']")
    # 复制主机按键
    copy_host_btn_locator = (By.XPATH,"//div/button[@class='ant-btn']")
    # 主机标识输入框
    host_tag_input_locator = (By.XPATH,"//input[@id='hostName']")
    # 主机名称输入框
    host_name_input_locator = (By.XPATH,"//input[@id='hostTitle']")
    # 添加确认按键
    confirm_add_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
    # 成功图标
    success_logo_locator = (By.XPATH, "//div[@class='ant-message-notice']//span")
    # 最后一个设备的名字
    last_sda_name_locator = (By.XPATH,"//tbody//tr[last()]/td/a")
    # 最后一个设备的复选框
    last_sda_box_locator = (By.XPATH,"//tbody//tr[last()]/td//input")
    # 复制主机窗口中顶级机构下的第一个下级机构的复选框
    copy_sub_org_box_locator = (By.XPATH,"//ul[contains(@class,'ant-tree-child-tree')]/li[1]//span[@class='ant-tree-checkbox-inner']")
    # 批量按键
    batch_btn_locator = (By.XPATH,"//button[@id='batch']")
    # 移动组织机构按键
    move_org_btn_locator = (By.XPATH,"//ul/li[3]//a[@class='cms-Video-dropdownLink']")
    # 组织机构选择框
    select_org_btn_locator = (By.XPATH,"//span[@id='orgUnitCode']//span[@class='ant-select-selection__rendered']//following-sibling::span")
    # 移动组织机构树下的顶级机构
    tree_top_org_locator = (By.XPATH,"//div[contains(@style,'776px; top: 215px;')]//ul[@role='tree-node']/li/span[2]")
    # 删除按键
    del_btn_locator = (By.XPATH,"//ul[contains(@class,'menu-vertical')]/li[last()]")



    def open_sdalarm(self):
        """打开安防设备-虚拟事件设备页面"""
        sda_alarm_locator =(By.XPATH,"//a[@href='/equipment/home/sdaalarmdevice']")
        locator = (By.XPATH,"//div[@class='ant-menu-submenu-title']")
        self.driver.get(self.url)
        time.sleep(1)
        self.get_element(locator).click()
        self.get_element(sda_alarm_locator).click()


    def switch_org(self):
        """从顶级机构切换到其第一个下级机构"""
        self.wait_element_clickable(self.org_tree_locator).click()
        self.wait_element_clickable(self.arrow_btn_locator).click()
        self.wait_element_clickable(self.first_sub_org_locator).click()
        return self.wait_element_precence(self.first_sub_org_name_locator).get_attribute("innerText")

    def add_host(self):
        """添加虚拟主机设备"""
        tag_name = time.strftime('tag%H%M%S'.format(time.localtime(time.time())))
        host_name = time.strftime('自动化主机%H%M%S'.format(time.localtime(time.time())))
        # 点击添加
        self.wait_element_clickable(self.add_host_btn_locator).click()
        # 输入主机标识
        self.get_element(self.host_tag_input_locator).send_keys(tag_name)
        # 输入主机名称
        self.get_element(self.host_name_input_locator).send_keys(host_name)
        # 点击确认
        self.get_element(self.confirm_add_btn_locator).click()
        # 判断弹出编辑成功窗口
        add_result_logo = self.wait_element_text(self.success_logo_locator,"编辑成功")
        # 判断页面中是否新增添加数据
        add_result_data = self.wait_element_text(self.last_sda_name_locator,host_name)
        return add_result_logo,add_result_data

    def edit_host(self):
        """编辑虚拟主机信息"""
        # 点击最后一个设备进入设备编辑页面
        last_device = self.get_element(self.last_sda_name_locator)
        name = last_device.text
        last_device.click()
        time.sleep(1)
        # 修改名称
        self.wait_element_visible(self.host_name_input_locator).send_keys("test")
        time.sleep(1)
        # 点击确定
        self.get_element(self.confirm_add_btn_locator).click()
        new_name = name + "test"
        edit_result_logo = self.wait_element_text(self.success_logo_locator,"编辑成功")
        edit_result_data = self.wait_element_text(self.last_sda_name_locator,new_name)
        return edit_result_logo,edit_result_data


    def copy_host(self):
        """复制虚拟主机设备到下级机构"""
        name = self.wait_element_visible(self.last_sda_name_locator).text
        # 勾选最后一个主机设备
        while True:
            try:
                self.get_element(self.last_sda_box_locator).click()
                break
            except Exception:
                continue
        # 点击复制主机
        self.wait_element_clickable(self.copy_host_btn_locator).click()
        # 勾选下级机构
        self.get_element(self.copy_sub_org_box_locator).click()
        # 点击确定
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        # 判断是否有复制成功的弹窗
        copy_result_logo = self.wait_element_text(self.success_logo_locator,"复制成功")
        time.sleep(1)
        # 切换到下级机构
        self.wait_element_clickable(self.org_tree_locator).click()
        self.wait_element_clickable(self.first_sub_org_locator).click()
        # 判断主机信息是否复制到下级机构中
        copy_result_data = self.wait_element_text(self.last_sda_name_locator,name)
        return copy_result_logo,copy_result_data

    def move_org(self):
        """移动组织机构"""
        """还未调通"""
        # 勾选最后一个设备
        self.get_element(self.last_sda_box_locator).click()
        # 点击批量
        self.get_element(self.batch_btn_locator).click()
        # 点击移动组织机构
        self.wait_element_clickable(self.move_org_btn_locator).click()
        time.sleep(2)
        # 点击组织机构选择框
        self.get_element(self.select_org_btn_locator).click()
        # 点击顶级机构
        time.sleep(1800)
        # top_org = self.get_element(self.tree_top_org_locator)
        # self.ac_hover(top_org)
        # self.ac_click(top_org)
        time.sleep(2)
        self.get_element(self.tree_top_org_locator).click()
        # 点击确定
        self.get_element(self.confirm_add_btn_locator).click()
        return self.wait_element_text(self.success_logo_locator,"编辑成功")


    def del_host(self):
        """删除虚拟主机"""
        # 获取要删除的设备
        del_device_name = self.get_element(self.last_sda_name_locator).text
        del_device_locator = (By.XPATH, "//tbody/tr[last()]//a[text()='{}']".format(del_device_name))
        # 勾选最后一个设备
        self.get_element(self.last_sda_box_locator).click()
        # 点击批量
        self.get_element(self.batch_btn_locator).click()
        # 点击删除
        self.wait_element_clickable(self.del_btn_locator).click()
        # 点击确定
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        del_result_logo = self.wait_element_text(self.success_logo_locator,"删除成功")
        del_result_data = self.isElementExist(del_device_locator)
        return del_result_logo,del_result_data

    def search_host(self):
        """搜索设备"""
        select_all_locator = (By.ID,"includeSub")
        query_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-search-btn']")
        input_locator = (By.XPATH,"//input[@class='ant-input']")
        any_locator = (By.XPATH,"//div/h2")
        first_name_locator = (By.XPATH,"//tbody/tr[1]//a")
        key_word = "自动化主机"
        while True:
            try:
                self.get_element(select_all_locator).click()
                break
            except Exception:
                continue
        self.get_element(query_btn_locator).click()
        self.get_element(input_locator).send_keys(key_word)
        time.sleep(1)
        self.get_element(any_locator).click()
        time.sleep(1)
        name = self.wait_element_visible(first_name_locator).text
        return key_word in name


