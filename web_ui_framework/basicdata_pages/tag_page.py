
import time
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf

class TagPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("basicdata_url", "tag")

    def open_tag(self):
        """打开标签管理页面"""
        return self.driver.get(self.url)

    def add_tag(self):
        """新建标签"""
        first_add_btn_locator = (By.XPATH,"//div[@class='basiceMarginBottom']/table//tr[1]//button")
        tag_input_locator = (By.XPATH,"//div[@class='basiceMarginBottom']/table//tr[1]//input")
        any_locator = (By.XPATH,"//div[@class='basiceMarginBottom']/h2")
        last_tag_name_locator = (By.XPATH,"//div[@class='basiceMarginBottom']/table//tr[1]//div[@id][last()]")
        name = 'test'
        self.get_element(first_add_btn_locator).click()
        time.sleep(0.5)
        self.get_element(tag_input_locator).send_keys(name)
        self.get_element(any_locator).click()
        return self.wait_element_text(last_tag_name_locator,name)

    def del_tag(self):
        """删除标签"""
        del_btn_locator = (By.XPATH,"//div[@class='basiceMarginBottom']/table//tr[1]//div[@id][1]/i")
        first_tag_name_locator = (By.XPATH,"//div[@class='basiceMarginBottom']/table//tr[1]//div[@id][1]")
        name = self.get_element(first_tag_name_locator).text
        self.get_element(del_btn_locator).click()
        self.alert_switch_wait().accept()
        return self.wait_element_not_text(first_tag_name_locator,name)