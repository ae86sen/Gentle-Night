
import locale
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf

locale.setlocale(locale.LC_CTYPE, "chinese")
import os

steps_path = os.path.join(os.path.dirname(__file__), "vault_page.yaml")


class VaultPage(BasePage):
    """防范平台-金库客户端-远程值守页面"""
    url = conf.get_str("env", "url") + conf.get_str("config_center_url", "vault")
    # 第一条金库名称输入框
    first_name_input_locator = (By.XPATH, "//ul/li[1]//input")
    # 第一条金库名称
    first_name_locator = (By.XPATH, "//ul/li[1]//span")
    # 名称编辑保存按键
    name_save_btn_locator = (By.XPATH, "//i[@class='fa fa-save']")
    # 金库画面选择框
    golden_locator = (By.XPATH, "//input[@value=1]")
    # 值守视图选择框
    view_locator = (By.XPATH, "//input[@value=2]")
    # 授权开门后报警自动撤防
    check_box_1st_locator = (By.XPATH, "//div[@id='vaultTabPaneCheckbox']")
    # 不接收报警防区
    check_box_2nd_locator = (By.XPATH, "//div[@id='vaultTabPane_check'][1]//input")
    # 处理开门时自动拨通现场语音对讲
    check_box_3rd_locator = (By.XPATH, "//div[@id='vaultTabPane_check'][2]//input")
    # 不接收报警
    check_box_4rd_locator = (By.XPATH, "//div[@id='vaultTabPane_check'][3]//input")
    # 被勾选状态
    checked_locator = (By.XPATH, "//span[@class='ant-checkbox ant-checkbox-checked']")
    # 第一个设备
    first_equip_locator = (By.XPATH, "//div[@id='SelectDeviceLeftTable']//tbody/tr[1]//input")
    # 添加
    selected_add_locator = (By.XPATH, "//button[@id='SelectDeviceAdd']")
    # 确认
    confirm_btn_locator = (By.XPATH, "//span[text()='确 认']/parent::button")
    # 添加数量
    number_add_locator = (By.XPATH, "//div[@class='ant-col-12 basicePullRgithg']")
    # 删除确认按键
    del_confirm_btn_locator = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-sm']")

    def open_vault(self):
        """打开防范平台-远程值守页面"""
        return self.driver.get(self.url)

    def edit_vault_name(self):
        """编辑金库名称"""
        # 获取第一条金库名称
        name = time.strftime('金库%H%M%S'.format(time.localtime(time.time())))
        # 鼠标移动到第一条金库名称编辑按键上并点击
        self.ac_hover_by_offset_and_click(200, 300)
        self.get_element((By.XPATH, "//ul[@id='vaultTabPaneMenu']/li[1]//a")).click()
        # 在名称输入框编辑名称
        time.sleep(0.5)
        self.get_element(self.first_name_input_locator).clear()
        time.sleep(0.5)
        self.get_element(self.first_name_input_locator).send_keys(name)
        time.sleep(0.5)
        # 点击保存
        self.get_element(self.name_save_btn_locator).click()
        edit_result = self.wait_element_text(self.first_name_locator, name)
        return edit_result

    def edit_vault_param(self):
        """编辑金库默认参数"""
        self.get_element(self.view_locator).click()
        # 勾选
        check_boxes = [self.check_box_1st_locator, self.check_box_2nd_locator,
                      self.check_box_3rd_locator, self.check_box_4rd_locator]
        for i in check_boxes:
            self.get_element(i).click()
            time.sleep(0.5)
        # 刷新页面
        self.driver.refresh()
        time.sleep(2)
        return len(self.get_elements(self.checked_locator)) == 4

    def edit_vault_param_clear(self):
        """清理环境"""
        self.get_element(self.golden_locator).click()
        # 勾选
        check_boxes = [self.check_box_1st_locator, self.check_box_2nd_locator,
                      self.check_box_3rd_locator, self.check_box_4rd_locator]
        for i in check_boxes:
            self.get_element(i).click()
            time.sleep(0.5)

    def add_equipment(self, tab_xpath, add_xpath, form_xpath):
        """添加关联设备"""
        tab_locator = (By.XPATH, f"{tab_xpath}")
        add_locator = (By.XPATH,
                       f"//div[contains(@class,'cms-Vault-boxMargin')]//div[@role='tabpanel'][{add_xpath}]//button[@id='add']")
        form_locator = (By.XPATH, f"//*[@id='{form_xpath}']//tbody/tr")
        # 点击tab标签
        self.get_element(tab_locator).click()
        # 获取添加前的设备数量
        time.sleep(1)
        num_equipment = len(self.get_elements(form_locator))
        # 点击添加
        self.get_element(add_locator).click()
        time.sleep(1)
        # 选择第一组设备
        self.get_element(self.first_equip_locator).click()
        # 获取添加的设备数量
        e: str = self.wait_element_visible(self.number_add_locator).text
        l = e.split(" ")
        add_num_equipment = int(l[0])
        # 点击添加到右侧
        self.get_element(self.selected_add_locator).click()
        # 点击确认
        self.get_element(self.confirm_btn_locator).click()
        time.sleep(1.5)
        # 获取添加后的设备数量
        new_num_equipment = len(self.get_elements(form_locator))
        print(new_num_equipment)
        return new_num_equipment - num_equipment == add_num_equipment

    def del_equipment(self, tab_xpath, del_xpath, form_xpath):
        """删除关联设备"""
        form_locator = (By.XPATH, f"//*[@id='{form_xpath}']//thead//input")
        del_locator = (By.XPATH,
                       f"//div[contains(@class,'cms-Vault-boxMargin')]//div[@role='tabpanel'][{del_xpath}]//button[@id='delete']")
        tab_locator = (By.XPATH, f"{tab_xpath}")
        num_locator = (By.XPATH, f"//*[@id='{form_xpath}']//tbody/tr")
        # 点击tab标签页
        self.get_element(tab_locator).click()
        time.sleep(1)
        # 勾选所有设备
        self.get_element(form_locator).click()
        # 点击删除
        self.wait_element_clickable(del_locator).click()
        # 点击确认
        self.wait_element_clickable(self.del_confirm_btn_locator).click()
        time.sleep(1)
        # 获取删除后的设备数量
        num_del_equipment = len(self.get_elements(num_locator))
        return num_del_equipment == 0

    def config_output(self):
        """客户端配置-配置呼出设备"""
        values = self.steps(steps_path)
        return values

    def add_view(self):
        """客户端配置-添加金库值守视图"""
        return self.steps(steps_path)

    def del_view(self):
        """客户端位置-删除金库值守视图"""
        return self.steps(steps_path)

    def add_golden(self):
        """客户端配置-添加管辖金库"""
        return self.steps(steps_path)

    def del_golden(self):
        """客户端配置-删除管辖金库"""
        return self.steps(steps_path)
