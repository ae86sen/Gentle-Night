
import locale
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
locale.setlocale(locale.LC_CTYPE, "chinese")

class OtherPage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","other")
    # 添加按键
    add_btn_locator = (By.XPATH,"//div[@class='cms-box-inlineBlock']/button")
    # 组织机构箭头按键
    org_arrow_btn_locator = (By.XPATH,"//span[@id='orgUnitCode']//span[@class='ant-select-arrow']")
    # 顶级机构
    top_org_locator = (By.XPATH,"//span[contains(@class,'ant-select-tree-node')]")
    # 名称输入框
    name_input_locator = (By.XPATH,"//input[@id='name']")
    # 文本输入框
    text_input_locator = (By.XPATH,"//input[@id='defaultShowValue']")
    # 字体选择框箭头按键
    type_face_arrow_locator = (By.XPATH,"//div[@class='ant-row']/div[@class='ant-col-12'][1]//span[@class='ant-select-arrow']")
    # 选择宋体
    song_locator = (By.XPATH,"//li[text()='宋体']")
    # 串口箭头
    com_arrow_locator = (By.XPATH,"//div[@class='ant-row']/div[@class='ant-col-12'][2]//div[@class='ant-row ant-form-item']")
    # COM5
    com5_locator = (By.XPATH,"//li[text()='COM5']")
    # 确认添加
    confirm_add_btn_locator = (By.XPATH,"//span[text()='确 认']/parent::button")
    # 成功图标
    success_logo_locator = (By.XPATH, "//div[@class='ant-message-notice']//span")
    # 第一条led名称
    first_led_name_locator = (By.XPATH,"//div[@id='ledTable']//tbody/tr[1]//a")
    # 第一个led的复选框
    led_box_locator = (By.XPATH,"//div[@id='ledTable']//tbody/tr[1]//input")
    # led删除按键
    del_led_btn_locator = (By.XPATH,"//button[@id='ledCancel']")
    # 确认删除按键
    confirm_del_btn_locator =(By.XPATH,"//button[contains(@class,'primary ant-btn-sm')]")
    # 温湿度探头标签
    meter_tab_locator = (By.XPATH,"//div[@role='tab' and text()='温湿度探头']")
    # 温湿度探头添加按键
    add_meter_btn_locator = (By.XPATH,"//button[@data-permission='/equipment/api/meter']")
    # 温湿度ip输入框
    ip_input_locator = (By.XPATH,"//div[@class='ant-col-16']/input")
    # 第一个温湿度探头的名称
    first_meter_name_locator = (By.XPATH,"//div[@id='meterTable']//tbody/tr[1]//a")
    # 删除温湿度探头按键
    del_meter_btn_locator = (By.XPATH,"//button[@id='meterDel']")
    # 第一个温湿度的复选框
    meter_box_locator = (By.XPATH,"//div[@id='meterTable']//tbody/tr[1]//input")
    # SMS短信设备标签
    sms_tab_locator = (By.XPATH,"//div[@role='tab' and text()='SMS短信设备']")
    # 添加SMS按键
    add_sms_btn_locator = (By.XPATH,"//button[@data-permission='/equipment/api/sms']")
    # 波特率箭头下拉框按键
    bps_arrow_btn_locator = (By.XPATH,"//form/div[4]//span[@class='ant-select-arrow']")
    # 波特率9600
    bps_locator = (By.XPATH,"//li[text()='9600']")
    # 第一个短信设备的名称
    first_sms_name_locator = (By.XPATH,"//div[@id='SMSMessageDeviceTable']//tbody/tr[1]//a")
    # 第一个短信设备的复选框
    sms_box_locator = (By.XPATH,"//div[@id='SMSMessageDeviceTable']//tbody/tr[1]//input")
    # 短信设备删除按键
    del_sms_btn_locator = (By.XPATH,"//button[@id='SMSMessageDeviceDel']")


    def open_other(self):
        """打开安防设备-其他页面"""
        return self.driver.get(self.url)

    def add_led(self):
        """添加led"""
        name = time.strftime('LED%H%M%S'.format(time.localtime(time.time())))
        # 点击添加
        self.get_element(self.add_btn_locator).click()
        # 选择顶级机构
        self.wait_element_clickable(self.org_arrow_btn_locator).click()
        self.get_element(self.top_org_locator).click()
        # 输入名称
        self.get_element(self.name_input_locator).send_keys(name)
        time.sleep(0.5)
        # 输入文本
        self.wait_element_visible(self.text_input_locator).send_keys("autotesting")
        time.sleep(0.5)
        # 选择宋体
        self.wait_element_clickable(self.type_face_arrow_locator).click()
        self.wait_element_clickable(self.song_locator).click()
        for i in range(6,11):
            locator = (By.XPATH,"//li[text()='COM{}']".format(i))
            # 选择串口
            self.wait_element_clickable(self.com_arrow_locator).click()
            self.wait_element_clickable(locator).click()
            # 点击确认
            self.wait_element_clickable(self.confirm_add_btn_locator).click()
            logo_text = self.wait_element_visible(self.success_logo_locator).text
            time.sleep(2)
            if "添加LED成功" not in logo_text:
                continue
            else:
                break
        add_result_data = self.wait_element_text(self.first_led_name_locator,name)
        return add_result_data,name

    def edit_led(self,name):
        """编辑第一个led"""
        # 选中第一条led进入编辑页面
        self.wait_element_clickable(self.first_led_name_locator).click()
        # 修改名称
        time.sleep(0.5)
        self.get_element(self.name_input_locator).send_keys("test")
        # time.sleep(1)
        # 点击确定
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        new_name = name + "test"
        edit_result_logo = self.wait_element_text(self.success_logo_locator,"修改LED成功")
        edit_result_data = self.wait_element_text(self.first_led_name_locator,new_name)
        return edit_result_logo,edit_result_data,new_name

    def del_led(self,new_name):
        """删除第一个led"""
        # 要删除的led
        locator = (By.XPATH,"//div[@id='ledTable']//tbody/tr[1]//a[text()='{}']".format(new_name))
        # 选择第一个led的复选框
        self.get_element(self.led_box_locator).click()
        # 点击删除
        self.wait_element_clickable(self.del_led_btn_locator).click()
        # 点击确认
        self.wait_element_clickable(self.confirm_del_btn_locator).click()
        del_result_logo = self.wait_element_text(self.success_logo_locator,"删除LED成功")
        del_result_data = self.isElementExist(locator)
        return del_result_logo,del_result_data


    def add_meter(self):
        """添加温湿度探头"""
        name = time.strftime('TEM%H%M%S'.format(time.localtime(time.time())))
        ip = self.random_ip()
        # 点击温湿度探头
        self.get_element(self.meter_tab_locator).click()
        # 点击添加
        self.wait_element_clickable(self.add_meter_btn_locator).click()
        # 输入名称
        self.wait_element_visible(self.name_input_locator).send_keys(name)
        # 输入ip
        self.wait_element_visible(self.ip_input_locator).send_keys(ip)
        # 点击确定
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        return self.wait_element_text(self.success_logo_locator,"添加成功")


    def edit_meter(self):
        """编辑第一个温湿度探头"""
        self.get_element(self.meter_tab_locator).click()
        # 选中第一条温湿度探头进入编辑页面
        self.wait_element_clickable(self.first_meter_name_locator).click()
        # 修改名称
        self.wait_element_visible(self.name_input_locator).send_keys("test")
        # 点击确定
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        return self.wait_element_text(self.success_logo_locator,"修改成功")

    def del_meter(self):
        """删除第一个温湿度探头"""
        self.get_element(self.meter_tab_locator).click()
        # 选择第一个温湿度探头的复选框
        self.get_element(self.meter_box_locator).click()
        # 点击删除
        self.wait_element_clickable(self.del_meter_btn_locator).click()
        # 点击确认
        self.wait_element_clickable(self.confirm_del_btn_locator).click()
        return self.wait_element_text(self.success_logo_locator, "删除成功")


    def add_sms(self):
        """添加SMS短信设备"""
        name = time.strftime('SMS%H%M%S'.format(time.localtime(time.time())))
        # 点击SMS短信设备标签
        self.get_element(self.sms_tab_locator).click()
        # 点击添加
        self.wait_element_clickable(self.add_sms_btn_locator).click()
        # 输入名称
        self.wait_element_visible(self.name_input_locator).send_keys(name)
        # 选择波特率9600
        self.wait_element_clickable(self.bps_arrow_btn_locator).click()
        self.wait_element_clickable(self.bps_locator).click()
        # 点击确定
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        return self.wait_element_text(self.success_logo_locator,"添加成功")

    def edit_sms(self):
        """编辑SMS短信设备"""
        self.get_element(self.sms_tab_locator).click()
        # 选中第一个短信设备进入编辑页面
        self.wait_element_clickable(self.first_sms_name_locator).click()
        # 修改名称
        self.wait_element_visible(self.name_input_locator).send_keys("test")
        # 点击确定
        self.wait_element_clickable(self.confirm_add_btn_locator).click()
        return self.wait_element_text(self.success_logo_locator,"修改成功")

    def del_sms(self):
        """删除SMS短信设备"""
        self.get_element(self.sms_tab_locator).click()
        # 选中第一个短信设备的复选框
        self.get_element(self.sms_box_locator).click()
        # 点击删除
        self.wait_element_clickable(self.del_sms_btn_locator).click()
        # 确认删除
        self.wait_element_clickable(self.confirm_del_btn_locator).click()
        return self.wait_element_text(self.success_logo_locator,"删除成功")