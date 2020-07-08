


from selenium.webdriver.common.by import By
from common.base_page import BasePage
from common.getconfig import conf

class IndexPage(BasePage):
    url = conf.get_str("env", "url") + conf.get_str("basicdata_url", "index")
    user_element_locator = (By.XPATH,'//a[@title="管理员"]')

    def get_element_user(self):
        """定位用户元素"""
        return self.get_element(self.user_element_locator)

    def open_index(self):
        """打开首页"""
        self.driver.get(self.url)
