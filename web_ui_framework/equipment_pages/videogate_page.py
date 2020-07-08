
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
class VideoGatePage(BasePage):
    url = conf.get_str("env","url") + conf.get_str("equipment_url","videogate")
    ip = conf.get_str("video_gate","ip")
    port = conf.get_str("video_gate","port")
    username = conf.get_str("video_gate","username")
    password = conf.get_str("video_gate","password")
    # 网关信息编辑按键
    edit_gate_btn_locator = (By.XPATH,"//button[@id='editBtn']")
    # ip输入框
    ip_input_locator = (By.XPATH,"//div[@class='ant-col-16']/input")
    # 端口输入框
    port_input_locator = (By.XPATH,"//div[@role='spinbutton']/input")
    # 保存按键
    save_btn_locator = (By.XPATH,"//button[@id='submitBtn']")
    # 成功图标
    success_logo_locator = (By.XPATH, "//div[@class='ant-message-notice']//span")
    # 授权按键
    authorize_btn_locator = (By.XPATH,"//a[@id='authorization']")
    # 网关授权用户名输入框
    gate_name_input_locator = (By.XPATH,"//input[@name='loginname']")
    # 网关授权密码输入框
    gate_pwd_input_locator = (By.XPATH,"//input[@name='password']")
    # 确认授权
    confirm_btn_locator = (By.XPATH,"//input[@value='授权']")
    # 重置网关按键
    reset_gate_btn_locator = (By.XPATH,"//a[@id='reset']")
    # 确认重置
    confirm_reset_btn_locator = (By.XPATH,"//div[@class='ant-modal-content']//button[@class='ant-btn ant-btn-primary']")

    def open_videogate(self):
        """打开安防设备-视频网关页面"""
        return self.driver.get(self.url)

    def edit_gate(self):
        """编辑网关信息"""
        # 点击编辑
        self.get_element(self.edit_gate_btn_locator).click()
        # 清空输入框
        self.get_element(self.ip_input_locator).clear()
        # 输入ip
        self.get_element(self.ip_input_locator).send_keys(self.ip)
        # 输入端口
        js_code = 'arguments[0].value = {}'.format(self.port)
        e = self.get_element(self.port_input_locator)
        self.driver.execute_script(js_code,e)
        # 点击保存
        self.wait_element_clickable(self.save_btn_locator).click()
        return self.wait_element_text(self.success_logo_locator,"修改成功")


    def authorize_gate(self):
        """授权网关"""
        # 点击授权
        self.get_element(self.authorize_btn_locator).click()
        # 跳转到网关授权页面输入网关账号
        self.wait_element_visible(self.gate_name_input_locator).send_keys(self.username)
        # 输入网关密码
        self.wait_element_visible(self.gate_pwd_input_locator).send_keys(self.password)
        # 确认
        self.wait_element_clickable(self.confirm_btn_locator).click()
        return self.wait_element_text(self.success_logo_locator,"授权成功")

    def reset_gate(self):
        """重置网关"""
        self.wait_element_clickable(self.reset_gate_btn_locator).click()
        self.wait_element_clickable(self.confirm_reset_btn_locator).click()
        time.sleep(1800)
        # 获取p标签个数，重置中p标签数量为3，重置成功p标签数量为6
        return len(self.get_elements((By.TAG_NAME,"p")))