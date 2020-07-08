
from selenium.webdriver.common.by import By

from common.base_page import BasePage
from common.getconfig import conf
class BaseServicePage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("basicdata_url", "baseservice")
    locator = (By.XPATH,"//div[@class='cms-marginBottom-default']/h2")
    def open_baseservice(self):
        """打开基础服务页面"""
        self.driver.get(self.url)
        return self.get_element(self.locator).text
