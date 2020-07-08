
import locale
import time
from selenium.webdriver.common.by import By
locale.setlocale(locale.LC_CTYPE, "chinese")
from common.base_page import BasePage
from common.getconfig import conf


class AlarmGroupPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("alarm_url","alarmgroup")
    add_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
    # 报警源名称输入框
    input_name_locator = (By.XPATH,"//input[@id='name']")
    # 报警源选择框
    select_as_locator = (By.XPATH,"//span[text()='选择报警源']")
    # 全选报警源下拉框中的第一个报警源
    first_as_locator = (By.XPATH,"//span[@title='服务器']/preceding-sibling::span/span")
    # 资源分组选择框
    select_sg_locator = (By.XPATH,"//span[text()='选择资源分组']")
    # 全选资源分组下拉框中的第一个资源分组
    first_sg_locator = (By.XPATH,"//span[@title='摄像机']/preceding-sibling::span/span")
    # 确认添加按键
    confirm_add_btn_locator = (By.XPATH,"//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']")
    # 结果图标
    result_logo_locator = (By.XPATH, "//div[@class='ant-message-notice']//span")
    # 最后一个报警源分组
    last_ag_locator = (By.XPATH,"//tbody/tr[last()]/td[2]//a[@class='cms-AlarmTh-tabLink']")
    text_locator = (By.XPATH,"//label[@title='报警源']")
    # 最后一个报警源分组的名称
    last_ag_name_locator = (By.XPATH,"//tbody/tr[last()]//a/a")
    # 最后一个报警源分组的复选框
    last_ag_box_locator = (By.XPATH,"//tbody/tr[last()]//input")
    # 删除按键
    del_btn_locator = (By.XPATH,"//button[@id='alarmSourceGroupDelete']")
    # 确认删除按键
    confirm_del_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary ant-btn-sm']")



    def open_alarmgroup(self):
        """打开报警管理-报警源分组页面"""
        return self.driver.get(self.url)

    def add_as_group(self):
        """添加报警源分组"""
        name = time.strftime('AG%H%M%S'.format(time.localtime(time.time())))
        self.get_element(self.add_btn_locator).click()
        # 输入分组名称
        self.get_element(self.input_name_locator).send_keys(name)
        # 点击选择报警源
        self.wait_element_clickable(self.select_as_locator).click()
        # 勾选第一个报警源
        self.wait_element_clickable(self.first_as_locator).click()
        # 点击选择资源分组
        self.get_element(self.text_locator).click()
        self.wait_element_clickable(self.select_sg_locator).click()
        # 勾选第一个资源分组
        self.wait_element_clickable(self.first_sg_locator).click()
        # 点击确认
        self.get_element(self.confirm_add_btn_locator).click()
        time.sleep(1)
        add_result_logo = self.wait_element_text(self.result_logo_locator,"添加成功")
        while True:
            try:
                self.wait_element_text(self.last_ag_name_locator, name)
            except Exception:
                self.get_element((By.XPATH, "//ul[@class='ant-pagination mini']/li[last()-1]/a")).click()
                time.sleep(5)
                continue
            else:
                return add_result_logo

    def edit_as_group(self):
        """编辑报警源分组"""
        last_group = self.get_element(self.last_ag_name_locator)
        name = last_group.text
        # 点击最后一条进入编辑页面
        self.wait_element_clickable(self.last_ag_name_locator).click()
        # 修改名称
        self.get_element(self.input_name_locator).send_keys("test")
        # 点击确认
        self.get_element(self.confirm_add_btn_locator).click()
        new_name = name + "test"
        edit_result_logo = self.wait_element_text(self.result_logo_locator,"修改成功")
        edit_result_data = self.wait_element_text(self.last_ag_name_locator,new_name)
        return edit_result_logo, edit_result_data

    def del_as_group(self):
        """删除报警源分组"""
        # 获取要删除的设备
        del_group_name= self.get_element(self.last_ag_name_locator).text
        # 勾选最后一个分组的复选框
        self.get_element(self.last_ag_box_locator).click()
        # 点击删除
        self.get_element(self.del_btn_locator).click()
        # 确认
        self.get_element(self.confirm_del_btn_locator).click()
        del_result_logo = self.wait_element_text(self.result_logo_locator,"删除成功")
        del_result_data = self.wait_element_not_text(self.last_ag_name_locator,del_group_name)
        return del_result_logo,del_result_data

