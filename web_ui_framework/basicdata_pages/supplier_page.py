
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
class SupplierPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("basicdata_url", "supplier")
    add_btn_locator = (By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
    name_locator = (By.XPATH,"//input[@id='name']")
    duty_locator = (By.XPATH,"//input[@id='contactDuty']")
    address_locator = (By.XPATH,"//input[@id='address']")
    postcode_locator = (By.XPATH,"//input[@id='postCode']")
    contact_name_locator = (By.XPATH,"//input[@id='contactName']")
    phone_locator = (By.XPATH,"//input[@id='phone']")
    email_locator = (By.XPATH,"//input[@id='email']")
    confirm_btn_locator = (By.XPATH,"//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']")
    new_add_locator = (By.XPATH,"//div[@id='name_0']/a[@data-permission='/cms/other/supplier']")
    def open_supplier(self):
        """打开供应商管理页面"""
        return self.driver.get(self.url)


    def add_supplier(self):
        """添加供应商"""
        self.get_element(self.add_btn_locator).click()
        self.get_element(self.name_locator).send_keys("西蜀3")
        self.get_element(self.duty_locator).send_keys("五虎上将")
        self.get_element(self.address_locator).send_keys("蜀汉路99号")
        self.get_element(self.postcode_locator).send_keys("611730")
        self.get_element(self.contact_name_locator).send_keys("关羽")
        self.get_element(self.phone_locator).send_keys("13989841424")
        self.get_element(self.email_locator).send_keys("123423@qq.com")
        time.sleep(1)
        self.get_element(self.confirm_btn_locator).click()
        self.open_supplier()
        return self.get_element(self.new_add_locator).text